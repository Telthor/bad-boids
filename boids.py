"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

# Created a class structure
class Boids(object):

	def __init__(self, Boids_total = 50,
										dimension_limits = [-450, 300.0, 50, 600.0], # x = 0,1 y = 2, 3
										velocity_limits = [0, -20.0, 10, 20.0],
										move_to_middle_strength = 0.01,
										alert_distance = 100,
										formation_flying_distance = 10000,
										formation_flying_strength = 0.125,
										):# x = 0,1 y = 2,3
									self.boid_locations = self.create_flock(Boids_total, np.array(dimension_limits[2:4]), np.array(dimension_limits[0:2]))
									self.boid_velocities = self.create_flock(Boids_total, np.array(velocity_limits[2:4]),   np.array(velocity_limits[0:2]))
									self.move_to_middle_strength = move_to_middle_strength
									self.alert_distance = alert_distance
									self.formation_flying_distance = formation_flying_distance
									self.formation_flying_strength = formation_flying_strength






	@classmethod
	def init_from_data(cls, data):
		flock = cls()
		data = [np.array(element) for element in data]
		flock.boid_locations[0], flock.boid_locations[1], flock.boid_velocities[0], flock.boid_velocities[1] = data
		return flock

	@property
	def data(self):
		x, y = self.boid_locations
		xv, yv = self.boid_velocities
		return (x, y, xv, yv)

	# def update_boids(self):
	# 	# Head to middle
	# 	middle = np.mean(self.boid_locations, 1)
	# 	direction_to_middle = self.boid_locations - middle[:,np.newaxis]
	# 	self.boid_velocities -= direction_to_middle*self.move_to_middle_strength
	# 	# Avoid colisions
	# 	separations = self.boid_locations[:,np.newaxis,:] - self.boid_locations[:,:,np.newaxis]
	# 	squared_displacements = separations*separations
	# 	squared_distances = np.sum(squared_displacements,0)
	# 	far_away = squared_distances>self.alert_distance
	# 	separations_if_close = np.copy(separations)
	# 	separations_if_close[0,:,:][far_away] = 0
	# 	separations_if_close[1,:,:][far_away] = 0
	# 	self.boid_velocities += np.sum(separations_if_close, 1)
	# 	# match velocities
	# 	velocity_differences = self.boid_velocities[:,np.newaxis,:] - self.boid_velocities[:,:,np.newaxis]
	# 	very_far = squared_distances>self.formation_flying_distance
	# 	velocity_differences_if_close = np.copy(velocity_differences)
	# 	velocity_differences_if_close[0,:,:][very_far] = 0
	# 	velocity_differences_if_close[1,:,:][very_far] = 0
	# 	self.boid_velocities -= np.mean(velocity_differences_if_close, 1) * self.formation_flying_strength
	#
	# 	self.boid_locations += self.boid_velocities

	def get_separation(self):

		separations = self.boid_locations[:,np.newaxis,:] - self.boid_locations[:,:,np.newaxis]
		squared_displacements  = separations*separations
		squared_distances = np.sum(squared_displacements,0)
		return separations, squared_distances

	def go_to_middle(self):

		middle = np.mean(self.boid_locations, 1)
		direction_to_middle = self.boid_locations - middle[:,np.newaxis]
		return direction_to_middle*self.move_to_middle_strength

	def avoid_collisions(self):

		separations, squared_distances = self.get_separation()
		far_away = squared_distances>self.alert_distance
		separations_if_close = np.copy(separations)
		separations_if_close[0,:,:][far_away] = 0
		separations_if_close[1,:,:][far_away] = 0
		return np.sum(separations_if_close, 1)

	def match_velocities(self):
		separations, squared_distances = self.get_separation()
		velocity_differences = self.boid_velocities[:,np.newaxis,:] - self.boid_velocities[:,:,np.newaxis]
		very_far = squared_distances>self.formation_flying_distance
		velocity_differences_if_close = np.copy(velocity_differences)
		velocity_differences_if_close[0,:,:][very_far] = 0
		velocity_differences_if_close[1,:,:][very_far] = 0
		return np.mean(velocity_differences_if_close, 1) * self.formation_flying_strength

	def update_boids(self):
		# fly to middle
		middle_correction = self.go_to_middle()
		self.boid_velocities -= middle_correction
		# avoid collisions
		collision_correction = self.avoid_collisions()
		self.boid_velocities += collision_correction
		# match velocities
		match_correction = self.match_velocities()
		self.boid_velocities -= match_correction
		# update position
		self.boid_locations += self.boid_velocities


	def create_flock(self, count, upperlimits, lowerlimits):
		width = upperlimits - lowerlimits
		return (lowerlimits[:, np.newaxis] + np.random.rand(2, count)*width[:, np.newaxis])

Limits = [-500, 1500]

flock_1 = Boids()
figure = plt.figure()
axes = plt.axes(xlim = Limits, ylim = Limits)
scatter = axes.scatter(flock_1.boid_locations[0],flock_1.boid_locations[1])

def animate(frame):
	flock_1.update_boids()
	scatter.set_offsets(flock_1.boid_locations.transpose())

anim=animation.FuncAnimation(figure, animate,
                                 frames=50, interval=50)



if __name__ == "__main__":
	plt.show()

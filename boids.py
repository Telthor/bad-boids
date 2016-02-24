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
										dimension_limits = [-450, 50, 300.0, 600.0], # x = 0,1 y = 2, 3
										velocity_limits = [0, 10.0, -20.0, 20.0],
										move_to_middle_strength = 0.01,
										alert_distance = 2000,
										formation_flying_distance = 10000,
										formation_flying_strength = 0.125,
										):# x = 0,1 y = 2,3
									self.boid_locations = self.create_flock(self.Boids_total,self.dimension_limits[1,3], self.dimension_limits[0,2])
									self.boid_velocities = self.create_flock(self.Boids_total, self.velocity_limits[1,3],self.velocity_limits[0,2])
									self.move_to_middle_strength = move_to_middle_strength
									self.alert_distance = alert_distance




	#boids_x=[random.uniform(-450,50.0) for x in range(50)]
	#boids_y=[random.uniform(300.0,600.0) for x in range(50)]
	#boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
	#boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
	#boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)



	def update_boids(self):
		# Head to middle
		middle = np.mean(self.boid_locations, 1)
		direction_to_middle = self.boid_locations - middle[:,np.newaxis]
		boid_velocities -= self.boid_velocities - direction_to_middle*self.move_to_middle_strength
		# Avoid colisions
		separations = self.boid_locations[:,np.newaxis,:] - self.boid_locations[:,:,np.newaxis]
		squared_displacements = separations*separations
		squared_distances = np.sum(squared_displacements,0)
		far_away = squared_distances>self.alert_distance
		separations_if_close = np.copy(separations)
		separations_if_close[0,:,:][far_away] = 0
		separations_if_close[1,:,:][far_away] = 0
		velocities += np.sum(separations_if_close,1)
		# match velocities
		velocity_differences = boid_velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]
		very_far = squared_distances>self.formation_flying_distance
		velocity_differences_if_close = np.copy(velocity_differences)
		velocity_differences_if_close[0,:,:][very_far] = 0
		velocity_differences_if_close[1,:,:][very_far] = 0
		boid_velocities -= np.mean(velocity_differences_if_close, 1) * self.formation_flying_strength

		boid_locations += boid_velocities





	def create_flock(self, count, upperlimits, lowerlimits):
		width = upperlimits - lowerlimits
		return (lowerlimits[:, np.newaxis] + np.random.rand(2, count)*width[:, np.newaxis])



	figure=plt.figure()
	axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
	scatter=axes.scatter(boids[0],boids[1])

	def animate(self):
	   update_boids(boids)
	   scatter.set_offsets(zip(boids[0],boids[1]))


	anim = animation.FuncAnimation(figure, animate,
	                               frames=50, interval=50)

	if __name__ == "__main__":
	    plt.show()

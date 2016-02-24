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
										velocity_limits = [0, 10.0, -20.0, 20.0]):# x = 0,1 y = 2,3
									self.boid_locations = self.create_flock(self.Boids_total,self.dimension_limits[1,3], self.dimension_limits[0,2])
									self.boid_velocities = self.create_flock(self.Boids_total, self.velocity_limits[1,3],self.velocity_limits[0,2])




	#boids_x=[random.uniform(-450,50.0) for x in range(50)]
	#boids_y=[random.uniform(300.0,600.0) for x in range(50)]
	#boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
	#boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
	#boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

	def update_boids(boids):
		xs,ys,xvs,yvs=boids
		# Fly towards the middle
		for i in range(len(xs)):
			for j in range(len(xs)):
				xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
		for i in range(len(xs)):
			for j in range(len(xs)):
				yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
		# Fly away from nearby boids
		for i in range(len(xs)):
			for j in range(len(xs)):
				if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
					xvs[i]=xvs[i]+(xs[i]-xs[j])
					yvs[i]=yvs[i]+(ys[i]-ys[j])
		# Try to match speed with nearby boids
		for i in range(len(xs)):
			for j in range(len(xs)):
				if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
					xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
					yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
		# Move according to velocities
		for i in range(len(xs)):
			xs[i]=xs[i]+xvs[i]
			ys[i]=ys[i]+yvs[i]

	def create_flock(self, count, upperlimits, lowerlimits):
		width = upperlimits - lowerlimits
		return (lowerlimits[:, np.newaxis] + np.random.rand(2, count)*width[:, np.newaxis])



	figure=plt.figure()
	axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
	scatter=axes.scatter(boids[0],boids[1])

	def animate(frame):
	   update_boids(boids)
	   scatter.set_offsets(zip(boids[0],boids[1]))


	anim = animation.FuncAnimation(figure, animate,
	                               frames=50, interval=50)

	if __name__ == "__main__":
	    plt.show()

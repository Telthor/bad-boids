from boids import Boids
from matplotlib import pyplot as plt
from matplotlib import animation
import yaml

def boid(config_name = 'config.yaml')
    config = yaml.load(open(config_name, 'r'))
    print config
    flock_1 = Boids(Boids_total =config['boid_count'], dimension_limits = config['dimension_limits'], velocity_limits = config['velocity_limits'], Limits = config['Limits'], move_to_middle_strength = config['move_to_middle_strength'], alert_distance = config['alert_distance'], formation_flying_distance = config['formation_flying_distance'], formation_flying_strength = config['formation_flying_strength'])
    figure = plt.figure()
    axes = plt.axes(xlim = flock_1.Limits, ylim = flock_1.Limits)
    scatter = axes.scatter(flock_1.boid_locations[0],flock_1.boid_locations[1])


	flock_1.update_boids()
	scatter.set_offsets(flock_1.boid_locations.transpose())

    anim=animation.FuncAnimation(figure, animate,
                                     frames=50, interval=50)



if __name__ == "__main__":
	# go_flock = Boids()
	# go_flock.show()
	plt.show()

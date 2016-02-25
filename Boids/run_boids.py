from boids import Boids
from matplotlib import pyplot as plt
from matplotlib import animation
import yaml



def boid(config_name = 'config.yaml'):
    config = yaml.load(open(config_name, 'r'))
    flock_1 = Boids(Boids_total =config['boid_count'], dimension_limits = config['dimension_limits'], velocity_limits = config['velocity_limits'], Limits = config['Limits'], move_to_middle_strength = config['move_to_middle_strength'], alert_distance = config['alert_distance'], formation_flying_distance = config['formation_flying_distance'], formation_flying_strength = config['formation_flying_strength'], frames = config['frames'], interval = config['interval'])


    flock_1.show_sim()

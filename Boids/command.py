from argparse import ArgumentParser
from boids import Boids
from run_boids import boid
from matplotlib import pyplot as plt

def process():
    parser = ArgumentParser(description = 'A simulation of bird-like flocking behaviour')

    parser.add_argument('--config','-c',default = 'config.yaml', help = 'your configuration file for boids')

    arguments = parser.parse_args()

    boid(arguments.config)


if __name__ == '__main__':
    plt.show()

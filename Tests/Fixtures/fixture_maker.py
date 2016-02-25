from boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml

with open('fixture.yml', 'r') as f:
    reg_data = yaml.load(f)

before = reg_data['before']
flock_data = Boids.init_from_data(reg_data['before'])
flock_data.update_boids()
separationsarr, squared_distancesarr = flock_data.get_separation()
separations = [list(item) for item in separationsarr]
squared_distances = [list(item) for item in squared_distancesarr]
middles = [list(item) for item in flock_data.go_to_middle()]
collisions = [list(item) for item in flock_data.avoid_collisions()]
match = [list(item) for item in flock_data.match_velocities()]
after = [list(item) for item in flock_data.data]

print match

reg_data['after'] = after
reg_data['separations'] = separations
reg_data['squared_distances'] = squared_distances
reg_data['middles'] = middles
reg_data['collisions'] = collisions
reg_data['match'] = match

print reg_data

fixture_file = open('fixture.yml', 'w')
fixture_file.write(yaml.dump(reg_data))
fixture_file.close()

from boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml

fixture_file = open('fixture.yml', 'r+b')
reg_data = yaml.load(fixture_file)
before = reg_data['before']
flock_data = Boids.init_from_data(reg_data['before'])
flock_data.update_boids()
reg_data['after'] = flock_data.data
print reg_data


fixture_file.write(yaml.dump(reg_data))
fixture_file.close()

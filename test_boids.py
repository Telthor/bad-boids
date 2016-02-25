from boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    flock_test = Boids.init_from_data(boid_data)
    flock_test.update_boids()
    boid_data = flock_test.data
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before):
            assert_almost_equal(after_value,before_value,delta=0.01)

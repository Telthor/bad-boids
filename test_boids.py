from boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml


# Load a file with all fixture data in it, create a mock flock from that data

test_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures','fixture.yml')))
test_flock = Boids.init_from_data(test_data['before'])


def test_bad_boids_regression():
    # regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    # boid_data=regression_data["before"]
    # flock_test = Boids.init_from_data(boid_data)
    test_flock.update_boids()
    boid_data = test_flock.data
    for after,before in zip(test_data["after"],boid_data):
        for after_value,before_value in zip(after,before):
            assert_almost_equal(after_value,before_value,delta=0.01)

def test_separations():
    mock_separations = test_data['separations']
    calc_separations, calc_squares = test_flock.get_separation()
    for x, y in zip(mock_separations, calc_separations):
        for w, z in zip(x, y):
            for d, f in zip(w,z):
                print d, f
                assert_almost_equal(d, f, delta=0.01)

def test_squares():
    mock_squares = test_data['squared_distances']
    calc_separations, calc_squares = test_flock.get_separation()
    for x, y in zip(mock_squares, calc_squares):
        for w, z in zip(x, y):
            assert_almost_equal(w, z, delta=0.01)

def test_middle():
    mock_middles = test_data['middles']
    calc_middles = test_flock.go_to_middle()
    for x, y in zip(mock_middles, calc_middles):
        for w, z in zip(x, y):
            assert_almost_equal(w, z, delta=0.01)

def test_avoid():
    mock_avoid = test_data['collisions']
    calc_avoid = test_flock.avoid_collisions()
    for x, y in zip(mock_avoid, calc_avoid):
        for w, z in zip(x, y):
            assert_almost_equal(w, z, delta = 0.01)

def test_match():
    mock_match = test_data['match']
    calc_match = test_flock.match_velocities()
    for x, y in zip(mock_match, calc_match):
        for w, z in zip(x, y):
            assert_almost_equal(w, z, delta = 0.01)

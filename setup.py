from setuptools import setup, find_packages

setup(
        name = 'Boids'
        version = '0.0.1'
        packages = find_packages()
        scripts = ['boids/boids.py']
        install_requires = ['matplotlib','numpy','nose','yaml','random']
        license = 'MIT'
        author = 'David Wise'
        author_email = 'd.wise.15@ucl.ac.uk'
        scripts = ['scripts/boids']
)

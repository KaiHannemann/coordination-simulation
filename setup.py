from setuptools import setup, find_packages
requirements = [
    'simpy',
    'networkx',
    'geopy',
    'pyyaml>=5.1',
    'numpy',
    'coord-interface',
    'simianarmy'
]

test_requirements = [
    'flake8',
    'pytest',
    'nose2'
]

dependency_links = [
    'git+https://github.com/RealVNF/coord-env-interface',
    'git+https://git.cs.upb.de/kaiha/bachelorarbeit'
]

setup(
    name='coord-sim',
    version='0.9.3',
    description='Simulate flow-level, inter-node network coordination including scaling and placement of services and '
                'scheduling/balancing traffic between them.',
    url='https://github.com/CN-UPB/coordination-simulation',
    author='Stefan Schneider',
    dependency_links=dependency_links,
    author_email='stefan.schneider@upb.de',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=requirements + test_requirements,
    tests_require=test_requirements,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'coord-sim=coordsim.main:main',
        ],
    },
)

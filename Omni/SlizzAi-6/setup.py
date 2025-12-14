# setup.py
from setuptools import setup, find_packages

setup(
    name='slizzaiengine',
    version='0.1.0',
    description='SlizzAi-6 inference engine',
    packages=find_packages(where='core'),
    package_dir={'': 'core'},
    install_requires=[
        'torch==2.1.0',
        'numpy>=1.24.0',
        'pyyaml',
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'slizzai-run=slizzaiengine.entrypoint:main'
        ]
    }
)

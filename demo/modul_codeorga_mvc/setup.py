import os, sys
from setuptools import setup, find_packages

setup(
    name="program",
    version="0.1.0",
    package_dir={'':'program'},
    packages=find_packages('program'),
    entry_points={
        "console_scripts": [
            "program = program.__main__:main"
        ]
    },
)
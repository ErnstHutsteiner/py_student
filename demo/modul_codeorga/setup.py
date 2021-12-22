from setuptools import setup

setup(
    name="program",
    version="0.1.0",
    packages=["program"],
    entry_points={
        "console_scripts": [
            "program = program.__main__:main"
        ]
    },
)
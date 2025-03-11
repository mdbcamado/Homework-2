from setuptools import find_packages, setup

setup(
    name="diabetesProj",
    packages=find_packages(exclude=["diabetesProj_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)

from setuptools import setup, find_packages


setup(
    name="time2feat",
    version="0.1.0",
    packages=find_packages(include=["t2f", "t2f.*"]),
    python_requires=">=3.8",
)

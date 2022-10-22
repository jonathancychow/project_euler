import os

from setuptools import setup

install_requires = []
requirmentsTxt = 'requirements.txt'
if os.path.isfile(requirmentsTxt):
    with open(requirmentsTxt) as f:
        for line in f.read().splitlines():
            if not line.startswith("--"):
                install_requires.append(line)

__version__ = "0.10.0"

setup(
    name="primelib",
    version=__version__,
    author="Jonathan Chow",
    description="Prime number tools",
    url="",
    packages=['primelib'],
    install_requires = install_requires,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ]
)
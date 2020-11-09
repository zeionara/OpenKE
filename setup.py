import os
from distutils.command.build_scripts import build_scripts

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


class PostInstallCommand(build_scripts):
    def run(self):
        os.system('g++ openke/base/Base.cpp -fPIC -shared -o openke/release/Base.so -pthread -O3 -march=native -std=c++11')
        build_scripts.run(self)


setuptools.setup(
    name='openke',
    version='0.92',
    scripts=['openke_'],
    authors=["thunlp", "zeionara"],
    author_email="zeionara@gmail.com",
    description="A library for operating knowledge graph models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zeionara/OpenKE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['numpy'],
    cmdclass={
        'build_scripts': PostInstallCommand
    },
    include_package_data=True
)

from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="dac-autoreg",
    version="0.3.0",
    include_package_data=True,
    packages=find_packages(),
    author="Hasan Aliyev", 
    author_email="hasan.aliyev.555@gmail.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    description="Register endpoints and services in DAC",
    license="MIT",
    url="https://github.com/OnePoint-Team/DAC-autoreg",
    install_requires=["httpx"],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

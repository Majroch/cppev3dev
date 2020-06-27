# CPPEV3DEV
*Author: Majroch <jakuboch4@gmail.com>*

## Table of Content
  - [What it is?](#what-it-is)
  - [Pre-Requirements](#pre-requirements)
    - [Ubuntu-based systems](#ubuntu-based-systems)
    - [Other systems](#other-systems)
  - [Usage](#usage)
    - [Ubuntu](#ubuntu)
    - [Other systems](#other-systems-1)

## What it is?
This package provides basic compiling, sending and debugging capabillities for Newbies.

It's goal is to provide program for cross-compiling for ARM, sending programs from/to EV3DEV Linux-based system and debugging capabilities with good written documentation, and basic examples of usage.

## Pre-Requirements

### Ubuntu-based systems
```bash
sudo apt install python3 pip3
sudo pip3 install -r requirements_linux.txt
```

### Other systems
You'll need to run this program in docker.

Search how to install Docker for your specific system. Then you can pull image from repo:
```bash
docker pull majroch/cppev3dev:latest
```

or build it yourself:
```bash
docker build . -t your_tag_here
```

## Usage
Run program:
### Ubuntu
```bash
./cppev3dev.py
```

### Other systems
```bash
docker run -ti \
           -v $PWD/:/compile
           majroch/cppev3dev:latest
```

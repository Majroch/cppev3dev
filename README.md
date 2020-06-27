# CPPEV3DEV
*Author: Majroch <jakuboch4@gmail.com>*

## Table of Content
  - [What it is?](#what-it-is)
  - [Pre-Requirements](#pre-requirements)
    - [Ubuntu-based systems](#ubuntu-based-systems)
    - [Other systems](#other-systems)
  - [Usage](#usage)
    - [Linux](#linux)
    - [Other systems](#other-systems-1)
  - [TODO](#todo)

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
You'll need to run in docker: [there's a link](https://hub.docker.com/repository/docker/majroch/cppev3dev)

## Usage
Run program:
### Ubuntu
```bash
./cppev3dev.py
```

### Other systems
Go to docker page [here](https://hub.docker.com/repository/docker/majroch/cppev3dev)

## TODO
- [ ] Requirements:
   - [ ] mono / .NET
   - [ ] Python
   - [ ] ev3dev-lang-cpp
   - [ ] arm cross-compiler from source

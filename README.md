# CPPEV3DEV
*Author: Majroch <jakuboch4@gmail.com>*

## Table of Content
  - [What it is?](#what-it-is)
  - [Pre-Requirements](#pre-requirements)
    - [Ubuntu-based systems](#ubuntu-based-systems)
    - [Arch-based systems](#arch-based-systems)
    - [Windows](#windows)
  - [Usage](#usage)
    - [Linux](#linux)
    - [Windows](#windows-1)
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

### Arch-based systems
```bash
pacman -Suy python python-pip
pip install -r requirements_linux.txt
```

### Windows
First, install python3 with pip from: [here](https://www.python.org/downloads/windows/)

***Note: Make sure Python is in PATH environment variable***

Then open `cmd` with Administrator privileges and run:
```cmd
pip install -r requirements_windows.txt
```

## Usage
Run program:
### Linux
```bash
./cppev3dev.py
```
### Windows
From `cmd` go to project folder, and then:
```cmd
cppev3dev.py
```

## TODO
- [ ] Requirements:
   - [ ] mono / .NET
   - [ ] Python
   - [ ] ev3dev-lang-cpp
   - [ ] arm cross-compiler from source
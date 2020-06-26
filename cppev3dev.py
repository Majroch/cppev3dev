#!/usr/bin/python3

##########################
#          TODO          #
##########################
# 
# echo self.ssh['password'] | sudo -S sh -c "echo 'robot	ALL=(ALL:ALL) NOPASSWD: ALL' >> /etc/sudoers"
# into sudoers file!
# 
##########################
import os
import platform
import subprocess
from getpass import getpass

host_os = platform.system()

def isAdmin(hostos):
	if hostos == "Windows":
		try:
			temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\\windows'),'temp']))
		except:
			return False
		else:
			return True
	else:
		if 'SUDO_USER' in os.environ:
			return True
		else:
			return False

def cls():
	if(host_os == "Windows"):
		os.system("cls")
	else:
		os.system('clear')

if host_os == "Windows":
	try:
		from msvcrt import getch
	except ImportError:
		print("Trying to install all required packages from requirements_windows.txt")
		if isAdmin(host_os):
			os.system('pip install -r requirements_windows.txt')
		else:
			print("To install required packages, need to have an admin privileges first!")
			exit()
		try:
			from msvcrt import getch
		except:
			print("Cannot load all required packages!")
			exit()
	except:
		print("Cannot load all required packages!")
		exit()
else:
	try:
		from getch import getch
	except ImportError:
		print("Trying to install all required packages from requirements_linux.txt")
		if isAdmin(host_os):
			os.system('sudo pip install -r requirements_linux.txt')
		else:
			print("To install required packages, need to have an admin privileges first!")
			exit()
		try:
			from getch import getch
		except:
			print("Cannot load all required packages!")
			exit()
			
import libbrick
import libconfig

config_files = {
	"error": "/var/log/cppev3dev/errors.log",
	"config": "/etc/cppev3dev/config.cfg",
	"logs": '/var/log/cppev3dev/logs.log'
}

config = libconfig.Config(config_files['config'])

brick = libbrick.Brick(config.get('username'), config.get('password'), config.get('ip'))

compilling_first = "{compiler} -Wall -static -static-libgcc -pthread -c {filename} -o {output}"
compilling_last = "{compiler} -Wall -static -static-libgcc -pthread {filenames} -o {output}"

options = {
	"menu": [
		['connect', 'Check Connection'],
		['compile2', 'Compile & upload'],
		['compile1', 'Compile'],
		['config', 'Configure'],
		['exit', 'Exit']
	],
	"config": [
		['updatel', "Update Login"],
		['updatep', "Update Password"],
		['updateai', "Update Address IP"],
		['menu', "Back"]
	]
}

selected = 'menu'
out = ""

if __name__ == "__main__":
	menu_pos = 0
	try:
		while True:
			cls()
			print("---------------------------")
			print("|      EV3DEV LINKER      |")
			print("---------------------------")
			print("Login:", brick.ssh['username'])
			print("Address IP:", brick.ssh['ip'])
			print("Running as Admin:", isAdmin(host_os))
			print("Brick output:", out)
			print("---------------------------")
			print("|           MENU          |")
			print("---------------------------")
			for option in range(len(options[selected])):
				if menu_pos == option:
					print(options[selected][option][1], "<<")
				else:
					print(options[selected][option][1])
			print("---------------------------")
			try:
				key = getch()
				if key == b'\xe0' or key == "[":
					key = getch()
					if key == b'P' or key == "B":
						menu_pos += 1
					elif key == b'H' or key == "A":
						menu_pos -= 1
				elif key == b'\x03' or key == b'\x1b':
					raise(KeyboardInterrupt)
				elif key == b'\r' or key == "\n":
					#Logic
					
					if options[selected][menu_pos][0] == 'exit':
						raise(KeyboardInterrupt)
					elif options[selected][menu_pos][0] == "config":
						selected = options[selected][menu_pos][0]
						menu_pos = 0
					elif options[selected][menu_pos][0] == "menu":
						selected = options[selected][menu_pos][0]
						menu_pos = 0
					elif options[selected][menu_pos][0] == "updatel":
						inp = input("Enter new login: ")
						config.update('username', inp)
						brick.update('username', inp)
					elif options[selected][menu_pos][0] == "updatep":
						inp = getpass("Enter new password: ")
						config.update('password', inp)
						brick.update('password', inp)
					elif options[selected][menu_pos][0] == "updateai":
						inp = input("Enter new Adress IP: ")
						config.update('ip', inp)
						brick.update('ip', inp)
					elif options[selected][menu_pos][0] == "connect":
						try:
							out = brick.send('whoami')
						except BrickCannotSendException:
							out = False
						if out == [config.get('username')]:
							out = True
					elif options[selected][menu_pos][0] == "compile1":
						print("Initializing!")
						os.system("git clone https://majroch.pl/git/ev3dev-compile.git")
						os.system("cp ev3dev-compile/ev3dev/ev3dev* ./")
						os.system("rm -rf ev3dev-compile")
						
						filename = input("Enter file localization: ")
						output = input("Enter output filename: ")
						print("Trying to compile!")
						
						os.system(compilling_first.format(compiler=config.get('compiler'), filename=filename, output=output+".o"))
						os.system(compilling_first.format(compiler=config.get('compiler'), filename="ev3dev.cpp", output="ev3dev.o"))
						os.system(compilling_last.format(compiler=config.get('compiler'), filenames="ev3dev.o "+output+".o", output=output))
						
						input("Finished! Click enter...")
						
					
			except OverflowError:
				raise(KeyboardInterrupt)

			if menu_pos >= len(options[selected]):
				menu_pos = 0
			if menu_pos < 0:
				menu_pos = len(options[selected])-1
			#print(key)
	except KeyboardInterrupt:
		print("Exitting...")
		exit()
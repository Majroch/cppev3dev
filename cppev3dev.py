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
import subprocess
from getpass import getpass

import functions as func
import libbrick
import libconfig

config_files = {
	"error": "./errors.log",
	"config": "./config.cfg",
	"logs": './logs.log'
}

config = libconfig.Config(config_files['config'])

tmp_dir = config.get('tmp')

brick = libbrick.Brick(config.get('username'), config.get('password'), config.get('ip'))

options = {
	"menu": [
		['connect', 'Check Connection'],
		['customCommand', 'Send Custom Command'],
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
			func.cls()
			print("---------------------------")
			print("|      EV3DEV LINKER      |")
			print("---------------------------")
			print("Login:", brick.ssh['username'])
			print("Address IP:", brick.ssh['ip'])
			print("Running as Admin:", func.isAdmin())
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
				key = func.getch()
				if key == b'\xe0' or key == "[":
					key = func.getch()
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
							if out == ['pi']:
								out = True
						except libbrick.BrickCannotSendException:
							out = False
					elif options[selected][menu_pos][0] == "compile1":
						func.compiling(config)
						input("Finished! Click enter...")
					elif options[selected][menu_pos][0] == "compile2":
						filename = func.compiling(config)
						brick.send_file(filename)
						input("Finished! Click enter...")
					elif options[selected][menu_pos][0] == "customCommand":
						command = input("Insert command: ")
						try:
							out = brick.send(command)
						except libbrick.BrickCannotSendException:
							out = False

						
					
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
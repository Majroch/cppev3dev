# BRICK CLASS
import subprocess
import time
import platform

#if platform.system() == "Windows":
#	if platform.architecture() == "64bit":
#		ssh = "plink-64.exe {username}@{ip} -pw {password} -o StrictHostKeyChecking=accept-new"
#	else:
#		ssh = "plink-32.exe {username}@{ip} -pw {password} -o StrictHostKeyChecking=accept-new"
#else:
#	ssh = "sshpass -p {password} ssh {username}@{ip} -o StrictHostKeyChecking=accept-new"
ssh = "sshpass -p {password} ssh {username}@{ip} -o StrictHostKeyChecking=accept-new"

class BrickMissingOptionException(Exception):
	pass
class BrickNoConnectedException(Exception):
	pass
class BrickCannotSendException(Exception):
	pass

class Brick:
	ssh = {}
	instance = None
	def __init__(self, username="", password="", ip="127.0.0.1"):
		"""Gets: username, password, ip
where:
	username - Login to ssh
	password - Password to ssh
	ip - address ip to connect to"""
		self.ssh['username'] = username
		self.ssh['password'] = password
		self.ssh['ip'] = ip
	
	def update(self, option, value):
		"""Gets: option, value
where:
	option - Option to update
	value - Value to update"""
		if option in self.ssh:
			self.ssh[option] = value
		else:
			raise(BrickMissingOptionException("Cannot find" + str(option) + "in brick config!"))
	
	def send(self, command):
		"""Gets: command
where:
	command - Command to execute"""
		try:
			cmd = []
			for l in ssh.format(username=self.ssh['username'], ip=self.ssh['ip'], password=self.ssh['password']).split(" "):
				cmd.append(l)
			
			if " " in command:
				for l in command.split(' '):
					cmd.append(l)
			else:
				cmd.append(command)
			
			terminal = subprocess.Popen(cmd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			
			temp = terminal.stdout.readlines()
			
			out = []
			if type(temp) == type([]):
				for line in temp:
					line = line.decode().strip().replace('\r\n', "").replace('/n', '')
					if line != command and line != "":
						out.append(line)
			else:
				out.append(line.decode().strip().replace('\r\n', "").replace('/n', ''))
			return out
		except:
			raise(BrickCannotSendException("Cannot send command: " + str(command)))
		
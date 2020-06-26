# CONFIG CLASS
class ConfigWriteError(Exception):
	pass

class ConfigOpenError(Exception):
	pass

class ConfigOptionError(Exception):
	pass

class Config:
	def __init__(self, filename):
		"""Gets: filename
where:
	filename - config filename"""
		self.filename = filename
		config = {}
		try:
			with open(filename, "r") as file:
				for opt in self._purify_config(file):
					config[opt[0]] = opt[1]
		except FileNotFoundError:
			#print("File", config_files['config'], "not found! Creating one!")
			with open(filename, "w") as file:
				file.write("# SSH\n")
				file.write("username = robot\n")
				file.write('password = maker\n')
				file.write('ip = 127.0.0.1\n')
				file.write('compiler = arm-linux-gnueabi-g++\n')
				file.write('tmp = ./tmp')
				config['username'] = "robot"
				config['password'] = "maker"
				config['ip'] = "127.0.0.1"
				config['compiler'] = "arm-linux-gnueabi-g++"
				config['tmp'] = "./tmp/"
		self.config = config
		
	def _purify_config(self, file):
		"""Gets: file
where:
	file - File object"""
		lines = []
		for line in file.readlines():
			line = line.strip()
			if line != "" or line != None:
				if "#" in line:
					if line[0] != "#":
						hash_pos = line.find("#")
						line = line[:hash_pos]
					else:
						continue
				line = line.replace(" ", "").split("=")
				lines.append(line)
		return lines
	
	def get(self, option):
		"""Gets: option
where:
	option - returns value from config file"""
		if option in self.config:
			return self.config[option]
		else:
			raise(ConfigOptionError("Option not found!"))
	
	def write(self, option, value):
		"""Gets: option, value
where:
	option - value name to save
	value - value to store"""
		if not option in self.config:
			try:
				with open(self.filename, "a") as file:
					file.write(option)
					file.write(" = ")
					file.write(value)
					file.write("\n")
				self.config[option] = value
				return True
			except FileNotFoundError:
				raise(ConfigOpenError("File", self.filename, "not found!"))
		else:
			raise(ConfigWriteError("Value exists!"))
	
	def update(self, option, value):
		"""Gets: option, value
where:
	option - value name to save
	value - value to store"""
		if option in self.config:
			del self.config[option]
			lines = []
			try:
				with open(self.filename, "r") as file:
					lines = self._purify_config(file)
				for line in lines:
					if line[0] == option:
						line[1] = value
				with open(self.filename, "w") as file:
					for line in lines:
						file.write(line[0])
						file.write(" = ")
						file.write(line[1])
						file.write("\n")
						self.config[line[0]] = line[1]
				return True
			except FileNotFoundError:
				raise(ConfigOpenError("File", self.filename, "not found!"))
		else:
			raise(ConfigWriteError("Value not exists!"))
	
	def delete(self, option):
		"""Gets: option
where:
	option - value name to delete"""
		if option in self.config:
			del self.config[option]
			lines = []
			try:
				with open(self.filename, "r") as file:
					lines = self._purify_config(file)
				for line in range(len(lines)):
					if lines[line][0] == option:
						del lines[line]
				with open(self.filename, "w") as file:
					for line in lines:
						file.write(line[0])
						file.write(" = ")
						file.write(line[1])
						file.write("\n")
						self.config[line[0]] = line[1]
				return True
			except FileNotFoundError:
				raise(ConfigOpenError("File", self.filename, "not found!"))
		else:
			raise(ConfigWriteError("Value not exists!"))
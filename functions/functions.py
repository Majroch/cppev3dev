import platform, os
import libconfig

host_os = platform.system()

def isAdmin():
	if host_os == "Windows":
		try:
			os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\\windows'),'temp']))
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
		if isAdmin():
			os.system('pip install -r requirements_windows.txt')
		else:
			print("To install required packages, need to have an admin privileges first!")
			exit()
		try:
			from msvcrt import getch # pylint: disable=import-error
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
		if isAdmin():
			os.system('sudo pip install -r requirements_linux.txt')
		else:
			print("To install required packages, need to have an admin privileges first!")
			exit()
		try:
			from getch import getch # pylint: disable=no-name-in-module
		except:
			print("Cannot load all required packages!")
			exit()

def get_linux_os():
	config = libconfig.Config('/etc/os-release')
	return config.get('ID')

def initialize_compilator(config: libconfig.Config):
	if host_os == "Windows":
		distro = "Windows"
	else:
		distro = get_linux_os()
	
	compiler = config.get('compiler')

	awk = "'{print $2}'"

	if distro == "Windows":
		return False
	elif distro == "arch":
		# tmp_dir = config.get('tmp')
		output = os.popen("whereis {compiler} | awk {awk}".format(compiler=compiler, awk=awk)).read().strip('\n')
		if output == "":
			os.system('echo "{compiler}"'.format(compiler=compiler)) # TODO
		else:
			return True
	elif distro == "ubuntu":
		output = os.popen("whereis {compiler} | awk {awk}".format(compiler=compiler, awk=awk)).read().strip('\n')
		if output == "":
			os.system('sudo apt install {compiler}'.format(compiler=compiler))
		else:
			return True
	else:
		return False

def compiling(config: libconfig.Config) -> str:
	compilling_first = "{compiler} -Wall -static -static-libgcc -pthread -c {filename} -o {output}"
	compilling_last = "{compiler} -Wall -static -static-libgcc -pthread {filenames} -o {output}"

	filename = input("Enter file localization: ")
	output = input("Enter output filename: ")

	print("Initializing!")
	tmp_dir = config.get('tmp')
	if not os.path.isfile("./ev3dev.h") or not os.path.isfile('./ev3dev.cpp'):
		os.system(f"git clone https://github.com/Majroch/ev3dev-compile.git {tmp_dir}ev3dev-compile")
		os.system(f"cp {tmp_dir}ev3dev-compile/ev3dev/ev3dev* ./")
		os.system(f"rm -rf {tmp_dir}ev3dev-compile")
	
	initialize_compilator(config)

	print("Trying to compile!")
	
	os.system(compilling_first.format(compiler=config.get('compiler'), filename=filename, output=output+".o"))
	os.system(compilling_first.format(compiler=config.get('compiler'), filename="ev3dev.cpp", output="ev3dev.o"))
	os.system(compilling_last.format(compiler=config.get('compiler'), filenames="ev3dev.o "+output+".o", output=output))

	return output
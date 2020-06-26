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

	if distro == "Windows":
		return False
	elif distro == "arch":
		# tmp_dir = config.get('tmp')
		
		output = os.popen("whereis gcc-arm-linux-gnueabi | awk '{print $2}'").read().strip('\n')
		if output == "":
			os.system('echo "Hello World!"') # TODO
		else:
			return True
	elif distro == "ubuntu":
		output = os.popen("whereis gcc-arm-linux-gnueabi | awk '{print $2}'").read().strip('\n')
		if output == "":
			os.system('sudo apt install gcc-arm-linux-gnueabi g++-arm-linux-gnueabi')
		else:
			return True
	else:
		return False
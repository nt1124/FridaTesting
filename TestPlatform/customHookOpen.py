import sys
import frida
from scriptFactory import *



def on_message(message, data):
	print(message)


logfile = open("logfile.txt", "w")
session = frida.get_remote_device().attach("com.android.settings")

libcModule = None
modulesList = session.enumerate_modules()

for i in range(0, len(modulesList)):
	if "libc.so" in modulesList[i].name:
		libcModule = modulesList[i]
		break

print i
print libcModule

exportsOfLibc = libcModule.enumerate_exports()


for i in range(0, len(exportsOfLibc)):
	addressInt = libcModule.base_address + exportsOfLibc[i].relative_address
	tempStr = exportsOfLibc[i].name + "  " + str(hex(addressInt))
	logfile.write(tempStr + "\n")
	if "open" == exportsOfLibc[i].name:
		openAddress = addressInt


logfile.close()

print openAddress

script = createScriptForFunction(session, openAddress)

script.on('message', on_message)

script.load()
sys.stdin.read()

import frida

session = frida.get_remote_device().attach("com.android.settings")

modulesList = session.enumerate_modules()

for i in range(0, len(modulesList)):
	if "libc.so" in modulesList[i].name:
		print i
		print modulesList[i]
		print " "

# print([x.name for x in session.enumerate_modules()])


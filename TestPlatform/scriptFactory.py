def createScriptForFunction(session, functionAddress):
	script = session.create_script('''
	Interceptor.attach(ptr("%s"),
		{
			onEnter: function(args)
			{
				send("Loggy Loggy Log");
			}
		}
	);
	''' % int(functionAddress))

	return script
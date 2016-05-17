
def validar(a, b):
	
	if len(b) > 4 and b.isalnum():
		print "usuario valida"
	else:
		print "usuario debe contener al menos 4 caracteres y ser alfanumerico "

	if len(a) > 6 and a.isdigit():
		print "contrasena valida"
	else:
		print "contrasena debe contener al menos 6 caracteres y ser numerico "




x = raw_input("ingrese usuario: ")

y = raw_input("ingrese contrasena: ")

validar(x, y)


### Basis

* La diferencia entre python v2 y python v3 es grande. v2 está más extendida por lo general. Ejemplo: **print**.
* Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.
* Comentarios con `#`


### print examples

	myint = 1
	mystr = 'Hola Mundo'

	print myint+1
	# spaces?
	print myint, mystr  
	print "number:", myint, "-", mystr  

	myPI = 3.14159265359
	print 'The value of PI is approximately %5.3f.' % myPI
	
	# Mixing operators between numbers and strings is not supported:
	print myint + 2 + mystr


### Numbers

	myint = 5
	myfloat = 5.0
	# or...
	myfloat1 = float(5)

### Strings

Es válido tanto `'esto'` como `"esto"` but...

	mystring = "Don't worry about apostrophes"

Concatenación de strings

	hello = "hello"
	world = "world"
	helloworld = hello + " " + world
	
### Assignments  
	
	# OK: 
	a = 1
	b, c = 2, 3 
	d, str = 4, 'Hola Mundo'
	
	# ERRROR:
	c, d = 5
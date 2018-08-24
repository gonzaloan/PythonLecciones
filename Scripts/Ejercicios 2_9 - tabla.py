import sys

if(len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit() and (int(sys.argv[1]) > 0 and int(sys.argv[1]) < 10) and (int(sys.argv[2]) > 0 and int(sys.argv[2]) < 10)):
	filas = int(sys.argv[1])
	columnas = int( sys.argv[2])
	for i in range(filas):
		for x in range(columnas):
			print(" * ", end='')
		print("")
else:
	print("Deben ingresarse dos valores como parámetros y ser números entre 1 y 9")
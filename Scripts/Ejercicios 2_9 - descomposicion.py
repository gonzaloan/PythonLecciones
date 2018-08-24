import sys

if(len(sys.argv) == 2 and sys.argv[1].isdigit() and int(sys.argv[1])>0):
	largonum = len(sys.argv[1])
	formateo = "{:0" + str(largonum) + "d}"
	for indice,num in enumerate(sys.argv[1]):
		ceros=largonum-indice-1
		resultado = num + '0'*ceros
		print(formateo.format(int(resultado)))
else:
	print("Se debe introducir un parámetro, que debe ser un entero positivo")
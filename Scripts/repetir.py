import sys
#Verificamos los argumenos
if(len(sys.argv)) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("Error, los argumentos no están correctos.")
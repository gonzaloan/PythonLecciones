#import saludos
#saludos.saludar()

import sys
#Agregamos el path del directorio anterior. Donde está saludos.py
sys.path.insert(1, '..')
print(sys.path)

from saludos import Saludo

Saludo()
from setuptools import setup

setup(
    name="paquete",
    version="0.1",
    description="Este es un paquete de ejemplo",
    author="Gonzalo Muñoz",
    author_email = "gonzalo.munoz@zeke.cl",
    url="http://google.cl",
    #scripts=['script.py'] En caso de querer scripts 
    packages=["paquete","paquete.adios","paquete.hola"] #Declaracion de paquetes incluidos
)
#Para crear el distribuible se coloca desde linea de comandos
#python setup.py sdist
#Esto creará una carpeta dist con el archivo comprimido. para instalarlo.
# Para instalar este archivo se ejecuta pip install paquete-0.1.tar.gz
#Una vez así, e puede llamar el paquetedesde cualquier ubicacion. 
#borrar paquete pip uninstall paquete

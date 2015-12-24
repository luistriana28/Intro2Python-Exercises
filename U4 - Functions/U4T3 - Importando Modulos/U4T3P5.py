"""
U4 - Funciones

T3 - Importando modulos.

P5 - Habemous dragones!!!

Los imports universales pueden parecer excelentes a simple vista. Pero no lo son.
La razon principal es que llenan tu programa con muchas, MUCHAS variables y 
funciones sin la seguridad de que los nombres utilizados estan asociados a los
nombres de los modulos que importaste.

Tu tienes una funcion que creaste llamada sqrt y tu importas math. Tu funcion
esta segura: Existe tu sqrt y math.sqrt.
Si haces from math import *, tendras problemas: dos funciones diferentes con el
mismo nombre.

Por esta razon es mejor usar import module y escribir module.name. O simplemente
importar las variables y funciones que vayas a utilizar.

"""

#El codigo siguiente te mostrara todo, TODO lo que trae el modulo math.

import math
todo=dir(math)
print todo
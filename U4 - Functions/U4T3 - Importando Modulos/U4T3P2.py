"""
U4 - Funciones

T3 - Importando modulos.

P2 - Importaciones genericas

Veamos el error que el interprete arrojo:
    NameError: name 'sqrt' is not defined 

    Significa que Python aun no sabe que es una raiz cuadrada, aun.
    
Existe un modulo llamado math que, entre varias funciones utiles, trae sqrt().
Para poder accesar a math, hay que mandarla llamar con la palabra clave import.
Cuando importas un modulo de esta manera, es llamado una importacion generica.
"""

#Hay que hacer dos cosas
#1. Escribir import math
#2. Escribir math. antes de sqrt() para que ahora se lea math.sqrt(). Esto le 
#dice a Python no solo que importe math, pero que utilice la funcion sqrt()
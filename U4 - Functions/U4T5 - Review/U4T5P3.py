"""
U4 - Funciones

T5 - Review

P3 - Funciones pre-establecidas.

Por ultimo, revicemos las funciones pre-establecidas.

"""

def es_numero(num):
    return type(num)==int or type(num)==float

max(2,3,4) #4
min(2,3,4) #2

abs(2) #2
abs(-2) #2

"""
1. Define una funcion llamada distancia_de_cero, con un argumento (el que 
quieras).
2. Si el tipo del argumento es int o float, la funcion regresara el valor 
absoluto del argumento.
3. Si no, la funcion regresa "Nop"
"""
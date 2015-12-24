"""
U4 - Funciones

T2 - Sintaxis de las funciones

P5 - La practica hace al maestro

Hagamos mas funciones nada mas porque podemos.

"""
def gritar(frase):
    if frase==frase.upper():
        return "ESTAS GRITANDO AAHHH!!!"
    else:
        return "Podrias hablar un poco mas alto?"
        
print gritar("QUIERO GRITAR")

"""
Este ejemplo es solamente para referencia de la sintaxis de las funciones.

Ejercicio:
    1. Primero, define una funcion llamada cubo, que su argumento sea numero.
    2. Esa funcion regresa el cubo de ese numero. (El numero multiplicado por 
    si mismo 3 veces)
    3. Define una segunda funcion llamada por_tres, su argumento sera numero.
    4.Si ese numero es divisible por tres, por_tres debera llamar a cubo(numero).
    Si no, regresa falso
"""

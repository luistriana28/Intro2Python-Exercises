"""
Unidad 3 - Condicionales y Control de Flujo.

T4 - If, Else y Elif

P4 - Tengo 99 problemas, pero un switch no es uno de ellos.

"Elif" es corto para "else if". Y significa los siguiente:"sin embargo, 
si la siguiente expresion es verdad, haz lo siguiente!"
Ejemplo:
    if 8>9:
        print "Yo no me imprimo!"
    elif 8<9:
        print "Yo si me imprimo!"
    else:
        print "Yo tampoco me imprimo"

En el ejemplo de arriba, el "elif" entra solamente si el primer "if" es 
False.
"""

#En la primer linea, el if debe checar si la respuesta es mayor a 5.
#En la siguiende linea, el if debe checar si la respuesta es menor a 5.

def mayor_menor_igual_5(respuesta):
    if ________:
        return 1
    elif ________:          
        return -1
    else:
        return 0
        
print mayor_menor_igual_5(4)
print mayor_menor_igual_5(5)
print mayor_menor_igual_5(6)

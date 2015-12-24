"""
U4 - Funciones

T2 - Sintaxis de las funciones

P4 - Funciones llamando funciones

Hemos hecho funciones que pueden imprimir texto o hacer operaciones matematicas.
Sin embargo, las funciones pueden hacer cosas mucho mas poderosas que eso. Por
ejemplo, una funcion puede llamar a otra funcion:
    
    def fun_uno(n):
        return n*5
    
    def fun_dos(m):
        return fun_uno(m)+7

Veamos las siguientes dos funciones en el editor:
    una_buena_vuelta (agrega 1 al numero que entra de argumento)
    merece_otra (agrega 2 al numero que entra de argumento)
"""

#Cambia el cuerpo de merece_otra para que agregue 2 a una_buena_vuelta

def una_buena_vuelta(n):
    return n+1
    
def merece_otra(n):
    return n+2

print merece_otra(2) #debe salir 5

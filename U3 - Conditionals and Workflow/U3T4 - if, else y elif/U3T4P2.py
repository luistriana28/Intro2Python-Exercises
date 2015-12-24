"""
Unidad 3 - Condicionales y Control de Flujo.

T4 - If, Else y Elif

P2 - Si tu tienes...

Practiquemos con con if. Recordemos que la sintaxis se ve asi:
    if alguna_funcion():
        #Sentencia uno
        #Sentencia dos
        #etcetera

Viendo el ejemplo de arriva, en el evento de que alguna_funcion() regrese True,
la linea de codigo con sangria sera ejecutada. Si regresa False, esta linea sera
brincada.

Es de notar los dos puntos ":" al final del if.

Ejercicio:
    En el editor veras dos funciones. No te apures si no le entiendes. Todo a su
    debido tiempo.
    
    1. Escribe una expresion que evalue a True.
    2. Escribe una expresion que evalue a True.
"""
#Escribe dos ejemplos de if!

def usando_if_una_vez():
    if  :              #Pon tu sentencia 'if' aqui!
        return "Lo lograste 1"
    return "No lo lograste 1"

def usando_if_otra_vez():
    if :               #Pon tu sentencia 'if' aqui!
        return "Lo lograste 2"
    return "No lo lograste 2"
        
#Si lo hiciste bien debe de imprimir "Lo lograste 1" y "Lo lograste 2"
print usando_if_una_vez() 
print usando_if_otra_vez()
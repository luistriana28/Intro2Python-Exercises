"""
U4 - Funciones

T1 - Introduccion a las funciones

P1 - Para que sirven las funciones?

Habras considerado el reutilizar una pieza de codigo, solo cambiando algunos 
valores. En lugar de reescribir todo el codigo, es mucho mejor y mas limpio 
definir una FUNCION, la cual puede ser utilizada repetidas veces.

Reviza el siguiente codigo, esta basado en el proyecto "Calculadora de 
propinas". Podras observar que hemos definido dos funciones:
    impuesto -> Calcular el iva de una cuenta.
    propina -> Calcular la propina.

Ve cuanto del codigo puedes entender a simple vista (todo se explicara con 
detenimiendo). 

"""

def iva(cuenta):
    """
    Agregamos el 16% de iva a la cuenta
    """
    cuenta *= 1.16
    print "Con iva:", cuenta
    return cuenta

def propina(cuenta):
    """
    Agrega el 15% de propina a la cuenta
    """
    cuenta *= 1.15
    print "Con la propina:", cuenta

cena_costo=100
cena_con_iva=iva(cena_costo)
cena_con_propina=propina(cena_con_iva)

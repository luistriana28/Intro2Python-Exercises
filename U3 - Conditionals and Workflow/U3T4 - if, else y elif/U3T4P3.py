"""
Unidad 3 - Condicionales y Control de Flujo.

T4 - If, Else y Elif

P3 - Si no...

La sentencia else complementa al if. Un par if/else dice:
    "Si esta expresion es verdad, corre este codigo;
    Si no, corre este otro codigo".

A diferencia del if, el else no depende de una expresion. Por 
ejemplo:
    if 8>9:
        print "No me imprimi."
    else:
        print "Yo si me imprimi."
"""
#Escribe dos sentencias else!
respuesta = "Solo es un raspon!"

def caballero_negro():
    if respuesta == "Solo es un raspon":
        return True
    else:              #Pon tu else aqui.
        return         #Tu else debe regresar "False"

def soldado_frances():
    if respuesta == "Alejate! Que te dare de nuevo!":
        return True
    else:              #Pon tu else aqui.
        return        #Tu else debe regresar "False"

print caballero_negro()
print soldado_frances()
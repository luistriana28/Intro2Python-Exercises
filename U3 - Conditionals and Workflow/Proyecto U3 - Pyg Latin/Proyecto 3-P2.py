# -*- coding: utf-8 -*-
"""
Proyecto U3 - Pyg Latin

Parte 2.

Ay B C

Revisemos de nuevo las reglas para la traduccion:
    1) Si la palabra original empieza con una consonante, agregas "ay" al final
    de la palabra.
    Ejemplo: anaconda -> anacondaay
    
    2) Si la palabra original inicia con una consonante, mueves la primera letra
    de la palabra al final y despues le pones "ay".
    Ejemplo: python -> ythonpay
"""

#Crea una variable llamada pyg donde guardes el valor "ay"
pyg = 'ay'

"""
Simplifiquemos las cosas. Hagamos las letras de nuestra palabra todas 
minusculas:
    la_cadena = "Hola"
    la_cadena = la_cadena.lower()
    
La funcion .lower() no modifica la cadena en si, solamente regresa una version 
en minuscula de toda la cadena. En el ejemplo anterior, guardamos el resultado 
en la misma variable.

Tambien requerimos la primera letra de la palabra.
    primera_letra = la_cadena[0]
    segunda_letra = la_cadena[1]
    tercera_letra = la_cadena[2]

Recuerda que iniciamos a contar en cero, no uno. Asi que para accesar la primera
letra preguntamos por [0]
"""

#Dentro del if:
#1. Crea una nueva variable llamada "palabra" que guarde la conversion .lower() 
#de original
#2. Crea una nueva variable llamada "primero" que guarde palabra[0], la primera
#letra de palabra

print "Pyg Latin"

original = raw_input("Ingresa una palabra: ")

if len(original)>0 and original.isalpha():
    print original
else:
    print "Vacio"


"""
Ya que tenemos guardada la primera letra, necesitamos agregar la letra y la 
cadena guardada en la variable "pyg" al final de la cadena original.

Para esto requerimos concatenar:
    saludo="Hola "
    nombre="D. Y."
    bienvenida=saludo+nombre
"""

#En una nueva linea despues de crear la variable "primero":
#Crea una nueva variable llamada "nueva_palabra" e igualala a la suma de palabra,
#primero y pyg.

"""
Final!

Excelente! Ya solo nos que unos pasos por hacer. Te habras dado cuenta que la 
letra inicial se repite al principio y al final. Para arreglar eso utilizaremos 
la particion de listas.

Ejemplo:
    s = "Alberto"
    print s[0] #Imprimira A
    
    print s[1:] #imprimira lberto
"""

#Iguala la variable nueva_palabra a la particion del indice uno hasta el final
#de la variable nueva_palabra. Utiliza [1:] para hacerlo.

"""
Te daras cuenta que este traductor solo funciona para palabras que inician con 
consonantes. Recordando la regla:
    Si una palabra inicia con vocal solo se le agrega la terminacion "ay" a la
    palabra. Ejemplo:
        Ala -> Alaay
        Ergo -> Ergoay

Haz las modificaciones necesarias al programa para que funcione con vocales.

Pista: Solo hay que agregar otra condicion if/else.
"""
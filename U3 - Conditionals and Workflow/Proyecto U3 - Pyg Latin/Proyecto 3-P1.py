# -*- coding: utf-8 -*-
"""
Proyecto U3 - Pyg Latin

Problemas pequeños.

Veamos que hemos aprendido hasta ahora y escribir tu propio traductor de Pig 
Latin.

Pyg Latin es un juego de idiomas (Piensa en el idioma de la F), donde tu mueves
la primera letra de una palabra al final y le agregas "ay". Asi "Python" se 
convierte en "ythonpay". Para escribir tu traductor en Python, estos son los 
pasos que tienes que seguir.

    1. Preguntarle al usuario que escriba una palabra en español.
    2. Asegurarte que el usuario haya escrito una palabra valida.
    3. Convertir la palabra de Español a Pig Latin.
    4. Mostrar el resultado de la traduccion.
"""

#Imprime la Frase "Pig Latin"
print "Pyg Latin"

#Usa raw_input("Ingresa una palabra:"), para preguntarle al usuario que ingrese
#una palabra. Salva el resultado en una variable llamada "original"
original = raw_input("Ingresa una palabra")

#Escribe una sentencia if que verifique que la cadena tenga caracteres.
#Agrega un if que cheque que len(original) es mayor que cero.
#Si la cade es mayor que cero imprime la palabra.
#Si no, imprime "Vacio"
if len(original)>0 and original.isalpha():
    print original
else:
    print "Vacio"

"""
Ya sabemos si existe una cadena no vacia. Hagamos otra validacion.

    x= "J123"
    x.isalpha() #False

En la primera linea, creamos una cadena con letras y numeros.

La segunda linea corre la funcion isalpha() que regresa False ya que la 
cadena contiene caracteres numericos.

Hay que asegurarnos que la palabra que ingresa el usuario contenga solo 
caracteres del alfabeto. Puedes usar isalpha() para revisar esto.
"""

#En el if anterior puedes agregar un and para ingresar una segunda condicion.
#Aqui debes usar .isalpha() para asegurarte que solo contiene letras.
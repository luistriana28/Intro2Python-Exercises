# -*- coding: utf-8 -*-
"""
U1T2 - Espacios en blanco y enunciados

Ahora que conocemos y entendemos lo que son las variables, los valores y la 
asignacion, veamos que son los espacios en blanco y los enunciados. Las 
sentencias del lenguaje Python.
"""

"""
Ejercicio 01 - Que es un enunciado?

Un enunciado en Python es similar a un enunciado en español: Es la mas pequeña
unidad del español que tiene sentido. Por ejemplo, 'Yo', 'quiero', 'Spam' no
son enunciados por si mismos. Sin embargo, 'Yo quiero Spam', si lo es. Las
variables y los tipos de datos no son enunciados, pero son la base que los
forman.

Para continuar con la analogia, es necesario algun tipo de puntuacion para hacer
obvio donde termina un enunciado y donde inicia otro. Si tienes experiencia en
algunos lenguajes de programacion, sabras que en algunos de ellos el final de un
enunciado lo marca el punto y coma ';'.

En Python, los enunciados son separados por espacios en blanco (' '). Y de la
misma manera en la cual no podemos poner puntos y comas cuando y como queramos,
no podemos poner espacios en blanco donde queramos en Python.

Tomara algo de tiempo en acostumbrarte, en especial si tienes experiencia en 
lenguajes de programacion donde los espacios en blanco no importan.
"""

#Al correr este ejercicio nos aparecera un error de indentacion. Eso lo 
#arreglaremos en un momento

def spam():
huevos = 12
return huevos
        
print spam()
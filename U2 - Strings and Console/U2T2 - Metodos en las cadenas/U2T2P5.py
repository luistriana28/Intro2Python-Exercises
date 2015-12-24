# -*- coding: utf-8 -*-
"""
U2T2 - Metodos en las cadenas

Modificar las cadenas es util. Pero hacerlo a mano es una ...(inserte 
palabra altisonante preferida). Sin embargo, Python trae de fabrica varios
metodos para hacer eso automaticamente.
"""

"""
Ej 05 - Notacion punto

Lo prometido es deuda. Ahora explicaremos la razon de porque usamos
len(str) y str(obj), pero notacion punto ("str".upper()) para el resto.

La notacion punto funciona para cadenas ("El ministerio de caminar 
tonto".lower()) y variables con valor de cadena (ministerio.upper()). Esto,
porque esos metodos son especificos a las cadenas. Osease que solo trabajan
con cadenas y nadamas.

Por el contrario, len() y str() pueden trabajar con muchos y variados objetos
(los cuales veremos mas adelante). Por lo tanto, no pueden usar la notacion 
punto solo con las cadenas.

Vamos a practicar un poco mas
"""

#Declara la variable 'ministerio' y asignale el valor "El ministerio de caminar
#tonto".


#Despues imprime el tamaño de 'ministerio'


#finalmente convierte a mayusculas 'ministerio'
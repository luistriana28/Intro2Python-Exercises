"""
U2T1 - Cadenas

Las cadenas son un tipo de dato muy importante y bastante comun en Python. 
En los siguientes ejercicios demostraremos como construirlas y manipularlas.
"""

"""
Ej 03 - Accesando a las cadenas...

Recordemos que las cadenas son una serie de caracteres unidos. Sin embargo, no
seria genial que pudieramos accesar a cada uno de los caracteres? Pues si, si
podemos.

Cada caracter en una cadena tiene un indice. En otras palabras, tiene un numero
pegado. El numero inicia en 0 desde la extrema izquierda y se incrementa de uno
en uno mientras te mueves a la derecha.

La cadena "PYTHON" tiene 6 caracteres, numerados del 0 al 5 como se muestra 
abajo:

---+---+---+---+---+---+-
 P | Y | T | H | O | N |
---+---+---+---+---+---+-
 0   1   2   3   4   5

Si quisieramos la 'T' escribiriamos "PYTHON"[2]. Siempre cuenta desde 0.
"""

segunda="PYTHON"[2]
print segunda

#Si quisieramos la quinta letra de "monty" como le harias?
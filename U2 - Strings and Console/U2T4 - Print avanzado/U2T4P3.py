"""
U2T4 - Print avanzado

Ahora que ya sabes imprimir a la consola, veamos algunas cosas mas avanzadas de
print
"""

"""
Ej 03 - Formateo de cadenas, parte 1.

Excelente trabajo hasta ahora! Una mas y hacemos review.

Vimos anteriormente que podiamos accesar a los caracteres individualmente de una
cadena utilizando un indice.

Desafortunadamente, las cadenas en Python son inmutables. No cambian despues de
ser creadas.

Sin embargo, hay una manera de ser algo flexible con tus cadenas. Y eso es el 
formateo de cadenas. Usa el simbolo % (no confundirlo con el modulo). Piensa en
el como una variable para tu cadena
"""

#Corre el codigo de abajo. Como crees que se vera en la consola?

camelot = "Camelot"
lugar = "lugar"
print "No vayamos a %s. Es un %s tonto." % (camelot, lugar)
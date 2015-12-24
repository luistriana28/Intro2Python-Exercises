"""
U2T4 - Print avanzado

Ahora que ya sabes imprimir a la consola, veamos algunas cosas mas avanzadas de
print
"""

"""
Ej 04 - Formateo de cadenas, parte 2.

Te fijaste? El % cambio el %s (s de string, cadena en ingles) en nuestra cadena
con las variables en los parentesis. Pudimos haber puesto directamente "camelot"
y "lugar" en el parentesis pero queria mostrarte como trabaja con variables

La sintaxis es asi:
    print "%s" % (variable_cadena)
    
Puedes tener tantas variables (o cadenas) separadas por comas en los parentesis
como gustes.

    print "Los %s que %s %s!" % ("Caballeros", "dicen", "Ni")

Esto imprime "Los caballeros que dicen Ni!"

Para el gran final de esta nueva leccion mostraremos una pieza de codigo nueva.
No hay problema si no le entiendes lo mostraremos mas adelante.

Por ahora, solo remplaza los '___' con la forma de % que es necesaria para 
completar la mision:
    %s dentro de la cadena y % para ligar la cadena con los argumentos.

Contesta las preguntas que vayan saliendo en la consola!
"""
nombre = raw_input("Cual es tu nombre?")
mision = raw_input("Cual es tu mision?")
color = raw_input("Cual es tu color favorito?")

print "Ah, so your name is ___, your quest is ___, \
and your favorite color is ___."___(nombre, mision, color)
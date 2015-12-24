"""
U5 - Listas y diccionarios de Python

T1 - Listas

P1 - Introduccion a Listas

Las listas son un tipo de dato en el cual puedes guardar colecciones de 
informacion en secuencia bajo el mismo nombre. Los tipos de datos que ya has 
utilizado son cadenas, numeros y booleanos.

Puedes asignar objetos a una lista con una expresion con la siguiente forma:
    nombre_lista=[item_1, item_2]
con los objetos que tu quieras entre brackets. Una lista tambien puede estar 
vacia:
    lista_vacia = []

Las listas tienen varias similaridades con las cadenas.
"""
#La lista zoologico solo tiene 3 objetos. Agrega un cuarto animal.

zoologico=["leon", "liebre", "puma", ""]

if len(zoologico)>3:
    print "El primer animal del zoologico es", zoologico[0]
    print "El primer animal del zoologico es", zoologico[1]
    print "El primer animal del zoologico es", zoologico[2]
    print "El primer animal del zoologico es", zoologico[3]

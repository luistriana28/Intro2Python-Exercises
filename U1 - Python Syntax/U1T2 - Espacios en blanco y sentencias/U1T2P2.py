"""
U1T2 - Espacios en blanco y enunciados

Ahora que conocemos y entendemos lo que son las variables, los valores y la 
asignacion, veamos que son los espacios en blanco y los enunciados. Las 
sentencias del lenguaje Python.
"""

"""
Ejercicio 2 - Espacio en blanco significa espacio en lo correcto

El error que obtuvimos en el ejercicio pasado es el siguiente:
    
    IndentationError: expected an indented   block
    
Obtendremos este error siempre que tengamos algun espacio en blanco mal. Si
tienes experiencia en otros lenguajes piensa que es similar al mal uso de ';'
o '{}'. Cuando la puntuacion esta mal, el significado puede cambiar 
completamente.

    No quiero comer, gracias.
    No, quiero comer, gracias.

Ves a lo que me refiero?
"""

#Para arreglarlo solo agregaremos 4 espacios a la linea 22 y 23

def spam():
    huevos = 12
    return huevos
        
print spam()
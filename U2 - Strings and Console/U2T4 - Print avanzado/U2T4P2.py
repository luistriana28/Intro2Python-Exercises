"""
U2T4 - Print avanzado

Ahora que ya sabes imprimir a la consola, veamos algunas cosas mas avanzadas de
print
"""

"""
Ej 02 - Conversion explicita de cadenas

Recordemos el metodo str() y su habilidad de convertir datos que no son cadenas
a cadenas. El nombre formal para ese proceso es "Conversion explicita de 
cadenas".

Explicitamente le estas diciendo a Python, "se que no es una cadena, pero 
quiero que lo sea". Bastante diferente a nada mas poner comillas alrededor de
una secuencia de caracteres para crear una cadena.

Convertir un numero en una cadena te permite pegar cadenas y numeros. Python
normalmente no lo permite
"""

print "Tengo un monton de ricos cocos. Son "+str(99)+". Como vez?"

#Si corres el codigo de abajo, obtendremos un error.

print "El valor de pi es aproximadamente "+3.1516

#Corrige el valor usando str() 
"""
U4 - Funciones

T4 - Funciones pre-establecidas

P1 - Mas alla de las cadenas...

Ya sabemos que son las funciones y como importar modulos, veamos algunas de las
funciones que trae de default Python. Y no es necesesario importar modulos.

Ya hemos usado algunas de las funciones de default en las cadenas, como .upper(),
.lower(), str() y len(). Estas son excelentes funciones si vamos a trabajar con 
cadenas. Y si queremos algo mas analitico?

"""

#Que crees que hace el siguiente codigo?

def mas_grande(*args):
    print max(args)
    return max(args)
    
def mas_pequeno(*args):
    print min(args)
    return min(args)

def distancia_de_cero(arg):
    print abs(arg)
    return abs(arg)


mas_grande(-10, -5, 5, 10)
mas_pequeno(-10, -5, 5, 10)
distancia_de_cero(-10)
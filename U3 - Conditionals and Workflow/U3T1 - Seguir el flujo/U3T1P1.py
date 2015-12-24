"""
Unidad 3 - Condicionales y Control de Flujo.

T1 - Introduccion al control de Flujo

P1 - Seguir el flujo

Igual que en la vida real, habra veces que nuestros programas tomen decisiones.

Los programas en Python, que hemos estado escribiendo van en un solo sentido:
    Suman dos numeros o imprimen algo. Sin embargo, no tienen la abilidad de 
    escoger hacer alguno de estos. 
    
El control de flujo nos da esta habilidad de escoger entre estos resultados en 
base a lo que suceda en el programa
"""

def clinica():
    print "Has entrado a la clinica!"
    print "Te vas hacia la derecha o la izquierda?"
    answer = raw_input("Escribe izquierda o derecha y presiona 'Enter'.")
    if answer == "IZQUIERDA" or answer == "Izquierda" or answer == "izquierda":
        print "Este es el cuarto de abuso verbal, maldito hijo de p#$%&!"
    elif answer == "DERECHA" or answer == "Derecha" or answer == "derecha":
        print "Este es el cuarto de los argumentos, eso ya te lo habia dicho!"
    else:
        print "No escogiste ni derecha ni izquierda, intentalo de nuevo!"
        clinica()

clinica()
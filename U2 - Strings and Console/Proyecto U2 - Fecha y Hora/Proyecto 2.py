# -*- coding: utf-8 -*-
"""
La libreria datetime

Muchas veces quieres saber cuando algo sucedio.
En Python lo podemos hacer de manera sencilla utilizando "datetime"

Aqui nosotros usaremos "datetime" para imprimir la fecha y hora en 
un formato bonito.
"""
#Importa la libreria datetime

from datetime import datetime

"""
Obteniendo la fecha y hora actual

Podemos usar una funcion llamada datetime.now() para obtener la fecha y hora
actual
"""

#Crea una variable llamada "ahora" y guarda el resultado de datetime.now()


#Ahora imprime la variable "ahora"


"""
Sacando la informacion.

Observa lo que imprimiste. No es agradable a la vista.

Veamos como podemos extraer porciones de la fecha y hora y acomodarlos.

Empezaremos obteniendo el mes, dia y año de datetime.now(). Podemos usar la
variable "ahora" de la siguiente manera:
    año_actual=ahora.year
    
Podemos usar una sintaxis similar para obtener el mes (month) y el dia (day).
"""

#Imprime a pantalla el dia, mes y año actual en lineas separadas.




"""
Fecha importante.

Vamos a agregar barras a nuestra fecha para verse de la siguiente manera
dd/mm/yyyy

Vamos a usar concatenacion. Recuerda que solo funciona con cadenas. Por lo tanto
usaremos tambien la funcion str() para convertir numeros a cadenas.
"""

#Imprime la fecha de la siguiente manera dd/mm/yyyy



"""
Bonito Tiempo.

Excelente trabajo! Hagamos lo mismo para la hora, minuto y segundo.

Usemos de nuevo la variable "ahora" para imprimir la informacion de la hora.
Por ejemplo, la hora actual seria:
    hora_actual=ahora.hour

De la misma manera para obtener el minuto (minute) y los segundos (second)
"""

#De igual manera que el anterior ejercicio, imprime la hora en el siguiente formato
#hh:mm:ss


"""
El Gran Final

Ya imprimiste la fecha y la hora por separado. Ahora, los combinaremos.
"""

#Imprime la fecha y hora juntos, con el siguiente formato:
#dd/mm/yyyy hh:mm:ss (nota que hay un espacio entre la fecha y la hora.)
"""
Proyecto 4 - Vacacionando!

P1 - Planeando el viaje.

Organicemos nuestro viaje vacacional. Es importante saber cuanto vamos a gastar.

"""

def pago(horas):
    return 105.50 * horas

"""
La funcion anterior solo es una manera de como las funciones son definidas.

Usemos funciones para calcular los costos del viaje.
"""

#Define una funcion que se llame costo_hotel con un argumento llamado noche.
#El hotel cuesta $1500 pesos la noche, por lo tanto la funcion debe de regresar
# 1500 * noche.



#Define una funcion llamada costo_avion que toma de argumento una cadena llamada
#ciudad. La funcion debe devolver un precio diferente dependiendo del lugar.
# "D.F.":1300, "Monterrey": 1200, "Acapulco":2000 y "Cancun":3000



#Define una funcion llamada renta_carro con un argumento llamado dias.
#Calcula el costo de rentar el carro.
#Cada dia cuesta 400 pesos
#Si lo rentas por 7 dias o mas se te hace un descuento de 500 pesos
#Si lo rentas por 3 dias o mas se te descuentan 200 pesos.
#No puedes tener los dos descuentos. Y regresa ese precio.



#Define una funcion llamada costo_viaje que tome dos argumentos ciudad y dias
#La funcion tiene que regresar las funciones suma de renta_carro(dias), 
#costo_hotel(noche), costo_avion(ciudad). Es valido llamar la funcion 
#costo_hotel(noches) con la variable dias.



#Modifica la funcion costo_viaje y agrega un tercer argumento gasto_corriente. 
# Agrega la variable gasto_corriente a la suma que regresa la funcion 
#costo_viaje



#Por ultimo imprime el costo de 5 noches de hotel a cancun con 7000 pesos de 
#gasto corriente
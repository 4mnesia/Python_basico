import numpy as np

lista = [1,2,3,4,5]
arreglo = np.array(lista)

print(arreglo)

#ndim = indica cuantas dimensiones posee el arreglo
print(f"el arreglo es de {arreglo.ndim} dimension")

#len = indica el largo del arreglo
print(f"el arreglo es de largo {len(arreglo)}")

#Slice
#Start:Stop:Step = indicando cuanto quiero mostrar del arreglo
#Star:: = indica desde donde vamos a consultar
#:Stop: = indica hasta donde vamos a consultar
#::Step = indica de cuanto en cuanto vamos a consultar
print(arreglo[::2])

#rellena arreglo
#for
lista2 = [i for i in range(1,11)]
arreglo2 = np.array(lista2)
print(arreglo2)

#arange(Start:Stop:Step) = rellena el arreglo con valores segun lo indicado
arreglo3 = np.arange(1,11)
print(arreglo3)

#operaciones
#sumar
arreglo3 += 5
print(arreglo3)

#multiplicar 
arreglo3 *= 10
print(arreglo3)

#comparacionesa o operaciones relacionales 
print(arreglo3>arreglo2)

#sum() = entrega la suma de los valores del arreglo
print(arreglo3.sum())

#mean() = Entrega el promedio de valores del arreglo
print(arreglo3.mean())

#max = muestra valor mas alto
#min = muestra valor mas bajo
print(f"numero mas alto: {arreglo3.max()}")
print(f"numero mas alto: {arreglo3.min()}")


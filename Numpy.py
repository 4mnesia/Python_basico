#¿que es un array?
#un array o matriz es un vector que contiene elementos homogeneos, es decir, que pertenencen al mismo tipo de datos
import array as arr
a = arr.array('d',[1.1,3.5,4.5])
print(a)
#listas= puede constar de elementos pertenecientes a diferentes tipos de datos
#arrays = solo consta de elementos que pertenecieron al mismo tipo de dato
matriz = arr.array('i',[1,2,3,4,5])
for arr in matriz:
    print(arr)
#---------------------------------------------------------------------------------
import numpy as np
#el array es para que se reconozca como arreglo numpy
m = np.array([1,2,3,4,5,6,7,8,9,10])
print(m)
#el arange es para poder meter una cantidad de datos, con inicio, final y salto
#reshape es para poder ordenar en filas y columnas: .reshape(columna,fila)
m = np.arange(1,43).reshape(7,6)
print(m)

#size es para saber cuantos elementos hay en la matriz
print(m.size)

#ndim para ver las dimensiones que tiene la matriz
print(m.ndim)

#recuerda que la fila es la hilera horizontal y la columna la vertical
m = np.zeros((3,4))
print(m)

m = np.arange(27).reshape(3,3,3)
print(m)
#----------------------------------------------------------------------

m = np.arange(24).reshape(4,6)
print(m)
#esto es para ubicar un posicion dependiendo de donde esta segun columnas y filas
#se cuenta del 0 hacia adelante
print(m[3,4])

m1 = np.array([90,7,9,4,2,1])
#np.sort(matriz)es para poder ordenar lo que contiene la matriz
print(np.sort(m1))

m1 = np.array([2,3])
#con power se elevan con una determinada potencia 
print(np.power(m1,2))
print("")
m1 = np.array([2,3,4,5,6,7])
print("")
#tambien el array cumple condiciones
print(np.array(m1 >= 4))
print("")
#encontrar el valor maximo con max con "max" y min con "min"
print(np.array(m1.max()))
print("")
print(np.array(m1.min()))
print("")
#esto hace que se junten matrices
m1 = np.array([2,3,4,5,6,7])
m2 = np.array([11,34,67,99])
print(np.concatenate((m1,m2)))
print("")
#sumas de matrices dependiendo del indice
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[5,6],[7,8]])
print(m1 + m2)
print("")
#para poder sumar un numero a la matriz 
print(m1+2)
print(np.add(m1,m2))
print("")
#como sacar numeros de manera aleatoria
#randint es la funcion para ocupar el random
m = np.random.randint(10)
print(m)
print("")

#si quieres tener un tamaño especifico
aleatorio = np.random.randint(10, size=(5))
print(aleatorio)
#si es de 2 dimensiones
aleatorio = np.random.randint(10, size=(3,3))
print(aleatorio)
print("")

#para controlar el paramentro de cada funcion
m = np.array([[0,1,2],[4,2,3]])
print(m)
print("")
#haciendo lo de axis=0 sumara de manera vertical, osea sumara las columnas
print(np.sum(m,axis=0))
#axis=1 suma las filas
print("")

print(np.sum(m,axis=1))


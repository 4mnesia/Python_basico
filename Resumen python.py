"""#palabras reservadas
#if en python
mi_edad = int(input("¿Que edad tengo?: ")) 
if (mi_edad >= 18):
    print("Adulto")
elif (mi_edad < 18 and mi_edad >= 12):
    print("Adolescente")
else:
    print("Niñ@")

if (mi_edad >18 or mi_edad < 25):
    print("Adulto joven")
else:
    print("Adulto mayor")

#El "and" se ocupa que ambas condiciones sean true
#El "or" ocupa que una de las condiciones sean true

def suma1(a,b):
    resultado = a + b
    print("La suma de "+ str(a) + " mas " + str(b) + " es igual a: " + str(resultado))
suma1(132,20)

import time

contador = 0
boolwhile = True

while (boolwhile):
    print("Contador va por el numero: " + str(contador))

    time.sleep(1) #dependiendo del dato dentro del time.sleep son los segundos.
    #sin el time.sleep, procesara muchos datos por milesima de segundos.

    contador = contador + 1
#hay que poner un break para que pare o si no, se volvera un bucle infinito.
    if(contador == 5):
        break

arreglo_nombres = ["Juan","Esteban","Pepe"]

print("La cantidad de objetos que tiene este arreglo es de: "+ str(len(arreglo_nombres)))

for x in range(len(arreglo_nombres)):
    #el len del arreglo es 3, porque tenemos 3 valores
    #pero se empieza con el 0, osea
    #0 = Juan
    #1 = Esteban
    #2 = Pepe
    #o esto tambien demuestra el indice de cada nombre
    print("X: "+ str(x))
    print("Nombre: " + arreglo_nombres[x])


#--------------------------------------------------------------------------------------------------------------
#Funciones 
#Una función es un bloque de código con un nombre asociado, que
#recibe cero o más argumentos como entrada, sigue una secuencia de
#sentencias, la cuales ejecuta una operación deseada y devuelve un valor
#y/o realiza una tarea, este bloque puede ser llamados cuando se
#necesite.

#Operadores Python
#suma = (+)
#resta = (-)
#multiplicacion = (*)
#division = (/)
#exponente = (**)
#modulo = (%)

def suma(a,b):
    resultado = a + b
    return "El resultado de la suma es: "+ str(resultado)
print(suma(10,5))

def resta(a,b):
    resultado = a - b
    return "La resta es: " + str(resultado)
print(resta(10,5))

def multiplicacion(a,b):
    resultado = a*b
    return "La multiplicacion es: "+ str(resultado)
print(multiplicacion(10,5))

def division(a,b):
    resultado = a / b
    return "La division es: "+str(resultado)
#para divisiones simples se pueden poner //, para evitar el decimal
#resultado = a // b <---- asi
print(division(20,5))

def exponente(a,b):
    resultado = a**b
    return "El exponente es: "+ str(resultado)
print(exponente(2,5))

def  mensaje_entrada(nombre):
    print("Hola, bienvenido " + nombre)
mensaje_entrada("Pepe")

def mensaje_salida():
    print("Adios")
mensaje_salida()

def edad(mi_edad):
    return mi_edad
mi_edad_es = edad(20)
print("Tengo "+str(mi_edad_es), "años")

#ademas se pueden ocupar en cualquier lado las funciones recientemente creadas.

print(suma(8,5))

#--------------------------------------------------------------------------------------------------------------------------------
#arreglo N°1
n = int(input("Ingrese el tamaño del arreglo: "))
m = int(input("Ingrese el numero de multiplos: "))
Arreglo=[]
for i in range(0,n):
    Arreglo.append(i*m)
print(Arreglo)
#arrelgo N°2
Arreglo = [1,5,8,9,30,9,13]
V = []
for i in Arreglo:
    if i > 3 and i % 2 != 0:
        #esto fue para ver si es impar
        V.append(i)
print(V)
#arreglo N°3
#calcular 10 numeros de forma aleatoria
import random

def Vector_random(n):
    vector = [0]*n
    for i in range(n):
        vector [i] = random.randint(0,10)
    return vector
print("Ingrese cuantos numeros aleatorios desea obtener: ")
n = int(input())
aleatorio = Vector_random(n)
print(aleatorio)
#--------------------------------------------------------------------
#Arreglos unidimensionales y sus propiedades

#Append: Este metodo agrega un elemento al final de una lista.
#Count: Este metodo recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la lista.
#Extend: Este metodo extiende una lista agregando un iterable al final.
#Index: Este metodo recibe un elemento como argumento, y devuelve el indice de su primera aparicion en la lista.
#Insert: Este metodo inserta el elemento X en la lista, en el indice 1.
#Pop: Este metodo devuelve el ultimo elemento de la lista y lo borra de la misma .
#Remove: Este metodo recibe como argumento un elemento y borra su primera aparicion en la lista.
#Reverse: Este metodo invierte el orden de los elementos de una lista.
#Sort: Este metodo ordena los elementos de una lista.

Edades = [15,18,27]
print(Edades)
#Posicion (INDICE)
#0 = 15
#1 = 18
#2 = 27
mi_edad = Edades[1]
print("Mi edad es: ", str(mi_edad))

#Mutable

Edades[1] = 19
print(Edades)

#LEN

print("La cantidad de elementos en el arreglo son de: " + str(len(Edades)))

#1.- Append
Edades.append(15)
Edades.append(15)
Edades.append(27)
print(Edades) 

#2.- Count 
print("La cantidad de veces que hay un 15 en la lista son: " + str(Edades.count(15)))

#3.- Index
posicion = Edades.index(19)
print("la posicion de 19 es: " + str(posicion))
mi_edad = Edades[posicion]
print("Mi edad es: ", str(mi_edad))

#4.- Insert
num = 99 
Edades.insert(3,num)
print(Edades)

#5.- Pop
UltimoElemento = Edades.pop()
print("Ultimo elemento: "+ str(UltimoElemento))
print(Edades)

#6.- Remove
Edades.remove(99)
print(Edades)

#7.- Reverse
Edades.append(35)
print(Edades)
Edades.reverse()
print(Edades)

#8.- Sort
#Este ordena por default por menor a mayor
Edades.sort()
print(Edades)
#Este me lo ordena de mayor a menor
Edades.sort(reverse=True)
print(Edades)

#recorrer el arreglo con FOR
#range empieza de 0
#y llega hasta el final del len de edades(6)

for i in range(len(Edades)):
    print("La edad en la posicion: "+ str(Edades[i]))
    edad = Edades[i]
    resultado = edad+5
    print("La edad en la posicion: "+str(resultado))
    print("Esta edad en 5 años va ser: "+str(resultado))
#--------------------------------------------------------------------------
#Arreglos Multidimensionales

#Un arreglo multidimensional es un arreglo con más de dos dimensiones.
#En una matriz, las dos dimensiones se representan en filas y columnas.
#Cada elemento se define mediante dos subíndices, el índice de la fila y el
#índice de la columna.
#También se puede recorrer utilizando un “FOR”

#Los arreglos multidimensionales tambien son heterogeneos ( pueden estar conformadas por elementos de distinto tipo)
#y mutables(que sus elementos pueden modificarse)

#funciones de los arreglos: Append, Count, Extend, Index, Insert, Pop, Remove, Reverse, Sort

Arreglo = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(Arreglo)):
    for j in range(len(Arreglo[i])):
        print(Arreglo[i][j])
#[1,2,3],[4,5,6],[7,8,9]
#for i in range(len(Arreglo)):
#0 -> [1,2,3]
#1 -> [4,5,6]
#2 -> [7,8,9]
#for j in range(len(Arreglo[i])):
#j0 -> 7
#j1 -> 8
#j2 -> 9

#otra manera

array_datos = [[]]
array_datos[0].append("Pepe")
array_datos[0].append(27)
array_datos[0].append("Mexico")
array_datos[0].append(1412421412)

array_datos.append([])
#con lo de arriba, va creando otro arreglo
array_datos[1].append("Esteban")
array_datos[1].append(27)
array_datos[1].append(12412421421)
array_datos[1].append("Costa Rica")

array_datos.append([])
array_datos[2].append("Juan")
array_datos[2].append(18)
array_datos[2].append("Argentina")
array_datos[2].append(12412124421)

#print(array_datos)
#print("La cantidad de datos en el arreglo es de: " + str(len(array_datos[0])))
#o tambien
for i in range(len(array_datos)):
    for j in range(len(array_datos[i])):
        print(array_datos[i][j])
#o tambien
for i in range(len(array_datos)):
    print(array_datos[i][0])
    print(array_datos[i][1])
    print(array_datos[i][2])
    print(array_datos[i][3])
    #o tambien
    array_datos[i][0]
    array_datos[i][1]
    array_datos[i][2]
    array_datos[i][3]
print(array_datos)

#son mutables?
print("Arreglo antiguo: "+ str(array_datos[2]))
array_datos[2][1] = 25
print("Arreglo nuevo: "+ str(array_datos[2]))
#si, porque se modifica
"""

#importante= el return es para devolver la funcion 
def multi(a,b):
    return a*b
print(multi(10,100))
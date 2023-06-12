#Funciones
def mifuncion():
    print("hola mundo!")

#mifuncion()

def sumar():
    num1= 6
    num2= 5
    return(num1+num2)
    #return es como un print para regresar y mostrar valores
#print("La suma es: ", sumar())

#sumar a y b : osea dos numeros
def sumar(a,b):
    suma = a + b
    return(suma)
#num1= int(input("ingrese el primero numero: "))
#num2= int(input("ingrese el segundo numero: "))
#print(f"el resultado de la suma de {num1} + {num2} es : ",sumar(num1,num2))

#saludar
def saludo():
    print("Bienvenido usuario!")
#saludo()

#listar
#lent muestra lo que hay dentro de la lista.
lista = [10,50,100,1000,5000]
def listar():
    for i in range(len(lista)):
        print(lista[i])
#listar()

#eliminar un registro de la lista
#si elimino un valor que no existe, tirara un ValueError
def eliminar(valor):
    try:
        print("Elemento Eliminado!")
        lista.remove(valor)
    except ValueError:
        print("Error: Registro no existe ")
#num = int(input("ingrese el valor: "))
#eliminar(num)
#print(lista)
#Sumar todos los valores de lista 
def calcularLista():
    total = 0 
    for i in lista:
        total+=i
    return total
#sumaLista = calcularLista()

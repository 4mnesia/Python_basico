import numpy as np


print("Bienvenido , que desea servicios desea?")
print("1.- Grabar")
print("2.- Buscar")
print("3.- Imprimir certificado")
print("4.- Salir/Exit") 

opcion = int(input("Seleccione una opcion: "))

while opcion != 4:
   
    if opcion == 1:
        print("Selecciono grabar.")
        Nif = input("Niff: ")
        Edad= int(input("Edad: ")) 
        if Edad >= 0:
            print("Datos registrados")
        if Edad < 15:
            Nif = None
            print("No tienes Nif, ya que no eres mayor de 15 años")
        Nombre = str(input("Nombre: "))
        print("Datos Registrados")
        print(f"Su nombre es {Nombre}")
        print(f"Su edad es {Edad} años")
        print(f"Su Nif es : {Nif}")
        

    if opcion == 2:
        print("Selecciono buscar")
        nombreb = str(input("Seleccione el nombre: "))
        Edadb = int(input("Seleccione Edad: "))
        nifb = input("Seleccione nif: ")
        if nombreb == Nombre or Edadb == Edad or nifb == Nif:
            print(f"El nombre que buscaba es de {Nombre}")
            print(f"de {Edad} años")
            print(f"y su Nif es {Nif}")        
        else: 
            print("Datos no reconocidos")
    if opcion == 3:
        print("Imprimir certificado")
        import random
        print(f"certificado {random}")
        nombre = input("nombre: ")
        print(f"Nombre : {nombre}")
        Estado_coyugal = input("Solterx/casadx/viudx")
        print(f"Estado civil: {Estado_coyugal}")
        print("pertenece a la union europea?")
        Perte = input("si o no?")
        print(Perte)

    
   


def Guardar_info():
    print("Selecciono grabar.")
    numeroNif = input("seleccione los digitos")
    caracternif = input("seleccione los digitos")
    Nif = numeroNif + caracternif
    if Nif == int and Nif > 8:
        print("nif registrado")
    Edad= int(input("Edad: ")) 
    if Edad >= 0:
       print("Datos registrados")
    if Edad < 15:
        Nif = None
        print("No tienes Nif, ya que no eres mayor de 15 años")
    Nombre = str(input("Nombre: "))
    print("Datos Registrados")
    return
#Guardar_info()
def buscar():
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
def imprimir():
    import random
    print(f"certificado {random}")
    print(f"nombre : {Nombre}")
    Estado_coyugal = input("Solterx/casadx/viudx")
    Perte = input("pertenece a la union europea: si/no ")
    print("Certificado ADS")
    print(f"nombre: {}")
    
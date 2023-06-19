import numpy as np

print("Bienvenidos a VuelosDuoc")
print("1.- Entradas normales")
print("2.- Entradas VIP")
print("3.- Salir/Exit")
valornormal = 78900
valorpremiun = 240000
Anormal = np.arange(1, 31)
Apremiun = np.arange(31, 43)

opcion = int(input("Seleccione un tipo de entrada: "))

while opcion != 3:
    if opcion == 1:
        print("Escogiste normal")
        print("Estos asientos pertenecen a los pasajeros con entrada normal:")
        print(Anormal)
        Anormal = Anormal.reshape((6, 5))
        Anormal.sort(axis=1)
        print(Anormal)
        dato = int(input("Indique el asiento que desea: "))
        
        if dato < 1 or dato >= 31:
            print("Opción inválida")
        else:
            if dato in Anormal:
                Anormal = np.delete(Anormal, np.where(Anormal == dato))
                print("Asiento seleccionado con éxito.")
            else:
                print("El asiento no está disponible.")
        
    elif opcion == 2:
        print("Escogiste Premiun")
        print("Estos asientos pertenecen a los pasajeros con entrada premiun:")
        print(Apremiun)
        Apremiun = Apremiun.reshape((2, 6))
        Apremiun.sort(axis=1)
        print(Apremiun)
        dato = int(input("Indique el asiento que desea: "))
        
        if dato < 31 or dato >= 43:
            print("Opción inválida")
        else:
            if dato in Apremiun:
                Apremiun = np.delete(Apremiun, np.where(Apremiun == dato))
                print("Asiento seleccionado con éxito.")
            else:
                print("El asiento no está disponible.")
        
    else:
        print("See you later")
    
    opcion = int(input("Seleccione un tipo de entrada: "))

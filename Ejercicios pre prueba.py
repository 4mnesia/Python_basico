import numpy as np
print("Bienvenidos a VuelosDuoc")
print("1.- Entradas normales")
print("2.- Entradas VIP")
print("3.- Salir/Exit")
opcion= int(input("Seleccione un tipo de entrada: "))
Anormal = np.arange(1,31)
Apremiun = np.arange(31,43)
while opcion != 3:
    print("Estos asientos pertenecen a las pasajeros con entrada normal ")
    print(Anormal)
    print("Y estos son para entrada premiun ")
    print(Apremiun)

    if opcion == 1:
        print("Escogiste normal")
        print(Anormal)
        Anormal = Anormal.reshape((6, 5))
        Anormal.sort(axis=1)
        print(Anormal)
        dato = int(input("Indique el asiento que quiere"))
        if dato < 1:
            print("opcion invalida")
        if dato >= 30:
            print("te pasaste wey")
    if opcion == 2:
        print("Escogiste Premiun")
        print(Apremiun)
        Apremiun = Apremiun.reshape((2, 6))
        Apremiun.sort(axis=1)
        print(Apremiun)
        dato = int(input("Indique el asiento que quiere"))
        if dato < 30:
            print("opcion invalida")
        if dato >= 42:
            print("te pasaste wey")
    else:
        print("see you later")
        


        
        


        







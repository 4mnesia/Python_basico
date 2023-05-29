"""
lista  = [50, "mensaje" , 3.1415, {1,2,3}]
print(lista[-3])
"""
"""
lista = [1,2]
lista.append(3)
print(lista)
"""
"""
lista = [1, 4]
lista.insert(1, 2)
lista.insert(2,3)
print(lista)
"""
#append() es para agregar dato al final de la lista
lista = [1,5,15,25,100,500]
print("Inicial : ", lista)
lista.append(250)
print("Append : ", lista)
#extend([]) = extiende una lista con otra lista, osea agregandola
lista2 = [75,125]
lista.extend(lista2)
print("Extend: ", lista)
#insert() añade un elemento o dato en una posicion determinada, dependiendo del primer valor que le coloques con coma, como por ejemplo(1,x)
lista.insert(2,400)
print("Insert : ", lista)
#remove () busca y borra un dato de la lista
lista.remove(400)
print("Remove: ", lista)
#pop() elimina el ultimo registro
lista.pop()
print("Pop: ",lista)
#pop(posicion) elimina el dato ingresado
lista.pop(2)
print("Pop(2): " ,lista)
#reverse() invierte la lista
lista.reverse()
print("Reverse: ", lista)
#El sort() ordena los datos de menor a mayor
lista.sort()
print("Sort: ",lista)
#sort(reverse = true): ordena los datos de mayor a menor
lista.sort(reverse = True)
print("Sort(reverse): ", lista)

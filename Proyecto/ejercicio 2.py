#escribe una funcion llamada "es_positivo" que tome un numero como parametro y determine si es un numero positivo. La funcion debera devolver True si el numero es mayor que cero y False en caso contrario.
numero = int(input("selecciona un numero: "))
def es_positivo(numero):
    return numero > 0
resultado = es_positivo(numero)
print(resultado)
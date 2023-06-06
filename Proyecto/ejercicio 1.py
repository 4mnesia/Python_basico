def contar_palabras_diferentes(nombre_archivo):
    try:
        palabras_diferentes = set()
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                palabras = linea.lower().split()
                palabras_diferentes.update(palabras)

        cantidad_palabras_diferentes = len(palabras_diferentes)
        return cantidad_palabras_diferentes
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return 0
nombre_archivo=  r"C:\Users\flavi\Desktop\DUOC\holachivolo.txt"
cantidad_palabras = contar_palabras_diferentes(nombre_archivo)
print("La cantidad de palabras diferentes en el archivo es:", cantidad_palabras)
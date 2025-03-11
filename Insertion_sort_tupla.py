class OrderedRecordArray(object):
    def __init__(self, size):
        self.__a = [None] * size  # Lista con tamaño predefinido
        self.__size = size
        self.__count = 0  # Contador de elementos insertados

    def insert(self, record):
        if self.__count < self.__size:
            self.__a[self.__count] = record
            self.__count += 1
        else:
            raise IndexError("Array overflow.")


    def insertionSort(self):
        for i in range(1, self.__count):  # Comienza desde el segundo elemento
            temp = self.__a[i]  # Guarda el elemento que se va a insertar
            inner = i  # Variable para recorrer la lista
            # Compara el elemento con los elementos anteriores en la lista ordenada
            while inner > 0 and temp[0] < self.__a[inner - 1][0]:
                # Si el elemento en la posición inner es mayor que el de la posición anterior,
                # mueve el elemento hacia adelante
                self.__a[inner] = self.__a[inner - 1]
                inner -= 1  # Retrocede al siguiente elemento
            self.__a[inner] = temp  # Inserta el elemento en la posición correcta
        return self.__a  # Devuelve la lista ordenada



    def __str__(self):
        return str(self.__a[:self.__count])  # Muestra solo los elementos insertados


# Pruebas
array = OrderedRecordArray(3)  # Definir tamaño inicial de 3

# Insertar tuplas (clave numérica, valor)
array.insert((3, "b"))
array.insert((1, "c"))
array.insert((3, "a"))

# Mostrar lista sin ordenar
print("Array before sorting:", array)

# Aplicar ordenación y mostrar resultado
sorted_array = array.insertionSort()
print("\nArray after insertion sort:", sorted_array)

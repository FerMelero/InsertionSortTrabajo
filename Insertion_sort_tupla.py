class OrderedRecordArray:
    def __init__(self):
        self.__a = []  # Lista para almacenar las tuplas

    def insert(self, record):
        """Inserta una tupla (clave, valor) en la lista."""
        self.__a.append(record)  # Añade la tupla al final

    def insertionSort(self):
        """Devuelve una nueva lista ordenada con el algoritmo de ordenación por inserción."""
        sorted_list = self.__a[:]  # Copia de la lista original
        for i in range(1, len(sorted_list)):  
            temp = sorted_list[i]  
            inner = i  
            while inner > 0 and temp[0] < sorted_list[inner - 1][0]:  
                sorted_list[inner] = sorted_list[inner - 1]  
                inner -= 1  
            sorted_list[inner] = temp  
        return sorted_list  # Devuelve la lista ordenada

    def __str__(self):
        """Devuelve la lista sin ordenar como string."""
        return str(self.__a)


# Pruebas
array = OrderedRecordArray()

# Insertar tuplas (clave numérica, valor)
array.insert((2, "b"))
array.insert((1, "c"))
array.insert((2, "a"))

# Mostrar lista sin ordenar
print("Antes de ordenar:", array)

# Aplicar ordenación y mostrar resultado
sorted_array = array.insertionSort()
print("Después de ordenar:", sorted_array)

class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds
            return self.__a[n]  # Return item if in bounds

    def set(self, n, value):  # Set the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds
            self.__a[n] = value  # Only set item if in bounds

    def swap(self, j, k):  # Swap the values at 2 indices
        if 0 <= j < self.__nItems and 0 <= k < self.__nItems:  # Check if indices are in bounds
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):  # Insert item at end
        if self.__nItems >= len(self.__a):  # If array is full,
            raise Exception("Array overflow")  # Raise exception
        self.__a[self.__nItems] = item  # Item goes at current end
        self.__nItems += 1  # Increment number of items

    def find(self, item):  # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If found,
                return j  # Return index
        return -1  # Not found -> return -1

    def search(self, item):  # Search for item
        return self.get(self.find(item))  # Return item if found

    def delete(self, item):  # Delete first occurrence
        for j in range(self.__nItems):  # Loop through items
            if self.__a[j] == item:  # Found item
                self.__nItems -= 1  # One fewer at end
                for k in range(j, self.__nItems):  # Shift items left
                    self.__a[k] = self.__a[k + 1]
                return True  # Return success flag
        return False  # Couldn't find the item

    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems):  # Apply function
            function(self.__a[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket,
                ans += ", "  # Separate items with comma
            ans += str(self.__a[i])  # Add string form of item
        ans += "]"  # Close with right bracket
        return ans

    def insertionSort(self):  
        for i in range(1, self.__nItems):  # Comenzamos desde el segundo elemento
            temp = self.__a[i]  # Guardamos el valor actual que vamos a insertar
            inner = i  # Empezamos comparando desde la posición actual
            
            # Desplazamos elementos a la derecha si son mayores que temp
            while inner > 0 and temp < self.__a[inner - 1]:  
                self.__a[inner] = self.__a[inner - 1]  # Movemos el elemento a la derecha
                inner -= 1  # Retrocedemos en la lista para seguir comparando
                
            self.__a[inner] = temp  # Insertamos el valor en su posición correcta

    

arr = Array(5)
arr.insert(3)
arr.insert(2)
arr.insert(10)
arr.insert(1)
arr.insert(6)

print("Array before sorting:")
arr.traverse()

arr.insertionSort()
print("\nArray after insertion sort")
arr.traverse()



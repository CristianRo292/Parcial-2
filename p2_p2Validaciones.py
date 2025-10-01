# English: Class for validations and calculations
# Español: Clase para validaciones y cálculos
class validaciones():
    # English: Constructor method to initialize instance variables
    # Español: Método constructor para inicializar variables de instancia
    def __init__(self):
        # English: Variable to store the sum of numbers
        # Español: Variable para almacenar la suma de números
        self.suma = 0
        # English: Variable to store the average
        # Español: Variable para almacenar el promedio
        self.prom = 0.0

    # English: Method to validate if a string contains only digits
    # Español: Método para validar si una cadena contiene solo dígitos
    def validarNumeros(self,valor):
        # English: Check if the string consists only of digits
        # Español: Verifica si la cadena consiste solo de dígitos
        if valor.isdigit():
            # English: Return True if it's a valid number
            # Español: Retorna True si es un número válido
            return True
        # English: Return False if it's not a valid number
        # Español: Retorna False si no es un número válido
        return False
    
    # English: Method to calculate the average of a list of numbers
    # Español: Método para calcular el promedio de una lista de números
    def Promedio(self, lista):
        # English: Iterate through each element in the list
        # Español: Itera a través de cada elemento en la lista
        for i in lista:
            # English: Accumulate the sum of all elements
            # Español: Acumula la suma de todos los elementos
            self.suma += i
        
        # English: Calculate the average (sum divided by number of elements)
        # Español: Calcula el promedio (suma dividida por el número de elementos)
        self.prom = self.suma / len(lista)
        # English: Return the calculated average
        # Español: Retorna el promedio calculado
        return self.prom
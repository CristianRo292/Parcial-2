class validaciones():
    def __init__(self):
        self.suma = 0
        self.prom = 0.0

    def validarNumeros(self,valor):
        if valor.isdigit():
            return True
        return False
    
    def Promedio(self, lista):
        for i in lista:
            self.suma += i
        
        self.prom = self.suma / len(lista)
        return self.prom
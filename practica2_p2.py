from p2_p2Validaciones import validaciones
val = validaciones()



class principal(): 
    def __init__(self): # contructor, primer codigo que siempre se ejecuta primero, aqui se carga todo lo que ballas a necesitar
        self.lista = []
        self.num = 0
        self.a = ""


    def inicio(self):
        self.a = input("Escribe una calificacion: \n")
        if val.validarNumeros(self.a):
            self.num += 1
            self.lista.append(int(self.a))

            if self.num >= 5:

                print(self.lista)
                print(val.Promedio(self.lista))
            else:
                return self.inicio() # ya no se ocupa mandar parematero porque ya esta la variable en el entorno
        else:
            print('No es un numero')
            self.inicio()

if __name__== "__main__":
    app = principal()
    app.inicio()
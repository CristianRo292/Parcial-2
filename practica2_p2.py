from p2_p2Validaciones import validaciones   # Importa la clase validaciones desde otro archivo / Imports the class 'validaciones' from another file
val = validaciones()  # Crea un objeto de la clase validaciones / Creates an object of the class 'validaciones'


class principal(): 
    def __init__(self): 
        # constructor, primer código que siempre se ejecuta / constructor, first code that always runs
        # aquí se cargan las variables necesarias / here the needed variables are initialized
        self.lista = []   # lista vacía para guardar calificaciones / empty list to store grades
        self.num = 0      # contador de cuántas calificaciones se han ingresado / counter of how many grades have been entered
        self.a = ""       # variable para guardar la calificación temporal / variable to temporarily store the grade


    def inicio(self):
        self.a = input("Escribe una calificacion: \n")  # pide una calificación al usuario / asks the user for a grade
        if val.validarNumeros(self.a):  # valida si el dato ingresado es un número / checks if the entered data is a number
            self.num += 1  # incrementa el contador en 1 / increases the counter by 1
            self.lista.append(int(self.a))  # convierte la entrada a entero y la agrega a la lista / converts the input to integer and appends it to the list

            if self.num >= 5:  # cuando ya se ingresaron 5 calificaciones / when 5 grades have been entered
                print(self.lista)  # imprime la lista de calificaciones / prints the list of grades
                print(val.Promedio(self.lista))  # llama la función Promedio para calcular el promedio / calls Promedio function to calculate the average
            else:
                return self.inicio()  
                # se vuelve a llamar a sí misma hasta llegar a 5 / calls itself again until reaching 5
                # ya no se necesita pasar parámetros porque las variables están en el objeto / no need to pass parameters since variables are in the object
        else:
            print('No es un numero')  # si el dato no es número / if the input is not a number
            self.inicio()  # vuelve a pedir la calificación / asks again for the grade


if __name__== "__main__":  
    app = principal()   # crea un objeto de la clase principal / creates an object of the class 'principal'
    app.inicio()        # ejecuta el programa / runs the program

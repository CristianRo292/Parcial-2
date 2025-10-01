from tkinter import * 
from tkinter import messagebox  # Importa módulo para mostrar mensajes emergentes / imports module to show popup messages

class Ventana():
    def __init__(self):
        # Crear ventana principal / Create main window
        self.ven = Tk() 
        self.ven.title('Programa 1 con Ventanas')  # Título de la ventana / window title
        self.ven.geometry('400x200')  # Tamaño de la ventana / window size
        # todo debe ir dentro de aquí / everything must go inside this window
        # pack solo permite un elemento por renglón / pack only allows one element per row
        # Label(ven, text = "Hola mundo").pack()
        self.inicio()  # Llama al método que crea los widgets / calls the method that creates the widgets
       
    def inicio(self):
        # Etiqueta y caja de texto para usuario / Label and entry for username
        Label(self.ven, text = "Usuario: ").pack(pady=10)
        self.us = Entry(self.ven)  
        self.us.pack(pady= 3)

        # Etiqueta y caja de texto para contraseña / Label and entry for password
        Label(self.ven, text = "Pasword: ").pack(pady=10)  # pady: espacio vertical / vertical padding
        self.pas = Entry(self.ven)  
        self.pas.pack(pady=5)

        # Botón que ejecuta la validación / Button that runs validation
        self.boton = Button(self.ven,text='Aceptar',command=self.revisar)
        self.boton.pack(pady=3)
        
        self.ven.mainloop()  # Mantiene la ventana activa hasta que se cierre / keeps window running until closed


    def revisar(self):
        # Función que valida los datos / Function that validates data
        try:
            self.u = str(self.us.get())  # Obtiene lo escrito en usuario / gets what was typed in username
            self.p = str(self.pas.get()) # Obtiene lo escrito en password / gets what was typed in password

            if self.u == "" or self.p == "":  # Verifica que no estén vacíos / Checks if empty
                messagebox.showerror("Error","Faltan datos")
            else: 
                # Validación básica de usuario y contraseña / Basic user & password validation
                if self.u == "admin" and self.p == "12345":
                    messagebox.showinfo("Validacion","Usuario y contrasela Correctos")
                else:
                    messagebox.showerror('Error','Usuario y/o contraseña incorrectos')
            
        except ValueError:
            # Manejo de error si ocurre un problema inesperado / Handles unexpected input errors
            messagebox.showerror('Error','Introduce datos')



if __name__=="__main__":
    app = Ventana()  # Crea la instancia de la clase y lanza la app / Creates instance of the class and runs app

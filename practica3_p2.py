from tkinter import * 
from tkinter import messagebox   # Importa el módulo para mostrar mensajes emergentes / Imports the module to show popup messages


def Ventana():

    def revisar():
        try:
            u = str(us.get())   # obtiene el texto escrito en la caja de usuario / gets the text typed in the user entry
            p = str(pas.get())  # obtiene el texto escrito en la caja de contraseña / gets the text typed in the password entry
            if u == "" or p == "":  # valida que no estén vacíos / checks if either is empty
                messagebox.showerror("Error","Faltan datos")  # muestra error si faltan datos / shows error if data is missing
            else: 
                if u == "admin" and p == "12345":  # validación simple de usuario y contraseña / simple user and password validation
                    messagebox.showinfo("Validacion","Usuario y contrasela Correctos")  
                    # muestra mensaje de éxito / shows success message

                else:
                    messagebox.showerror('Error','Usuario y/o contraseña incorrectos')
                    # muestra error si usuario o contraseña son incorrectos / shows error if user or password are wrong
            
        except ValueError:
            messagebox.showerror('Error','Introduce datos')  
            # en caso de que haya un error inesperado con los datos / in case of unexpected error with input


    ven = Tk()  # crea la ventana principal / creates the main window
    ven.title('Programa 1 con Ventanas')  # título de la ventana / window title
    ven.geometry('400x200')  # define el tamaño de la ventana / defines window size

    # todo debe ir dentro de aquí / everything must go inside this window
    # pack solo permite un elemento por renglón / pack only allows one element per row

    Label(ven, text = "Usuario: ").pack(pady=10)  # etiqueta para el usuario / label for username
    us = Entry(ven)  # caja de texto para usuario / input box for username
    us.pack(pady= 3)

    Label(ven, text = "Pasword: ").pack(pady=10)  # etiqueta para contraseña / label for password
    pas = Entry(ven)  # caja de texto para contraseña / input box for password
    pas.pack(pady=5)

    boton = Button(ven,text='Aceptar',command=revisar)  
    # botón que llama a la función revisar / button that calls revisar function
    boton.pack(pady=3)
    
    ven.mainloop()  # mantiene la ventana abierta hasta que se cierre / keeps the window open until it is closed



if __name__=="__main__":
    Ventana()  # ejecuta la función principal / runs the main function

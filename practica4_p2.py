from tkinter import * 
from tkinter import messagebox

class Ventana():
    def __init__(self):
        self.ven = Tk() 
        self.ven.title('Programa 1 con Ventanas')
        self.ven.geometry('400x200')
        # todo debe ir dentro de qui
        # pack solo permite un elemtno por renglon
        # Label(ven, text = "Hola mundo").pack()
        self.inicio()
       
    def inicio(self):
        Label(self.ven, text = "Usuario: ").pack(pady=10)
        self.us = Entry(self.ven)
        self.us.pack(pady= 3)
        Label(self.ven, text = "Pasword: ").pack(pady=10) # pady 
        self.pas = Entry(self.ven)
        self.pas.pack(pady=5)
        self.boton = Button(self.ven,text='Aceptar',command=self.revisar)
        self.boton.pack(pady=3)
        
        self.ven.mainloop()


    def revisar(self):
        
        try:
            self.u = str(self.us.get())
            self.p = str(self.pas.get())
            if self.u == "" or self.p == "":
                messagebox.showerror("Error","Faltan datos")
            else: 
                if self.u == "admin" and self.p == "12345":
                    messagebox.showinfo("Validacion","Usuario y contrasela Correctos")

                else:
                    messagebox.showerror('Error','Usuario y/o contraseña incorrectos')

            
        except ValueError:
            messagebox.showerror('Error','Introduce datos')
        





if __name__=="__main__":
    app = Ventana()
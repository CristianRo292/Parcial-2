
from tkinter import * 
from tkinter import messagebox


def Ventana():

    def revisar():
        try:
            u = str(us.get())
            p = str(pas.get())
            if u == "" or p == "":
                messagebox.showerror("Error","Faltan datos")
            else: 
                if u == "admin" and p == "12345":
                    messagebox.showinfo("Validacion","Usuario y contrasela Correctos")

                else:
                    messagebox.showerror('Error','Usuario y/o contraseña incorrectos')

            
        except ValueError:
            messagebox.showerror('Error','Introduce datos')


    ven = Tk() 
    ven.title('Programa 1 con Ventanas')
    ven.geometry('400x200')
    # todo debe ir dentro de qui
    # pack solo permite un elemtno por renglon
    # Label(ven, text = "Hola mundo").pack()
    Label(ven, text = "Usuario: ").pack(pady=10)
    us = Entry(ven)
    us.pack(pady= 3)
    Label(ven, text = "Pasword: ").pack(pady=10) # pady 
    pas = Entry(ven)
    pas.pack(pady=5)
    boton = Button(ven,text='Aceptar',command=revisar)
    boton.pack(pady=3)
    
    ven.mainloop()



if __name__=="__main__":
    Ventana()
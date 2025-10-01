'''hacer programa que lea nombre y 3 calificaciones que se agregara a una lista con las siguietes restricciones:
- las calififcaiones se agregaran en orden desendente, una vez registrado esto se realizara una pregunta 
si desea agregar otra persona, si la respuesta es si, la primer lista se agregara a otra lista que contenga los
4 datos, para agregar otra persona'''

from tkinter import *
from tkinter import messagebox


class Ventana():
    def __init__(self):
        self.lista = []  # lista principal donde se guardarán todos los registros / main list to store all records
        self.ven = Tk()  # crea la ventana principal / creates the main window
        self.ven.title("Registro de calificacion")  # título de la ventana / window title
        self.ven.geometry("400x200")  # tamaño de la ventana / window size
        self.inicio()  # llama a la función que dibuja los widgets / calls function to draw widgets

    def inicio(self):
        # Etiqueta y entrada para el nombre / Label and entry for name
        Label(self.ven, text = "Nombre: ").pack(pady  = 10)
        self.name = Entry(self.ven)
        self.name.pack(pady = 3)

        # Etiquetas y entradas para calificaciones / Labels and entries for grades
        Label(self.ven, text = "Calificacion 1: ").pack(pady = 10)
        self.cal1 = Entry(self.ven)
        self.cal1.pack(pady = 3)

        Label(self.ven, text = "Calificacion 2: ").pack(pady = 10)
        self.cal2 = Entry(self.ven)
        self.cal2.pack(pady = 3)

        Label(self.ven, text = "Calificacion 3: ").pack(pady = 10)
        self.cal3 = Entry(self.ven)
        self.cal3.pack(pady = 3)

        # Botón para agregar otro registro / button to add another record
        self.botonAg = Button(self.ven, text = "Agregar otro", command = self.estruct)
        self.botonAg.pack(pady = 2)

        # Botón para salir y mostrar lista final / button to exit and show final list
        self.botonSalir = Button(self.ven, text = "Salir", command = self.fin)
        self.botonSalir.pack(pady = 2)

        self.ven.mainloop()  # mantiene abierta la ventana / keeps window open
    
    
    def fin(self):
         self.estruct()  # guarda el último registro antes de salir / saves last record before exiting
         messagebox.showinfo("Registro",self.lista)  # muestra lista final / shows final list
         exit(0)  # cierra el programa / closes program

    def estruct(self):
        temlis = []  # lista temporal para un registro (nombre + calificaciones) / temp list for one record

        try : 
            # obtiene valores de las entradas / gets values from entries
            self.nam = str(self.name.get())
            self.c1 = int(self.cal1.get())
            self.c2 = int(self.cal2.get())
            self.c3 = int(self.cal3.get())
    
            temlis.append(self.nam)  # agrega nombre / adds name
            temlis.append(self.c1)   # agrega calificación 1 / adds grade 1
            temlis.append(self.c2)   # agrega calificación 2 / adds grade 2
            temlis.append(self.c3)   # agrega calificación 3 / adds grade 3

            # ordena calificaciones de mayor a menor (sin mover nombre) / sorts grades descending (name fixed)
            temlis = self.orden(temlis)  

            # agrega el registro ya ordenado a la lista principal / adds sorted record to main list
            self.lista.append(temlis)

            messagebox.showinfo("Registro",f"registro guardado: {temlis}")
            
        except ValueError:
            messagebox.showerror('Error','Introduce datos')  # error si no es número / error if not a number

    def orden(self,lis):
        # ordenamiento tipo burbuja para posiciones 1 a n (sin afectar el nombre en [0]) 
        # bubble sort for positions 1 to n (keeps name at [0])
        ext = len(lis)
        for i in range(1, ext):
            for j in range(1, ext - 1 - i):
                if lis[j] < lis[j+1]:
                    aux = lis[j]
                    lis[j] = lis[j+1]
                    lis[j+1] = aux
    
        return lis  # regresa la lista ordenada / returns sorted list


if __name__ == "__main__":
    app = Ventana()  # instancia la clase y ejecuta la app / instantiates class and runs the app

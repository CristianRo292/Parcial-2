from tkinter import *
from tkinter import messagebox

class Ventana():
    def __init__(self):
        # Lista principal para almacenar todos los registros / Main list to store all records
        self.lista = []

        # Crea la ventana principal de Tkinter / Create the main Tkinter window
        self.ven = Tk()
        self.ven.title("Registro de calificacion")  # Título de la ventana / Window title
        self.ven.geometry("400x600")  # Tamaño de la ventana / Window size

        # Llama al método que crea todos los widgets / Call method to create all widgets
        self.inicio()

    def inicio(self):
        # Etiqueta y caja de texto para el nombre / Label and entry for the name
        Label(self.ven, text = "Nombre: ").pack(pady  = 10)
        self.name = Entry(self.ven)
        self.name.pack(pady = 3)

        # Etiqueta y caja de texto para la calificación 1 / Label and entry for grade 1
        Label(self.ven, text = "Calificacion 1: ").pack(pady = 10)
        self.cal1 = Entry(self.ven)
        self.cal1.pack(pady = 3)

        # Etiqueta y caja de texto para la calificación 2 / Label and entry for grade 2
        Label(self.ven, text = "Calificacion 2: ").pack(pady = 10)
        self.cal2 = Entry(self.ven)
        self.cal2.pack(pady = 3)

        # Etiqueta y caja de texto para la calificación 3 / Label and entry for grade 3
        Label(self.ven, text = "Calificacion 3: ").pack(pady = 10)
        self.cal3 = Entry(self.ven)
        self.cal3.pack(pady = 3)

        # Botón para agregar otro registro / Button to add another record
        self.botonAg = Button(self.ven, text = "Agregar otro", command = self.estruct)
        self.botonAg.pack(pady = 2)

        # Botón para finalizar el registro y mostrar todos los datos / Button to finish registration and show all data
        self.botonSalir = Button(self.ven, text = "Salir", command = self.fin)
        self.botonSalir.pack(pady = 2)

        # Mantiene la ventana abierta / Keep the window running
        self.ven.mainloop()
    
    def fin(self):
        # Guarda el último registro antes de salir / Save the last record before exiting
        self.estruct()

        # Muestra todos los registros almacenados / Show all stored records
        messagebox.showinfo("Registro", self.lista)

        # Cierra la aplicación / Close the application
        exit(0)

    def estruct(self):
        # Lista temporal para almacenar un solo registro / Temporary list for a single record
        temlis = []
        
        try: 
            # Obtiene el nombre y calificaciones desde los Entry / Get name and grades from Entry widgets
            self.nam = str(self.name.get())
            self.c1 = int(self.cal1.get())
            self.c2 = int(self.cal2.get())
            self.c3 = int(self.cal3.get())

            # Validación: no debería ser necesario porque int() ya lanza ValueError si está vacío
            # Si los datos son válidos, llama a la función de ordenamiento / If data is valid, call sorting function
            if not(self.nam == "" or self.c1 == "" or self.c2 == "" or self.c3 == ""):
                self.orden()
                
        except ValueError:
            # Muestra un mensaje de error si las calificaciones no son números válidos / Show error if grades are not valid numbers
            messagebox.showerror('Error','Introduce datos')

    def orden(self):
        # Lista temporal para almacenar los datos ordenados / Temporary list to store sorted data
        lista1 = []

        # Variables locales para mayor claridad / Local variables for clarity
        nom = self.nam
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3

        # Bloque de condicionales para ordenar las calificaciones de mayor a menor
        # Se mantiene el nombre en la primera posición / Conditional block to sort grades descending, keeping name first
        if (c1 > c2):
            if (c1 > c3):
                print(f"es mayor {c1}")
                lista1.append(nom)
                lista1.append(c1)
                if (c2 > c3):
                    print(f"es el de enmedio {c2}")
                    print(f"es el menor {c3}")
                    lista1.append(c2)
                    lista1.append(c3)
                    self.lista.append(lista1)  # Guarda el registro en la lista principal / Save record to main list
                else:
                    print(f"es el de enmedio{c3}")
                    print(f"el menor es {c2}")
                    lista1.append(c3)
                    lista1.append(c2)
                    self.lista.append(lista1)
            else:
                print(f"es el de enmedio {c1}")
                print(f"es el mayor {c3}")
                print(f"es el menor {c2}")
                lista1.append(nom)
                lista1.append(c3)
                lista1.append(c1)
                lista1.append(c2)
                self.lista.append(lista1)
        else:
            if (c2 > c3):
                print(f"Es mayor {c2}")
                lista1.append(nom)
                lista1.append(c2)
                if (c1 > c3):
                    print(f"El de en medio es {c1}")
                    print(f"es el menor {c3}")
                    lista1.append(c1)
                    lista1.append(c3)
                    self.lista.append(lista1)
                else:
                    print(f"es el de enmedio {c3}")
                    print(f"es el menor {c1}")
                    lista1.append(c3)
                    lista1.append(c1)
                    self.lista.append(lista1)
            else:
                print(f' es el de en medio {c2}')
                print(f' es mayor {c3}')
                print(f' es el de en menor {c1}')
                lista1.append(nom)
                lista1.append(c3)
                lista1.append(c2)
                lista1.append(c1)
                self.lista.append(lista1)

        # Muestra un mensaje indicando que el registro se guardó correctamente / Show a message indicating the record was saved
        messagebox.showinfo("Registro", f"re gistro guardado: {lista1}")

if __name__ == "__main__":
    # Instancia la clase Ventana y ejecuta la aplicación / Instantiate the Ventana class and run the application
    app = Ventana()

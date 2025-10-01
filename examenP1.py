'''hacer programa que lea nombre y 3 calificaciones que se agregara a una lista con las siguietes restricciones:
- las calififcaiones se agregaran en orden desendente, una vez registrado esto se realizara una pregunta 
si desea agregar otra persona, si la respuesta es si, la primer lista se agregara a otra lista que contenga los
4 datos, para agregar otra persona'''

# def inicio():
#     lista1 = []
#     nom = input("Escribe un nombre: ")
#     c1 = int(input("Escribe una calificacion: "))
#     c2 = int(input("Escribe una calificacion: "))
#     c3 = int(input("Escribe una calificacion: "))
#     lista1.append(nom)
#     lista1.append(c1)
#     lista1.append(c2)
#     lista1.append(c3)
#     lista2.append(ordenar(lista1))

# def ordenar(lis):
    
#     ext = len(lis)
#     for i in range(1, ext):
#         for j in range(1, ext - 1 - i):
#             if lis[j] < lis[j+1]:
#                 aux = lis[j]
#                 lis[j] = lis[j+1]
#                 lis[j+1] = aux
    
#     return lis

def inicio():
    # Initialize an empty list to store the current person's data (name and sorted grades)
    # Inicializa una lista vacía para almacenar los datos de la persona actual (nombre y calificaciones ordenadas)
    lista1 = []
    
    # Prompt user to input a name
    # Solicita al usuario que ingrese un nombre
    nom = input('Escribe un nombre')
    
    # Prompt user to input three grades as integers
    # Solicita al usuario que ingrese tres calificaciones como enteros
    c1 = int(input("Escribe una calificacion"))
    c2 = int(input("Escribe una calificacion"))
    c3 = int(input("Escribe una calificacion"))

    # Compare the three grades to sort them in descending order manually
    # Compara las tres calificaciones para ordenarlas manualmente en orden descendente
    if (c1 > c2):
        if (c1 > c3):
            # c1 is the highest grade
            # c1 es la calificación más alta
            print(f"es mayor {c1}")
            lista1.append(nom)
            lista1.append(c1)
            if (c2 > c3):
                # c2 is middle, c3 is lowest
                # c2 es la del medio, c3 es la más baja
                print(f"es el de enmedio {c2}")
                print(f"es el menor {c3}")
                lista1.append(c2)
                lista1.append(c3)
                lista2.append(lista1)
            else:
                # c3 is middle, c2 is lowest
                # c3 es la del medio, c2 es la más baja
                print(f"es el de enmedio{c3}")
                print(f"el menor es {c2}")
                lista1.append(c3)
                lista1.append(c2)
                lista2.append(lista1)

        else:
            # c3 is highest, c1 is middle, c2 is lowest
            # c3 es la más alta, c1 es la del medio, c2 es la más baja
            print(f"es el de enmedio {c1}")
            print(f"es el mayor {c3}")
            print(f"es el menor {c2}")
            lista1.append(nom)
            lista1.append(c3)
            lista1.append(c1)
            lista1.append(c2)
            lista2.append(lista1)
    else:
        if (c2 > c3):
            # c2 is the highest grade
            # c2 es la calificación más alta
            print(f"Es mayor {c2}")
            lista1.append(nom)
            lista1.append(c2)
            if (c1 > c3):
                # c1 is middle, c3 is lowest
                # c1 es la del medio, c3 es la más baja
                print(f"El de en medio es {c1}")
                print(f"es el menor {c3}")
                lista1.append(c1)
                lista1.append(c3)
                lista2.append(lista1)
            else:
                # c3 is middle, c1 is lowest
                # c3 es la del medio, c1 es la más baja
                print(f"es el de enmedio {c3}")
                print(f"es el menor {c1}")
                lista1.append(c3)
                lista1.append(c1)
                lista2.append(lista1)
        else:
            # c3 is highest, c2 is middle, c1 is lowest
            # c3 es la más alta, c2 es la del medio, c1 es la más baja
            print(f' es el de en medio {c2}')
            print(f' es mayor {c3}')
            print(f' es el de en menor {c1}')
            lista1.append(nom)
            lista1.append(c3)
            lista1.append(c2)
            lista1.append(c1)
            lista2.append(lista1)

# Global list to store all registered persons with their sorted grades
# Lista global para almacenar todas las personas registradas con sus calificaciones ordenadas
lista2 = []

if __name__=="__main__":
    # Infinite loop to keep registering people until user decides to stop
    # Bucle infinito para seguir registrando personas hasta que el usuario decida detenerse
    while(True):

        # Call the function to register a new person
        # Llama a la función para registrar una nueva persona
        inicio()
        
        # Ask user if they want to add another person
        # Pregunta al usuario si desea agregar otra persona
        a = input("desea agregar otra persona s/n")
        
        # If user inputs any form of "no", print the final list and exit
        # Si el usuario ingresa cualquier forma de "no", imprime la lista final y sale
        if a in ("n,N,NO,no,No"):
            print(lista2)
            break
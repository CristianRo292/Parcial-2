'''hacer programa que lea nombre y 3 calificaciones que se agregara a una lista con las siguietes restricciones:
- las calififcaiones se agregaran en orden desendente, una vez registrado esto se realizara una pregunta 
si desea agregar otra persona, si la respuesta es si, la primer lista se agregara a otra lista que contenga los
4 datos, para agregar otra persona'''

def inicio():
    lista1 = []  # lista temporal para guardar nombre y calificaciones / temporary list to store name and grades
    nom = input("Escribe un nombre: ")  # pide nombre / asks for a name
    c1 = int(input("Escribe una calificacion: "))  # pide calificación 1 / asks for grade 1
    c2 = int(input("Escribe una calificacion: "))  # pide calificación 2 / asks for grade 2
    c3 = int(input("Escribe una calificacion: "))  # pide calificación 3 / asks for grade 3
    lista1.append(nom)  # agrega el nombre en la lista / adds name to the list
    lista1.append(c1)   # agrega calificación 1 / adds grade 1
    lista1.append(c2)   # agrega calificación 2 / adds grade 2
    lista1.append(c3)   # agrega calificación 3 / adds grade 3
    lista2.append(ordenar(lista1))  # manda a ordenar y guarda en la lista principal / sorts and stores in main list

def ordenar(lis):
    # ordena de manera descendente (de mayor a menor) / sorts in descending order
    ext = len(lis)  # obtiene la longitud de la lista / gets length of the list
    for i in range(1, ext):  # recorre desde el segundo elemento (porque el primero es el nombre) / loops from 2nd element
        for j in range(1, ext - 1 - i):  # compara entre calificaciones / compares grades
            if lis[j] < lis[j+1]:  # si el actual es menor al siguiente, intercambia / if current < next, swap
                aux = lis[j]       # guarda temporal / temp store
                lis[j] = lis[j+1]  
                lis[j+1] = aux
    
    return lis  # regresa la lista ya ordenada / returns sorted list



lista2 = []  # lista final donde se guardan todas las personas con sus calificaciones / final list to store all students

if __name__=="__main__":
    while(True):  # ciclo para preguntar si se agregan más personas / loop to ask if more people should be added

        inicio()  # ejecuta la función de captura / runs the input function
        a = input("desea agregar otra persona s/n")  # pregunta si se desea continuar / asks if user wants to continue
        if a in ("n,N,NO,no,No"):  # si la respuesta es no, se termina / if answer is no, program ends
            print(lista2)  # muestra la lista completa de personas con sus calificaciones / prints full list
            break  # rompe el ciclo / breaks the loop

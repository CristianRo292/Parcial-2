
def inicio(num):
    # global num # indico que voy a usar la variable publica num / I indicate that I will use the public variable num
    a = int(input("Escribe una calificacion: \n"))  # pide una calificación al usuario / asks the user for a grade
    num += 1  # incrementa el contador en 1 / increases the counter by 1
    lista.append(a)  # agrega la calificación a la lista / adds the grade to the list

    if num >= 5:  # si ya se han ingresado 5 calificaciones / if 5 grades have been entered
        print(lista)  # imprime la lista de calificaciones / prints the list of grades
    else:
        return inicio(num)  # vuelve a llamar la función hasta llegar a 5 / calls the function again until reaching 5


lista = []  # lista vacía para guardar las calificaciones / empty list to store the grades
global num # declaro que es una bariable global / declare that num is a global variable
num = 0 # defino num con valor inicial en 0 / define num with initial value 0

if __name__=="__main__":
    inicio(num)  # llama a la función principal para iniciar / calls the main function to start

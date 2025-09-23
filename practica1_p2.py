
def inicio(num):
    # global num # indico que voy a usar la variable publica num
    a = int(input("Escribe una calificacion: \n"))
    num += 1
    lista.append(a)

    if num >= 5: 
        print(lista)
    else:
        return inicio(num)


lista = []
global num # declaro que es una bariable global
num = 0 # defino num

if __name__=="__main__":
    inicio(num)
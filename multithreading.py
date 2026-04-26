#multithreading = use to perform multiple tasks concurrently (multitasking)
                # good for I/O bound tasks like reading files or fetching data from APIs    
                #Permite usar multiple funciones en un mismo tiempo.
import threading
import time

def walk_dog(first, last):
    time.sleep(8)#pasaran 8 segundo hasta que imprima en pantalla
    print(f"You finish walking the {first} {last}.")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

#walk_dog()
#take_out_trash()
#get_mail()
#mediante los modulos de threading podemos "saltarnos" el orden prediseñado de python. De esta manera las funciones seran llamadas al mismo tiempo. Cada uno funcionando aparte 
#es como tener programas en segundo plano.

chore1 = threading.Thread(target=walk_dog, args=("Scooby","Doo"))#mandamos el valor mediante argumento. y ponemos la coma como tpple; Es necesario la coma sino se rompera el programa, al interpretarlo como string (En caso de tener 1 solo valor)
chore1.start()                                         

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()#Pondra el programa en pausar hasta que termine los chore, o que termine la funcion.
chore2.join()
chore3.join()

print("All chores are complete!!")

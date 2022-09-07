#CICLO MIENTRAS 

#DECLARAR UNA VARIABLE CENTINELA 
#O VARIABLE DE CONTROL PARA EVALUAR LA EJECUCION DEL PROCESO 

from ast import If


i=0
#menu de opciones

print("***MENU***")
print("1. SUMAR DOS NUMEROS ")
print("2. RESTAR DOS NUMEROS ")
print("3. ENCONTRAR LA RAIZ CUADRADA DE UN NUMERO  ")
print("4. MULTIPLICAR 2 NUMEROS ")
print("5. SALIR ")



#programar la estructura del ciclo mientras

while(i!=5):
    i=int(input("Digite un OPCION DEL MENU:" ))
    numero1= int (input("Digite el numero 1"))
    numero2= int (input("Digite el numero 2"))

    if (i==1):
        total=numero1+numero2
        print("La suma de los dos numeros es: ",total)

    elif(i==2):
         print("chao")
    elif(i==3):
         print("Medellin")
    elif(i==4):
         print("no llueve en medallo")
    elif(i==5):
         break
    else:
        print("Digita una opcion valida ")

print("Salimos del While  ")
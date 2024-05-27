#Bucles for: Básico 1

# Ejercicio uno: Imprimir todo los numeros enteros del 0 al 100:

for a in range(101):
    print(a)

# Ejercicio dos: Imprimir los numeros múltiplos de 2 entre 2 y 500-

for b in range(2, 501, 2):
    print(b)

# Ejercicio tres: Imprimir los números enteros del 1 al 100. Si es divisible
# por 5 imprimir "ice ice" en vez del número. Si es divisible por 10, imprime "baby".

for c in range(1, 101, 5):
    print("ice ice")
    if c in range(1, 101, 10):
        print("baby")

#Sumar los números pares del 0 al 500,000 e imprimir la suma total:

#sumatoria = 0
#for d in range(0, 500001,2):
    #sumatoria += d
    #print(sumatoria)

#Imprimir los numeros positivos comenzando desde 2024 en cuenta regresiva de 3 en 3.

for e in range(2024, 0, -3):
    print(e)

#Establecer 3 variables:  numInicial, numFinal y multiplo. 

numInicial = 5
numFinal = 20
multiplo = 4

for f in range(5, 21, 4):
    print(f)

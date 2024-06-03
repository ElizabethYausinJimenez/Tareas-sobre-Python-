#Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]

from pprint import pprint

#Ejercicio 1: Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]

matriz[1][0] = 6
print(matriz)

#Ejercicio 2: Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)


#Ejercicio 3: En ciudades, cambia “Cancún” por “Monterrey”.

ciudades["México"][2] = "Monterrey"

print(ciudades)

#Ejercicio 4: En las coordenadas, cambia el valor de “latitud” por 9.9355431

coordenadas[0]["latitud"] = 9.9355431

print(coordenadas)


cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente

for iterarDiccionario in cantantes:

    print(iterarDiccionario)


for iterarDiccionario in cantantes:
    print(f"nombre - {iterarDiccionario['nombre']}, pais - {iterarDiccionario['pais']}")


#Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for cantante in cantantes:
        print(cantante[llave], "\n") 
iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)

#Iterar a través de un diccionario con valores de lista:

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):    
    for llave in diccionario.keys():
        print(len(diccionario[llave]), llave.upper(), "\n")
        for elemento in diccionario[llave]:
            print(elemento, "\n")

imprimirInformacion(costa_rica)

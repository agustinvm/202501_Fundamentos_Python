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
 
#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0] = 6
print(matriz)

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0] = "Enrique Martin Morales"
print(cantantes)

#En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"
print(ciudades)

#En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la 
#lista e imprima cada llave y el valor correspondiente. Por ejemplo:
#BONUS: Que aparezcan en este formato:
#nombre - Ricky Martin, pais - Puerto Rico

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

def iterarDiccionario(lista):
    for diccionario in lista:
        print(", ".join(f"{key} - {value}" for key, value in diccionario.items()))

iterarDiccionario(cantantes)

#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios.
#La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. 
#Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir:Ricky 
# Martin
#Chayanne
#José José
#Juan Luis Guerra

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]


def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:  # Verificamos que la clave exista en el diccionario
            print(diccionario[llave])


iterarDiccionario2("nombre", cantantes)


#Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función debe 
#imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave. Por ejemplo:

costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def imprimirInformacion(diccionario):
    for key, values in diccionario.items():
        print(f"{len(values)} - {key.upper()}")
        for value in values:
            print(value)

imprimirInformacion(costa_rica)
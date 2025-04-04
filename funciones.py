#valores por defecto
def buenos_dias(nombre="alegría", cantidad=1):

   print(("Buenos días "+nombre) * cantidad)


#1

def cantidad_de_vocales():

   return 5

print(cantidad_de_vocales())

#2


#3

def anio_independencia_chile():

   return 1810

   return 1851

print(anio_independencia_chile())

#4

def cantidad_de_departamentos_colombia():

   return(32)

   print(33)

print(cantidad_de_departamentos_colombia())

def sumar(a, b):
    print(a + b)  # Muestra el resultado en la consola, pero no lo devuelve

resultado = sumar(3, 5)  # Muestra 8, pero `resultado` será None
print(resultado)  # Muestra None

#5

def altura_machu_picchu():

   print(2438)

x = altura_machu_picchu()

print(x)

#6

def suma(a, b):

   print(a+b)

print(suma(10, 5) + suma(4, 3))

#7

def concatenar(a, b):

   return str(b) + str(a)

print(concatenar(7, 15))

#8

def paises_latinoamerica_o_lenguas_indigenas():

   a = 560

   print(a)

   if a < 180:

       return 33

   else:

       return 46

   return 21

print(paises_latinoamerica_o_lenguas_indigenas())


#9

def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):

   if a < b:

       return 365

   else:

       return 12

   return 52

print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))

print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4))

print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))


#10

def sumatoria(a, b):

   return a + b

   return 157

print(sumatoria(3, 4))


#11
a = 150

print(a)

def funcion():

   a = 350

   print(a)

print(a)

funcion()

print(a)

#12

a = 150

print(a)

def funcion():

   a = 350

   print(a)

   return a

print(a)

funcion()

print(a)


#Multiplica por 2: crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos, desde el 0 hasta el número proporcionado como entrada.
#Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]

def function(a):

   lista = []

   for i in range(a+1):

       lista.append(i*2)

   return lista

#Suma y resta: crea una función que reciba una lista con dos números. Imprime la suma de los dos números y regresa la resta de los dos números.
#Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1

def function(lista):
         
      print(lista[0] + lista[1])
   
      return lista[0] - lista[1]

resultado = function([1,2])
print(resultado)

#Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.
#Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)

def function(lista):
   return sum(lista) - len(lista)

resultado = function([1,5,7,8])
print(resultado)

#Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. Imprime la longitud de la lista y regresa la nueva lista.
#Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.
#Ejemplo: valores_multiplicados_segundo([1, 3, 5, 7]) debe imprimir 4 y devolver [3, 9, 15, 21]
#Ejemplo: valores_multiplicados_segundo([1]) debe imprimir 1 y devolver [ ]

def function(lista):
   if (len(lista) < 2):
      return[]
   else:
      segundo = lista[1]
      new_lista = [i * segundo for i in lista]
      print(len(lista))
      return new_lista
   
resultado = function([1,3,5,7])
print(resultado)

#Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.
#Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
#Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]

def function(valor, longitud):
   return [valor * longitud] * longitud

resultado = function(2,4)
print(resultado)  
print(resultado)
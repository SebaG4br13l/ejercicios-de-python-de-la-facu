# -*- coding: utf-8 -*-
"""Trabajo practico 4 - Arreglos_SENDRA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W34duFtntSLft4ct6GI_h8YtSLYimxoS

# ![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/50px-Python-logo-notext.svg.png) **Trabajo Práctico 4: Arreglos uni y multidimensionales** ![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/50px-Python-logo-notext.svg.png)

En este trabajo práctico, vamos a trabajar con arreglos uni y multidimensionales en Python. Recuerden crear una copia de este archivo en su ***Google Drive*** para tener permisos de edición.

### email Sergio: **sergio.gonzalez@unahur.edu.ar**
### email Ariel: **aclocchi@gmail.com**

### **Ejercicio 1**

Escribir un programa que le pida al usuario que ingrese 10 números  enteros (primero uno, luego otro, y así hasta que el usuario ingrese 10 numeros). Al final, el programa debe imprimir los números que fueron ingresados en orden inverso, la suma total de los valores y el promedio.
"""

"""
for i in range (cantNum):
  numIngresado = int(input("Ingrese un número entero: "))
  vector[cantNum - i - 1 ] = numIngresado #el último en la nueva matriz es vector[-1]
  sumaTotal+= numIngresado
"""


import numpy as np
cantNum = int(input())
sumaTotal= 0
vector = np.zeros((cantNum),int)
vectorInverso = None
for i in range(len(vector)): # de 0 a la cant de espacios del vector
  numIngresado = int(input("Ingrese un número entero: "))
  vector[len(vector)-1 -i ] = numIngresado
  sumaTotal+= numIngresado

print (f" Vector inversa: {vector} Suma Total: {sumaTotal} Promedio: {sumaTotal / cantNum}")

"""### **Ejercicio 2**

Escribir una función que recibe un arreglo de enteros por parámetro y lo retorna con el contenido desplazado una posición hacia la derecha: el primero pasa a ser el segundo, el segundo pasa a ser el tercero y así sucesivamente. El último pasa a ser el primero. 

Luego, escribir un programa que cargue un arreglo con valores ingresados por el usuario y llame a la función con ese arreglo. Mostrar el contenido del arreglo por pantalla, antes y después de la función.
"""

## vector = [1 2 3 6 2 54 7]
## vector = [7 1 2 3 6 2 54]

import numpy as np

def correADerecha(vector):
  nVector = len(vector)
  aux = vector[nVector-1]
  for pos in reversed(range(1,nVector)):
    vector[pos] = vector[pos - 1]
  vector[0] = aux

v = np.array([1,2,3,6,2,54,7])
print(v)
correADerecha(v)
print(v)

"""### **Ejercicio 3**

Desarrollar una función que inserte un elemento en un arreglo de enteros dada la posición de inserción. Al insertar un elemento en una posición, se produce un desplazamiento a la derecha, si el arreglo estaba lleno, el último elemento se pierde.
"""

## vector = [1 2 4 5 3]
##Insertamos el 10 en la posicion 1
## vector = [1 10 2 4 5]
def insertarDezplazandoAlaDerecha(vector,valor,posicion):

"""### **Ejercicio 4**

Escribir una función que elimine el elemento que ocupa una determinada posición de un arreglo de enteros.  Al eliminar se debe mantener la continuidad, es decir, los elementos a la derecha del eliminado, deben desplazarse a la izquierda un lugar.
"""

## vector = [1 2 8 5 3 4 5]
## Eliminar el elemento de la posicion 3
## vector = [1 2 8 3 4 5 0]

def eliminarElemento(vector, posEliminar):
  if 0 > posEliminar > len(vector)-1:
    raise Exception("Posicion invalida.")
  for pos in range(posEliminar,len(vector)-1):
    vector[pos] = vector[pos+1]
  vector[len(vector)-1] = 0

v = np.array([1, 2, 8, 5, 3, 4, 5])
print(v)
eliminarElemento(v,3)
print(v)

"""### **Ejercicio 5**

Escribir una función que elimine todas las apariciones de un determinado elemento de un arreglo de enteros.
"""

## vector = [1 3 3 4 5 6 3 7 3]
## vector = [1 3 4 5 6 3 7 3 0]

"""### **Ejercicio 6**

Escribir una función recursiva que reciba un arreglo de números reales como parámetro y retorne la suma de todos los elementos del arreglo. 
"""

## vector = [1 2 6 2 5 7 3 3 5 6]
## sum(vector) = vector[0] + sum([2 6 2 5 7 3 3 5 6])
## Caso base = Vector de un elemento

def sumaVector(vector):
  suma = 0
  if len(vector) == 1:
    suma = vector[0]
  else:
    suma = vector[0] + sumaVector(vector[1:])
  return suma

v = np.array([1, 2, 8, 5, 3, 4, 5])
print(v)
print(sumaVector(v))

def sumaVector2(vector, posActual = 0):
  suma = 0
  if posActual == len(vector)-1:
    suma = vector[posActual]
  else:
    suma = vector[posActual] + sumaVector2(vector, posActual+1)
  return suma

print(sumaVector2(v))

"""### **Ejercicio 7**

Escribir un programa que crea y cargar dos matrices de tamaño 3x3, las suma y muestra el resultado.
"""



"""### **Ejercicio 8**

Escribir una función que recibe una matriz y la rellena de la siguiente forma: En la posición M[ n , m ] debe contener n + m. 
"""

### 0 1 2
### 1 2 3
### 2 3 4

def llenaMatriz(matriz):
  nFilas, nColumnas = matriz.shape
  for fila in range(nFilas):           ###for fila in range(len(matriz))
    for columna in range(nColumnas):
      matriz[fila,columna] = fila + columna

m = np.zeros((8,4), int)
print(m)
llenaMatriz(m)
print(m)

"""### **Ejercicio 9**

Desarrollar una función que recibe una matriz cuadrada de números reales (N x N) por parámetro y calcula la suma de los elementos que están por encima de la diagonal principal (excluyendo la diagonal).

En el ejemplo de la imagen, la función deberia retornar: *b + c + f*

![texto alternativo](https://economipedia.com/wp-content/uploads/Captura-de-Pantalla-2019-07-29-a-les-13.18.05-1.png)
"""

import random as rdm

def asignarValoresAleatorios(matriz):
  for j in range(len(matriz)):
    for k in range(len(matriz[j])):
      h = rdm.randint(0,9)
      matriz[j][k] = h

m = np.zeros((4,4),int)
asignarValoresAleatorios(m)


## 62 38 51 26   fila 0 -> 1:final
## 68  9 75 40   fila 1 -> 2:final
## 63 12 69 24   fila 2 -> 3:final
## 74  3 64 10

print(m) 
def sumaSobreDiagonal(matriz):
  nFilas, nColumnas = matriz.shape
  suma = 0
  for fila in range(nFilas-1):
    for columna in range(fila+1,nColumnas):
      print("pos:",fila,",",columna)
      print(matriz[fila, columna])
      suma += matriz[fila, columna]
  return suma

print(sumaSobreDiagonal(m))

"""### **Ejercicio 10**

Escribir una función que retorna *True* si una matriz cuadrada de enteros es matriz diagonal y *False* en caso contrario.

Una matriz diagonal es una matriz que tiene ceros en todos sus elementos, menos en la diagonal principal.
"""



"""### **Ejercicio 11**

Escribir una función que retorna *True* si una matriz cuadrada de enteros es simétrica y *False* en caso contrario.

Una matriz simétrica es como la de la imagen (no importan los elementos de la diagonal principal):

![texto alternativo](https://economipedia.com/wp-content/uploads/Captura-de-Pantalla-2019-09-23-a-les-15.58.25.png) 
"""



"""### **Ejercicio 12**

Escribir una función recursiva, que calcule la suma de los elementos de la diagonal principal de una matriz.

Nota: La suma de los elementos de la diagonal principal de una matriz se llama "traza de la matriz".
"""

### 1 2 5
### 3 6 1
### 5 6 8

## 1 + sum 6 1
##         6 8  
## Caso base = Matriz de 1x1

# m[1:,1:]

"""### **Comentario**

En los ejercicios que usan cadenas de caracteres, pueden usar el tipo *str*, salvo que necesiten modificar elementos de la cadena luego de crearla, en ese caso, tienen que usar arreglos de caracteres.

### **Ejercicio 13**

Escribir 3 procedimientos que reciben una cadena de caracteres y..:
- Imprima los dos primeros caracteres.
- Imprima los tres últimos caracteres.
- Imprima la cadena cada dos caracteres. Por ej.: 'recta' debería imprimir 'rca'
"""

cadena = "carrera"

for pos in range(len(cadena)):
  print(cadena[pos])

"""### **Ejercicio 14**

Desarrollar una función recursiva que retorna *True* si una cadena de caracteres es un palíndromo y *False* en caso contrario.

Nota: Palíndromo es la forma elegante de "capicua"
"""

## palabra = neuquen
## comparo primer letra con ultima y llamado recursivo con el resto

def esPalindromo(palabra):
  resultado = True
  if len(palabra) <= 3:
    resultado = palabra[0] == palabra[len(palabra)-1]
  else:
    resultado = (palabra[0] == palabra[len(palabra)-1]) and esPalindromo(palabra[1:len(palabra)-1])
  return resultado

esPalindromo("neuqwequen")

"""### **Ejercicio 15**

Escribir una función que recibe una cadena de caracteres y un caracter y retorna una nueva cadena que tiene el caracter entre cada letra de la cadena de entrada. 

Por ej si la cadena es: ' separar ' y el caracter es: ' , ', debería retornar ' s,e,p,a,r,a,r '
"""



"""### **Ejercicio 16**

Escribir una función que recibe un arreglo variables de tipo "Tiempo" (TDA del ejercicio 4 del TP de TDA) y retorna un nuevo arreglo solo con los tiempos que son mayores a una hora (1:00:00).

Escribir un programa para probar a la función.

Nota: Van a tener que copiar el TDA "Tiempo" en el bloque de código de abajo y para que un *print* de un vector de variables de tipo "Tiempo" funcione, tienen que programar la operacion "\_\_repr__()" en el TDA "Tiempo". Pueden hacer a la operación "\_\_repr__()" igual a "\_\_str__()", porque *repr* es una generalización de *str*.
"""

class Tiempo:
  def __init__(self, h, m, s):
    self.horas = h
    self.minutos = m
    self.segundos = s

  def __repr__(self):
    return str(self.horas)+":"+str(self.minutos)+":"+str(self.segundos)

v = np.zeros(10,Tiempo)
v[0] = Tiempo(2,34,45)
v[2] = Tiempo(20,3,21)

print(v)

"""### **Ejercicio 17**

Una de las aplicaciones de matrices en programación es la representación y procesamiento de imágenes. Vamos a ver algunas cosas que se pueden hacer. Para esto primero tenemos que cargarnos una imagen en el colab y generar una matriz a partir de ella.

- Descarguen el archivo "felix.csv" del siguiente link:
https://drive.google.com/file/d/19CkOd04p6zw9qoKrF88TR2j-UFZnV9Uh/view?usp=sharing
- Suban el archivo "felix.csv" al "colab" para poder cargarlo con el programa de Python de abajo (haciendo click en el icono de la carpeta ![texto alternativo](https://i.ibb.co/jzqwMsc/carpeta.png), de arriba a la izquierda y luego en "Subir")
- Completen el programa, procesando a la imagen guardada en la matriz "felix" para obtener las imágenes de la siguiente figura (La "A" es la imagen original), pueden hacer funciones que generen cada transformación en la imagen: 

![texto alternativo](https://i.ibb.co/BcW3mwF/felix-results.png)
"""

import numpy as np
import matplotlib.pyplot as plt

###Lectura del archivo en la matriz#####
felix = np.genfromtxt('felix.csv', delimiter=',')
########################################

######Para mostrar matriz como imagen###########
plt.imshow(felix)
plt.show()
########################################

print(felix[0:4,0:4])

######Completar procesamiento en matriz felix para obtener imagenes################
print(felix.shape)

###Figura B
def matrizTraspuesta(matriz):
  nFilas,nColumnas = felix.shape
  traspuesta = np.zeros((nColumnas,nFilas),int)
  for f in range(nFilas):
    traspuesta[:,f] = matriz[f,:]
  return traspuesta

def matrizTraspuesta2(matriz):
  nFilas,nColumnas = felix.shape
  traspuesta = np.zeros((nColumnas,nFilas),int)
  for f in range(nFilas):
    for c in range(nColumnas):
      traspuesta[c,f] = matriz[f,c]
  return traspuesta
 
figuraB = matrizTraspuesta(felix)
plt.imshow(figuraB)
plt.show()
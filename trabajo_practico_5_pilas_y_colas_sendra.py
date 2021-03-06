# -*- coding: utf-8 -*-
"""Trabajo practico 5 - Pilas y Colas_SENDRA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lf1axZDFW2yWn7sVz-oYHEf18P7B-PhX

# ![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/50px-Python-logo-notext.svg.png) **Trabajo Práctico 5: Pilas y colas dinámicas** ![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/50px-Python-logo-notext.svg.png)

En este trabajo práctico, vamos a trabajar con las estructuras de datos **Pila** y **Cola** dinámicas en Python. Recuerden crear una copia de este archivo en su ***Google Drive*** para tener permisos de edición.

### Sergio: **sergio.gonzalez@unahur.edu.ar** ###
### Ariel: **aclocchi@gmail.com** ###

## **Parte 1: Pilas dinámicas**

### **Ejercicio 1**

Implementar el TDA Pila (Stack), con las siguientes operaciones:
- Crear (__init__())
- Vaciar
- Apilar elemento (push)
- Desapilar elemento (pop)
- Obtener primer elemento (top)
- Clonar
- Obtener tamaño de pila
- Esta vacía.
- __repr__(). Para poder imprimir una Pila por consola
"""

class Pila:
  def __init__(self):
    self.pila = []
  
  def __repr__(self):
    return str(self.pila)
  
  def estaVacia(self):
    return len(self.pila) == 0

  def apilarElemento(self, dato):
    self.pila.append(dato)

  def desapilarElemento(self, dato):
    if not self.estaVacia():
      dato = self.pila.pop()
      return dato

  def primerElemento(self):
    dato = None
    if not self.estaVacia():
      dato = self.pila[len(self.pila)-1]
    return dato
 
  def tamanio(self):
    return len(self.pila)

  def clonar(self):
    pilaClon = Pila()
    for elemento in self.pila:
      pilaClon.pila.append(elemento)
    return pilaClon
  
  def vaciar(self):
    #self.pila = []
    for elemento in self.pila:
      self.pila.pop(elemento)
    return self.pila

"""### A partir del **Ejercicio 2** vamos a trabajar fuera del TDA Pila usando la interface que creamos en el **Ejercicio 1**. Es decir, se pueden usar solo las operaciones de la interface, no se puede acceder a los componentes internos del TDA. Si necesitan estructuras auxiliares, pueden usar otra pila, arreglos o listas.

### **Ejercicio 2**

Escribir un programa que declare una pila de enteros y le apile 4 elementos. Luego debe mostrar la pila y su tamaño, desapilar 2 elementos y volver a imprimirla junto con el nuevo tamaño.
"""

pila1 = Pila()
pila1.apilarElemento(1);pila1.apilarElemento(2);pila1.apilarElemento(3);pila1.apilarElemento(4)
print(pila1)
print(pila1.tamanio())
pila1.desapilarElemento(4);pila1.desapilarElemento(3)
print(pila1)
print(pila1.tamanio())

pila1.vaciar()
print(pila1)
print(pila1.tamanio())

"""### **Ejercicio 3**

Escribir una función que invierta el orden de una pila. No debe devolver una nueva pila invertida, sino invertir la pila que ingresa por parámetro.
"""

def intertir(pilaEntrada):

"""### **Ejercicio 4**

Escribir una función que toma el último elemento de una pila y lo ponga en la cima (de la misma pila), respetando el orden del resto de los elementos. Utilizar una pila auxiliar.
"""



"""### **Ejercicio 5**

Escribir una función que coloque en el fondo de una pila un nuevo elemento.
"""



"""### **Ejercicio 6**

Escribir una función que elimine de una pila todas las ocurrencias de un elemento dado. Usar una pila auxiliar.
"""



"""### **Ejercicio 7**

Escribir un función que duplique el contenido de una pila.
"""



"""### **Ejercicio 8**

Escribir una función que realiza el cálculo de la suma de dos números enteros de muchos dígitos (los dos números tienen la misma cantidad de dígitos). La función recibe dos pilas por parámetro, las que almacenan los dígitos de los números a sumar (esta pilas no deben estar modificadas al terminar la función). La función debe retornar una nueva pila con el resultado.

Por ejemplo para sumar: 85699625 + 75426652

Las pilas de entrada a la función son:

Pila1 = 8, 5, 6, 9, 9, 6, 2, 5

Pila2 = 7, 5, 4, 2, 6, 6, 5, 2

La salida:

pilaSalida = 1, 6, 1, 1, 2, 6, 2, 7, 7
"""



"""### **Ejercicio 9**

Escribir la función “reemplazar”, que recibe como parámetro una pila de enteros y dos números enteros: “viejo” y “nuevo”. La función debe modificar la pila ingresada por parámetro, reemplazando cada ocurrencia del número “viejo” por el “nuevo”.

"""



"""### **Ejercicio 10**

Escribir una función que recibe una pila de enteros y retorna dos pilas, una con solo los números pares y otra con solo los impares, provenientes de la pila de entrada. Al finalizar la función, la pila de entrada no debe estar modificada.
"""



"""## **Parte 2: Colas dinámicas**

### **Ejercicio 1**

Implementar el TDA Cola (Queue), con las siguientes operaciones:
- Crear (__init__())
- Vaciar
- Encolar elemento (enqueue)
- Desancolar elemento (dequeue)
- Obtener primer elemento (top)
- Clonar
- Obtener tamaño de cola
- Esta vacía.
- __repr__(). Para poder imprimir una Cola por consola
"""



"""### A partir del **Ejercicio 2** vamos a trabajar fuera del TDA Cola usando la interface que creamos en el **Ejercicio 1**. Es decir, se pueden usar solo las operaciones de la interface, no se puede acceder a los componentes internos del TDA. Si necesitan estructuras auxiliares, pueden usar otra cola, pilas, arreglos o listas."""



"""### **Ejercicio 2**

Escribir una función que invierta el orden de una cola. No debe devolver una nueva cola invertida, sino invertir la cola que ingresa por parámetro.
"""



"""### **Ejercicio 3**

Escribir una función que extraiga el primer elemento de una cola y lo ponga en el final, respetando el orden del resto de los elementos. Utiliza para ello una cola auxiliar.


"""



"""### **Ejercicio 4**

Escribir una función que coloque en el principio de una cola un nuevo elemento.
"""



"""### **Ejercicio 5**

Escribir una función que elimine de una cola todas las ocurrencias de un elemento dado.

"""



"""### **Ejercicio 6**

Escribir una función que recibe una cola de enteros y genera dos colas: una con los números primos y otra con los números no primos, de la pila de entrada. Al terminar la función, la cola de entrada no debe estar modificada.
"""



"""### **Ejercicio 7**

Implementar la función "mezcla" de dos colas, que recibe como parámetros dos colas ordenadas de menor a mayor y devuelve una nueva cola con la unión de ambas colas de entrada con sus elementos ordenados de la misma manera.

"""


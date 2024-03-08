"""
EJ1 
Escribir un programa que lea un número impar por teclado.
Si el usuario no introduce un número impar, debe repetirse
el proceso hasta que lo introduzca correctamente.

"""


print("============EJ1==================")
while True:
    if int(input('Introduce un numero impar:'))% 2==0:
        print('Incorrecto introduce un numero impar')
    else:
    
        print('Ciclo finalizado')
        break

print("==============================")


"""
EJ2
Escribir un programa que pida al usuario cuántos números
quiere introducir. Luego que lea todos los números y realice
una media aritmética.

"""

print("============EJ2==================")
cantidad=int(input('Introduce una cantidad de numeros para sacar la media:'))
lista=[]

for i in range(cantidad):
    a=float(input('Introduce el numero {}:'.format(i+1)))
    lista.append(a)
print('La media de los numeros es:', sum(lista)/len(lista))

print("==============================")


"""
Utilizando la función range() y la conversión a listas generar
las siguientes listas dinámicamente:
✓ Todos los números del 0 al 10 [0, 1, 2, ..., 10]
✓ Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
✓ Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
✓ Todos los números impares entre -20 y 0 [-19, -17, -15,
..., -1]
✓ Todos los números múltiples de 5 del 0 al 50 [0, 5, 10,
..., 50]

"""
print("============EJ3==================")
print(list(range(0,10+1,1)));
print([x for x in range(-10, 1)])
print([x for x in range(0,20+1,1) if x%2==0])
print([x for x in range(-19, -1+1)])
print([x for x in range(0,50+1,1) if x%5==0])
print("==============================")

"""
Dadas dos listas (las que se quiera crear), generar una
tercera con los elementos que estén presentes en AMBAS
listas. Retornar esta nueva lista pero sin elementos
duplicados.

"""

print("============EJ4==================")
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
nueva_lista = []
for element in lista_2:
    if element in lista_1:
        nueva_lista.append(element)
print([*set(nueva_lista)])
"""
Escribir un programa que sume todos los números enteros
impares desde el 0 hasta el 100
"""
print("============EJ5==================")
lista_v=[]
for i in range(1,100+1,1):
    if i %2 ==0:
        lista_v.append(0)
    else:
        lista_v.append(i)
print(sum(lista_v))
print("==============================")

"""
Contar cuantas veces aparece un elemento en una lista
"""
print("============EJ6==================")
def conteo(lista, elemento):
    contador = 0
    for elemento in lista:
        if (elemento == x):
            contador = contador + 1
    return contador
lt = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8 #elemento
print('{} aparece {} veces'.format(x, conteo(lt, x)))
print("==============================")

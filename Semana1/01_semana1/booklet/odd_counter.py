"""
Escribir un programa que sume todos los numeros enteros impares desde el 0 hasta el 100
"""


def main():
    #Metodo 1
    total = 0
    for i in range(101):
        if i%2 == 1:
            total+=i
    print(total)
    #Metodo 2
    num_impares = [i for i in range(101) if i%2==1]
    resultado = sum(num_impares)
    print(resultado)


if __name__ == "__main__":
    main()

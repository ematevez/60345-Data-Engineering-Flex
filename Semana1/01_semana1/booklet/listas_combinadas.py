"""
Dadas dos listas (las que se quiera crear), generar una tercera con los elementos que estén presentes
en ambas listas. Retornar una nueva lista pero sin elementos duplicados."""


def main():
    try:
        n_1 = int(input(
                "introduzca cuantos elementos van a haber en la lista 1:"
            ))
        n_2 = int(input (
                "introduzca cuantos elementos van a haber en la lista 2:"
        ))
    except ValueError:
        print("Por favor introduzca una cantidad válida, programa finalizado.")
        exit()
    lista1=[]
    lista2=[]
    for i in range(max(n_1,n_2)):
        if i<n_1:
            element_lista1 = input(f"Elemento {i+1}, lista 1:")
            lista1.append(element_lista1)
        if i<n_2:        
            element_lista2 = input(f"Elemento {i+1}, lista 2:")
            lista2.append(element_lista2)
    resultado = list(set(lista1 + lista2))
    print(lista1)
    print(lista2)
    print(resultado)


if __name__ == "__main__":
    main()

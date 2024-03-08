"""
Escribir un programa que pida al usuario cuantos números quiere introducir. Luego que lea todos 
los números y realice una media aritmética."""
def main():
    try:
        n = int(
            input("introduzca cuantos números va a introducir para el cálculo de la media:")
        )
    except ValueError:
        print("Por favor introduzca una cantidad válida, programa finalizado.")
        exit()
    total = 0
    for i in range(n):
        try:
            number = float(input(f"Número {i+1}:"))
            total += number
        except ValueError:
            print("Introduzca un número válido, programa finalizado.")
            exit()
    print(f"La media es {total/float(n)}")
if __name__ == "__main__":
    main()
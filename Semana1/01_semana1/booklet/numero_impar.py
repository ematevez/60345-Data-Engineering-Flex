"""
Escriba un programa que solicite al usuario introducir un número. Si el número introducido es par, debe continuar solicitando un número. Si el número es impar. El proceso finaliza.
"""
def main():
    t = 1
    while t == 1:
        if int(input("Introduce un número impar para finalizar este loop:")) % 2 == 0:
            print("Introduciste un número par")
        else:
            print("loop finalizado")
            t=0
if __name__== "__main__":
    main()
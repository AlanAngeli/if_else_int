numero_int = input("Digite um número inteiro: ")

if numero_int.isdigit():
    numero_int = int(numero_int)

    if numero_int % 2 == 0:
        print(numero_int, "é par")
    else:
        print(numero_int, "é par ímpar")
else:
    print("Você não digitou um número inteiro")

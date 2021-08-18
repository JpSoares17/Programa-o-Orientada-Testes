def contador_divisores(numero):
    divisor = 1
    contador = 0
    while divisor <= numero:
        if numero % divisor == 0:
            contador += 1
        divisor += 1
    return contador


def main():
    # Leitura:
    numero = int(input("Digite um número: ").strip())
    # Processamento:
    divisores = contador_divisores(numero)
    # Saída:
    print(f"{numero} tem {divisores} divisores")


if __name__ == "__main__":
    main()

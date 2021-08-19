def maximo(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior


def main():
    # Leitura:
    for serie in range(4):
        numeros = []
        for leitura in range(4):
            numero = int(input(
                f"Digite o {leitura + 1}º número da {serie + 1}ª série: "))
            numeros.append(numero)
        # Processamento:
        meu_maior = maximo(numeros)
        # Saída:
        print(
            f"O maior número da {serie + 1}ª série é {meu_maior}\n")


if __name__ == "__main__":
    main()

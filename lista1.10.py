def main():
    # Leitura:
    for serie in range(4):
        numeros = []
        for leitura in range(4):
            numero = int(input(
                f"Digite o {leitura + 1}º número da {serie + 1}ª série: "))
            numeros.append(numero)
        # Processamento:
        meu_maior = max(numeros)
        # Saída:
        print(
            f"O maior número da {serie + 1}ª série é {meu_maior}\n")


if __name__ == "__main__":
    main()

def peso_ideal(altura, sexo):
    if sexo == 1:
        return (62.1 * altura) - 44.7
    elif sexo == 2:
        return (72.7 * altura) - 58


def main():
    # Leitura:
    altura = float(input("Digite sua altura: ").strip())
    sexo = int(input("Qual seu sexo?(1-Feminino 2-Masculino) ").strip())
    # Processamento:
    if sexo in (1, 2):
        meu_peso_ideal = peso_ideal(altura, sexo)
        # Saida 1:
        print(f"Seu peso ideal é {meu_peso_ideal}Kg")
    else:
        print("Opção de sexo inválida!")


if __name__ == "__main__":
    main()

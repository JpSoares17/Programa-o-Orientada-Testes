from math import pi


def perimetro(raio):
    return 2 * pi * raio


def area(raio):
    return pi * raio ** 2


def main():
    # Leitura:
    raio = float(input("Digite o raio da circunferência: ").strip())
    # Processamento:
    minha_area = area(raio)
    meu_perimetro = perimetro(raio)
    # Saída:
    print(f"A área da circuferência é {minha_area} m²")
    print(f"O perímetro da circunferência é {meu_perimetro} m")


if __name__ == "__main__":
    main()

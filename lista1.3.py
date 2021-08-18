def conversao(temperatura):
    return ((temperatura - 32) / 9) * 5


def main():
    # Leitura:
    fahrenheit = float(input("Digite a temperatura: ").strip())
    # Processamento:
    celsius = conversao(fahrenheit)
    # Saída:
    print(f"{fahrenheit}ºF em Celsius é {celsius}ºC")


if __name__ == "__main__":
    main()

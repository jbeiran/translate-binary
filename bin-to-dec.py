def binario_a_decimal(binario: str) -> float:
    parte_entera, _, parte_frac = binario.partition('.')
    decimal = 0
    for i, digit in enumerate(reversed(parte_entera)):
        decimal += int(digit) * (2 ** i)
    for i, digit in enumerate(parte_frac, start=1):
        decimal += int(digit) * (2 ** -i)
    return decimal

def decimal_a_binario(decimal: float, precision: int = 10) -> str:
    parte_entera = int(decimal)
    parte_frac = decimal - parte_entera
    binario_entero = ''
    if parte_entera == 0:
        binario_entero = '0'
    else:
        while parte_entera > 0:
            binario_entero = str(parte_entera % 2) + binario_entero
            parte_entera = parte_entera // 2
    binario_frac = ''
    while parte_frac > 0 and len(binario_frac) < precision:
        parte_frac *= 2
        bit = int(parte_frac)
        binario_frac += str(bit)
        parte_frac -= bit
    if binario_frac:
        return f"{binario_entero}.{binario_frac}"
    else:
        return binario_entero

def es_binario(binario: str) -> bool:
    allowed_chars = {'0', '1', '.'}
    return all(char in allowed_chars for char in binario)

def menu():
    print("Conversor Binario-Decimal")
    print("1. Binario a Decimal")
    print("2. Decimal a Binario")
    print("3. Salir")

def ejecutar_conversion():
    while True:
        menu()
        opcion = input("Selecciona una opción (1-3): ").strip()
        if opcion == '1':
            binario = input("Introduce el número binario (e.g., 1010.101): ").strip()
            if es_binario(binario):
                decimal = binario_a_decimal(binario)
                print(f"Binario {binario} a decimal es {decimal}\n")
            else:
                print("Entrada inválida. Asegúrate de introducir solo 0s, 1s y un punto decimal.\n")
        elif opcion == '2':
            decimal_input = input("Introduce el número decimal (e.g., 34.567): ").strip()
            try:
                decimal_num = float(decimal_input)
                binario_resultado = decimal_a_binario(decimal_num)
                print(f"Decimal {decimal_num} a binario es {binario_resultado}\n")
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número decimal válido.\n")
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 3.\n")

if __name__ == "__main__":
    ejecutar_conversion()
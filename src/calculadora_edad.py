"""
Programa: Calculadora de edad interactiva
Autor: Tu nombre
"""

# ==============================
# CONSTANTES
# ==============================
ANIO_ACTUAL = 2025
EDAD_MAYORIA_DE_EDAD = 18

# ==============================
# FUNCIÓN PRINCIPAL
# ==============================


def calcular_edad_interactivo():
    # Validación del año de nacimiento
    while True:
        anio_nacimiento_texto = input("¿En qué año naciste? ")

        try:
            anio_nacimiento = int(anio_nacimiento_texto)

            if anio_nacimiento > ANIO_ACTUAL:
                print(f"❌ No puedes nacer en el futuro (máx {ANIO_ACTUAL}).")

            elif anio_nacimiento < 1900:
                print("❌ Ingresa un año más realista (>= 1900).")

            else:
                break

        except ValueError:
            print("❌ Entrada inválida. Escribe solo números.")

    # Cálculo de edad
    edad = ANIO_ACTUAL - anio_nacimiento
    print(f"\nTu edad aproximada es: {edad} años")

    # Evaluación de mayoría de edad
    if edad >= EDAD_MAYORIA_DE_EDAD:
        print("✔️ Eres mayor de edad")
    else:
        print("❌ Eres menor de edad")
        faltan = EDAD_MAYORIA_DE_EDAD - edad
        print(f"Te faltan {faltan} años para ser mayor de edad")


# ==============================
# EJECUCIÓN DEL PROGRAMA
# ==============================
if __name__ == "__main__":
    calcular_edad_interactivo()

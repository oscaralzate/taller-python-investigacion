"""
Calculadora Simple
Operaciones: suma, resta, multiplicación y división
"""

print("=== CALCULADORA SIMPLE ===")

# ==============================
# ENTRADA DE DATOS
# ==============================
try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
except ValueError:
    print("❌ Error: Debes ingresar números válidos.")
    exit()

# ==============================
# MENÚ DE OPERACIONES
# ==============================
print("\nOperaciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("\nElige la operación (1-4): ")

# ==============================
# PROCESAMIENTO
# ==============================
if opcion == "1":
    resultado = numero1 + numero2
    print(f"\n{numero1} + {numero2} = {resultado}")

elif opcion == "2":
    resultado = numero1 - numero2
    print(f"\n{numero1} - {numero2} = {resultado}")

elif opcion == "3":
    resultado = numero1 * numero2
    print(f"\n{numero1} * {numero2} = {resultado}")

elif opcion == "4":
    if numero2 == 0:
        print("\n❌ Error: No se puede dividir entre cero")
    else:
        resultado = numero1 / numero2
        print(f"\n{numero1} / {numero2} = {resultado}")

else:
    print("\n❌ Opción no válida")

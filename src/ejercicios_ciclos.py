"""
Ejercicio: Practicando Ciclos
Diferentes ejemplos de for y while
"""

# ==============================
# EJERCICIO 1: CONTAR NÚMEROS
# ==============================
print("=== EJERCICIO 1: CONTAR NUMEROS ===")

for i in range(1, 6):
    print(f"Contando: {i}")

# ==============================
# EJERCICIO 2: SUMA ACUMULATIVA
# ==============================
print("\n=== EJERCICIO 2: SUMA ACUMULATIVA ===")

suma = 0

for numero in range(1, 11):
    suma += numero
    print(f"Suma hasta {numero}: {suma}")

print(f"\nTotal final: {suma}")

# ==============================
# EJERCICIO 3: PEDIR NÚMEROS
# ==============================
print("\n=== EJERCICIO 3: PEDIR NUMEROS ===")

contador = 0

while contador < 5:
    numero = input(f"Dame el número {contador + 1}: ")

    if numero.isdigit():
        print(f"Guardaste: {numero}")
    else:
        print("Entrada inválida, pero se guarda igual.")

    contador += 1

# ==============================
# EJERCICIO 4: NÚMEROS PARES
# ==============================
print("\n=== EJERCICIO 4: NUMEROS PARES ===")
print("Números pares del 1 al 20:")

for num in range(1, 21):
    if num % 2 == 0:
        print(num, end=" ")

print("\n")

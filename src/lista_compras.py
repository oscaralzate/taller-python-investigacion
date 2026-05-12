"""
Lista de compras con cálculo de total y descuento
"""

# ==============================
# CONSTANTES
# ==============================
DESCUENTO = 0.10  # 10%
MINIMO_DESCUENTO = 100

# ==============================
# INICIO
# ==============================
print("=== LISTA DE COMPRAS ===")

# Validación de cantidad de productos
try:
    cantidad_productos = int(input("¿Cuántos productos vas a comprar? "))
    if cantidad_productos <= 0:
        print("❌ Debes ingresar al menos 1 producto.")
        exit()
except ValueError:
    print("❌ Entrada inválida. Debes ingresar un número entero.")
    exit()

total = 0

# ==============================
# CAPTURA DE PRODUCTOS
# ==============================
for i in range(1, cantidad_productos + 1):
    print(f"\nProducto {i}:")

    nombre = input("  Nombre del producto: ")

    try:
        precio = float(input("  Precio: $"))
    except ValueError:
        print("  ❌ Precio inválido. Se tomará como 0.")
        precio = 0

    total += precio
    print(f"  Agregado: {nombre} - ${precio:.2f}")

# ==============================
# RESUMEN
# ==============================
print("\n--- RESUMEN ---")
print(f"Subtotal: ${total:.2f}")

if total >= MINIMO_DESCUENTO:
    descuento = total * DESCUENTO
    total_final = total - descuento

    print(f"Descuento (10%): -${descuento:.2f}")
    print(f"TOTAL A PAGAR: ${total_final:.2f}")

else:
    faltante = MINIMO_DESCUENTO - total
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print(f"Te faltan ${faltante:.2f} para obtener el 10% de descuento")

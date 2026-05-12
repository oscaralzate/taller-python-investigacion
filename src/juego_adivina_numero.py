"""
Juego: Adivina el número secreto (máximo 5 intentos)
"""

# ==============================
# CONSTANTES
# ==============================
NUMERO_SECRETO = 42
MAX_INTENTOS = 5

# ==============================
# INICIO DEL JUEGO
# ==============================
print("=== JUEGO: ADIVINA EL NUMERO ===")
print(f"Tengo un número entre 1 y 100. Tienes {MAX_INTENTOS} intentos.")

intentos = 0
adivinado = False

# ==============================
# LÓGICA DEL JUEGO
# ==============================
while intentos < MAX_INTENTOS and not adivinado:
    intentos += 1

    try:
        intento = int(
            input(f"\nIntento {intentos}/{MAX_INTENTOS}. Tu número: "))
    except ValueError:
        print("❌ Debes ingresar un número válido.")
        continue

    if intento == NUMERO_SECRETO:
        print(f"🎉 ¡Felicitaciones! Adivinaste en {intentos} intentos!")
        adivinado = True

    elif intento < NUMERO_SECRETO:
        print("📈 El número secreto es MAYOR")

    else:
        print("📉 El número secreto es MENOR")

# ==============================
# FINAL DEL JUEGO
# ==============================
if not adivinado:
    print(f"\n💀 Se acabaron los intentos. El número era {NUMERO_SECRETO}")

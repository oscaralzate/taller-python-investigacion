"""
Programa: Hola Mundo Interactivo
Descripción: Saluda al usuario y presenta un menú de opciones
Autor: Tu Nombre
Fecha: 2025
"""

# ==========================================
# CONSTANTES DEL PROGRAMA
# ==========================================
NOMBRE_PROGRAMA = "Hola Mundo Interactivo"
VERSION = "1.0"
MAX_INTENTOS = 3
ANIO_ACTUAL = 2025

# ==========================================
# PARTE 1: SALUDO INICIAL
# ==========================================
print("=" * 50)
print(f" {NOMBRE_PROGRAMA} v{VERSION}")
print("=" * 50)
print()

nombre_usuario = input("¿Cuál es tu nombre? ")

if nombre_usuario == "":
    print("No ingresaste un nombre. Te llamaré Usuario")
    nombre_usuario = "Usuario"
else:
    print(f"Hola, {nombre_usuario}! Bienvenido/a al programa.")

print()

# ==========================================
# PARTE 2: EDAD
# ==========================================
edad_texto = input("¿Cuántos años tienes? ")

if edad_texto.isdigit():
    edad = int(edad_texto)
else:
    print("Edad inválida. Se asignará 0.")
    edad = 0

if edad < 18:
    print(f"Eres menor de edad, {nombre_usuario}.")
    categoria = "joven"
elif edad < 60:
    print(f"Eres adulto, {nombre_usuario}.")
    categoria = "adulto"
else:
    print(f"Eres adulto mayor, {nombre_usuario}.")
    categoria = "adulto mayor"

anio_nacimiento = ANIO_ACTUAL - edad
print(f"Naciste aproximadamente en el año {anio_nacimiento}")
print()

# ==========================================
# PARTE 3: MENÚ
# ==========================================
print("=" * 50)
print("MENU DE OPCIONES")
print("=" * 50)
print("1. Ver tu información")
print("2. Contar del 1 al 10")
print("3. Tabla de multiplicar")
print("4. Salir")
print("=" * 50)

continuar = True
intentos_fallidos = 0

while continuar:
    opcion = input("\nElige una opción (1-4): ")

    if opcion == "1":
        print("\n--- TU INFORMACIÓN ---")
        print(f"Nombre: {nombre_usuario}")
        print(f"Edad: {edad} años")
        print(f"Categoría: {categoria}")
        print(f"Año de nacimiento: {anio_nacimiento}")
        intentos_fallidos = 0

    elif opcion == "2":
        print("\n--- CONTANDO DEL 1 AL 10 ---")
        for numero in range(1, 11):
            print(f"Número: {numero}")
        intentos_fallidos = 0

    elif opcion == "3":
        numero_tabla = input("\n¿De qué número quieres la tabla? ")

        if numero_tabla.isdigit():
            numero_tabla = int(numero_tabla)
            print(f"\n--- TABLA DEL {numero_tabla} ---")
            for i in range(1, 11):
                print(f"{numero_tabla} x {i} = {numero_tabla * i}")
        else:
            print("Número inválido.")

        intentos_fallidos = 0

    elif opcion == "4":
        print(f"\nHasta luego, {nombre_usuario}!")
        print("Gracias por usar el programa.")
        continuar = False

    else:
        intentos_fallidos += 1
        print(
            f"\nOpción inválida. Intento {intentos_fallidos} de {MAX_INTENTOS}")

        if intentos_fallidos >= MAX_INTENTOS:
            print("Demasiados intentos fallidos. Cerrando programa...")
            continuar = False

print("\n" + "=" * 50)
print("PROGRAMA FINALIZADO")
print("=" * 50)

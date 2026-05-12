Pregunta 1: Variables en Python
Una variable es un espacio en memoria con un nombre que almacena un valor.

Tipos de datos que pueden almacenar:
  - int (entero): edad = 25
  - float (decimal): precio = 9.99
  - str (texto): nombre = 'Ana'
  - bool (verdadero/falso): activo = True

Nombres VALIDOS:    nombre, edad_usuario, total1, _privado
Nombres INVALIDOS:  1numero (empieza con numero), mi-variable (guion medio),
                    for (palabra reservada de Python)


Pregunta 2: Diferencia entre = y ==
= (asignacion): guarda un valor en una variable.
    Ejemplo: nombre = 'Juan'   <- Guarda 'Juan' en la variable nombre

== (comparacion): verifica si dos valores son iguales. Devuelve True o False.
    Ejemplo: nombre == 'Juan'  <- Devuelve True si nombre es 'Juan'

Uso en contexto:
    edad = 18           <- asignacion (guarda el valor)
    if edad == 18:      <- comparacion (verifica el valor)


Pregunta 3: Indentacion en Python
La indentacion (espacios al inicio de las lineas) define los bloques de codigo.
Python usa indentacion obligatoria en lugar de llaves {} como otros lenguajes.

Estandar: 4 espacios por nivel de indentacion.

Si no indentas correctamente, obtienes un IndentationError y el programa
no puede ejecutarse. Python falla al interpretar la estructura del codigo.


Pregunta 4: Ciclo for vs while
for: se usa cuando conoces de antemano cuantas veces se repetira.
     Ejemplo: recorrer una lista, contar del 1 al 10.
     for i in range(1, 11):
         print(i)

while: se usa cuando la repeticion depende de una condicion que puede cambiar.
       Ejemplo: menu de opciones, repetir hasta que el usuario escriba 'salir'.
       while continuar == True:
           opcion = input('Elige una opcion: ')


Pregunta 5: La funcion range()
range() genera una secuencia de numeros para usar en ciclos for.

range(5)         -> 0, 1, 2, 3, 4         (desde 0, hasta 5 excluido)
range(1, 10)     -> 1, 2, 3, 4, 5, 6, 7, 8, 9  (desde 1 hasta 10 excluido)
range(0, 10, 2)  -> 0, 2, 4, 6, 8         (desde 0, hasta 10, de 2 en 2)




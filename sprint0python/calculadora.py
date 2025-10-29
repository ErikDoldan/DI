from operaciones import suma, resta, multiplicacion, division

continuar = "s"

while continuar == "s":
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    operacion = input("Operación (suma/resta/multiplicacion/division): ")

    if operacion == "suma":
        print(suma(num1, num2))
    elif operacion == "resta":
        print(resta(num1, num2))
    elif operacion == "multiplicacion":
        print(multiplicacion(num1, num2))
    elif operacion == "division":
        print(division(num1, num2))

    continuar = input("¿Más operaciones? (s/n): ")
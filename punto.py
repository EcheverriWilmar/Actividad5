def ejercicio1():
    
    numero = int(input("Ingresa un número para calcular su factorial: "))
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")

def ejercicio2():
    inicio = int(input("Ingresa el número de inicio del rango: "))
    fin = int(input("Ingresa el número de fin del rango: "))
    suma_pares = 0
    suma_impares = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            suma_pares += numero
        else:
            suma_impares += numero
    print(f"Suma de pares: {suma_pares}")
    print(f"Suma de impares: {suma_impares}")

def ejercicio3():
    n = int(input("Ingresa el número máximo para la secuencia de Fibonacci: "))
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()

def ejercicio4():

    base = float(input("Ingresa la longitud de la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")

def ejercicio5():
    numero = int(input("Ingresa un número para calcular la suma de sus dígitos: "))
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    print(f"La suma de los dígitos es: {suma}")

# Agrega este ejercicio al menú existente

def main():
    while True:
        print("Menú de ejercicios:")
        print("1. Calcular factorial de un número")
        print("2. Sumar numeros pares e impares en un rango")
        print("3. Generar una secuencia de Fibonacci hasta un número dado")
        print("4. Calcular el área de un triángulo")
        print("5. Calcular la suma de los dígitos de un número")
        print("6. Salir")

        opcion = int(input("Selecciona un ejercicio (0-5): "))

        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            ejercicio1()
        elif opcion == 2:
            ejercicio2()
        elif opcion == 3:
            ejercicio3()
        elif opcion == 4:
            ejercicio4()
        elif opcion == 5:
            ejercicio5()
        else:
            print("Opción no válida. Por favor, selecciona un ejercicio válido (0-5).")

main()
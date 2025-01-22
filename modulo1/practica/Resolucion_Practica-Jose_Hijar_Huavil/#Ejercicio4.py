# Ejercicio 4
# Escribe un programa que pida un numero entero y determine si es par o impar

num = int(input("Ingrese el número a evaluar: "))

if num < 0:
    print("Ingrese un número positivo, inténtelo nuevamente")
elif num % 2 == 0:
    print(f"El número ingresado {num} es PAR.")
else:
    print(f"El número ingresado {num} es IMPAR.")
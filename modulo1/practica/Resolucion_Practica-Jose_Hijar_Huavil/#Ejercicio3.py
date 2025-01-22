# Ejercicio 3
# Escribe un programa que pida tu edad y muestre si es mayor de edad o no lo es.

edad = int(input("Ingrese su edad: "))

if edad <= 0:
    print("Ingrese un número POSITIVO, intente nuevamente")
elif edad >= 18:
    print("Usted es MAYOR de edad")
else:
    print("Usted es MENOR de edad")
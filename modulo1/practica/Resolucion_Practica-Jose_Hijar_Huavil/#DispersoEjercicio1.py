# Ejercicio 1 (Problemas Disperso)

c = float(input("Ingrese monto a depositar: "))
r= 4

cf1= round(c*(1+r/100)**1,2)
cf2= round(c*(1+r/100)**2,2)
cf3= round(c*(1+r/100)**3,2)

print (f"La cantidad de ahorros tras el primer año es: {round(cf1-c,2)} soles, teniendo un total en la cuenta de : {cf1} soles")
print (f"La cantidad de ahorros tras el segundo año es: {round(cf2-c,2)} soles, teniendo un total en la cuenta de : {cf2} soles")
print (f"La cantidad de ahorros tras el tercer año es: {round(cf3-c,2)} soles, teniendo un total en la cuenta de : {cf3} soles")
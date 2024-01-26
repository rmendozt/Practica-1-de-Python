consumo=float(input("¿Cuánto fue su consumo ? : "))
porcentaje=float(input("¿Qué porcentaje del consumo desea dar de propina ? : "))
propina = consumo * porcentaje/100
print(f"Dejar de propina {round(propina,2)}")
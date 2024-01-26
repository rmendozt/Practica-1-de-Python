edad=int(input("¿Qué edad tiene?"))
if edad >=0 and edad< 4:
    print("Puede entrar gratis")
elif edad >=4 and edad <=18:
    print("Pagar $ 5")
elif edad>18:
    print("Pagar $ 10")
else:
    print("Validar edad")
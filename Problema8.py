time=input("ingrese :")
time2= time.split(":")
hora=float(time2[0])
minutos=float(time2[1])
horario=hora+minutos/60
if horario>=7 and horario<=8:
    print("Es hora de desayunar")
elif horario>=12 and horario<=13: 
    print("Es hora de almorzar")
elif horario>=18 and horario<=19: 
    print("Es hora de cenar")  
num_payasos= int(input("Cuantos payasos se vendieron : "))
num_muñecas= int(input("Cuantas muñecas se vendieron : "))
# Sabemos que los pesos son:
p_payaso=112
p_muñeca=75
peso_total=num_payasos*p_payaso+num_muñecas*p_muñeca
print(f"El peso del paquete es : {peso_total} gr.")
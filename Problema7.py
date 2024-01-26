num1 = float(input("Introduce un número: ") )
num2 = float(input("Introduce otro número: ") ) 
opcion=0       
print("¿Qué desea hacer con los números? \n1) Sumar los  números\n2) Restar los números\n3) Multiplicar los números")
opcion = int(input("Escoja la opción") )     

if opcion == 1:
    print("La suma de",num1,"+",num2,"es",num1+num2)
elif opcion == 2:
    print("La resta de",num1,"-",num2,"es",num1-num2)
elif opcion == 3:
    print("El producto de",num1,"*",num2,"es",num1*num2)
else:
    print("Opción inválida")
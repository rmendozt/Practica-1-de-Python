nombre=input("ingrese nombre de archivo:")
nombre2=nombre.split(".")
extensiones=["gif","jpg","jpg","png","pdf","txt","zip"]
if nombre2[1] in extensiones:
    print("Generar programa")
else:
    print(" application/octet-stream")
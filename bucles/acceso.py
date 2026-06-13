passw = "123"

max_int = 3

inte = 0

while inte < max_int:
    contra = input("Ingrese el password: ")

    if contra == passw:
        print(" acceso exitos")
        break
    else:
        print("password incorrecto")
        inte += 1

if inte == max_int:
    print("Acceso bloqueado")
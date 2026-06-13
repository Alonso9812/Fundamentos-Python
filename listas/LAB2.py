beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")


# El usuario puede agregar más miembros
for i in range(2):
    member = input("Agrega un miembro de la banda: ")
    beatles.append(member)

print("Los miembros de la banda son:")
for beatle in beatles:
    print(beatle)

del beatles[3:5] 
print("Después de eliminar algunos miembros, la banda queda así:")
for beatle in beatles:
    print(beatle)  

beatles.insert(0, "Ringo Starr")  # Agregar Ringo al inicio
print("Después de agregar a Ringo Starr, la banda queda así:")
for beatle in beatles:
    print(beatle)       


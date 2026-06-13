dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])


#############################

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)


###########################
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['gato'] = 'minou'
print(dictionary)

## ordenar un diccionario = for key in sorted(dictionary.keys()):

## tambien 

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for french in dictionary.values():
    print(french)


## agregar clave

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['cisne'] = 'cygne'
print(dictionary)

## ahora con update

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary.update({"pato": "canard"})
print(dictionary)

## eliminar clave

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

del dictionary['perro']
print(dictionary)

## 3l3iminar ultimo elemento

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary.popitem()
print(dictionary)    # salida: {'gato': 'chat', 'perro': 'chien'}

## copiar diccionario

pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }

copy_dictionary = pol_esp_dictionary.copy()

## unir diccionarios
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)
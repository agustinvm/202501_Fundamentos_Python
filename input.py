while True:

    print("1.- Escribir tu nombre")
    print("2.- Salir")

    opciones = input("\nElige una opcion: ")
    if opciones == "2":
        break

    if opciones == "1":
        nombre = input("\nEscribe tu nombre: ")
        print(f"Hola {nombre}")


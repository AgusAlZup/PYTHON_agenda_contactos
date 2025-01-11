contactos = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    email = input("Ingrese el correo electrónico: ")
    contactos[nombre] = {"telefono": telefono, "email": email}
    print(f"Contacto <{nombre}> agregado exitosamente.")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in contactos:
        print(f"Información de {nombre}:")
        print(f"Teléfono: {contactos[nombre]['telefono']}")
        print(f"Email: {contactos[nombre]['email']}")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto eliminado: {nombre}.")
    else:
        print(f"Contacto no encontrado: {nombre}.")

def mostrar_contactos():
    if contactos:
        print("\nLista de contactos:")
        for nombre, info in contactos.items():
            print("\n")
            print(f"Nombre: {nombre}: Numero: {info['telefono']}, Mail: {info['email']}")
            print("-" * 25)
    else:
        print("No hay contactos registrados.")
        
while True:
    print("\nMenú:")
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar contactos")
    print("5. Salir")
    # print("-" *40)
    
    opcion = input("\nIngrese una opción: ")
    
    if opcion == '1':
        agregar_contacto()
    elif opcion == '2':
        buscar_contacto()
    elif opcion == '3':
        eliminar_contacto()
    elif opcion == '4':
        mostrar_contactos()
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
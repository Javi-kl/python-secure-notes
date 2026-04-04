

def validar_opcion(opcion, opciones_validas):
    opciones_formated = opciones_validas[0] + "-" + opciones_validas[-1]
    if opcion not in opciones_validas:
        raise ValueError(f"Debes introducir un digito: {opciones_formated}")

def opciones_menu_principal():
    print("\n--- Menú principal ---")
    print("1 -> Opciones Cifrado")
    print("2 -> Opciones Notas")
    print("3 -> Opciones archivo")
    print("4 -> Salir")
    opcion = input("-> ")
    validar_opcion(opcion, ["1", "2", "3", "4"])
    return opcion


def opciones_submenu_notas_existentes():
    print("\nNota encontrada\n")
    print("Opciones notas existentes:")
    print("1 -> Leer nota")
    print("2 -> Modificar nota")
    print("3 -> Borrar nota")
    print("4 -> Volver atrás")
    opcion = input("-> ")
    validar_opcion(opcion, ["1", "2", "3", "4"])
    return opcion


def opciones_submenu_notas():
    print("Opciones notas:\n1 -> Nueva nota")
    print("2 -> Seleccionar nota existente 'por título'")
    print("4 -> Volver atrás")
    opcion = input("-> ").lower()
    validar_opcion(opcion, ["1", "2", "4"])
    return opcion


def opciones_submenu_cifrado():
    print("Opciones cifrado")
    print("1 -> Cifrar archivo")
    print("2 -> Descifrar archivo")
    print("4 -> Volver atrás")
    opcion = input("-> ")
    validar_opcion(opcion, ["1", "2", "4"])
    return opcion


def opciones_submenu_archivo():
    print("Opciones archivo")
    print("1 -> Crear archivo")
    print("2 -> Borrar archivo")
    print("4 -> Volver atrás")
    opcion = input("-> ")
    validar_opcion(opcion, ["1", "2", "4"])
    return opcion
from ..notas.notas import Notas
from ..archivo.cifrar_descifrar import Cifrador
from .menu_options import opciones_submenu_archivo,opciones_submenu_cifrado, opciones_submenu_notas, opciones_menu_principal, opciones_submenu_notas_existentes
from ..archivo.archivo import ArchivoSeguro
from .recolector_data import recibir_titulo


def submenu_notas(notas):
    print("\nNotas actuales: ")
    for t in notas.listar_titulos():
        print(t)
    print()
    try:
        opcion_notas = opciones_submenu_notas()
    except ValueError as e:
        print(f"Error: {e}")
        return

    if opcion_notas == "4":
        print("\nVolviendo al menú principal")
        return
    elif opcion_notas == "1":
        notas.crear()
    elif opcion_notas == "2":
        titulo = recibir_titulo()
        try:
            notas.existencia_titulo(titulo)
        except ValueError as e:
            print(f"Error: {e}")
            print("Volviendo a menú")
            return
        try:
            opcion_notas_existentes = opciones_submenu_notas_existentes()
        except ValueError as e:
            print(f"Error: {e}")
            return
        match opcion_notas_existentes:
            case "1":
                print(f"\nLeyendo nota: {titulo}")
                print(notas.leer_cuerpo(titulo))
            case "2":
                print(f"\nModificando nota: {titulo}")
                notas.modificar(titulo)
            case "3":
                print(f"\nEliminando nota: {titulo}")
                notas.eliminar(titulo)
            case "4":
                print("\nVolviendo al menú principal")
                return


def submenu_archivo(archivo):
    try:
        opcion = opciones_submenu_archivo()
    except ValueError as e:
        print(f"Error: {e}")
        return
    match opcion:
        case "1":
            if not (archivo.existencia() or archivo.existencia_cifrado()):
                archivo.crear()
                print("\nArchivo creado")
            else:
                print("Archivo ya existente, no puedes crear uno ahora")

        case "2":
            print(
                "¿Estas seguro de querer eliminar el archivo seguro?\n3 -> Si\n4 -> Atrás"
            )
            confirmacion = input()
            match confirmacion:
                case "3":
                    borrado1 = archivo.eliminar_archivo_simple()
                    borrado2 = archivo.eliminar_archivo_cifrado()
                    if borrado1 or borrado2:
                        print("Archivo borrado")
                    else:
                        print("No había nada que borrar")

                case "4":
                    print("\nVolviendo al menú principal")
                    return
        case "4":
            return


def submenu_cifrado(archivo, cifrador):
    try:
        opcion = opciones_submenu_cifrado()
    except ValueError as e:
        print(f"Error: {e}")
        return

    match opcion:
        case "1":
            if not archivo.existencia_cifrado():
                try:
                    ruta_cifrada = cifrador.cifrar(archivo.ruta)
                    archivo.guardar_archivo_cifrado(ruta_cifrada)
                    print(f"Archivo guardado: {archivo.ruta_cifrada}")
                    archivo.eliminar_archivo_simple()
                except ValueError as e:
                    print(f"Error: {e}")
                except FileNotFoundError as e:
                    print(f"Error: {e}")
            else:
                print("El archivo ya está cifrado")
        case "2":
            if archivo.existencia_cifrado():
                try:
                    cifrador.descifrar(archivo.ruta_cifrada)
                    archivo.eliminar_archivo_cifrado()
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("No hay archivo cifrado que descifrar")
        case "4":
            return


def menu_principal():
    
    archivo = ArchivoSeguro()
    notas = Notas(archivo)
    cifrador = Cifrador()
    print("\n--- Bienvenido ---")
    while True:
        try:
            opcion = opciones_menu_principal()
        except ValueError as e:
            print(f"Error: {e}")
            continue

        match opcion:
            case "1":
                if not archivo.existencia() and not archivo.existencia_cifrado():
                    print("Archivo no existe, crea uno antes.")
                    continue
                else:
                    submenu_cifrado(archivo, cifrador)

            case "2":
                if archivo.existencia() and not archivo.existencia_cifrado():
                    submenu_notas(notas, recibir_titulo)
                else:
                    print(
                        "No puedes acceder a notas, archivo no existe o está cifrado."
                    )
                    continue

            case "3":
                submenu_archivo(archivo)
            case "4":
                break

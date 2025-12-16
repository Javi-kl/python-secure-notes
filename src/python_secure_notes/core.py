import json
import os
from .cifrar_descifrar import Cifrador


class ArchivoSeguro:
    def __init__(self) -> None:
        self.ruta = "caja_fuerte.json"
        self.ruta_cifrada = ""
        self.ruta_estado = "estado_archivo_cifrado.json"

        self.cargar_estado()

    def guardar_archivo_cifrado(self, ruta_cifrada):
        self.ruta_cifrada = ruta_cifrada
        self.guardar_estado()

    def guardar_estado(self):
        with open(self.ruta_estado, "w") as f:
            json.dump({"ruta_cifrada": self.ruta_cifrada}, f, indent=4)

    def cargar_estado(self):
        if not os.path.isfile(self.ruta_estado):
            return
        with open(self.ruta_estado, "r") as file:
            data = json.load(file)
            self.ruta_cifrada = data.get("ruta_cifrada", "")
        if self.ruta_cifrada and not os.path.isfile(self.ruta_cifrada):
            self.ruta_cifrada = ""

    def crear(self, contenido=[]):
        with open(self.ruta, "w") as file:
            json.dump(contenido, file, indent=4)

    def existencia_cifrado(self) -> bool:
        return os.path.isfile(self.ruta_cifrada)

    def existencia(self) -> bool:
        return os.path.isfile(self.ruta)

    def eliminar_archivo_cifrado(self):
        if self.existencia_cifrado():
            os.remove(self.ruta_cifrada)
            return True
        return False

    def eliminar_archivo_simple(self):
        if self.existencia():
            os.remove(self.ruta)
            return True
        return False


class RecolectorDatos:
    @staticmethod
    def recibir_titulo():
        titulo_input = input("Introduce el titulo.\n-> ").lower().strip()
        if not titulo_input:
            raise ValueError("Rellena todos los campos")

        if titulo_input.isdigit():
            raise ValueError("El titulo no puede contener solo digitos")

        if len(titulo_input) > 150:
            raise ValueError("Titulo demasiado largo. Max: 150 caracteres")
        return titulo_input

    @staticmethod
    def recibir_cuerpo():
        cuerpo_input = input("Introduce el cuerpo.\n-> ").lower()
        if not cuerpo_input:
            raise ValueError("Rellena todos los campos")

        if len(cuerpo_input) > 5000:
            raise ValueError("Cuerpo demasiado largo. Max: 5000 caracteres")
        return cuerpo_input

    @staticmethod
    def crear_contenido():
        titulo_input = RecolectorDatos.recibir_titulo()
        cuerpo_input = RecolectorDatos.recibir_cuerpo()
        contenido = {
            "titulo": titulo_input,
            "cuerpo": cuerpo_input,
        }
        return contenido


class Notas:
    def __init__(self, recolector: RecolectorDatos, archivo: ArchivoSeguro) -> None:
        self.recolector = recolector
        self.archivo = archivo

    def extraer_notas(self):
        with open(self.archivo.ruta, "r") as file:
            notas = json.load(file)
            return notas

    def crear(self):
        try:
            contenido = self.recolector.crear_contenido()
            notas = self.extraer_notas()
            notas.append(contenido)
            self.archivo.crear(notas)
        except ValueError as e:
            print(f"Error: {e}")

    def modificar(self, titulo):
        try:
            nuevo = self.recolector.crear_contenido()
            notas = self.extraer_notas()
            for n in notas:
                if n["titulo"] == titulo:
                    n["titulo"] = nuevo["titulo"]
                    n["cuerpo"] = nuevo["cuerpo"]
                    break
            self.archivo.crear(notas)
        except ValueError as e:
            print(f"Error: {e}")

    def listar_titulos(self):
        notas = self.extraer_notas()
        notas_ordenadas = sorted(notas, key=lambda x: x["titulo"])
        return [n["titulo"] for n in notas_ordenadas if len(notas) >= 1]

    def leer_cuerpo(self, titulo):
        notas = self.extraer_notas()
        return "".join([n["cuerpo"] for n in notas if n["titulo"] == titulo])

    def existencia_titulo(self, titulo):
        notas = self.extraer_notas()
        existe = any(n["titulo"] == titulo for n in notas)
        if not existe:
            raise ValueError("Ese titulo no existe")

    def eliminar(self, titulo):
        notas = self.extraer_notas()
        notas_nuevas = [n for n in notas if n["titulo"] != titulo]
        self.archivo.crear(notas_nuevas)

    def existen_notas(self):
        notas = self.extraer_notas()
        return notas != None


class MostradorOpciones:
    @staticmethod
    def validar_opcion(opcion, opciones_validas):
        opciones_formated = opciones_validas[0] + "-" + opciones_validas[-1]
        if opcion not in opciones_validas:
            raise ValueError(f"Debes introducir un digito: {opciones_formated}")

    @staticmethod
    def menu_principal():
        print("\n--- Menú principal ---")
        print("1 -> Opciones Cifrado")
        print("2 -> Opciones Notas")
        print("3 -> Opciones archivo")
        print("4 -> Salir")
        opcion = input("-> ")
        MostradorOpciones.validar_opcion(opcion, ["1", "2", "3", "4"])
        return opcion

    @staticmethod
    def submenu_notas_existentes():
        print("\nNota encontrada\n")
        print("Opciones notas existentes:")
        print("1 -> Leer nota")
        print("2 -> Modificar nota")
        print("3 -> Borrar nota")
        print("4 -> Volver atrás")
        opcion = input("-> ")
        MostradorOpciones.validar_opcion(opcion, ["1", "2", "3", "4"])
        return opcion

    @staticmethod
    def submenu_notas():
        print("Opciones notas:\n1 -> Nueva nota")
        print("2 -> Seleccionar nota existente 'por título'")
        print("4 -> Volver atrás")
        opcion = input("-> ").lower()
        MostradorOpciones.validar_opcion(opcion, ["1", "2", "4"])
        return opcion

    @staticmethod
    def submenu_cifrado():
        print("Opciones cifrado")
        print("1 -> Cifrar archivo")
        print("2 -> Descifrar archivo")
        print("4 -> Volver atrás")
        opcion = input("-> ")
        MostradorOpciones.validar_opcion(opcion, ["1", "2", "4"])
        return opcion

    @staticmethod
    def submenu_archivo():
        print("Opciones archivo")
        print("1 -> Crear archivo")
        print("2 -> Borrar archivo")
        print("4 -> Volver atrás")
        opcion = input("-> ")
        MostradorOpciones.validar_opcion(opcion, ["1", "2", "4"])
        return opcion


opciones = MostradorOpciones()
archivo = ArchivoSeguro()
recolector = RecolectorDatos()
notas = Notas(recolector, archivo)
cifrador = Cifrador()


def submenu_notas():
    print("\nNotas actuales: ")
    for t in notas.listar_titulos():
        print(t)
    print()
    try:
        opcion_notas = opciones.submenu_notas()
    except ValueError as e:
        print(f"Error: {e}")
        return

    if opcion_notas == "4":
        print("\nVolviendo al menú principal")
        return
    elif opcion_notas == "1":
        notas.crear()
    elif opcion_notas == "2":
        titulo = recolector.recibir_titulo()
        try:
            notas.existencia_titulo(titulo)
        except ValueError as e:
            print(f"Error: {e}")
            print("Volviendo a menú")
            return
        try:
            opcion_notas_existentes = opciones.submenu_notas_existentes()
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


def submenu_archivo():
    try:
        opcion = opciones.submenu_archivo()
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


def submenu_cifrado():
    try:
        opcion = opciones.submenu_cifrado()
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
    print("\n--- Bienvenido ---")
    while True:
        try:
            opcion = opciones.menu_principal()
        except ValueError as e:
            print(f"Error: {e}")
            continue

        match opcion:
            case "1":
                if not archivo.existencia() and not archivo.existencia_cifrado():
                    print("Archivo no existe, crea uno antes.")
                    continue
                else:
                    submenu_cifrado()

            case "2":
                if archivo.existencia() and not archivo.existencia_cifrado():
                    submenu_notas()
                else:
                    print(
                        "No puedes acceder a notas, archivo no existe o está cifrado."
                    )
                    continue

            case "3":
                submenu_archivo()
            case "4":
                break

import json
import os
import time


class ArchivoSeguro:
    def __init__(self) -> None:
        self.titulo = "cajafuerte.json"

    def crear(self, contenido=[]):
        with open(self.titulo, "w") as file:
            json.dump(contenido, file, indent=4)

    def existencia(self) -> bool:
        return os.path.isfile(self.titulo)

    def eliminar(self):
        os.remove(self.titulo)


class RecolectorDatos:
    @staticmethod
    def recibir_inputs():
        titulo_input = input("Introduce el titulo.\n-> ").lower().strip()
        cuerpo_input = input("Introduce el cuerpo.\n-> ").lower()
        if not titulo_input or not cuerpo_input:
            raise ValueError("Rellena todos los campos")

        if titulo_input.isdigit():
            raise ValueError("El titulo no puede contener solo digitos")

        if len(titulo_input) > 150:
            raise ValueError("Titulo demasiado largo. Max: 150 caracteres")

        if len(cuerpo_input) > 5000:
            raise ValueError("Cuerpo demasiado largo. Max: 5000 caracteres")

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
        with open(self.archivo.titulo, "r") as file:
            notas = json.load(file)
            return notas

    def crear(self):
        try:
            contenido = self.recolector.recibir_inputs()
            notas = self.extraer_notas()
            notas.append(contenido)
            self.archivo.crear(notas)
        except ValueError as e:
            print(f"Error: {e}")

    def modificar(self, titulo):
        notas.eliminar(titulo)
        notas.crear()

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


class MostradorOpciones:
    @staticmethod
    def principal():
        print("\n--- Menú principal ---")
        print("1 -> Nueva nota")
        print("2 -> Listar notas")
        print("3 -> Eliminar archivo CIFRADO")
        print("4 -> Salir")
        opcion = input("-> ")

        if not opcion.isdigit() or opcion not in [
            "1",
            "2",
            "3",
            "4",
        ]:
            raise ValueError("Debes introducir un digito (1-4)")
        return opcion

    @staticmethod
    def notas_existentes():
        print("\nNota encontrada\n")
        print("Menú de notas:")
        print("1 -> Leer nota")
        print("2 -> Modificar nota")
        print("3 -> Borrar nota")
        print("4 -> Atrás")
        opcion = input("-> ")
        if not opcion.isdigit() or opcion not in ["1", "2", "3", "4"]:
            raise ValueError("Debes introducir un digito (1-4)")
        return opcion

    @staticmethod
    def titulo_o_atras():
        print("Opciones:\nEscribir titulo para opciones")
        print("4 -> Volver al atrás")
        opcion = input("-> ").lower()

        if opcion.isdigit() and opcion != "4" or not opcion.isalnum():
            raise ValueError("Debes introducir (4) o texto")
        return opcion


opciones = MostradorOpciones()
archivo = ArchivoSeguro()
recolector = RecolectorDatos()
notas = Notas(recolector, archivo)


def gestionar_notas_existentes():

    print("\nNotas actuales: ")
    for t in notas.listar_titulos():
        print(t)
    print()
    try:
        opcion_titulo = opciones.titulo_o_atras()
    except ValueError as e:
        print(f"Error: {e}")
        return

    if opcion_titulo == "4":
        print("\nVolviendo al menú principal")
        return
    else:
        try:
            notas.existencia_titulo(opcion_titulo)
        except ValueError as e:
            print(f"Error: {e}")
            print("Volviendo a menú")
            return
        try:
            opcion_notas = opciones.notas_existentes()
        except ValueError as e:
            print(f"Error: {e}")
            return
        match opcion_notas:
            case "1":
                print(f"\nLeyendo nota: {opcion_titulo}")
                print(notas.leer_cuerpo(opcion_titulo))
            case "2":
                print(f"\nModificando nota: {opcion_titulo}")
                notas.modificar(opcion_titulo)
            case "3":
                print(f"\nEliminando nota: {opcion_titulo}")
                notas.eliminar(opcion_titulo)
            case "4":
                print("\nVolviendo al menú principal")
                menu_principal()


def menu_principal():
    if not archivo.existencia():
        print(f"Creando archivo seguro...")
        archivo.crear()
        time.sleep(1)

    print("\n--- Bienvenido ---")
    while True:
        try:
            opcion = opciones.principal()
        except ValueError as e:
            print(f"Error: {e}")
            continue
        match opcion:
            case "1":
                notas.crear()
            case "2":
                gestionar_notas_existentes()
            case "3":
                print(
                    "¿Estas seguro de querer eliminar el archivo seguro?\n3 -> Si\n4 -> Atrás"
                )
                confirmacion = input()
                match confirmacion:
                    case "3":
                        print("Archivo borrado")
                        archivo.eliminar()
                    case "4":
                        print("\nVolviendo al menú principal")
                        continue
            case "4":
                break

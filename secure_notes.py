import json
import os
import time


class ArchivoSeguro:
    def __init__(self) -> None:
        self.titulo_archivo = "cajafuerte.json"

    def crear(self):
        with open(self.titulo_archivo, "w") as file:
            json.dump([], file, indent=2)

    def existencia(self) -> bool:
        return os.path.isfile(self.titulo_archivo)

    def eliminar(self):
        os.remove(self.titulo_archivo)


class RecolectorDatos:
    @staticmethod
    def recibir_inputs():
        titulo_input = input("Introduce el titulo de la nota.\n-> ")
        cuerpo_input = input("Introduce el cuerpo de la nota.\n-> ")
        contenido = {
            "titulo": titulo_input,
            "cuerpo": cuerpo_input,
        }
        return contenido


class Notas:
    # No tengo claro porque debo/buena practica, pasar estas instancias como atributo, si puedo acceder directamente a ellas.
    def __init__(self, recolector: RecolectorDatos, archivo: ArchivoSeguro) -> None:
        self.recolector = recolector
        self.archivo = archivo

    def crear(self):
        contenido = recolector.recibir_inputs()
        with open(archivo.titulo_archivo, "r") as file:
            notas = json.load(file)
            notas.append(contenido)
        with open(archivo.titulo_archivo, "w") as file:
            json.dump(notas, file, indent=4)

    def listar_titulos(self):
        with open(archivo.titulo_archivo, "r") as file:
            notas = json.load(file)
            notas_ordenadas = sorted(notas, key=lambda x: x["titulo"])
            return [n["titulo"] for n in notas_ordenadas if len(notas) >= 1]

    def leer_cuerpo(self, titulo):
        with open(archivo.titulo_archivo, "r") as file:
            notas = json.load(file)
            return "".join([n["cuerpo"] for n in notas if n["titulo"] == titulo])

    def existencia_titulo(self, titulo) -> bool:
        with open(archivo.titulo_archivo, "r") as file:
            notas = json.load(file)
            return any(
                n["titulo"] == titulo for n in notas
            )  # en cuanto 'any' encuentra un True se detiene y retorna

    def eliminar(self, titulo):
        with open(archivo.titulo_archivo, "r") as file:
            notas = json.load(file)
            notas_nuevas = [n for n in notas if n["titulo"] != titulo]

        with open(archivo.titulo_archivo, "w") as file:
            json.dump(notas_nuevas, file, indent=4)


archivo = ArchivoSeguro()
recolector = RecolectorDatos()
notas = Notas(recolector, archivo)


def menu_principal():
    print("Bienvenido")
    if archivo.existencia():
        print(f"Accediendo al programa...")
        time.sleep(1)
    else:
        print(f"Creando archivo seguro...")
        archivo.crear()
        time.sleep(1)

    while True:
        if archivo.existencia():
            print("\n--- Menú principal ---")
            print("1 -> Nueva nota")
            print("2 -> Listar notas")
            print("3 -> Eliminar archivo CIFRADO")
            print("4 -> Salir")
            opcion_menu_principal = str(input("-> "))

            match opcion_menu_principal:
                case "1":
                    notas.crear()
                case "2":
                    print("\nNotas actuales: ")
                    for t in notas.listar_titulos():
                        print(t)
                    print()
                    opcion_titulo_o_atras = str(
                        input(
                            "Escribe el titulo de una nota para mas opciones"
                            "\nO pulsa '4' para volver atrás-> "
                        ).lower()
                    )
                    if opcion_titulo_o_atras == "4":
                        print("\nVolviendo al menú principal")
                        continue
                    else:
                        if (
                            notas.existencia_titulo(opcion_titulo_o_atras)
                            and archivo.existencia()
                        ):
                            print("\nNota encontrada\n")
                            print("Menú de notas:")
                            print("1 -> Leer nota")
                            print("2 -> Modificar nota")
                            print("3 -> Borrar nota")
                            print("4 -> Atrás")
                            opcion_menu_notas = input("-> ")
                            match opcion_menu_notas:
                                case "1":
                                    print(f"\nLeyendo nota: {opcion_titulo_o_atras}")
                                    print(notas.leer_cuerpo(opcion_titulo_o_atras))
                                case "2":
                                    print(
                                        f"\nModificando nota: {opcion_titulo_o_atras}"
                                    )
                                    notas.eliminar(opcion_titulo_o_atras)
                                    notas.crear()

                                case "3":
                                    print(f"\nEliminando nota: {opcion_titulo_o_atras}")
                                    notas.eliminar(opcion_titulo_o_atras)

                                case "4":
                                    print("\nVolviendo al menú principal")
                                    continue

                        else:
                            print(
                                "La nota no existe o el titulo esta mal (manejar error)???"
                            )
                            print("\nVolviendo al menú principal")

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
                    print("\nSaliendo del programa")
                    time.sleep(1)
                    break
        else:
            print("No se encuentra el archivo, reinicia el programa para crear otro.")


menu_principal()

import json
import os
import time


class ArchivoSeguro:
    def __init__(self) -> None:
        self.titulo_archivo = "cajafuerte.json"

    def crear_archivo(self):
        with open(self.titulo_archivo, "w") as file:
            json.dump([], file, indent=2)

    def existencia_archivo(self) -> bool:
        return os.path.isfile(self.titulo_archivo)

    def eliminar_archivo_seguro(self):
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


class AdministradorNotas:
    # No tengo claro porque debo/buena practica, pasar estas instancias como atributo, si puedo acceder directamente a ellas.
    def __init__(self, recolector: RecolectorDatos, archivo: ArchivoSeguro) -> None:
        self.recolector = recolector
        self.archivo = archivo

    def crear_nota(self):
        if archivo.existencia_archivo():
            contenido = recolector.recibir_inputs()
            with open(archivo.titulo_archivo, "r") as file:
                notas = json.load(file)  # Extrae la lista que hay dentro del json
                notas.append(contenido)

            with open(archivo.titulo_archivo, "w+") as file:
                json.dump(notas, file, indent=4)
            # return True
        else:
            print("El archivo no existe, reinicia el programa para crear uno nuevo")
            # En un futuro quizas aplicar aqui la opción de crear un nuevo archivo seguro
            # return False

    def listar_titulos(self):
        if archivo.existencia_archivo() and administrador.existencia_nota():
            with open(archivo.titulo_archivo, "r") as file:
                notas = json.load(file)
                for nota in notas:
                    print(f"Nota: {nota['titulo']}")

        else:
            print("No existen notas, crea alguna primero")
            return

    def modificar(self):
        pass

    def mostrar_contenido(self):
        pass

    def existencia_nota(self) -> bool:
        with open(archivo.titulo_archivo, "r") as file:
            notas = json.load(file)
            return len(notas) >= 1

    def eliminar_nota(self) -> bool:
        pass


archivo = ArchivoSeguro()
recolector = RecolectorDatos()
administrador = AdministradorNotas(recolector, archivo)


def menu_principal():
    print("Bienvenido")
    # 1.-
    if archivo.existencia_archivo():
        print(f"Accediendo al programa...")
        time.sleep(1)
    else:
        print(f"Creando archivo seguro...")
        archivo.crear_archivo()
        time.sleep(1)

    while True:
        print("\n--- Menú principal ---")
        print("1 -> Nueva nota")
        print("2 -> Listar notas")
        print("3 -> Eliminar archivo seguro")
        print("4 -> Salir")
        opcion_menu_principal = str(input("Elige una opción.\n-> "))

        match opcion_menu_principal:
            case "1":
                administrador.crear_nota()
            case "2":
                administrador.listar_titulos()
                opcion_notas = str(
                    input(
                        "Escribe el titulo de una nota para mas opciones"
                        "\nO pulsa '4' para volver atrás-> "
                    ).lower()
                )
                if opcion_notas == "4":
                    continue
                """elif existencia_nota:
                    
                    print("Menú de notas:")
                    print("1 -> Leer nota")
                    print("2 -> Modificar nota")
                    print("3 -> Borrar nota")
                    print("4 -> Atrás")
                elif not existencia_nota:
                    print("La nota no existe o el titulo esta mal (manejar error)???")
                else:
                    print("Introduce una opción valida, Indica la excepcion")
                    raise Exception"""

            case "3":
                print(
                    "¿Estas seguro de querer eliminar el archivo seguro?\n3 -> Si\n4 -> Atrás"
                )
                confirmacion = input()
                match confirmacion:
                    case "3":
                        print("Archivo borrado")
                        archivo.eliminar_archivo_seguro()
                    case "4":
                        continue

            case "4":
                print("Saliendo")
                break


menu_principal()

import json
import os
import time


class ArchivoSeguro:
    def __init__(self) -> None:
        self.titulo_archivo_seguro = "cajafuerte.json"
        self.contenido = {}

    def guardar_contenido(self): #TODO
        self.contenido = 
    
    def crear_archivo(self):
        self.contenido = {
            "titulo": "cajafuerte.json",
            "cuerpo": "Este es un ejemplo de nota segura",
        }

        with open(self.titulo_archivo_seguro, "w") as file:
            json.dump(self.contenido, file, indent=2)

    def existencia_archivo(self) -> bool:
        return os.path.isfile(self.titulo_archivo_seguro)

    def eliminar_archivo_seguro(self):
        os.remove(self.titulo_archivo_seguro)


class RecolectorDatos:
    # Este metodo sirve para crear, o modificar notas en general

    @staticmethod
    def recibir_inputs():
        titulo_input = input("Introduce el titulo de la nota.\n-> ")
        cuerpo_input = input("Introduce el cuerpo de la nota.\n-> ")
        contenido = {"titulo": titulo_input, "cuerpo": cuerpo_input}
        return contenido


class AdministradorNotas:
    # No tengo claro porque debo/buena practica, pasar estas instancias como atributo, si puedo acceder directamente a ellas.
    def __init__(
        self, recolector_datos: RecolectorDatos, archivo_seguro: ArchivoSeguro
    ) -> None:
        self.recolector_datos = recolector_datos
        self.archivo_seguro = archivo_seguro

    def crear_nota(self):
        if archivo_seguro.existencia_archivo():
            #TODO Esto debe hacerse en archivoseguro.guardarcontenido =???????
            contenido = recolector_datos.recibir_inputs()
            with open(archivo_seguro.titulo_archivo_seguro, "a") as file:
                json.dump(contenido, file, indent=4)
        else:
            print("El archivo no existe, reinicia el programa para crear uno nuevo")

    def listar_titulos(self):
        pass

    def modificar(self):
        pass

    def mostrar_contenido(self):
        pass

    def existencia_nota(self) -> bool:
        pass

    def eliminar_nota(self) -> bool:
        pass


archivo_seguro = ArchivoSeguro()
recolector_datos = RecolectorDatos()
administrador_notas = AdministradorNotas(recolector_datos, archivo_seguro)


def menu_principal():
    print("Bienvenido")
    # 1.-
    if archivo_seguro.existencia_archivo():
        print(f"Accediendo al programa...")
        time.sleep(1)
    else:
        print(f"Creando archivo seguro...")
        archivo_seguro.crear_archivo()
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
                administrador_notas.crear_nota()
            case "2":
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
                        archivo_seguro.eliminar_archivo_seguro()
                    case "4":
                        continue

            case "4":
                print("Saliendo")
                break


menu_principal()

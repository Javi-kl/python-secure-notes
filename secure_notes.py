import json


class ArchivoSeguro:
    def __init__(self) -> None:
        self.archivo_seguro = []

    def guardar_archivo(self) -> bool:
        pass

    def crear_archivo(self):
        titulo_archivo = f"cajafuerte{1}.json"
        contenido_vacio = {"titulo": "", "cuerpo": ""}
        with open(titulo_archivo, "w") as file:
            json.dump(contenido_vacio, file, indent=2)

    def existencia_archivo(self) -> bool:
        return len(self.archivo_seguro) > 0

    def eliminar_archivo_seguro(self) -> bool:
        pass


class AdministradorNotas:

    def __init__(self) -> None:
        pass

    def crear_nota(self):
        pass

    def listar_titulos(self):
        pass

    def modificar(self):
        pass

    def mostrar_contenido(self):
        pass

    def comprobar_existencia_nota(self) -> bool:
        pass

    def eliminar_nota(self) -> bool:
        pass


archivo_seguro = ArchivoSeguro()
administrador_notas = AdministradorNotas()


def menu_principal():
    print("Bienvenido")
    # 1.-
    print(archivo_seguro.existencia_archivo())
    if archivo_seguro.existencia_archivo() == False:
        archivo_seguro.crear_archivo()
        print(f"Existencia: {archivo_seguro.existencia_archivo()}")
    else:
        # Load archivo seguro
        """Si no existe ningun archivo seguro: # TODO
        print("Creando archivo seguro ")
        Delay 2 seg
        Si existe:
        print("Accediendo al archivo seguro")
        Delay 2 seg
        """
    while True:
        print("Menú principal:")
        print("1 -> Nueva nota")
        print("2 -> Listar notas")
        print("3 -> Eliminar archivo seguro")
        print("4 -> Salir")
        opcion_menu_principal = str(input("Elige una opción.\n-> "))

        match opcion_menu_principal:
            case "1":
                pass
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
                    raise Exception
                
            case "3":
                pass
            case "4":
                break"""


menu_principal()

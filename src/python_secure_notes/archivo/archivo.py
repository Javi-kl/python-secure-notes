import json
import os


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
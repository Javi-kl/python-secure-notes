from ..core.recolector_data import crear_contenido 
from ..archivo.archivo import ArchivoSeguro
import json

class Notas:
    def __init__(self, archivo: ArchivoSeguro) -> None:
        self.archivo = archivo

    def extraer_notas(self):
        with open(self.archivo.ruta, "r") as file:
            notas = json.load(file)
            return notas

    def crear(self):
        try:
            contenido = crear_contenido()
            notas = self.extraer_notas(). He
            notas.append(contenido)
            self.archivo.crear(notas)
        except ValueError as e:
            print(f"Error: {e}")

    def modificar(self, titulo):
        try:
            nuevo = crear_contenido()
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
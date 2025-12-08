from cryptography.fernet import Fernet
from .core import archivo


class Cifrador:

    def generar_clave(self):
        key = Fernet.generate_key()
        return Fernet(key)

    def cifrar_archivo(self, archivo):
        f = self.generar_clave()
        token = f.encrypt(archivo)


cifrador = Cifrador()
cifrador.cifrar_archivo(archivo)

import base64
import os

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass


class Cifrador:
    ITERACIONES = 480000  # Estandar 2025
    SALT_BYTES = 16

    def __init__(self, ruta_salt="salt.bin"):
        self.ruta_salt = ruta_salt
        if not os.path.exists(ruta_salt):
            self._generar_salt()

    def _generar_salt(self):
        salt = os.urandom(self.SALT_BYTES)
        with open(self.ruta_salt, "wb") as file:
            file.write(salt)
        print(f"Salt generado en {self.ruta_salt}")

    def _derivar_clave(self, password: str) -> bytes:
        """Deriva clave Fernet desde contraseña
        args: Contraseña usuario
        returns: Clave Fernet válida en base64"""
        with open(self.ruta_salt, "rb") as file:
            salt = file.read()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=self.ITERACIONES,
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    # se llama al cifrar por primera vez y al cerrar archivo
    def cifrar(self, ruta_archivo: str, password: str = None):
        """args: ruta del archivo a cifrar
            Contraseña(Si es None, la pide por consola)
        returns: Path del archivo cifrado
        """
        if password is None:
            password = getpass.getpass("Crea una contraseña para cifrar el archivo")

        key = self._derivar_clave(password)
        f = Fernet(key)

        with open(ruta_archivo, "rb") as file:
            datos = file.read()

        datos_cifrados = f.encrypt(datos)

        ruta_cifrada = ruta_archivo + ".encrypted"

        with open(ruta_cifrada, "wb") as file:
            file.write(datos_cifrados)

        print(f"Cifrado: {ruta_cifrada}")
        return ruta_cifrada

    def descifrar(self, ruta_cifrada: str, password: str = None):
        """args: ruta del archivo a descifrar
        returns: path del archivo descifrado"""

        if password is None:
            password = getpass.getpass("Introduce tu contraseña")

        key = self._derivar_clave(password)
        f = Fernet(key)

        with open(ruta_cifrada, "rb") as file:
            datos_cifrados = file.read()

        try:
            datos_originales = f.decrypt(datos_cifrados)
        except InvalidToken:
            raise ValueError("Contraseña incorrecta")

        ruta_descifrada = ruta_cifrada.replace(".encrypted", "")

        with open(ruta_descifrada, "wb") as file:
            file.write(datos_originales)

        print(f"Descifrado {ruta_descifrada}")
        return ruta_descifrada

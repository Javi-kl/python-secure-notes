import base64  # urlsafe_b64encode permite transformar los bytes generados por PBKDF2HMAC en una clave legible para Fernet
import os  # Permite usar el sistema operativo
from cryptography.fernet import Fernet  # Realiza el cifrado y descifrado
from cryptography.hazmat.primitives import (
    hashes,
)  # Permite a PBKDF2HMAC , utilizar SHA256(estándar actual) para crear la clave

# Convierte la clave de usuario + salt, en una clave válida para fernet, ejecutando 480000iteraciones (estandar actual)
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass  # Permite al usuario introducir una contraseña oculta en pantalla
from .core import archivo


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
            password = getpass.getpass(
                "Introduce tu contraseña"
            )  # Getpass se puede utilizar en windows?

        key = self._derivar_clave(password)
        f = Fernet(key)

        with open(ruta_cifrada, "rb") as file:
            datos_cifrados = file.read()

        try:
            datos_originales = f.decrypt(datos_cifrados)
        except:
            ValueError("Contraseña incorrecta")

        ruta_descifrada = ruta_cifrada.replace(".encrypted", "")

        with open(ruta_descifrada, "wb") as file:
            file.write(datos_originales)

        print(f"Descifrado {ruta_descifrada}")
        return ruta_descifrada


cifrador = Cifrador()

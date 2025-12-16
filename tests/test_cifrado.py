from pathlib import Path
from src.python_secure_notes.cifrar_descifrar import Cifrador
import pytest


def test_cifrar_crea_archivo_encrypted(tmp_path):
    ruta = tmp_path / "datos.txt"
    ruta.write_text("Hola", encoding="utf-8")

    cif = Cifrador(ruta_salt=str(tmp_path / "salt.bin"))
    ruta_cifrada = cif.cifrar(str(ruta), password="1234")

    assert Path(ruta_cifrada).is_file()


def test_descifrar_password_incorrecta_lanza_valueerror(tmp_path):
    ruta = tmp_path / "datos.txt"
    ruta.write_text("Hola", encoding="utf-8")

    cif = Cifrador(ruta_salt=str(tmp_path / "salt.bin"))
    ruta_cifrada = cif.cifrar(str(ruta), password="bien")

    with pytest.raises(ValueError):
        cif.descifrar(ruta_cifrada, password="mal")


def test_cifrar_y_descifrar_recupera_contenido(tmp_path):
    ruta = tmp_path / "datos.txt"
    ruta.write_text("Hola", encoding="utf-8")

    cif = Cifrador(ruta_salt=str(tmp_path / "salt.bin"))
    ruta_cifrada = cif.cifrar(str(ruta), password="1234")
    ruta_descifrada = cif.descifrar(ruta_cifrada, password="1234")

    assert Path(ruta_descifrada).read_text(encoding="utf-8") == "Hola"

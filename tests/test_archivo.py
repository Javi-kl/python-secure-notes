import json
from src.python_secure_notes.core import ArchivoSeguro


def test_archivo_crear_y_guardar_contenido(tmp_path):
    ruta_archivo = tmp_path / "archivo_cifrado_test.json"
    archivo = ArchivoSeguro()
    archivo.titulo = str(ruta_archivo)

    contenido = [{"titulo": "t1", "cuerpo": "c1"}]

    archivo.crear(contenido)

    assert ruta_archivo.exists()

    with ruta_archivo.open("r") as f:
        datos = json.load(f)
    assert datos == contenido


def test_existencia_devuelve_bool(tmp_path):
    ruta_archivo = tmp_path / "archivo_cifrado_test.json"
    archivo = ArchivoSeguro()
    archivo.titulo = str(ruta_archivo)

    assert archivo.existencia() is False

    archivo.crear([])

    assert archivo.existencia() is True


def test_eliminar_borra_archivo(tmp_path):
    ruta_archivo = tmp_path / "cajafuerte_test.json"

    archivo = ArchivoSeguro()
    archivo.titulo = str(ruta_archivo)

    archivo.crear([])

    assert ruta_archivo.exists()

    archivo.eliminar()

    assert not ruta_archivo.exists()

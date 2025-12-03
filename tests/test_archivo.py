import pytest
import json
import os
from src.python_secure_notes.core import ArchivoSeguro


def test_archivo_creado_correctamente():
    # --- 1. ARRANGE (Preparar) ---
    archivo = ArchivoSeguro()

    archivo.titulo = "test_temporal.json"

    datos_a_guardar = [{"titulo": "prueba", "cuerpo": "test"}]

    # --- 2. ACT (Actuar) ---
    archivo.crear(datos_a_guardar)

    # --- 3. ASSERT (Comprobar) ---
    assert os.path.isfile("test_temporal.json") is True

    with open("test_temporal.json", "r") as f:
        contenido_leido = json.load(f)
        assert contenido_leido == datos_a_guardar

    # limpiar archivo
    if archivo.existencia():
        archivo.eliminar()

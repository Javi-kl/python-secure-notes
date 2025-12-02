import pytest
from src.python_secure_notes.core import RecolectorDatos

# Casos de prueba válidos
casos_validos = [("mi titulo", "mi cuerpo"), ("título con ñ", "cuerpo con acentos é")]


@pytest.mark.parametrize("titulo_input, cuerpo_input", casos_validos)
def test_recibir_inputs_correctamente(monkeypatch, titulo_input, cuerpo_input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter([titulo_input, cuerpo_input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    resultado = RecolectorDatos.recibir_inputs()

    # --- 3. ASSERT (Comprobar) ---
    assert resultado == {"titulo": titulo_input, "cuerpo": cuerpo_input}


"""casos_invalidos = []


@pytest.mark.parametrize("titulo_input", "cuerpo_input")
def test_recibr_inputs_correctamente(monkeypatch, titulo_input, cuerpo_input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter([titulo_input, cuerpo_input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    resultado = RecolectorDatos.recibir_inputs()

    # --- 3. ASSERT (Comprobar) ---
    assert resultado == {"titulo": "titulo_input", "cuerpo": "cuerpo_input"}"""

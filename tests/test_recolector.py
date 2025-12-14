import pytest
from src.python_secure_notes.core import RecolectorDatos


@pytest.mark.parametrize(
    "titulo_input", ["mi titulo", "título conñ", "titulo_con-signos."]
)
def test_recibir_titulo_correctamente(monkeypatch, titulo_input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter([titulo_input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    resultado = RecolectorDatos.recibir_titulo()

    # --- 3. ASSERT (Comprobar) ---
    assert resultado == titulo_input


@pytest.mark.parametrize(
    "cuerpo_input", ["mi cuerpo", "cuerpo con acentos é", "cuerpo normal"]
)
def test_recibir_cuerpo_correctamente(monkeypatch, cuerpo_input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter([cuerpo_input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    resultado = RecolectorDatos.recibir_cuerpo()

    # --- 3. ASSERT (Comprobar) ---
    assert resultado == cuerpo_input


@pytest.mark.parametrize("titulo_input", ["", "  ", "a" * 151, "1"])
def test_titulos_no_validos_lanzan_error(monkeypatch, titulo_input):

    respuestas = iter([titulo_input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    with pytest.raises(ValueError):
        RecolectorDatos.recibir_titulo()


@pytest.mark.parametrize("cuerpo_input", ["", "c" * 5001])
def test_cuerpos_no_validos_lanzan_error(monkeypatch, cuerpo_input):

    respuestas = iter([cuerpo_input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    with pytest.raises(ValueError):
        RecolectorDatos.recibir_cuerpo()

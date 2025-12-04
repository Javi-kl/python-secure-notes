import pytest
from src.python_secure_notes.core import RecolectorDatos

casos_validos = [
    ("mi titulo", "mi cuerpo"),
    ("título conñ", "cuerpo con acentos é"),
    (
        "titulo_con-signos.",
        "cuerpo normal",
    ),
]


@pytest.mark.parametrize("titulo_input, cuerpo_input", casos_validos)
def test_recibir_inputs_correctamente(monkeypatch, titulo_input, cuerpo_input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter([titulo_input, cuerpo_input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    resultado = RecolectorDatos.recibir_inputs()

    # --- 3. ASSERT (Comprobar) ---
    assert resultado == {"titulo": titulo_input, "cuerpo": cuerpo_input}


casos_invalidos = [
    ("", "cuerpo normal"),
    ("titulo normal", ""),
    ("  ", "cuerpo normal"),
    ("a" * 151, "cuerpo normal"),
    ("titulo normal", "c" * 5001),
    ("1", "cuerpo normal"),
]


@pytest.mark.parametrize("titulo_input, cuerpo_input", casos_invalidos)
def test_inputs_invalidos_lanzan_error(monkeypatch, titulo_input, cuerpo_input):

    respuestas = iter([titulo_input, cuerpo_input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    with pytest.raises(ValueError):
        RecolectorDatos.recibir_inputs()

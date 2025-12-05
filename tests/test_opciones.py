import pytest
from src.python_secure_notes.core import MostradorOpciones
import re


# Casos validos para menu principal
@pytest.mark.parametrize("input", ["1", "2", "3", "4"])
def test_recibir_input_numeros_validos_principal(monkeypatch, input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter(input)
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    resultado_menu_principal = MostradorOpciones.principal()

    # --- 3. ASSERT (Comprobar) ---
    assert resultado_menu_principal == input


# Casos validos para notas existentes
@pytest.mark.parametrize("input", ["1", "2", "3", "4"])
def test_recibir_input_numeros_validos_notas(monkeypatch, input):
    respuestas = iter(input)
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    resultado_notas_existentes = MostradorOpciones.notas_existentes()

    assert resultado_notas_existentes == input


# Casos validos para titulos
@pytest.mark.parametrize("input", ["a", "4"])
def test_recibir_input_letras_o_numeros_validos_titulos(monkeypatch, input):
    respuestas = iter(input)
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    resultado = MostradorOpciones.titulo_o_atras()

    assert resultado == input


# Casos NO validos para menú principal
@pytest.mark.parametrize("input", ["0.1", "t", " ", ".", "5"])
def test_recibir_inputs_lanzan_error_principal(monkeypatch, input):
    respuestas = iter([input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    mensaje_esperado = re.escape("Debes introducir un digito: 1-4")

    with pytest.raises(ValueError, match=mensaje_esperado):
        MostradorOpciones.principal()


# Casos NO validos para notas existentes
@pytest.mark.parametrize(
    "input",
    [
        "0.1",
        "t",
        " ",
        ".",
        "5",
    ],
)
def test_recibir_inputs_lanzan_error_notas(monkeypatch, input):
    respuestas = iter([input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    mensaje_esperado = re.escape("Debes introducir un digito: 1-4")

    with pytest.raises(ValueError, match=mensaje_esperado):
        MostradorOpciones.notas_existentes()


# Casos NO validos para titulos
@pytest.mark.parametrize("input", ["0.1", " ", ".", "3"])
def test_recibir_inputs_lanzan_error_titulos(monkeypatch, input):
    respuestas = iter([input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    mensaje_esperado = re.escape("Error: introduce (4) para volver o un titúlo de nota")

    with pytest.raises(ValueError, match=mensaje_esperado):
        MostradorOpciones.titulo_o_atras()

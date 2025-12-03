import pytest
from src.python_secure_notes.core import MostradorOpciones


casos_validos1 = [("1"), ("2"), ("3"), ("4")]


@pytest.mark.parametrize("input", casos_validos1)
def test_recibir_input_numeros_validos_principal(monkeypatch, input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter(input)
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    resultado_menu_principal = MostradorOpciones.principal()

    # --- 3. ASSERT (Comprobar) ---
    assert resultado_menu_principal == input


casos_validos2 = [("1"), ("2"), ("3"), ("4")]


@pytest.mark.parametrize("input", casos_validos2)
def test_recibir_input_numeros_validos_notas(monkeypatch, input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter(input)
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---

    resultado_notas_existentes = MostradorOpciones.notas_existentes()

    # --- 3. ASSERT (Comprobar) ---
    assert resultado_notas_existentes == input


casos_validos3 = ["a", "4"]


@pytest.mark.parametrize("input", casos_validos3)
def test_recibir_input_letras_o_numeros_validos_titulos(monkeypatch, input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter(input)
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    resultado = MostradorOpciones.titulo_o_atras()

    # --- 3. ASSERT (Comprobar) ---
    assert resultado == input


casos_no_validos1 = [("0.1"), ("t"), (" "), (".")]  # TODO cualquier número distinto 1-4


@pytest.mark.parametrize("input", casos_no_validos1)
def test_recibir_inputs_lanzan_error_principal(monkeypatch, input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter([input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    # --- 3. ASSERT (Comprobar) ---
    with pytest.raises(ValueError, match="Debes introducir un digito(1-4)"):
        MostradorOpciones.principal()


casos_no_validos2 = [("0.1"), ("t"), (" "), (".")]  # TODO cualquier número distinto 1-4


@pytest.mark.parametrize("input", casos_no_validos2)
def test_recibir_inputs_lanzan_error_notas(monkeypatch, input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter([input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    # --- 3. ASSERT (Comprobar) ---
    with pytest.raises(ValueError, match="Debes introducir un digito(1-4)"):
        MostradorOpciones.notas_existentes()


casos_no_validos3 = [("0.1"), (" "), (".")]  # TODO cualquier número distinto 4


@pytest.mark.parametrize("input", casos_no_validos3)
def test_recibir_inputs_lanzan_error_titulos(monkeypatch, input):
    # --- 1. ARRANGE (Preparar) ---
    respuestas = iter([input])
    monkeypatch.setattr("builtins.input", lambda msg: next(respuestas))

    # --- 2. ACT (Actuar) ---
    # --- 3. ASSERT (Comprobar) ---
    with pytest.raises(ValueError, match="Debes introducir un (4) o texto"):
        MostradorOpciones.notas_existentes()

"""Pruebas de la semana 2.

    PYTHON_DESDE_0_SOLUCION=1 pytest modulos/02-strings
"""

from pathlib import Path

from soporte.cargar import cargar

ejercicios = cargar(Path(__file__).resolve().parent)


def test_gritar_agrega_un_signo():
    assert ejercicios.gritar("hola") == "HOLA!"
    assert ejercicios.gritar("  cuidado  ") == "CUIDADO!"


def test_gritar_no_repite_signos():
    assert ejercicios.gritar("ya!!!") == "YA!"
    assert ejercicios.gritar("¡epa!") == "¡EPA!"
    assert ejercicios.gritar("   ") == "!"


def test_normalizar_correo():
    assert ejercicios.normalizar_correo("  Eva@Mail.COM ") == "eva@mail.com"


def test_formatear_ficha():
    assert (
        ejercicios.formatear_ficha("Evelyn", 28, "Querétaro")
        == "Evelyn tiene 28 años y vive en Querétaro."
    )


def test_contar_fragmento_sin_encimar():
    assert ejercicios.contar_fragmento("Banana", "na") == 2
    assert ejercicios.contar_fragmento("banana", "ANA") == 1
    assert ejercicios.contar_fragmento("aaa", "aa") == 1
    assert ejercicios.contar_fragmento("hola", "z") == 0


def test_palabras_colapsa_espacios():
    assert ejercicios.palabras("hola   mundo\tEvelyn") == ["hola", "mundo", "Evelyn"]
    assert ejercicios.palabras("   ") == []


def test_unir():
    assert ejercicios.unir(["Evelyn", "Arias"], " ") == "Evelyn Arias"
    assert ejercicios.unir(["2026", "10", "23"], "-") == "2026-10-23"
    assert ejercicios.unir([], "-") == ""
    assert ejercicios.unir(["solo"], ", ") == "solo"


def test_dominio_de_correo():
    assert ejercicios.dominio_de_correo("Eva@Mail.COM") == "mail.com"
    assert ejercicios.dominio_de_correo("  A@B@c.COM ") == "c.com"
    assert ejercicios.dominio_de_correo("sin-arroba") == "sin-arroba"


def test_enmascarar_telefono():
    assert ejercicios.enmascarar_telefono("5512345678") == "******5678"
    assert ejercicios.enmascarar_telefono("12345") == "*2345"
    assert ejercicios.enmascarar_telefono("1234") == "1234"
    assert ejercicios.enmascarar_telefono("") == ""
    assert ejercicios.enmascarar_telefono("abcde") == "*bcde"

"""Pruebas de la semana 6.

    PYTHON_DESDE_0_SOLUCION=1 pytest modulos/06-funciones
"""

from pathlib import Path

import pytest

from soporte.cargar import cargar

ejercicios = cargar(Path(__file__).resolve().parent)


def test_saludar():
    assert ejercicios.saludar("Evelyn") == "Hola, Evelyn."
    assert ejercicios.saludar("Evelyn", False) == "Hola, Evelyn."
    assert ejercicios.saludar("Evelyn", formal=True) == "Buenos días, Evelyn."


def test_con_iva_no_modifica_la_lista():
    precios = [100.0]
    assert ejercicios.con_iva(precios) == [116.0]
    assert precios == [100.0]
    assert ejercicios.con_iva([80], 0.05) == [84.0]
    assert ejercicios.con_iva([100], 0) == [100.0]


def test_estadisticas():
    assert ejercicios.estadisticas([4, 8, 6]) == {
        "minimo": 4,
        "maximo": 8,
        "promedio": 6,
        "cantidad": 3,
    }
    assert ejercicios.estadisticas([1, 2])["promedio"] == pytest.approx(1.5)


def test_estadisticas_vacias():
    with pytest.raises(ValueError, match="No se pueden calcular estadísticas de una lista vacía"):
        ejercicios.estadisticas([])


def test_unir():
    assert ejercicios.unir("hola", "Evelyn") == "hola Evelyn"
    assert ejercicios.unir("2026", "10", "23", separador="-") == "2026-10-23"
    assert ejercicios.unir() == ""


def test_aplicar_a_cada():
    assert ejercicios.aplicar_a_cada(str.upper, ["hola", "eva"]) == ["HOLA", "EVA"]
    assert ejercicios.aplicar_a_cada(str.upper, []) == []


def test_crear_saludo_recuerda_su_prefijo():
    hola = ejercicios.crear_saludo("Hola")
    noches = ejercicios.crear_saludo("Buenas noches")
    assert hola("Evelyn") == "Hola, Evelyn"
    assert noches("Evelyn") == "Buenas noches, Evelyn"
    assert hola("Luis") == "Hola, Luis"


def test_elegir():
    def hola():
        return "hola"

    def adios():
        return "adiós"

    assert ejercicios.elegir({"hola": hola, "adios": adios}, "adios", hola) == "adiós"
    assert ejercicios.elegir({}, "nada", hola) == "hola"


def test_anotar_no_comparte_la_lista_por_defecto():
    assert ejercicios.anotar("comprar café") == ["comprar café"]
    assert ejercicios.anotar("estudiar") == ["estudiar"]


def test_anotar_modifica_la_lista_que_le_pasan():
    base = ["pan"]
    assert ejercicios.anotar("leche", base) == ["pan", "leche"]
    assert base == ["pan", "leche"]

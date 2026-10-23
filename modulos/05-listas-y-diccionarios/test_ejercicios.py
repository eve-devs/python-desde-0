"""Pruebas de la semana 5.

Por defecto importan ejercicios.py.
macOS y Linux:  PYTHON_DESDE_0_SOLUCION=1 pytest modulos/05-listas-y-diccionarios
PowerShell:     $env:PYTHON_DESDE_0_SOLUCION="1"; pytest modulos/05-listas-y-diccionarios
CMD:            set PYTHON_DESDE_0_SOLUCION=1
"""

from pathlib import Path

import pytest

from soporte.cargar import cargar

ejercicios = cargar(Path(__file__).resolve().parent)


def test_primer_y_ultimo():
    assert ejercicios.primer_y_ultimo([1, 2, 3]) == (1, 3)
    assert ejercicios.primer_y_ultimo([7]) == (7, 7)
    assert ejercicios.primer_y_ultimo(["pan", "leche"]) == ("pan", "leche")


def test_primer_y_ultimo_vacio():
    with pytest.raises(ValueError, match="La lista está vacía"):
        ejercicios.primer_y_ultimo([])


def test_sin_extremos_no_modifica_la_original():
    datos = [1, 2, 3, 4]
    assert ejercicios.sin_extremos(datos) == [2, 3]
    assert datos == [1, 2, 3, 4]
    assert ejercicios.sin_extremos([1]) == []
    assert ejercicios.sin_extremos([]) == []


def test_agregar_unico_copia():
    original = [1, 2]
    assert ejercicios.agregar_unico(original, 3) == [1, 2, 3]
    assert original == [1, 2]
    assert ejercicios.agregar_unico([1, 2], 1) == [1, 2]


def test_promedio():
    assert ejercicios.promedio([10, 20, 30]) == 20
    assert ejercicios.promedio([1, 2]) == pytest.approx(1.5)


def test_promedio_vacio():
    with pytest.raises(ValueError, match="No se puede promediar una lista vacía"):
        ejercicios.promedio([])


def test_contar_palabras():
    assert ejercicios.contar_palabras("Hola hola Eva") == {"hola": 2, "eva": 1}
    assert ejercicios.contar_palabras("Café café") == {"café": 2}
    assert ejercicios.contar_palabras("   ") == {}


def test_invertir_diccionario():
    original = {"ana": "555", "eva": "111"}
    assert ejercicios.invertir_diccionario(original) == {"555": "ana", "111": "eva"}
    assert original == {"ana": "555", "eva": "111"}
    assert ejercicios.invertir_diccionario({"a": 1, "b": 1}) == {1: "b"}


def test_filtrar_mayores_no_modifica():
    numeros = [1, 5, 5, 8]
    assert ejercicios.filtrar_mayores(numeros, 5) == [8]
    assert numeros == [1, 5, 5, 8]
    assert ejercicios.filtrar_mayores([], 0) == []


def test_combinar_no_pisa_los_originales():
    base = {"a": 1}
    extra = {"a": 2, "b": 3}
    assert ejercicios.combinar(base, extra) == {"a": 2, "b": 3}
    assert base == {"a": 1}
    assert extra == {"a": 2, "b": 3}

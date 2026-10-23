"""Pruebas de la semana 4.

    PYTHON_DESDE_0_SOLUCION=1 pytest modulos/04-ciclos
"""

from pathlib import Path

import pytest

from soporte.cargar import cargar

ejercicios = cargar(Path(__file__).resolve().parent)


def test_suma_del_1_al():
    assert ejercicios.suma_del_1_al(4) == 10
    assert ejercicios.suma_del_1_al(1) == 1
    assert ejercicios.suma_del_1_al(0) == 0
    assert ejercicios.suma_del_1_al(-5) == 0


def test_contar_pares():
    assert ejercicios.contar_pares(1, 10) == 5
    assert ejercicios.contar_pares(2, 2) == 1
    assert ejercicios.contar_pares(1, 1) == 0
    assert ejercicios.contar_pares(5, 1) == 0
    assert ejercicios.contar_pares(-3, 2) == 3


def test_tabla_de_multiplicar():
    tabla = ejercicios.tabla_de_multiplicar(2)
    assert len(tabla) == 10
    assert tabla[0] == "2 x 1 = 2"
    assert tabla[-1] == "2 x 10 = 20"
    assert ejercicios.tabla_de_multiplicar(7)[2] == "7 x 3 = 21"


def test_contar_vocales():
    assert ejercicios.contar_vocales("Hola") == 2
    assert ejercicios.contar_vocales("Árbol") == 2
    assert ejercicios.contar_vocales("pingüino") == 4
    assert ejercicios.contar_vocales("AEIOU") == 5
    assert ejercicios.contar_vocales("y") == 0
    assert ejercicios.contar_vocales("") == 0


def test_invertir():
    assert ejercicios.invertir("hola") == "aloh"
    assert ejercicios.invertir("") == ""
    assert ejercicios.invertir("Anita") == "atinA"


def test_factorial():
    assert ejercicios.factorial(0) == 1
    assert ejercicios.factorial(1) == 1
    assert ejercicios.factorial(5) == 120


def test_factorial_negativo():
    with pytest.raises(ValueError, match="El factorial no está definido para números negativos"):
        ejercicios.factorial(-1)


def test_fizzbuzz():
    assert ejercicios.fizzbuzz(0) == []
    resultado = ejercicios.fizzbuzz(15)
    assert len(resultado) == 15
    assert resultado[0] == "1"
    assert resultado[2] == "Fizz"
    assert resultado[4] == "Buzz"
    assert resultado[14] == "FizzBuzz"


def test_primer_indice():
    assert ejercicios.primer_indice("programar", "a") == 5
    assert ejercicios.primer_indice("programar", "P") == -1
    assert ejercicios.primer_indice("programar", "z") == -1
    assert ejercicios.primer_indice("", "a") == -1

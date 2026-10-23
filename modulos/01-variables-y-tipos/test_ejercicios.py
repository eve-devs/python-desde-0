"""Pruebas de la semana 1.

Por defecto importan ejercicios.py. Para usar la solución:

    PYTHON_DESDE_0_SOLUCION=1 pytest modulos/01-variables-y-tipos
"""

from pathlib import Path

import pytest

from soporte.cargar import cargar

ejercicios = cargar(Path(__file__).resolve().parent)


def test_suma_del_cafe_y_el_pan():
    assert ejercicios.suma(35, 18) == 53


def test_suma_de_decimales_exactos():
    assert ejercicios.suma(2.5, 1.5) == 4.0


def test_promedio_de_tres_calificaciones():
    assert ejercicios.promedio(10, 20, 30) == 20.0


def test_promedio_con_decimales():
    assert ejercicios.promedio(1, 2, 3) == pytest.approx(2.0)


def test_cero_es_par():
    assert ejercicios.es_par(0) is True


def test_numeros_pares_e_impares():
    assert ejercicios.es_par(8) is True
    assert ejercicios.es_par(7) is False
    assert ejercicios.es_par(-4) is True
    assert ejercicios.es_par(-3) is False


def test_celsius_conocidos():
    assert ejercicios.celsius_a_fahrenheit(0) == 32
    assert ejercicios.celsius_a_fahrenheit(100) == 212


def test_celsius_de_un_dia_templado():
    assert ejercicios.celsius_a_fahrenheit(36.6) == pytest.approx(97.88)


def test_horas_y_minutos():
    assert ejercicios.horas_y_minutos(135) == (2, 15)
    assert ejercicios.horas_y_minutos(60) == (1, 0)
    assert ejercicios.horas_y_minutos(59) == (0, 59)
    assert ejercicios.horas_y_minutos(0) == (0, 0)
    assert ejercicios.horas_y_minutos(1000) == (16, 40)


def test_precio_con_descuento():
    assert ejercicios.precio_con_descuento(200, 10) == 180
    assert ejercicios.precio_con_descuento(200, 0) == 200
    assert ejercicios.precio_con_descuento(80, 100) == 0
    assert ejercicios.precio_con_descuento(199, 15) == pytest.approx(169.15)


def test_perimetro_de_una_mesa():
    assert ejercicios.perimetro_rectangulo(3, 4) == 14
    assert ejercicios.perimetro_rectangulo(2.5, 1) == 7


def test_la_cuenta_se_reparte():
    assert ejercicios.cuota_por_persona(300, 4) == 75
    assert ejercicios.cuota_por_persona(100, 3) == pytest.approx(100 / 3)

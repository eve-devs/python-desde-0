"""Pruebas de la semana 3.

Por defecto importan ejercicios.py.
macOS y Linux:  PYTHON_DESDE_0_SOLUCION=1 pytest modulos/03-condicionales
PowerShell:     $env:PYTHON_DESDE_0_SOLUCION="1"; pytest modulos/03-condicionales
CMD:            set PYTHON_DESDE_0_SOLUCION=1
"""

from pathlib import Path

import pytest

from soporte.cargar import cargar

ejercicios = cargar(Path(__file__).resolve().parent)


@pytest.mark.parametrize(
    ("numero", "esperado"),
    [(3, "positivo"), (0.1, "positivo"), (0, "cero"), (0.0, "cero"), (-2, "negativo")],
)
def test_signo(numero, esperado):
    assert ejercicios.signo(numero) == esperado


def test_signo_cero():
    assert ejercicios.signo(0) == "cero"


@pytest.mark.parametrize(
    ("edad", "esperado"),
    [
        (-1, "no válida"),
        (0, "niñez"),
        (12, "niñez"),
        (13, "adolescencia"),
        (17, "adolescencia"),
        (18, "adultez"),
        (64, "adultez"),
        (65, "adultez mayor"),
        (90, "adultez mayor"),
    ],
)
def test_clasificar_edad(edad, esperado):
    assert ejercicios.clasificar_edad(edad) == esperado


@pytest.mark.parametrize(
    ("calificacion", "esperado"),
    [
        (-0.1, "fuera de rango"),
        (0, "reprobado"),
        (69.9, "reprobado"),
        (70, "aprobado"),
        (89.9, "aprobado"),
        (90, "excelente"),
        (100, "excelente"),
        (100.1, "fuera de rango"),
    ],
)
def test_resultado_examen(calificacion, esperado):
    assert ejercicios.resultado_examen(calificacion) == esperado


def test_puede_votar():
    assert ejercicios.puede_votar(18, True) is True
    assert ejercicios.puede_votar(18, False) is False
    assert ejercicios.puede_votar(17, True) is False
    assert ejercicios.puede_votar(40, True) is True


@pytest.mark.parametrize(
    ("hora", "esperado"),
    [
        (-1, "hora no válida"),
        (24, "hora no válida"),
        (0, "buenos días"),
        (11, "buenos días"),
        (12, "buenas tardes"),
        (18, "buenas tardes"),
        (19, "buenas noches"),
        (23, "buenas noches"),
    ],
)
def test_saludo_por_hora(hora, esperado):
    assert ejercicios.saludo_por_hora(hora) == esperado


@pytest.mark.parametrize(
    ("horas", "esperado"),
    [(0, 0), (-2, 0), (1, 20), (2, 35), (6, 95), (7, 100), (20, 100)],
)
def test_tarifa_estacionamiento(horas, esperado):
    assert ejercicios.tarifa_estacionamiento(horas) == esperado


@pytest.mark.parametrize(
    ("dia", "esperado"),
    [
        ("lunes", True),
        ("  Jueves ", True),
        ("miércoles", True),
        ("miercoles", True),
        ("Miércoles", True),
        ("sábado", False),
        ("sabado", False),
        ("domingo", False),
        ("", False),
    ],
)
def test_dia_laboral(dia, esperado):
    assert ejercicios.dia_laboral(dia) is esperado


def test_precio_boleto_reglamento():
    assert ejercicios.precio_boleto(0, False) == 0
    assert ejercicios.precio_boleto(3, True) == 0
    assert ejercicios.precio_boleto(4, False) == 40
    assert ejercicios.precio_boleto(11, True) == 40
    assert ejercicios.precio_boleto(12, True) == 60
    assert ejercicios.precio_boleto(12, False) == 80
    assert ejercicios.precio_boleto(64, True) == 60
    assert ejercicios.precio_boleto(64, False) == 80
    assert ejercicios.precio_boleto(65, True) == 40
    assert ejercicios.precio_boleto(65, False) == 40


def test_precio_boleto_rechaza_edad_negativa():
    with pytest.raises(ValueError, match="La edad no puede ser negativa"):
        ejercicios.precio_boleto(-1, False)

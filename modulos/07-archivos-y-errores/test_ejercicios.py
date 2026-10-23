"""Pruebas de la semana 7.

    PYTHON_DESDE_0_SOLUCION=1 pytest modulos/07-archivos-y-errores
"""

import json
from pathlib import Path

import pytest

from soporte.cargar import cargar

ejercicios = cargar(Path(__file__).resolve().parent)


def test_dividir():
    assert ejercicios.dividir(10, 4) == 2.5
    assert ejercicios.dividir(-6, 2) == -3


def test_dividir_entre_cero_avisa_en_espanol():
    with pytest.raises(ZeroDivisionError, match="no se puede dividir entre cero"):
        ejercicios.dividir(1, 0)


def test_leer_entero():
    assert ejercicios.leer_entero("42") == 42
    assert ejercicios.leer_entero("  -7 ") == -7
    assert ejercicios.leer_entero("+8") == 8
    assert ejercicios.leer_entero("3.14") is None
    assert ejercicios.leer_entero("hola") is None
    assert ejercicios.leer_entero("") is None
    assert ejercicios.leer_entero("   ") is None


def test_escribir_y_leer_texto_con_enie(tmp_path):
    ruta = tmp_path / "nota.txt"
    ejercicios.escribir_texto(ruta, "La canción\n")
    assert ejercicios.leer_texto(ruta) == "La canción\n"
    assert ruta.read_bytes() == "La canción\n".encode("utf-8")


def test_escribir_reemplaza(tmp_path):
    ruta = tmp_path / "nota.txt"
    ejercicios.escribir_texto(ruta, "uno")
    ejercicios.escribir_texto(ruta, "dos")
    assert ejercicios.leer_texto(ruta) == "dos"


def test_leer_texto_que_no_existe(tmp_path):
    with pytest.raises(FileNotFoundError):
        ejercicios.leer_texto(tmp_path / "no-esta.txt")


def test_agregar_linea_crea_y_no_duplica_el_salto(tmp_path):
    ruta = tmp_path / "lista.txt"
    ejercicios.agregar_linea(ruta, "uno")
    ejercicios.agregar_linea(ruta, "dos\n")
    assert ejercicios.leer_texto(ruta) == "uno\ndos\n"


def test_guardar_y_cargar_json_con_acentos(tmp_path):
    ruta = tmp_path / "datos.json"
    ejercicios.guardar_json(ruta, {"canción": "café"})
    assert ruta.read_text(encoding="utf-8") == '{\n  "canción": "café"\n}\n'
    assert ejercicios.cargar_json(ruta) == {"canción": "café"}


def test_cargar_json_que_no_existe(tmp_path):
    with pytest.raises(FileNotFoundError):
        ejercicios.cargar_json(tmp_path / "no.json")


def test_json_invalido_sale(tmp_path):
    ruta = tmp_path / "mal.json"
    ruta.write_text("{", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        ejercicios.cargar_json(ruta)


def test_leer_json_si_existe_devuelve_el_mismo_objeto(tmp_path):
    ruta = tmp_path / "no.json"
    valor = {"vacio": True}
    assert ejercicios.leer_json_si_existe(ruta, valor) is valor
    assert not ruta.exists()


def test_leer_json_si_existe_cuando_si_esta(tmp_path):
    ruta = tmp_path / "si.json"
    ejercicios.guardar_json(ruta, [1, 2])
    assert ejercicios.leer_json_si_existe(ruta, []) == [1, 2]


def test_numeros_de_archivo(tmp_path):
    ruta = tmp_path / "numeros.txt"
    ruta.write_text("1\n\n2.5\nhola\n-3\n1e2\ninf\nnan\n\n4\n", encoding="utf-8")
    assert ejercicios.numeros_de_archivo(ruta) == [1.0, 2.5, -3.0, 100.0, 4.0]

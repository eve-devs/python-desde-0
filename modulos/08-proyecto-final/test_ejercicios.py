"""Pruebas del registro de gastos.

Por defecto importan ejercicios.py.
macOS y Linux:  PYTHON_DESDE_0_SOLUCION=1 pytest modulos/08-proyecto-final
PowerShell:     $env:PYTHON_DESDE_0_SOLUCION="1"; pytest modulos/08-proyecto-final
CMD:            set PYTHON_DESDE_0_SOLUCION=1
"""

from datetime import date
from pathlib import Path

import pytest

from soporte.cargar import cargar

ejercicios = cargar(Path(__file__).resolve().parent)


def _gasto(descripcion, monto, categoria, fecha):
    return ejercicios.crear_gasto(descripcion, monto, categoria, fecha)


def test_crear_gasto_normaliza():
    gasto = _gasto("  Café  ", 45, " Alimentos ", "2026-10-01")
    assert gasto == {
        "descripcion": "Café",
        "monto": 45.0,
        "categoria": "alimentos",
        "fecha": "2026-10-01",
    }
    assert isinstance(gasto["monto"], float)


def test_crear_gasto_redondea_a_centavos():
    assert _gasto("Pan", 10.126, "alimentos", "2026-10-01")["monto"] == 10.13
    assert _gasto("Pan", 10.124, "alimentos", "2026-10-01")["monto"] == 10.12


def test_crear_gasto_usa_hoy_si_no_hay_fecha():
    gasto = _gasto("Agua", 12.5, "alimentos", None)
    assert gasto["fecha"] == date.today().isoformat()


@pytest.mark.parametrize(
    ("argumentos", "mensaje"),
    [
        (("", 10, "cafe", "2026-10-01"), "La descripción no puede estar vacía."),
        (("   ", 10, "cafe", "2026-10-01"), "La descripción no puede estar vacía."),
        (("Pan", True, "cafe", "2026-10-01"), "El monto debe ser un número."),
        (("Pan", "45", "cafe", "2026-10-01"), "El monto debe ser un número."),
        (("Pan", float("inf"), "cafe", "2026-10-01"), "El monto debe ser un número."),
        (("Pan", float("nan"), "cafe", "2026-10-01"), "El monto debe ser un número."),
        (("Pan", 0, "cafe", "2026-10-01"), "El monto debe ser mayor que cero."),
        (("Pan", -3, "cafe", "2026-10-01"), "El monto debe ser mayor que cero."),
        (("Pan", 10, "   ", "2026-10-01"), "La categoría no puede estar vacía."),
        (("Pan", 10, "cafe", "2026-1-01"), "La fecha debe tener el formato AAAA-MM-DD."),
        (("Pan", 10, "cafe", "23-10-2026"), "La fecha debe tener el formato AAAA-MM-DD."),
        (("Pan", 10, "cafe", "2026-02-31"), "La fecha debe tener el formato AAAA-MM-DD."),
    ],
)
def test_crear_gasto_rechaza(argumentos, mensaje):
    with pytest.raises(ValueError, match=mensaje):
        _gasto(*argumentos)


def test_guardar_y_cargar_conserva_los_acentos(tmp_path):
    ruta = tmp_path / "gastos.json"
    gastos = [_gasto("Café", 45.5, "alimentos", "2026-10-01")]
    ejercicios.guardar_gastos(ruta, gastos)
    texto = ruta.read_text(encoding="utf-8")
    assert "Café" in texto
    assert "\\u" not in texto
    assert texto.endswith("\n")
    assert ejercicios.cargar_gastos(ruta) == gastos


def test_cargar_gastos_si_no_hay_archivo(tmp_path):
    ruta = tmp_path / "gastos.json"
    assert ejercicios.cargar_gastos(ruta) == []
    assert not ruta.exists()


def test_cargar_gastos_rechaza_json_invalido(tmp_path):
    ruta = tmp_path / "gastos.json"
    ruta.write_text("{", encoding="utf-8")
    with pytest.raises(ValueError, match="El archivo de gastos no contiene JSON válido"):
        ejercicios.cargar_gastos(ruta)


def test_cargar_gastos_exige_una_lista(tmp_path):
    ruta = tmp_path / "gastos.json"
    ruta.write_text('{"a": 1}\n', encoding="utf-8")
    with pytest.raises(ValueError, match="El archivo de gastos debe contener una lista"):
        ejercicios.cargar_gastos(ruta)


def test_agregar_gasto_persiste(tmp_path):
    ruta = tmp_path / "gastos.json"
    primero = ejercicios.agregar_gasto(ruta, "Café", 45.5, "alimentos", "2026-10-01")
    ejercicios.agregar_gasto(ruta, "Metro", 12, "transporte", "2026-10-02")
    guardados = ejercicios.cargar_gastos(ruta)
    assert guardados[0] == primero
    assert [gasto["descripcion"] for gasto in guardados] == ["Café", "Metro"]


def test_totales_y_filtro():
    gastos = [
        _gasto("Café", 10, "alimentos", "2026-10-01"),
        _gasto("Metro", 5.5, "transporte", "2026-10-02"),
        _gasto("Pan", 2.5, "alimentos", "2026-10-03"),
    ]
    assert ejercicios.total([]) == 0
    assert ejercicios.total(gastos) == 18.0
    assert ejercicios.total_por_categoria(gastos) == {
        "alimentos": 12.5,
        "transporte": 5.5,
    }
    assert ejercicios.total_por_categoria([]) == {}
    filtrados = ejercicios.filtrar_por_categoria(gastos, "  Alimentos ")
    assert [gasto["descripcion"] for gasto in filtrados] == ["Café", "Pan"]
    assert filtrados is not gastos


def test_resumen_vacio():
    assert ejercicios.formatear_resumen([]) == "No hay gastos registrados."


def test_resumen_con_gastos():
    gastos = [
        _gasto("Café", 45.5, "alimentos", "2026-10-01"),
        _gasto("Metro", 12, "transporte", "2026-10-02"),
    ]
    assert ejercicios.formatear_resumen(gastos) == (
        "Gastos (2)\n"
        "- 2026-10-01  Café  $45.50  alimentos\n"
        "- 2026-10-02  Metro  $12.00  transporte\n"
        "Total: $57.50\n"
        "Por categoría:\n"
        "- alimentos: $45.50\n"
        "- transporte: $12.00"
    )


def test_resumen_ordena_las_categorias_y_no_los_gastos():
    gastos = [
        _gasto("Zapatos", 100, "ropa", "2026-10-02"),
        _gasto("Café", 10, "alimentos", "2026-10-01"),
    ]
    resumen = ejercicios.formatear_resumen(gastos)
    assert resumen.index("Zapatos") < resumen.index("Café")
    assert resumen.index("- alimentos:") < resumen.index("- ropa:")


def test_main_ayuda_y_comando_desconocido(tmp_path):
    ruta = tmp_path / "gastos.json"
    assert ejercicios.main([], ruta) == (
        "Comandos:\n"
        "  agregar <descripcion> <monto> <categoria> [fecha]\n"
        "  listar\n"
        "  total\n"
        "  resumen\n"
        "  categoria <nombre>"
    )
    assert "No reconozco ese comando" in ejercicios.main(["volar"], ruta)


def test_main_flujo_completo(tmp_path):
    ruta = tmp_path / "gastos.json"
    assert ejercicios.main(["listar"], ruta) == "No hay gastos registrados."
    assert ejercicios.main(["total"], ruta) == "Total: $0.00"
    alta = ejercicios.main(
        ["AGREGAR", "Café", "45.50", "Alimentos", "2026-10-01"],
        ruta,
    )
    assert alta == "Listo: 2026-10-01  Café  $45.50  alimentos"
    ejercicios.main(["agregar", "Metro", "12", "transporte", "2026-10-02"], ruta)
    assert ejercicios.main(["listar"], ruta) == (
        "2026-10-01  Café  $45.50  alimentos\n"
        "2026-10-02  Metro  $12.00  transporte"
    )
    assert ejercicios.main(["total"], ruta) == "Total: $57.50"
    assert ejercicios.main(["resumen"], ruta) == ejercicios.formatear_resumen(
        ejercicios.cargar_gastos(ruta)
    )
    assert ejercicios.main(["categoria", "  Alimentos "], ruta) == (
        "alimentos: $45.50\n"
        "2026-10-01  Café  $45.50  alimentos"
    )
    assert ejercicios.main(["categoria", "renta"], ruta) == "No hay gastos en renta."


def test_main_errores_de_uso(tmp_path):
    ruta = tmp_path / "gastos.json"
    assert (
        ejercicios.main(["agregar", "Café"], ruta)
        == "Uso: agregar <descripcion> <monto> <categoria> [fecha]"
    )
    assert ejercicios.main(["agregar", "Café", "abc", "alimentos"], ruta) == (
        "El monto no es un número: abc"
    )
    assert (
        ejercicios.main(["agregar", "  ", "10", "alimentos"], ruta)
        == "La descripción no puede estar vacía."
    )
    assert ejercicios.main(["categoria"], ruta) == "Uso: categoria <nombre>"
    assert not ruta.exists()

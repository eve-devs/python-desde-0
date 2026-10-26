"""Comprueba que cada módulo ofrezca las mismas funciones en ambos archivos.

Así las pruebas pueden cambiar de ejercicios.py a solucion.py sin sorpresas.
"""

from pathlib import Path

from soporte.cargar import cargar_archivo

MODULOS = [
    "01-variables-y-tipos",
    "02-strings",
    "03-condicionales",
    "04-ciclos",
    "05-listas-y-diccionarios",
    "06-funciones",
    "07-archivos-y-errores",
    "08-proyecto-final",
]


def _funciones_propias(modulo) -> set[str]:
    nombres = set()
    for nombre, valor in vars(modulo).items():
        if nombre.startswith("_"):
            continue
        if not callable(valor):
            continue
        if getattr(valor, "__module__", None) != modulo.__name__:
            continue
        nombres.add(nombre)
    return nombres


def test_cada_modulo_define_las_mismas_funciones():
    raiz = Path(__file__).resolve().parents[1] / "modulos"
    for nombre in MODULOS:
        carpeta = raiz / nombre
        ejercicios = cargar_archivo(carpeta, "ejercicios")
        solucion = cargar_archivo(carpeta, "solucion")
        assert _funciones_propias(ejercicios) == _funciones_propias(solucion), nombre
        assert _funciones_propias(ejercicios), nombre

"""Carga ejercicios.py o solucion.py de un módulo del curso.

Por defecto se carga ejercicios.py.

Si la variable de entorno PYTHON_DESDE_0_SOLUCION vale 1, true, yes,
si, sí o solucion, se carga solucion.py. Así puedes practicar con tus
funciones y, cuando quieras, comparar con la solución:

    pytest modulos/01-variables-y-tipos
    PYTHON_DESDE_0_SOLUCION=1 pytest modulos/01-variables-y-tipos

En GitHub Actions las pruebas siempre corren contra las soluciones.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

_VALORES_SOLUCION = {"1", "true", "yes", "si", "sí", "solucion"}


def usar_solucion() -> bool:
    valor = os.environ.get("PYTHON_DESDE_0_SOLUCION", "").strip().lower()
    return valor in _VALORES_SOLUCION


def cargar_archivo(directorio: Path, nombre_archivo: str):
    """Ejecuta ``directorio/nombre_archivo.py`` y devuelve el módulo."""
    directorio = Path(directorio)
    ruta = directorio / f"{nombre_archivo}.py"
    slug = "".join(caracter if caracter.isalnum() else "_" for caracter in directorio.name)
    nombre_modulo = f"curso_{slug}_{nombre_archivo}"
    cargado = sys.modules.get(nombre_modulo)
    if cargado is not None and getattr(cargado, "__file__", None) == str(ruta):
        return cargado

    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta)
    if spec is None or spec.loader is None:
        raise ImportError(f"No se pudo cargar {ruta}")
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[nombre_modulo] = modulo
    spec.loader.exec_module(modulo)
    return modulo


def cargar(directorio: Path):
    """Carga ejercicios.py o solucion.py según PYTHON_DESDE_0_SOLUCION."""
    nombre = "solucion" if usar_solucion() else "ejercicios"
    return cargar_archivo(directorio, nombre)

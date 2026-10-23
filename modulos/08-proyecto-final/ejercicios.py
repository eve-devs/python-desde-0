"""Registro de gastos. Semana 8.

Completa las funciones de arriba hacia abajo. La guía está en notas.md.

    pytest modulos/08-proyecto-final

Para usarlo, desde esta carpeta:

    python ejercicios.py resumen
"""

# Ya están importados para que los uses en los TODO.
import json
import math
import re
from datetime import date
from pathlib import Path


def crear_gasto(
    descripcion: str,
    monto: float,
    categoria: str,
    fecha: str | None = None,
) -> dict:
    """Crea un diccionario de gasto, ya normalizado.

    descripcion: se le quitan los espacios de los extremos. Si queda vacía,
    lanza ValueError "La descripción no puede estar vacía."

    monto: tiene que ser int o float, finito y mayor que cero.
    True, False, los textos, inf y nan no sirven: ValueError
    "El monto debe ser un número."
    Si es 0 o negativo: ValueError "El monto debe ser mayor que cero."
    Se guarda como float redondeado a 2 decimales.

    categoria: sin espacios en los extremos, en minúsculas.
    Si queda vacía: ValueError "La categoría no puede estar vacía."

    fecha: None significa hoy, en formato AAAA-MM-DD.
    Si viene un texto, tiene que ser AAAA-MM-DD y una fecha real.
    Si no: ValueError "La fecha debe tener el formato AAAA-MM-DD."

    Las llaves del diccionario, en este orden: descripcion, monto,
    categoria, fecha.
    """
    # TODO: valida cada campo en el orden de la docstring y devuelve el dict.
    raise NotImplementedError


def cargar_gastos(ruta: str | Path) -> list[dict]:
    """Lee la lista de gastos desde un JSON en UTF-8.

    Si el archivo no existe, devuelve [] y no lo crees.
    Si el texto no es JSON, lanza ValueError
    "El archivo de gastos no contiene JSON válido."
    Si el JSON no es una lista, lanza ValueError
    "El archivo de gastos debe contener una lista."
    """
    # TODO: si no existe, devuelve []. Si existe, valida y devuelve la lista.
    raise NotImplementedError


def guardar_gastos(ruta: str | Path, gastos: list[dict]) -> None:
    """Escribe la lista de gastos como JSON.

    UTF-8, ensure_ascii=False, indent=2 y un salto de línea al final.
    """
    # TODO: usa json.dumps con esas opciones.
    raise NotImplementedError


def agregar_gasto(
    ruta: str | Path,
    descripcion: str,
    monto: float,
    categoria: str,
    fecha: str | None = None,
) -> dict:
    """Carga los gastos, agrega uno nuevo, los guarda y lo devuelve."""
    # TODO: combina cargar_gastos, crear_gasto y guardar_gastos.
    raise NotImplementedError


def total(gastos: list[dict]) -> float:
    """Suma los montos y redondea a 2 decimales.

    Una lista vacía suma 0.
    """
    # TODO: suma gasto["monto"] y redondea.
    raise NotImplementedError


def total_por_categoria(gastos: list[dict]) -> dict[str, float]:
    """Suma por categoría.

    Las llaves van en orden alfabético. Cada suma se redondea a 2 decimales.
    Una lista vacía devuelve {}.
    """
    # TODO: acumula y al final ordena las categorías.
    raise NotImplementedError


def filtrar_por_categoria(gastos: list[dict], categoria: str) -> list[dict]:
    """Devuelve los gastos de esa categoría, en el mismo orden.

    Compara en minúsculas y sin espacios en los extremos.
    Devuelve una lista nueva. No modifica la original.
    """
    # TODO: normaliza la categoría y filtra.
    raise NotImplementedError


def formatear_resumen(gastos: list[dict]) -> str:
    """Devuelve el resumen listo para imprimir.

    Sin gastos, el texto es exactamente "No hay gastos registrados."

    Con gastos:

        Gastos (2)
        - 2026-10-01  Café  $45.50  alimentos
        - 2026-10-02  Metro  $12.00  transporte
        Total: $57.50
        Por categoría:
        - alimentos: $45.50
        - transporte: $12.00

    Cada línea de gasto usa dos espacios entre fecha, descripción,
    monto y categoría. El monto lleva siempre dos decimales.
    Las líneas de gasto siguen el orden de la lista.
    Las categorías van en orden alfabético.
    """
    # TODO: arma las líneas y únelas con un salto. No pongas un salto final extra.
    raise NotImplementedError


def main(argumentos: list[str], ruta: str | Path) -> str:
    """Ejecuta un comando y devuelve el texto que vería la persona.

    No imprime. Los comandos están descritos en notas.md.
    "agregar" persiste el gasto en ruta. El resto solo lee.
    """
    # TODO: interpreta argumentos[0] y delega en las funciones de arriba.
    raise NotImplementedError


if __name__ == "__main__":
    import sys

    print(main(sys.argv[1:], "gastos.json"))

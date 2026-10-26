"""Solución de referencia del registro de gastos.

Intenta el proyecto antes de leer este archivo.
"""

import json
import math
import re
from datetime import date
from pathlib import Path

_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")

_AYUDA = (
    "Comandos:\n"
    "  agregar <descripcion> <monto> <categoria> [fecha]\n"
    "  listar\n"
    "  total\n"
    "  resumen\n"
    "  categoria <nombre>"
)


def _validar_fecha(fecha: str) -> str:
    if not isinstance(fecha, str) or _FECHA.fullmatch(fecha) is None:
        raise ValueError("La fecha debe tener el formato AAAA-MM-DD.")
    try:
        date.fromisoformat(fecha)
    except ValueError:
        raise ValueError("La fecha debe tener el formato AAAA-MM-DD.") from None
    return fecha


def _validar_monto(monto: float) -> float:
    """Devuelve el monto redondeado a centavos, o avisa por qué no sirve."""
    if isinstance(monto, bool) or not isinstance(monto, (int, float)):
        raise ValueError("El monto debe ser un número.")

    # El signo se mira antes de convertir: un entero negativo enorme
    # también es "menor o igual que cero", y float() reventaría.
    if isinstance(monto, int) and monto <= 0:
        raise ValueError("El monto debe ser mayor que cero.")

    try:
        como_float = float(monto)
    except OverflowError:
        raise ValueError("El monto es demasiado grande.") from None

    if not math.isfinite(como_float):
        raise ValueError("El monto debe ser un número.")

    redondeado = round(como_float, 2)
    if redondeado <= 0:
        raise ValueError("El monto debe ser mayor que cero.")
    return redondeado


def _gasto_bien_formado(gasto: object) -> bool:
    """Comprueba llaves y tipos. No repite las reglas de crear_gasto."""
    if not isinstance(gasto, dict):
        return False
    if not isinstance(gasto.get("descripcion"), str):
        return False
    if not isinstance(gasto.get("categoria"), str):
        return False
    if not isinstance(gasto.get("fecha"), str):
        return False
    monto = gasto.get("monto")
    if isinstance(monto, bool) or not isinstance(monto, (int, float)):
        return False
    try:
        return math.isfinite(monto)
    except OverflowError:
        return False


def crear_gasto(
    descripcion: str,
    monto: float,
    categoria: str,
    fecha: str | None = None,
) -> dict:
    """Crea un diccionario de gasto, ya normalizado.

    descripcion: se le quitan los espacios de los extremos. Si queda vacía,
    lanza ValueError "La descripción no puede estar vacía."

    monto: tiene que ser int o float, no bool, y finito.
    True, False, los textos, inf y nan no sirven: ValueError
    "El monto debe ser un número."
    Un entero tan grande que no cabe en un float: ValueError
    "El monto es demasiado grande."
    Se redondea con round(monto, 2). Ese resultado tiene que ser mayor
    que cero. Si es 0, negativo, o queda en 0.00: ValueError
    "El monto debe ser mayor que cero."
    0.001 y 0.004 quedan en 0.00 y no sirven. El float 0.005 no es
    exactamente 5 milésimas: round lo deja en 0.01 y sí sirve.
    Si cae justo en la mitad, round se queda con el centavo par:
    10.125 queda en 10.12 y 0.375 queda en 0.38.
    Se guarda como float.

    categoria: sin espacios en los extremos, en minúsculas.
    Si queda vacía: ValueError "La categoría no puede estar vacía."

    fecha: None significa hoy, en formato AAAA-MM-DD.
    Si viene un texto, tiene que ser AAAA-MM-DD y una fecha real.
    Si no: ValueError "La fecha debe tener el formato AAAA-MM-DD."

    Las llaves del diccionario, en este orden: descripcion, monto,
    categoria, fecha.
    """
    if not isinstance(descripcion, str) or not descripcion.strip():
        raise ValueError("La descripción no puede estar vacía.")

    monto_listo = _validar_monto(monto)

    if not isinstance(categoria, str) or not categoria.strip():
        raise ValueError("La categoría no puede estar vacía.")

    fecha_lista = date.today().isoformat() if fecha is None else _validar_fecha(fecha)
    return {
        "descripcion": descripcion.strip(),
        "monto": monto_listo,
        "categoria": categoria.strip().lower(),
        "fecha": fecha_lista,
    }


def cargar_gastos(ruta: str | Path) -> list[dict]:
    """Lee la lista de gastos desde un JSON en UTF-8.

    Si el archivo no existe, devuelve [] y no lo crees.
    Si el texto no es JSON, lanza ValueError
    "El archivo de gastos no contiene JSON válido."
    Si el JSON no es una lista, lanza ValueError
    "El archivo de gastos debe contener una lista."

    Cada elemento tiene que ser un diccionario con descripcion (texto),
    monto (int o float finito; no bool), categoria (texto) y fecha (texto).
    Si falta una llave, el tipo no es ese, o el monto no cabe en un float,
    lanza ValueError "El gasto N debe tener descripcion (texto),
    monto (número finito), categoria (texto) y fecha (texto)."
    N es la posición, empezando en 1. No repite las reglas de crear_gasto:
    un monto 0 escrito a mano se lee igual. Las llaves de más se conservan.
    Si un número tiene demasiados dígitos para leerlo, lanza ValueError
    "El archivo de gastos tiene un número demasiado grande."
    """
    path = Path(ruta)
    if not path.exists():
        return []
    try:
        datos = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError("El archivo de gastos no contiene JSON válido.") from error
    except ValueError as error:
        raise ValueError(
            "El archivo de gastos tiene un número demasiado grande."
        ) from error
    if not isinstance(datos, list):
        raise ValueError("El archivo de gastos debe contener una lista.")
    for indice, gasto in enumerate(datos, start=1):
        if not _gasto_bien_formado(gasto):
            raise ValueError(
                f"El gasto {indice} debe tener descripcion (texto), "
                "monto (número finito), categoria (texto) y fecha (texto)."
            )
    return datos


def guardar_gastos(ruta: str | Path, gastos: list[dict]) -> None:
    """Escribe la lista de gastos como JSON.

    UTF-8, ensure_ascii=False, indent=2, un salto de línea al final
    y newline="\\n" para que Windows no lo convierta en \\r\\n.
    """
    texto = json.dumps(gastos, ensure_ascii=False, indent=2)
    Path(ruta).write_text(texto + "\n", encoding="utf-8", newline="\n")


def agregar_gasto(
    ruta: str | Path,
    descripcion: str,
    monto: float,
    categoria: str,
    fecha: str | None = None,
) -> dict:
    """Carga los gastos, agrega uno nuevo, los guarda y lo devuelve."""
    gastos = cargar_gastos(ruta)
    gasto = crear_gasto(descripcion, monto, categoria, fecha)
    gastos.append(gasto)
    guardar_gastos(ruta, gastos)
    return gasto


def total(gastos: list[dict]) -> float:
    """Suma los montos y redondea a 2 decimales.

    Una lista vacía suma 0.
    """
    return round(sum(float(gasto["monto"]) for gasto in gastos), 2)


def total_por_categoria(gastos: list[dict]) -> dict[str, float]:
    """Suma por categoría.

    Las llaves van en orden alfabético. Cada suma se redondea a 2 decimales.
    Una lista vacía devuelve {}.
    """
    acumulado: dict[str, float] = {}
    for gasto in gastos:
        categoria = gasto["categoria"]
        acumulado[categoria] = acumulado.get(categoria, 0.0) + float(gasto["monto"])
    return {categoria: round(acumulado[categoria], 2) for categoria in sorted(acumulado)}


def filtrar_por_categoria(gastos: list[dict], categoria: str) -> list[dict]:
    """Devuelve los gastos de esa categoría, en el mismo orden.

    Compara en minúsculas y sin espacios en los extremos.
    Devuelve una lista nueva. No modifica la original.
    """
    buscada = categoria.strip().lower()
    return [gasto for gasto in gastos if gasto["categoria"] == buscada]


def _linea_gasto(gasto: dict) -> str:
    return (
        f"{gasto['fecha']}  {gasto['descripcion']}  "
        f"${gasto['monto']:.2f}  {gasto['categoria']}"
    )


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
    if not gastos:
        return "No hay gastos registrados."
    lineas = [f"Gastos ({len(gastos)})"]
    lineas.extend(f"- {_linea_gasto(gasto)}" for gasto in gastos)
    lineas.append(f"Total: ${total(gastos):.2f}")
    lineas.append("Por categoría:")
    for categoria, monto in total_por_categoria(gastos).items():
        lineas.append(f"- {categoria}: ${monto:.2f}")
    return "\n".join(lineas)


def main(argumentos: list[str], ruta: str | Path) -> str:
    """Ejecuta un comando y devuelve el texto que vería la persona.

    No imprime. Los comandos están descritos en notas.md.
    "agregar" persiste el gasto en ruta. El resto solo lee.
    """
    if not argumentos:
        return _AYUDA

    comando = argumentos[0].strip().lower()
    if comando == "agregar":
        if len(argumentos) not in (4, 5):
            return "Uso: agregar <descripcion> <monto> <categoria> [fecha]"
        descripcion, monto_texto, categoria = argumentos[1], argumentos[2], argumentos[3]
        fecha = argumentos[4] if len(argumentos) == 5 else None
        try:
            monto = float(monto_texto)
        except ValueError:
            return f"El monto no es un número: {monto_texto}"
        try:
            gasto = agregar_gasto(ruta, descripcion, monto, categoria, fecha)
        except ValueError as error:
            return str(error)
        return f"Listo: {_linea_gasto(gasto)}"

    if comando == "listar":
        gastos = cargar_gastos(ruta)
        if not gastos:
            return "No hay gastos registrados."
        return "\n".join(_linea_gasto(gasto) for gasto in gastos)

    if comando == "total":
        return f"Total: ${total(cargar_gastos(ruta)):.2f}"

    if comando == "resumen":
        return formatear_resumen(cargar_gastos(ruta))

    if comando == "categoria":
        if len(argumentos) != 2 or not argumentos[1].strip():
            return "Uso: categoria <nombre>"
        categoria = argumentos[1].strip().lower()
        encontrados = filtrar_por_categoria(cargar_gastos(ruta), categoria)
        if not encontrados:
            return f"No hay gastos en {categoria}."
        lineas = [f"{categoria}: ${total(encontrados):.2f}"]
        lineas.extend(_linea_gasto(gasto) for gasto in encontrados)
        return "\n".join(lineas)

    return (
        "No reconozco ese comando. "
        "Escribe el programa sin argumentos para ver la ayuda."
    )


if __name__ == "__main__":
    import sys

    print(main(sys.argv[1:], "gastos.json"))

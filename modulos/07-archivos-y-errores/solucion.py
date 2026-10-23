"""Solución de referencia de la semana 7.

Intenta los ejercicios antes de leer este archivo.
"""

import json
import math
from pathlib import Path


def dividir(a: float, b: float) -> float:
    """Devuelve a / b.

    Si b es 0, lanza ZeroDivisionError con el mensaje
    "no se puede dividir entre cero".
    """
    if b == 0:
        raise ZeroDivisionError("no se puede dividir entre cero")
    return a / b


def leer_entero(texto: str) -> int | None:
    """Convierte texto a entero.

    Acepta espacios en los extremos, un signo + o - y el número.
    "42" -> 42. "  -7 " -> -7. "+8" -> 8.
    Si no es un entero, devuelve None. "3.14", "hola" y "" son None.
    No lances el error: atrápalo y devuelve None.
    """
    try:
        return int(texto.strip())
    except ValueError:
        return None


def leer_texto(ruta: str | Path) -> str:
    """Devuelve el contenido del archivo como texto UTF-8.

    Si el archivo no existe, deja salir FileNotFoundError.
    """
    return Path(ruta).read_text(encoding="utf-8")


def escribir_texto(ruta: str | Path, contenido: str) -> None:
    """Escribe contenido en la ruta, reemplazando lo que hubiera.

    Usa UTF-8 y newline="\\n". En Windows, sin newline, Python
    guarda \\r\\n y los bytes del archivo cambian.
    No agregues nada que no te hayan pasado.
    """
    Path(ruta).write_text(contenido, encoding="utf-8", newline="\n")


def agregar_linea(ruta: str | Path, linea: str) -> None:
    """Agrega linea al final del archivo y garantiza un salto de línea.

    Si el archivo no existe, lo crea.
    Si linea ya termina en salto de línea, no pongas otro.
    "hola" y "hola\\n" dejan las dos el texto hola seguido de un salto.
    Usa UTF-8 y newline="\\n" para que el salto no se convierta en \\r\\n.
    """
    with Path(ruta).open("a", encoding="utf-8", newline="\n") as archivo:
        archivo.write(linea.rstrip("\n") + "\n")


def cargar_json(ruta: str | Path):
    """Lee un archivo JSON en UTF-8 y devuelve el dato de Python.

    Si el archivo no existe, deja salir FileNotFoundError.
    Si el texto no es JSON, deja salir el error de json.
    """
    return json.loads(Path(ruta).read_text(encoding="utf-8"))


def guardar_json(ruta: str | Path, datos: object) -> None:
    """Guarda datos como JSON en UTF-8.

    Usa ensure_ascii=False para que "café" se vea como café.
    Indenta con 2 espacios, termina el archivo con un salto de línea
    y usa newline="\\n" para no escribir \\r\\n en Windows.
    """
    texto = json.dumps(datos, ensure_ascii=False, indent=2)
    Path(ruta).write_text(texto + "\n", encoding="utf-8", newline="\n")


def leer_json_si_existe(ruta: str | Path, valor_si_falta):
    """Lee el JSON si el archivo existe.

    Si no existe, devuelve valor_si_falta, el mismo objeto, y no crees
    el archivo. Si existe y el contenido no es JSON, deja salir el error.
    """
    path = Path(ruta)
    if not path.exists():
        return valor_si_falta
    return json.loads(path.read_text(encoding="utf-8"))


def numeros_de_archivo(ruta: str | Path) -> list[float]:
    """Lee un número por línea y devuelve los que sean finitos.

    Se salta las líneas en blanco y las que no sean números.
    float entiende 1, 2.5, -3 y 1e2 (que vale 100.0).
    Se salta inf y nan: no son finitos.
    El archivo está en UTF-8.
    """
    numeros = []
    for linea in Path(ruta).read_text(encoding="utf-8").splitlines():
        limpia = linea.strip()
        if not limpia:
            continue
        try:
            valor = float(limpia)
        except ValueError:
            continue
        if math.isfinite(valor):
            numeros.append(valor)
    return numeros

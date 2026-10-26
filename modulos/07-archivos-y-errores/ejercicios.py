"""Ejercicios de la semana 7: archivos y errores.

Las rutas pueden ser texto o pathlib.Path.

    pytest modulos/07-archivos-y-errores
"""

# Ya están importados para que los uses en los TODO.
import json
import math
from pathlib import Path


def dividir(a: float, b: float) -> float:
    """Devuelve a / b.

    Si b es 0, lanza ZeroDivisionError con el mensaje
    "no se puede dividir entre cero".
    """
    # TODO: rechaza el cero y, si no, devuelve la división.
    raise NotImplementedError


def leer_entero(texto: str) -> int | None:
    """Convierte texto a entero.

    Acepta espacios en los extremos, un signo + o - y el número.
    "42" -> 42. "  -7 " -> -7. "+8" -> 8.
    Si no es un entero, devuelve None. "3.14", "hola" y "" son None.
    No lances el error: atrápalo y devuelve None.
    """
    # TODO: intenta int(texto.strip()) y atrapa ValueError.
    raise NotImplementedError


def leer_texto(ruta: str | Path) -> str:
    """Devuelve el contenido del archivo como texto UTF-8.

    Si el archivo no existe, deja salir FileNotFoundError.
    """
    # TODO: lee con pathlib y encoding="utf-8".
    raise NotImplementedError


def escribir_texto(ruta: str | Path, contenido: str) -> None:
    """Escribe contenido en la ruta, reemplazando lo que hubiera.

    Usa UTF-8 y newline="\\n". En Windows, sin newline, Python
    guarda \\r\\n y los bytes del archivo cambian.
    No agregues nada que no te hayan pasado.
    """
    # TODO: write_text con encoding="utf-8" y newline="\n".
    raise NotImplementedError


def agregar_linea(ruta: str | Path, linea: str) -> None:
    """Agrega una línea lógica al final del archivo.

    Si el archivo no existe, lo crea.
    Se le quitan los saltos del final (\\n, \\r\\n o varios seguidos)
    y se escribe exactamente un \\n. "hola", "hola\\n", "hola\\n\\n"
    y "hola\\r\\n" dejan el mismo texto: hola y un salto.
    Una línea vacía, "" o "\\n", deja una línea en blanco.
    Un salto en medio sí se conserva: "una\\ndos" escribe dos líneas
    y, al final, un solo salto.
    Usa UTF-8 y newline="\\n" para que el salto no se convierta en \\r\\n.
    """
    # TODO: abre en modo "a", con encoding="utf-8" y newline="\n".
    # Quita los saltos del final y escribe exactamente uno.
    raise NotImplementedError


def cargar_json(ruta: str | Path):
    """Lee un archivo JSON en UTF-8 y devuelve el dato de Python.

    Si el archivo no existe, deja salir FileNotFoundError.
    Si el texto no es JSON, deja salir el error de json.
    """
    # TODO: lee el texto y usa json.loads.
    raise NotImplementedError


def guardar_json(ruta: str | Path, datos: object) -> None:
    """Guarda datos como JSON en UTF-8.

    Usa ensure_ascii=False para que "café" se vea como café.
    Indenta con 2 espacios, termina el archivo con un salto de línea
    y usa newline="\\n" para no escribir \\r\\n en Windows.
    """
    # TODO: json.dumps con esas opciones, más un salto al final y newline="\n".
    raise NotImplementedError


def leer_json_si_existe(ruta: str | Path, valor_si_falta):
    """Lee el JSON si el archivo existe.

    Si no existe, devuelve valor_si_falta, el mismo objeto, y no crees
    el archivo. Si existe y el contenido no es JSON, deja salir el error.
    """
    # TODO: pregunta si existe. Si no, devuelve el valor. Si sí, carga el JSON.
    raise NotImplementedError


def numeros_de_archivo(ruta: str | Path) -> list[float]:
    """Lee un número por línea y devuelve los que sean finitos.

    Se salta las líneas en blanco y las que no sean números.
    float entiende 1, 2.5, -3 y 1e2 (que vale 100.0).
    Se salta inf y nan: no son finitos.
    El archivo está en UTF-8.
    """
    # TODO: recorre las líneas, intenta float y quédate con math.isfinite.
    raise NotImplementedError

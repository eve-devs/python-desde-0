"""Solución de referencia de la semana 2.

Intenta los ejercicios antes de leer este archivo.
"""


def gritar(texto: str) -> str:
    """Devuelve el texto en mayúsculas, sin espacios en los extremos, con un !.

    "hola" -> "HOLA!"
    "  cuidado  " -> "CUIDADO!"
    "ya!!!" -> "YA!"
    "¡epa!" -> "¡EPA!"

    Quita los signos ! que ya estén al final y pon uno solo.
    El ¡ inicial se queda. Si después de limpiar no queda texto, devuelve "!".
    """
    return texto.strip().upper().rstrip("!") + "!"


def normalizar_correo(correo: str) -> str:
    """Quita espacios de los extremos y pasa el correo a minúsculas.

    "  Eva@Mail.COM " -> "eva@mail.com"

    No hace falta comprobar que sea un correo de verdad.
    """
    return correo.strip().lower()


def formatear_ficha(nombre: str, edad: int, ciudad: str) -> str:
    """Arma la oración "Nombre tiene N años y vive en Ciudad."

    formatear_ficha("Evelyn", 28, "Querétaro") devuelve
    "Evelyn tiene 28 años y vive en Querétaro."
    Incluye el punto final.
    """
    return f"{nombre} tiene {edad} años y vive en {ciudad}."


def contar_fragmento(texto: str, fragmento: str) -> int:
    """Cuenta cuántas veces aparece fragmento dentro de texto.

    No distingue mayúsculas. No encima coincidencias: se comporta como
    el método count. "Banana" y "na" dan 2. "aaa" y "aa" dan 1.
    """
    return texto.lower().count(fragmento.lower())


def palabras(frase: str) -> list[str]:
    """Devuelve la lista de palabras de la frase.

    Corta por cualquier espacio. "hola   mundo" -> ["hola", "mundo"].
    Una frase en blanco devuelve []. Conserva las mayúsculas de cada palabra.
    """
    return frase.split()


def unir(palabras: list[str], separador: str) -> str:
    """Pega las palabras usando separador.

    unir(["Evelyn", "Arias"], " ") -> "Evelyn Arias"
    unir(["2026", "10", "23"], "-") -> "2026-10-23"
    unir([], "-") -> ""
    """
    return separador.join(palabras)


def dominio_de_correo(correo: str) -> str:
    """Devuelve la parte del correo que va después de la última @.

    "Eva@Mail.COM" -> "mail.com"
    "a@b@c.com" -> "c.com"

    Antes de cortar, quita espacios y pasa a minúsculas.
    Si no hay @, devuelve el correo ya normalizado.
    """
    return correo.strip().lower().split("@")[-1]


def enmascarar_telefono(telefono: str) -> str:
    """Oculta todos los caracteres menos los últimos cuatro.

    "5512345678" -> "******5678"
    "12345" -> "*2345"
    "1234" -> "1234"
    "" -> ""

    Trabaja con los caracteres tal como llegan: no quites espacios ni
    revises que sean dígitos.
    """
    # max(..., 0) cubre los teléfonos de 4 caracteres o menos sin un if.
    # La rebanada [-4:] devuelve el texto completo cuando es más corto.
    ocultos = max(len(telefono) - 4, 0)
    return "*" * ocultos + telefono[-4:]

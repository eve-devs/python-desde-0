"""Solución de referencia de la semana 6.

Intenta los ejercicios antes de leer este archivo.
"""

from collections.abc import Callable


def saludar(nombre: str, formal: bool = False) -> str:
    """Devuelve un saludo.

    saludar("Evelyn") -> "Hola, Evelyn."
    saludar("Evelyn", formal=True) -> "Buenos días, Evelyn."

    Las dos frases llevan punto final.
    """
    if formal:
        return f"Buenos días, {nombre}."
    return f"Hola, {nombre}."


def con_iva(precios: list[float], tasa: float = 0.16) -> list[float]:
    """Devuelve una lista nueva con cada precio más el IVA.

    La tasa por defecto es 0.16, o sea 16 por ciento.
    con_iva([100]) -> [116.0]
    con_iva([80], 0.05) -> [84.0]
    con_iva([100], 0) -> [100.0]

    Redondea cada resultado a 2 decimales con round.
    No modifiques la lista original.
    """
    return [round(precio * (1 + tasa), 2) for precio in precios]


def estadisticas(numeros: list[float]) -> dict[str, float | int]:
    """Devuelve mínimo, máximo, promedio y cantidad.

    Las llaves son exactamente "minimo", "maximo", "promedio" y "cantidad".
    estadisticas([4, 8, 6]) ->
        {"minimo": 4, "maximo": 8, "promedio": 6.0, "cantidad": 3}

    Si la lista está vacía, lanza ValueError con el mensaje
    "No se pueden calcular estadísticas de una lista vacía."
    """
    if not numeros:
        raise ValueError("No se pueden calcular estadísticas de una lista vacía.")
    return {
        "minimo": min(numeros),
        "maximo": max(numeros),
        "promedio": sum(numeros) / len(numeros),
        "cantidad": len(numeros),
    }


def unir(*palabras: str, separador: str = " ") -> str:
    """Pega cualquier cantidad de textos.

    unir("hola", "Evelyn") -> "hola Evelyn"
    unir("2026", "10", "23", separador="-") -> "2026-10-23"
    unir() -> ""
    """
    return separador.join(palabras)


def aplicar_a_cada(funcion: Callable, valores: list) -> list:
    """Devuelve una lista nueva aplicando funcion a cada valor.

    aplicar_a_cada(str.upper, ["hola", "eva"]) -> ["HOLA", "EVA"]
    aplicar_a_cada(str.upper, []) -> []
    Conserva el orden.
    """
    return [funcion(valor) for valor in valores]


def crear_saludo(prefijo: str) -> Callable[[str], str]:
    """Devuelve una función que saluda con ese prefijo.

    hola = crear_saludo("Hola")
    hola("Evelyn") -> "Hola, Evelyn"

    La frase es "{prefijo}, {nombre}", sin punto final.
    Cada llamada a crear_saludo recuerda su propio prefijo.
    """

    def saludar_con_prefijo(nombre: str) -> str:
        return f"{prefijo}, {nombre}"

    return saludar_con_prefijo


def elegir(
    opciones: dict[str, Callable[[], str]],
    nombre: str,
    predeterminada: Callable[[], str],
) -> str:
    """Llama a la función guardada en opciones[nombre] y devuelve su resultado.

    Las funciones no reciben argumentos.
    Si nombre no está en el diccionario, llama a predeterminada.

    def hola():
        return "hola"

    elegir({"hola": hola}, "hola", hola) -> "hola"
    elegir({}, "nada", hola) -> "hola"
    """
    funcion = opciones.get(nombre, predeterminada)
    return funcion()


def anotar(mensaje: str, notas: list[str] | None = None) -> list[str]:
    """Agrega mensaje a una lista de notas y devuelve esa lista.

    Si no te pasan lista, crea una nueva.
    Dos llamadas sin lista no comparten datos:
        anotar("comprar café") -> ["comprar café"]
        anotar("estudiar") -> ["estudiar"]

    Si te pasan una lista, agrega el mensaje ahí mismo y devuelve esa lista:
        base = ["pan"]
        anotar("leche", base) -> ["pan", "leche"]
        y base queda ["pan", "leche"].

    El valor por defecto tiene que ser None, no [].
    """
    if notas is None:
        notas = []
    notas.append(mensaje)
    return notas

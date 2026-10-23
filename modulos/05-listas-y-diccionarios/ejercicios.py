"""Ejercicios de la semana 5: listas y diccionarios.

    pytest modulos/05-listas-y-diccionarios
"""


def primer_y_ultimo(elementos: list) -> tuple:
    """Devuelve el primer elemento y el último, en una tupla.

    primer_y_ultimo([1, 2, 3]) es (1, 3).
    primer_y_ultimo([7]) es (7, 7): el único elemento es los dos.
    Si la lista está vacía, lanza ValueError con el mensaje
    "La lista está vacía."
    """
    # TODO: rechaza la lista vacía y devuelve el primero y el último.
    raise NotImplementedError


def sin_extremos(elementos: list) -> list:
    """Devuelve una lista nueva sin el primero ni el último.

    sin_extremos([1, 2, 3, 4]) es [2, 3].
    Si hay menos de 2 elementos, devuelve [].
    No modifiques la lista original.
    """
    # TODO: devuelve la rebanada del medio.
    raise NotImplementedError


def agregar_unico(elementos: list, valor) -> list:
    """Devuelve una lista nueva con valor al final, si todavía no estaba.

    agregar_unico([1, 2], 3) es [1, 2, 3].
    agregar_unico([1, 2], 1) es [1, 2].
    La lista que te pasaron no cambia.
    """
    # TODO: copia la lista y agrega valor solo si no está.
    raise NotImplementedError


def promedio(numeros: list[float]) -> float:
    """Devuelve el promedio de la lista.

    Si está vacía, lanza ValueError con el mensaje
    "No se puede promediar una lista vacía."
    """
    # TODO: divide la suma entre la cantidad. Cuida el caso vacío.
    raise NotImplementedError


def contar_palabras(frase: str) -> dict[str, int]:
    """Cuenta las palabras de la frase, en minúsculas.

    "Hola hola Eva" -> {"hola": 2, "eva": 1}
    Una frase en blanco devuelve {}.
    Corta con split, igual que en la semana 2. No quites comas ni puntos:
    este ejercicio no recibe puntuación.
    """
    # TODO: recorre las palabras y acumula en un diccionario.
    raise NotImplementedError


def invertir_diccionario(original: dict) -> dict:
    """Intercambia llaves y valores.

    {"ana": "555", "eva": "111"} -> {"555": "ana", "111": "eva"}

    Los valores tienen que poder usarse como llaves.
    Si dos llaves comparten valor, se queda la última que aparezca.
    {"a": 1, "b": 1} -> {1: "b"}.
    No modifiques el diccionario original.
    """
    # TODO: arma un diccionario nuevo recorriendo items().
    raise NotImplementedError


def filtrar_mayores(numeros: list[float], umbral: float) -> list[float]:
    """Devuelve los números estrictamente mayores que umbral.

    filtrar_mayores([1, 5, 5, 8], 5) es [8].
    Conserva el orden. No modifiques la lista original.
    """
    # TODO: arma una lista nueva con un ciclo o una comprensión.
    raise NotImplementedError


def combinar(base: dict, extra: dict) -> dict:
    """Devuelve un diccionario nuevo con las llaves de los dos.

    Si una llave está en ambos, gana el valor de extra.
    combinar({"a": 1}, {"a": 2, "b": 3}) es {"a": 2, "b": 3}.
    base y extra no cambian.
    """
    # TODO: usa el operador | .
    raise NotImplementedError

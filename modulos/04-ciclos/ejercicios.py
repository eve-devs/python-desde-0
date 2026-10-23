"""Ejercicios de la semana 4: ciclos.

Haz el trabajo con un ciclo, aunque exista un atajo de una línea.

    pytest modulos/04-ciclos
"""


def suma_del_1_al(n: int) -> int:
    """Suma 1 + 2 + ... + n usando un ciclo.

    suma_del_1_al(4) es 10. suma_del_1_al(1) es 1.
    Si n es menor que 1, devuelve 0.
    """
    # TODO: acumula con un for sobre range(1, n + 1).
    raise NotImplementedError


def contar_pares(inicio: int, fin: int) -> int:
    """Cuenta los pares entre inicio y fin, los dos inclusive.

    contar_pares(1, 10) es 5 (2, 4, 6, 8 y 10).
    contar_pares(2, 2) es 1. contar_pares(1, 1) es 0.
    Si inicio es mayor que fin, devuelve 0.
    Los negativos cuentan: entre -3 y 2 están -2, 0 y 2.
    """
    # TODO: recorre range(inicio, fin + 1) y cuenta los pares.
    raise NotImplementedError


def tabla_de_multiplicar(n: int) -> list[str]:
    """Devuelve las 10 filas de la tabla de n, del 1 al 10.

    Cada fila tiene esta forma exacta: "2 x 1 = 2"
    Con espacios alrededor de la x y del signo =.
    tabla_de_multiplicar(2) empieza en "2 x 1 = 2" y termina en "2 x 10 = 20".
    """
    # TODO: arma una lista de textos dentro de un ciclo.
    raise NotImplementedError


def contar_vocales(texto: str) -> int:
    """Cuenta las vocales del español en texto.

    Cuentan a, e, i, o, u, sus versiones con tilde (á, é, í, ó, ú) y la ü.
    No distingue mayúsculas. La y no cuenta.
    "Hola" tiene 2. "Árbol" tiene 2. "pingüino" tiene 4. "" tiene 0.
    """
    # TODO: recorre el texto en minúsculas y suma cuando el carácter sea vocal.
    raise NotImplementedError


def invertir(texto: str) -> str:
    """Devuelve el texto al revés, construido con un ciclo.

    "hola" -> "aloh". "" -> "". Conserva las mayúsculas: "Anita" -> "atinA".
    Junta los caracteres y únelos al final. No uses la rebanada [::-1].
    """
    # TODO: recorre el texto, guarda los caracteres, invierte y haz join.
    raise NotImplementedError


def factorial(n: int) -> int:
    """Devuelve n! calculado con un ciclo.

    5! es 120. 1! es 1. 0! es 1.
    Si n es negativo, lanza ValueError con el mensaje
    "El factorial no está definido para números negativos."
    """
    # TODO: rechaza los negativos y acumula el producto desde 1.
    raise NotImplementedError


def fizzbuzz(n: int) -> list[str]:
    """Devuelve la lista de FizzBuzz desde 1 hasta n, inclusive.

    - múltiplo de 15: "FizzBuzz"
    - múltiplo de 3: "Fizz"
    - múltiplo de 5: "Buzz"
    - en otro caso: el número convertido a texto

    Pregunta primero por el 15. Si n es menor que 1, devuelve [].
    """
    # TODO: recorre range(1, n + 1) y aplica las reglas en ese orden.
    raise NotImplementedError


def primer_indice(texto: str, caracter: str) -> int:
    """Devuelve la primera posición de caracter dentro de texto.

    Las posiciones empiezan en 0. Si no está, devuelve -1.
    Distingue mayúsculas: primer_indice("programar", "P") es -1.
    primer_indice("programar", "a") es 5.
    caracter se compara completo con cada carácter del texto.
    """
    # TODO: usa enumerate y regresa en cuanto haya coincidencia.
    raise NotImplementedError

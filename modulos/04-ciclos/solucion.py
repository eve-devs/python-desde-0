"""Solución de referencia de la semana 4.

Intenta los ejercicios antes de leer este archivo.
"""

_VOCALES = set("aeiouáéíóúü")


def suma_del_1_al(n: int) -> int:
    """Suma 1 + 2 + ... + n usando un ciclo.

    suma_del_1_al(4) es 10. suma_del_1_al(1) es 1.
    Si n es menor que 1, devuelve 0.
    """
    total = 0
    for numero in range(1, n + 1):
        total += numero
    return total


def contar_pares(inicio: int, fin: int) -> int:
    """Cuenta los pares entre inicio y fin, los dos inclusive.

    contar_pares(1, 10) es 5 (2, 4, 6, 8 y 10).
    contar_pares(2, 2) es 1. contar_pares(1, 1) es 0.
    Si inicio es mayor que fin, devuelve 0.
    Los negativos cuentan: entre -3 y 2 están -2, 0 y 2.
    """
    total = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            total += 1
    return total


def tabla_de_multiplicar(n: int) -> list[str]:
    """Devuelve las 10 filas de la tabla de n, del 1 al 10.

    Cada fila tiene esta forma exacta: "2 x 1 = 2"
    Con espacios alrededor de la x y del signo =.
    tabla_de_multiplicar(2) empieza en "2 x 1 = 2" y termina en "2 x 10 = 20".
    """
    filas = []
    for multiplicador in range(1, 11):
        filas.append(f"{n} x {multiplicador} = {n * multiplicador}")
    return filas


def contar_vocales(texto: str) -> int:
    """Cuenta las vocales del español en texto.

    Cuentan a, e, i, o, u, sus versiones con tilde (á, é, í, ó, ú) y la ü.
    No distingue mayúsculas. La y no cuenta.
    "Hola" tiene 2. "Árbol" tiene 2. "pingüino" tiene 4. "" tiene 0.
    """
    total = 0
    for caracter in texto.lower():
        if caracter in _VOCALES:
            total += 1
    return total


def invertir(texto: str) -> str:
    """Devuelve el texto al revés, construido con un ciclo.

    "hola" -> "aloh". "" -> "". Conserva las mayúsculas: "Anita" -> "atinA".
    Junta los caracteres y únelos al final. No uses la rebanada [::-1].
    """
    caracteres = []
    for caracter in texto:
        caracteres.append(caracter)
    caracteres.reverse()
    return "".join(caracteres)


def factorial(n: int) -> int:
    """Devuelve n! calculado con un ciclo.

    5! es 120. 1! es 1. 0! es 1.
    Si n es negativo, lanza ValueError con el mensaje
    "El factorial no está definido para números negativos."
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    for numero in range(2, n + 1):
        resultado *= numero
    return resultado


def fizzbuzz(n: int) -> list[str]:
    """Devuelve la lista de FizzBuzz desde 1 hasta n, inclusive.

    - múltiplo de 15: "FizzBuzz"
    - múltiplo de 3: "Fizz"
    - múltiplo de 5: "Buzz"
    - en otro caso: el número convertido a texto

    Pregunta primero por el 15. Si n es menor que 1, devuelve [].
    """
    resultado = []
    for numero in range(1, n + 1):
        if numero % 15 == 0:
            resultado.append("FizzBuzz")
        elif numero % 3 == 0:
            resultado.append("Fizz")
        elif numero % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(numero))
    return resultado


def primer_indice(texto: str, caracter: str) -> int:
    """Devuelve la primera posición de caracter dentro de texto.

    Las posiciones empiezan en 0. Si no está, devuelve -1.
    Distingue mayúsculas: primer_indice("programar", "P") es -1.
    primer_indice("programar", "a") es 5.
    caracter se compara completo con cada carácter del texto.
    """
    for indice, actual in enumerate(texto):
        if actual == caracter:
            return indice
    return -1

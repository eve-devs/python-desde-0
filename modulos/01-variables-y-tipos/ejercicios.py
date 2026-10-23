"""Ejercicios de la semana 1: variables y tipos.

Sustituye cada bloque TODO por tu código. Las pruebas llaman a estas
funciones y miran lo que devuelven:

    pytest modulos/01-variables-y-tipos
"""


def suma(a: float, b: float) -> float:
    """Devuelve la suma de a y b.

    Si el café costó 35 pesos y el pan 18, el total es 53.
    """
    # TODO: devuelve a + b.
    raise NotImplementedError


def promedio(a: float, b: float, c: float) -> float:
    """Devuelve el promedio de tres números.

    El promedio es la suma dividida entre 3. El resultado es un decimal
    aunque los tres números sean enteros: promedio(10, 20, 30) vale 20.0.
    """
    # TODO: suma los tres y divide entre 3. Usa /, no //.
    raise NotImplementedError


def es_par(numero: int) -> bool:
    """Dice si numero es par.

    Un número es par cuando el resto de dividirlo entre 2 es 0.
    El cero es par. Los negativos pares, como -4, también.
    """
    # TODO: devuelve True si numero es par y False si no lo es.
    raise NotImplementedError


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit.

    La fórmula es (celsius * 9 / 5) + 32.
    0 °C son 32 °F. 100 °C son 212 °F.
    """
    # TODO: aplica la fórmula y devuelve el resultado.
    raise NotImplementedError


def horas_y_minutos(total_minutos: int) -> tuple[int, int]:
    """Reparte un total de minutos en horas y minutos sobrantes.

    135 minutos son 2 horas y 15 minutos, así que el resultado es (2, 15).
    60 minutos son (1, 0). 59 minutos son (0, 59).
    total_minutos es mayor o igual que 0. No hace falta dar la vuelta
    al reloj de 24 horas: 1000 minutos son 16 horas y 40 minutos.
    """
    # TODO: usa // para las horas y % para los minutos que sobran.
    raise NotImplementedError


def precio_con_descuento(precio: float, porcentaje: float) -> float:
    """Devuelve el precio después de quitar un porcentaje.

    porcentaje va de 0 a 100. 10 significa diez por ciento, no 0.10.
    Un precio de 200 con 10 por ciento de descuento queda en 180.
    """
    # TODO: calcula precio * (1 - porcentaje / 100).
    raise NotImplementedError


def perimetro_rectangulo(base: float, altura: float) -> float:
    """Devuelve el perímetro de un rectángulo: 2 * (base + altura)."""
    # TODO: devuelve el perímetro.
    raise NotImplementedError


def cuota_por_persona(total: float, personas: int) -> float:
    """Reparte una cuenta entre varias personas.

    personas es mayor que 0. Si la cuenta es 300 y son 4, cada quien
    paga 75.0. La división tiene que ser decimal: 100 entre 3 no cabe
    exacto y el resultado es un float.
    """
    # TODO: divide total entre personas.
    raise NotImplementedError

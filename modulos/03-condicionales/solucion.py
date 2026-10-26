"""Solución de referencia de la semana 3.

Intenta los ejercicios antes de leer este archivo.
"""

_DIAS_LABORALES = {"lunes", "martes", "miércoles", "miercoles", "jueves", "viernes"}


def signo(numero: float) -> str:
    """Devuelve "positivo", "negativo" o "cero".

    El cero, incluido 0.0, es "cero".
    """
    if numero > 0:
        return "positivo"
    if numero < 0:
        return "negativo"
    return "cero"


def clasificar_edad(edad: int) -> str:
    """Clasifica una edad.

    - negativa: "no válida"
    - 0 a 12: "niñez"
    - 13 a 17: "adolescencia"
    - 18 a 64: "adultez"
    - 65 o más: "adultez mayor"

    Los extremos entran en el grupo. 12 es niñez. 13 es adolescencia.
    18 y 64 son adultez. 65 es adultez mayor.
    """
    if edad < 0:
        return "no válida"
    if edad <= 12:
        return "niñez"
    if edad <= 17:
        return "adolescencia"
    if edad <= 64:
        return "adultez"
    return "adultez mayor"


def resultado_examen(calificacion: float) -> str:
    """Describe una calificación de 0 a 100.

    - menor que 0 o mayor que 100: "fuera de rango"
    - 90 a 100: "excelente"
    - 70 a 89.999...: "aprobado"
    - 0 a 69.999...: "reprobado"

    90 es excelente. 70 es aprobado. 100 es excelente.
    """
    if calificacion < 0 or calificacion > 100:
        return "fuera de rango"
    if calificacion >= 90:
        return "excelente"
    if calificacion >= 70:
        return "aprobado"
    return "reprobado"


def puede_votar(edad: int, tiene_credencial: bool) -> bool:
    """Dice si la persona puede votar.

    Hacen falta las dos cosas: tener 18 años o más y tener credencial.
    """
    return edad >= 18 and tiene_credencial


def saludo_por_hora(hora: int) -> str:
    """Devuelve un saludo según la hora, en formato de 24 horas.

    - hora menor que 0 o mayor que 23: "hora no válida"
    - 0 a 11: "buenos días"
    - 12 a 18: "buenas tardes"
    - 19 a 23: "buenas noches"
    """
    if hora < 0 or hora > 23:
        return "hora no válida"
    if hora <= 11:
        return "buenos días"
    if hora <= 18:
        return "buenas tardes"
    return "buenas noches"


def tarifa_estacionamiento(horas: int) -> int:
    """Calcula el costo de estacionarse, en pesos enteros.

    Si horas es 0 o negativa, el costo es 0.
    La primera hora cuesta 20. Cada hora extra cuesta 15.
    El tope de un día es 100: nadie paga más que eso.

    1 hora -> 20. 2 horas -> 35. 6 horas -> 95. 7 horas -> 100.
    """
    if horas <= 0:
        return 0
    costo = 20 + (horas - 1) * 15
    if costo > 100:
        return 100
    return costo


def dia_laboral(dia: str) -> bool:
    """Dice si el día es de lunes a viernes.

    Ignora mayúsculas y espacios en los extremos.
    Acepta "miércoles" y también "miercoles", sin tilde.
    Sábado y domingo no son laborales, se escriban como se escriban.
    """
    return dia.strip().lower() in _DIAS_LABORALES


def precio_boleto(edad: int, es_estudiante: bool) -> int:
    """Devuelve el precio del boleto, en pesos enteros.

    Si la edad es negativa, lanza ValueError con el mensaje
    "La edad no puede ser negativa."

    El reglamento, en este orden:

    - de 0 a 3 años: 0
    - de 4 a 11 años, o 65 años o más: 40
    - estudiante que no entró en los casos anteriores: 60
    - cualquier otro caso: 80

    Una niña de 10 años estudiante paga 40, no 60.
    Una persona de 65 años estudiante paga 40, no 60.
    Alguien de 12 años estudiante paga 60.
    """
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad <= 3:
        return 0
    if edad <= 11 or edad >= 65:
        return 40
    if es_estudiante:
        return 60
    return 80

"""Ejercicios de la semana 3: condicionales.

    pytest modulos/03-condicionales
"""


def signo(numero: float) -> str:
    """Devuelve "positivo", "negativo" o "cero".

    El cero, incluido 0.0, es "cero".
    """
    # TODO: compara numero con 0.
    raise NotImplementedError


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
    # TODO: revisa los rangos en ese orden.
    raise NotImplementedError


def resultado_examen(calificacion: float) -> str:
    """Describe una calificación de 0 a 100.

    - menor que 0 o mayor que 100: "fuera de rango"
    - 90 a 100: "excelente"
    - 70 a 89.999...: "aprobado"
    - 0 a 69.999...: "reprobado"

    90 es excelente. 70 es aprobado. 100 es excelente.
    """
    # TODO: primero descarta lo que está fuera de rango.
    raise NotImplementedError


def puede_votar(edad: int, tiene_credencial: bool) -> bool:
    """Dice si la persona puede votar.

    Hacen falta las dos cosas: tener 18 años o más y tener credencial.
    """
    # TODO: combina las dos condiciones con and.
    raise NotImplementedError


def saludo_por_hora(hora: int) -> str:
    """Devuelve un saludo según la hora, en formato de 24 horas.

    - hora menor que 0 o mayor que 23: "hora no válida"
    - 0 a 11: "buenos días"
    - 12 a 18: "buenas tardes"
    - 19 a 23: "buenas noches"
    """
    # TODO: valida la hora y después elige el saludo.
    raise NotImplementedError


def tarifa_estacionamiento(horas: int) -> int:
    """Calcula el costo de estacionarse, en pesos enteros.

    Si horas es 0 o negativa, el costo es 0.
    La primera hora cuesta 20. Cada hora extra cuesta 15.
    El tope de un día es 100: nadie paga más que eso.

    1 hora -> 20. 2 horas -> 35. 6 horas -> 95. 7 horas -> 100.
    """
    # TODO: calcula 20 + (horas - 1) * 15 y aplica el tope.
    raise NotImplementedError


def dia_laboral(dia: str) -> bool:
    """Dice si el día es de lunes a viernes.

    Ignora mayúsculas y espacios en los extremos.
    Acepta "miércoles" y también "miercoles", sin tilde.
    Sábado y domingo no son laborales, se escriban como se escriban.
    """
    # TODO: normaliza el texto y compáralo con los cinco días.
    raise NotImplementedError


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
    # TODO: lanza el error si la edad es negativa y aplica el reglamento en orden.
    raise NotImplementedError

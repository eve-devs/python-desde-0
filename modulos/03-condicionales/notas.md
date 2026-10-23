# Semana 3. Condicionales

Un programa que siempre hace lo mismo no decide. Esta semana eliges un camino con `if`, `elif` y `else`: el saludo según la hora, el precio del boleto, si un día es laboral.

## La indentación es sintaxis

Python no usa llaves para agrupar. Usa espacios. En este curso son **4 espacios** por nivel. No mezcles tabuladores y espacios: el error se llama `TabError` o una indentación que "se ve bien" y no lo está.

```python
edad = 20
if edad >= 18:
    print("puede votar")
else:
    print("todavía no")
```

`elif` es "si no, prueba esta otra". Se lee en orden y se ejecuta **una** rama, la primera que sea verdadera:

```python
def signo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"
```

Con `return` dentro de cada rama, el `elif` se puede escribir también como un `if` nuevo: si ya regresaste, el resto de la función no corre. Las dos formas son claras. Elige la que se lea mejor.

## Comparar

```python
==  !=  <  <=  >  >=
```

Python deja encadenar comparaciones, y lo hace bien:

```python
0 <= calificacion <= 100
```

Eso significa "`calificacion` está entre 0 y 100, inclusive". En otros lenguajes esa línea es una trampa. Aquí es la forma natural.

## and, or, not

```python
puede_votar = edad >= 18 and tiene_credencial
es_fin_de_semana = dia == "sábado" or dia == "domingo"
abierto = not cerrado
```

`and` solo sigue al segundo lado si el primero es verdadero. `or` solo sigue si el primero es falso. Por eso este orden es cómodo: primero la edad, después la credencial.

No escribas `if tiene_credencial == True`. Escribe `if tiene_credencial:`. Comparar un booleano con `True` es ruido, y además `== True` es verdadero para el número `1`.

## El orden de las preguntas importa

En el boleto del cine la regla del adulto mayor tiene que ir **antes** que la del estudiante. Si preguntas primero "¿es estudiante?", una persona de 70 años con credencial de estudiante paga de menos o de más, según cómo lo escribas. La docstring de `precio_boleto` dice la prioridad. Léela como un reglamento, de arriba hacia abajo.

Lo mismo en FizzBuzz, la semana que viene: "¿múltiplo de 15?" tiene que ir antes que "¿múltiplo de 3?".

## Valores que se comportan como falso

En un `if`, estos valores cuentan como falso: `False`, `None`, `0`, `0.0`, `""` y las colecciones vacías (`[]`, `{}`). Todo lo demás cuenta como verdadero, incluido el texto `"0"` y el número `-1`.

No uses eso para edades. La edad `0` es un bebé, no "falta el dato". Si el dato puede faltar, usa `None` y compáralo con `is None`.

## match, para cuando el valor es uno de varios

Desde Python 3.10 existe `match` / `case`. Sirve cuando comparas un valor con opciones exactas. Los ejercicios de esta semana se resuelven con `if`, que es la herramienta general. `match` aparece mucho en programas que leen comandos, y el proyecto final podría usar uno. Conviene reconocer la forma:

```python
def interpretar(comando):
    match comando:
        case "salir" | "exit":
            return "hasta luego"
        case "ayuda":
            return "aquí tienes ayuda"
        case _:
            return "no entiendo"
```

Dentro de un `case`, la barra `|` significa "esta opción o esta otra". No es la unión de diccionarios de la semana 5: el mismo símbolo, otro contexto. `_` es el caso por defecto.

## Errores a propósito

`precio_boleto` lanza `ValueError` si la edad es negativa. Lanzar un error es decir "esta llamada no tiene sentido, me detengo y aviso":

```python
if edad < 0:
    raise ValueError("La edad no puede ser negativa.")
```

La semana 7 enseña a atrapar esos avisos. Hoy basta con lanzar este, con ese mensaje exacto, porque la prueba lo busca.

## Los ejercicios

| Función | Decisión |
| --- | --- |
| `signo` | Positivo, negativo o cero |
| `clasificar_edad` | Niñez, adolescencia, adultez, adultez mayor |
| `resultado_examen` | Excelente, aprobado, reprobado o fuera de rango |
| `puede_votar` | 18 años o más, y credencial |
| `saludo_por_hora` | Buenos días, tardes o noches |
| `tarifa_estacionamiento` | Primera hora, horas extra y un tope |
| `dia_laboral` | De lunes a viernes, con o sin tilde en miércoles |
| `precio_boleto` | Gratis, media, estudiante o completo |

# Semana 1. Variables y tipos

Esta semana vas a guardar datos y a calcular con ellos: la cuenta de un café, la temperatura del horno, si un número es par, cómo se reparte una cuenta.

## Cómo usar este módulo

1. Lee estas notas y corre los ejemplos.
2. Completa `ejercicios.py`. Cada función tiene un `# TODO`.
3. Desde la raíz del repositorio, con el entorno activo:

```bash
pytest modulos/01-variables-y-tipos
```

4. Cuando las pruebas pasen, marca la semana 1 en el `README.md`.

## Un nombre pegado a un valor

En Python una variable es un nombre que apunta a un valor. No tienes que declarar de qué tipo es: Python lo deduce del valor.

```python
precio_cafe = 35
temperatura = 36.6
nombre = "Evelyn"
hay_cafe = True
```

El nombre va en `snake_case`: minúsculas y guiones bajos, sin espacios. Puede llevar números, pero no empezar por un número. Evita las palabras que Python ya usa (`if`, `for`, `True`, `return`).

Python 3 permite tildes en los nombres. En los ejercicios usamos nombres sin acentos, para que se escriban igual en cualquier teclado: `precio`, `anio`, `numero`.

`=` guarda. `==` compara. Son dos cosas distintas.

```python
edad = 18
edad == 18  # True
```

Puedes preguntar el tipo con `type`:

```python
type(35)        # <class 'int'>
type(36.6)      # <class 'float'>
type("Evelyn")  # <class 'str'>
type(True)      # <class 'bool'>
```

En las funciones de los ejercicios verás pistas como `a: float`. Son notas para quien lee el código. Python **no** las revisa al ejecutar: si pasas un texto donde dice `float`, el programa no se detiene por eso.

## Los tipos de esta semana

| Tipo | Nombre en el curso | Ejemplos | Para qué |
| --- | --- | --- | --- |
| `int` | entero | `0`, `18`, `-4` | Contar cosas enteras |
| `float` | decimal | `1.5`, `36.6` | Medidas y precios |
| `str` | texto | `"hola"` | Palabras. La semana 2 es suya |
| `bool` | booleano | `True`, `False` | Sí o no |

`True` y `False` se escriben con mayúscula inicial. `true` suelto es un error.

Un entero de Python puede ser enorme. `2 ** 100` cabe sin trucos. El `**` es la potencia.

## Operaciones

```python
7 + 3     # 10
7 - 3     # 4
7 * 3     # 21
7 / 3     # 2.3333...  siempre un float
7 // 3    # 2          división entera, se queda con la parte baja
7 % 3     # 1          lo que sobra al dividir
7 ** 3    # 343
```

En Python 3, `7 / 3` **no** trunca. Si vienes de otro lenguaje, este es el susto clásico. Para quedarte con el cociente entero usa `//`. Para el resto, `%`.

Un número es par cuando el resto de dividirlo entre 2 es cero: `n % 2 == 0`. El cero es par. Los negativos también: `-4 % 2` vale `0`.

Ojo con los negativos y `//`. Python redondea hacia abajo, no hacia cero:

```python
-7 // 2   # -4
-7 % 2    # 1
```

No lo necesitas en los ejercicios. Conviene haberlo visto una vez para no desconfiar del lenguaje después.

## Decimales que no salen "redondos"

Prueba esto en el intérprete:

```python
0.1 + 0.2   # 0.30000000000000004
```

No es un bug de tu instalación. Los `float` se guardan en binario, y `0.1` no tiene un binario finito, igual que `1/3` no tiene un decimal finito. Para precios, en este curso redondeamos con `round(numero, 2)` cuando haga falta mostrar centavos. Comparar dos precios con `==` a veces miente; las pruebas del curso usan valores que sí son exactos, o comparan con un margen.

## Comparaciones

```python
edad = 20
edad >= 18     # True
edad < 18      # False
edad != 17     # True
```

El resultado es un booleano. Puedes guardarlo:

```python
puede_entrar = edad >= 18
```

## Una función, por ahora

Una función es una receta con nombre. Recibe datos y **devuelve** un resultado. Quien la llama decide qué hacer con ese resultado.

```python
def precio_con_descuento(precio, porcentaje):
    return precio * (1 - porcentaje / 100)

precio_con_descuento(200, 10)  # 180.0
```

Fíjate en tres cosas:

- Después de `def` y de los dos puntos, el cuerpo va **indentado 4 espacios**.
- `return` entrega el valor. Sin `return`, la función devuelve `None`, que significa "aquí no hay nada".
- `print` solo muestra texto en la pantalla. Las pruebas miran lo que devuelves, no lo que imprimes. Si imprimes el resultado y no lo devuelves, la prueba falla.

La semana 6 abre las funciones con calma: valores por defecto, funciones que arman otras funciones, y un error famoso de Python. Hoy basta con calcular y devolver.

## Probar ideas sueltas

`input` lee lo que escribes en la terminal. No lo usamos en los ejercicios porque las pruebas no pueden teclear, pero puedes jugar con él:

```python
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
```

La semana que viene armamos ese saludo con un f-string, que es la forma actual de interpolar texto.

## Errores que vas a ver

- `NameError`: usaste un nombre que no existe. Revisa la ortografía.
- `SyntaxError`: Python no pudo ni empezar a leer. Suele ser un paréntesis, unas comillas o la indentación.
- `ZeroDivisionError`: dividiste entre cero. `cuota_por_persona` asume que hay al menos una persona.
- `TypeError: unsupported operand`: mezclaste tipos que no se suman, por ejemplo `"3" + 4`. El texto `"3"` y el número `4` son distintos. La semana 7 convierte texto a número a propósito.

## Los ejercicios

| Función | Idea cotidiana |
| --- | --- |
| `suma` | Café más pan |
| `promedio` | Tres calificaciones |
| `es_par` | ¿Se puede repartir en dos montones iguales? |
| `celsius_a_fahrenheit` | Una receta que viene en Fahrenheit |
| `horas_y_minutos` | 135 minutos son 2 horas y 15 minutos |
| `precio_con_descuento` | 10 significa "10 por ciento de descuento" |
| `perimetro_rectangulo` | El borde de una mesa |
| `cuota_por_persona` | La cuenta dividida entre quienes comieron |

En `horas_y_minutos(135)` el resultado es la tupla `(2, 15)`. Una tupla es una pareja ordenada. Hoy solo tienes que devolverla; la semana 5 explica por qué existe.

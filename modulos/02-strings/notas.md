# Semana 2. Texto

Un `str` es una secuencia de caracteres Unicode. La eñe, el acento y el emoji cuentan como un carácter cada uno, no como un byte suelto:

```python
len("canción")  # 7
```

Esta semana vas a limpiar un correo, armar una ficha y enmascarar un teléfono.

## Comillas

Las comillas simples y las dobles valen lo mismo. Elige una y sé constante. En este curso usamos comillas dobles. Si el texto lleva un apóstrofo, las dobles se leen mejor:

```python
titulo = "la canción de hoy"
```

Tres comillas abren un texto de varias líneas. También se usan para documentar funciones; lo verás en la semana 6.

```python
menu = """Café
Pan
Agua"""
```

Para meter un carácter especial se usa `\`:

| Secuencia | Significa |
| --- | --- |
| `\n` | Salto de línea |
| `\t` | Tabulador |
| `\\` | Una barra invertida |
| `\"` | Una comilla dentro de un texto con comillas dobles |

## Índices y rebanadas

El primer carácter está en la posición **0**, no en la 1.

```python
palabra = "hola"
palabra[0]    # "h"
palabra[-1]   # "a", el último
palabra[1:3]  # "ol"  (desde el 1, hasta antes del 3)
palabra[:2]   # "ho"
palabra[2:]   # "la"
```

El final de una rebanada (`slice`) no se incluye. Es la misma idea que `range`, que verás en la semana 4.

Si el índice no existe, Python lanza `IndexError`. Una rebanada que se sale del texto no falla: devuelve lo que haya.

Para dar la vuelta a un texto corto existe la rebanada `palabra[::-1]`. En la semana 4 lo vas a hacer con un ciclo, para ver el trabajo que esa rebanada esconde.

## El texto no se modifica por dentro

Esto falla:

```python
palabra = "hola"
palabra[0] = "H"  # TypeError
```

Los métodos no cambian el original. Devuelven un texto nuevo, y el viejo sigue ahí si no lo reemplazas:

```python
nombre = "  Evelyn  "
limpio = nombre.strip()
# nombre sigue teniendo espacios
# limpio es "Evelyn"
```

El error típico es llamar `nombre.strip()` y olvidar guardar el resultado.

## Métodos que vas a usar

```python
"  Eva@Mail.COM  ".strip()          # "Eva@Mail.COM"
"  Eva@Mail.COM  ".strip().lower()  # "eva@mail.com"
"cuidado".upper()                   # "CUIDADO"
"hola mundo".replace("mundo", "Evelyn")
"Banana".lower().count("na")        # 2
"hola mundo".split()                # ["hola", "mundo"]
"-".join(["2026", "10", "23"])      # "2026-10-23"
"pregunta".endswith("?")            # False
"¿sí?".startswith("¿")              # True
```

`split()` sin argumentos corta por cualquier espacio, tabulación o salto, y no deja textos vacíos en medio. `"hola   mundo".split()` es `["hola", "mundo"]`.

`count` no encima las coincidencias. En `"aaa"`, `"aa"` aparece una vez: Python la encuentra al inicio y sigue buscando **después** de ella. La segunda `"aa"` (posiciones 1 y 2) no se cuenta. Los ejercicios piden ese mismo comportamiento.

`removeprefix` y `removesuffix` (desde Python 3.9) quitan un extremo solo si está:

```python
"gastos.json".removesuffix(".json")  # "gastos"
"precio".removesuffix(".json")       # "precio", no había nada que quitar
```

Para pegar muchos trozos, usa `join`. Sumar textos en un ciclo (`resultado = resultado + pedazo`) copia el texto entero en cada vuelta, porque el `str` no se puede modificar. Con pocos datos no se nota. Con muchos, sí. `join` reserva el espacio una vez.

## f-strings

La forma actual de armar un texto con valores es el f-string. La `f` va pegada a la comilla de apertura:

```python
nombre = "Evelyn"
edad = 28
ciudad = "Querétaro"
ficha = f"{nombre} tiene {edad} años y vive en {ciudad}."
```

Dentro de las llaves puedes calcular y formatear:

```python
precio = 45.5
print(f"Total: ${precio:.2f}")  # Total: $45.50
```

`.2f` significa "un decimal, dos cifras después del punto". El 45.5 se muestra como `45.50`.

Desde Python 3.8 puedes depurar mostrando el nombre y el valor:

```python
print(f"{precio=}")  # precio=45.5
```

Desde Python 3.12 las comillas de dentro pueden ser las mismas que las de fuera (antes esto era un error de sintaxis):

```python
mensaje = f"Ella dijo: {"hola"}"
```

Ese ejemplo es de 3.12 o posterior. Si tu versión es más vieja, usa comillas distintas: `f"Ella dijo: {'hola'}"`.

## ¿Está o no está?

```python
"eva" in "revanada"   # False
"@" in "eva@mail.com" # True
```

`in` busca un fragmento, no una palabra completa. `"pan" in "panadería"` es `True`.

## Errores frecuentes

- `"3" + "4"` es `"34"`, no `7`. Son textos. Para sumar números, conviértelos (semana 7) o no los pongas entre comillas.
- `nombre.upper` sin paréntesis no llama al método: te devuelve el método mismo. Las pruebas esperan el texto ya convertido, así que los paréntesis importan.
- Un índice al revés (`texto[len(texto)]`) se sale. El último índice válido es `len(texto) - 1`, o simplemente `-1`.

## Los ejercicios

No necesitas `if` todavía. Con `strip`, `lower`, `upper`, `split`, `join`, `count` y rebanadas alcanza.

| Función | Qué hace |
| --- | --- |
| `gritar` | Limpia, pasa a mayúsculas y deja un solo `!` al final |
| `normalizar_correo` | Quita espacios y pasa a minúsculas |
| `formatear_ficha` | Arma una oración con f-string |
| `contar_fragmento` | Cuenta sin distinguir mayúsculas y sin encimar |
| `palabras` | Corta una frase por espacios |
| `unir` | Pega una lista con un separador |
| `dominio_de_correo` | Lo que va después de la última `@` |
| `enmascarar_telefono` | Deja visibles solo los últimos 4 caracteres |

`max(a, b)` devuelve el mayor de los dos. En el teléfono, `max(len(telefono) - 4, 0)` vale 0 cuando el texto es corto, así que no hace falta un `if`. La rebanada `telefono[-4:]` devuelve el texto entero si tiene menos de 4 caracteres.

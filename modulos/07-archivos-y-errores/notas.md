# Semana 7. Archivos y errores

Un error de Python no es el fin del programa. Es un aviso con nombre: "división entre cero", "ese archivo no está", "eso no es un entero". Esta semana lanzas avisos, los atrapas y guardas texto en disco con `pathlib`.

## try / except

```python
def leer_entero(texto):
    try:
        return int(texto.strip())
    except ValueError:
        return None
```

`int("42")` vale 42. `int("3.14")` y `int("hola")` lanzan `ValueError`. El `except` solo debe nombrar el error que esperas. Un `except:` pelado también atrapa Control+C y esconde fallos de verdad. No lo uses.

`else` corre cuando **no** hubo error. `finally` corre siempre, haya error o no. Para cerrar un archivo, `with` es más claro que `finally`, y es lo que vamos a usar.

```python
try:
    numero = int(texto)
except ValueError:
    numero = None
else:
    print("sí era un entero")
```

Atrapar un error y callarlo está bien cuando el contrato de la función es "si no se puede, devuelve None", como `leer_entero`. En otros casos es mejor avisar con un mensaje claro.

## raise

```python
if b == 0:
    raise ZeroDivisionError("no se puede dividir entre cero")
```

`raise` detiene la función y entrega el aviso a quien la llamó. Si nadie lo atrapa, el programa termina y muestra el mensaje.

Puedes encadenar la causa:

```python
except json.JSONDecodeError as error:
    raise ValueError("el archivo no es JSON válido") from error
```

`from error` conserva el aviso original por si hace falta verlo. `from None` lo sustituye. En el proyecto final vas a usar las dos ideas: un mensaje para la persona, y la causa técnica guardada.

Los avisos que aparecen en estos ejercicios:

| Tipo | Cuándo |
| --- | --- |
| `ValueError` | El valor tiene el tipo correcto y el contenido no sirve |
| `TypeError` | El tipo no es el que la operación espera |
| `ZeroDivisionError` | División entre cero |
| `FileNotFoundError` | La ruta no existe |
| `KeyError` | La llave no está en el diccionario |
| `json.JSONDecodeError` | El texto no es JSON |

`JSONDecodeError` es un `ValueError`. Un `except ValueError` también lo atrapa. Cuando quieras distinguirlo, atrapa `json.JSONDecodeError` primero.

## Dos estilos, los dos válidos

Antes de abrir un archivo puedes preguntar `path.exists()`. O puedes intentar abrirlo y atrapar `FileNotFoundError`. A la segunda costumbre se le dice "es más fácil pedir perdón que permiso". Para convertir texto con `int`, pedir perdón queda natural: la forma de saber si se puede es intentarlo. Para un archivo que es normal que no exista, `exists()` se lee muy bien. Los ejercicios usan las dos, y la docstring dice cuál.

## pathlib

`pathlib.Path` es la forma actual de hablar de rutas. Los tutoriales viejos usan `os.path`. Hace lo mismo y se lee peor.

```python
from pathlib import Path

ruta = Path("notas") / "hoy.txt"
texto = ruta.read_text(encoding="utf-8")
ruta.write_text("Hola\n", encoding="utf-8")
```

El operador `/` entre un `Path` y un texto junta las partes con el separador del sistema. No pegues rutas a mano con `"/"`.

`write_text` crea el archivo o lo **sobrescribe**. Para agregar al final, ábrelo en modo `"a"`:

```python
with ruta.open("a", encoding="utf-8") as archivo:
    archivo.write("otra línea\n")
```

`with` cierra el archivo aunque haya un error a mitad de camino. Cuando el bloque termina, el archivo ya está cerrado.

Pasa siempre `encoding="utf-8"`. En tu Mac el idioma por defecto suele ser UTF-8 y "canción" se guarda bien aunque te olvides. En otras computadoras el olvido convierte la eñe en un error, o en otra letra. Escribir el encoding es parte de la solución, no un adorno.

Una ruta puede llegarte como texto o como `Path`. `Path(ruta)` acepta las dos cosas: si ya es un `Path`, te lo devuelve.

## JSON

JSON es un formato de texto para datos: diccionarios, listas, números, textos y `true` / `false` / `null`. En Python eso es `dict`, `list`, `int`, `float`, `str`, `True`, `False` y `None`.

```python
import json

texto = json.dumps({"canción": "café"}, ensure_ascii=False, indent=2)
datos = json.loads(texto)
```

`ensure_ascii=False` escribe `café` y no `\u00e9`. El archivo se lee mejor y, con `encoding="utf-8"`, es igual de correcto. `indent=2` lo parte en líneas con dos espacios. Sin indent, todo cabe en una línea: válido, ilegible.

Una tupla se guarda como lista. Al volver a leerla, es una lista. JSON no tiene tuplas.

`guardar_json` en el ejercicio escribe ese texto y un salto de línea al final. `cargar_json` lo lee. Si el archivo no existe, `read_text` lanza `FileNotFoundError`: déjalo salir. `leer_json_si_existe` es el otro contrato: si no está, devuelve el valor que te pasaron, el mismo objeto, sin crear el archivo.

No pongas `[]` como valor por defecto de `leer_json_si_existe`. Es el mismo problema de la semana 6. Quien llama pasa el valor.

## Números en un archivo

`numeros_de_archivo` lee un número por línea. Las líneas en blanco se saltan. Las que no son números, también. `float` entiende `1`, `2.5`, `-3` y `1e2` (que vale 100). También entiende `inf` y `nan`, que no son cantidades útiles aquí: si el número no es finito (`math.isfinite`), sáltalos.

## Los ejercicios

| Función | Contrato corto |
| --- | --- |
| `dividir` | Divide, o avisa en español si el divisor es 0 |
| `leer_entero` | `int` o `None` |
| `leer_texto` / `escribir_texto` | UTF-8. Escribir reemplaza el archivo |
| `agregar_linea` | Agrega una línea, creando el archivo si no está |
| `cargar_json` / `guardar_json` | Ida y vuelta, con acentos legibles |
| `leer_json_si_existe` | Si falta el archivo, devuelve lo que te pasaron |
| `numeros_de_archivo` | Lee decimales y se salta el resto |

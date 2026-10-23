# Semana 8. Proyecto final: registro de gastos

Vas a construir un programa de terminal para anotar en qué se te va el dinero. Cada gasto tiene descripción, monto, categoría y fecha. El programa los guarda en un archivo JSON y puede listarlos, sumarlos y agruparlos.

No es una simulación de juguete: cuando lo termines, puedes usarlo de verdad. El archivo `gastos.json` queda en la carpeta desde la que lo corras, y `.gitignore` evita que tus gastos se suban a GitHub por accidente.

Los precios se guardan como `float` redondeados a centavos. Para un registro personal alcanza. Un sistema de cobros profesional suele guardar centavos enteros, o usar `decimal.Decimal`, porque el binario de los `float` no representa bien todas las décimas. El README lo cuenta en la semana 1. Aquí `round(monto, 2)` es la decisión consciente.

## El dato

Un gasto es un diccionario con estas llaves, en este orden:

```python
{
    "descripcion": "Café",
    "monto": 45.5,
    "categoria": "alimentos",
    "fecha": "2026-10-01",
}
```

Reglas de `crear_gasto`:

| Campo | Regla |
| --- | --- |
| descripción | Texto. Se le quitan los espacios de los extremos. Si queda vacía: `ValueError` con `"La descripción no puede estar vacía."` |
| monto | Un `int` o un `float` finito, mayor que cero. `True` y `False` no cuentan, aunque en Python `bool` sea un `int`. Tampoco valen textos, `inf` ni `nan`. El mensaje es `"El monto debe ser un número."` Si el número es 0 o negativo: `"El monto debe ser mayor que cero."` Se guarda como `float` redondeado a 2 decimales. |
| categoría | Texto, sin espacios en los extremos, en minúsculas. `" Alimentos "` se guarda como `"alimentos"`. Si queda vacía: `"La categoría no puede estar vacía."` |
| fecha | Texto `AAAA-MM-DD`, por ejemplo `2026-10-01`. Si pasas `None`, se usa la fecha de hoy. Si el formato no es ese, o el día no existe (`2026-02-31`): `"La fecha debe tener el formato AAAA-MM-DD."` |

`2026-1-1` no sirve: el mes y el día van con dos cifras.

## El archivo

`guardar_gastos` escribe una lista de gastos en JSON, UTF-8, `ensure_ascii=False`, indentado a 2 espacios, con un salto de línea al final. Pasa también `newline="\n"`: en Windows, sin eso, Python guarda `\r\n` y el archivo cambia de una computadora a otra. Así "Café" se lee como Café dentro del archivo. Las rutas se arman con `pathlib.Path`, que entiende tanto `\` como `/`.

`cargar_gastos` hace el camino de vuelta.

- Si el archivo no existe, devuelve `[]` y no lo crea.
- Si el texto no es JSON, lanza `ValueError` con `"El archivo de gastos no contiene JSON válido."`
- Si el JSON no es una lista, lanza `ValueError` con `"El archivo de gastos debe contener una lista."`

`agregar_gasto` carga, crea el gasto, lo agrega, guarda y devuelve el gasto nuevo.

## Las cuentas

`total` suma los montos y redondea a 2 decimales. Una lista vacía suma 0.

`total_por_categoria` devuelve un diccionario. Las llaves van en orden alfabético y cada suma está redondeada a 2 decimales.

`filtrar_por_categoria` compara en minúsculas y sin espacios en los extremos. Devuelve una lista nueva, en el orden original. No borra nada del archivo: solo filtra la lista que le pases.

## El texto que ve la persona

`formatear_resumen([])` devuelve exactamente:

```text
No hay gastos registrados.
```

Con gastos, las líneas de cada gasto conservan el orden en que están guardados. Las categorías del final van en orden alfabético. Hay dos espacios entre la fecha, la descripción, el monto y la categoría:

```text
Gastos (2)
- 2026-10-01  Café  $45.50  alimentos
- 2026-10-02  Metro  $12.00  transporte
Total: $57.50
Por categoría:
- alimentos: $45.50
- transporte: $12.00
```

El monto siempre se muestra con dos decimales: `$45.50`, no `$45.5`.

## La terminal

`main(argumentos, ruta)` no imprime. Devuelve el texto que hay que mostrar. Así las pruebas pueden leerlo. Al final de `ejercicios.py` hay un bloque que sí imprime, y solo corre cuando tú ejecutas el archivo:

```text
cd modulos/08-proyecto-final
python ejercicios.py
python ejercicios.py agregar "Café" 45.50 alimentos 2026-10-01
python ejercicios.py listar
python ejercicios.py total
python ejercicios.py resumen
python ejercicios.py categoria alimentos
```

Esos comandos valen en macOS, Linux, PowerShell y CMD, con el entorno virtual activo. En Windows, si la eñe o el acento del argumento llegan mal, abre Windows Terminal o, en esa ventana, corre `chcp 65001` antes de escribir el gasto.

El archivo se llama `gastos.json` y aparece en la carpeta actual. Si lo corres desde otra carpeta, el JSON se crea ahí.

| Comando | Qué devuelve |
| --- | --- |
| sin argumentos | La ayuda de abajo |
| `agregar <descripcion> <monto> <categoria> [fecha]` | `Listo: ...` o el mensaje de error |
| `listar` | Una línea por gasto, o `"No hay gastos registrados."` |
| `total` | `Total: $0.00` si no hay nada |
| `resumen` | Lo mismo que `formatear_resumen` |
| `categoria <nombre>` | El total de esa categoría y sus líneas, o `"No hay gastos en alimentos."` |
| cualquier otra cosa | `"No reconozco ese comando. Escribe el programa sin argumentos para ver la ayuda."` |

La ayuda, tal cual, con estos saltos de línea:

```text
Comandos:
  agregar <descripcion> <monto> <categoria> [fecha]
  listar
  total
  resumen
  categoria <nombre>
```

Si `agregar` no trae 3 o 4 datos después del comando:

```text
Uso: agregar <descripcion> <monto> <categoria> [fecha]
```

Si el monto no se puede convertir a número, por ejemplo `abc`:

```text
El monto no es un número: abc
```

Si `categoria` no trae el nombre:

```text
Uso: categoria <nombre>
```

El comando se acepta en cualquier combinación de mayúsculas. `AGREGAR` es `agregar`. La categoría del comando también se normaliza: `Alimentos` busca `alimentos`.

Una línea de `listar`, y el detalle de `categoria`, tienen esta forma:

```text
2026-10-01  Café  $45.50  alimentos
```

La cabecera de `categoria` es `alimentos: $45.50`. Cuando `agregar` funciona, la respuesta empieza por `Listo: ` y sigue con esa misma línea.

## En qué orden implementarlo

Las pruebas no te obligan a ir en este orden, pero cada paso se apoya en el anterior:

1. `crear_gasto`, sin tocar archivos.
2. `guardar_gastos` y `cargar_gastos`.
3. `agregar_gasto`.
4. `total`, `total_por_categoria` y `filtrar_por_categoria`.
5. `formatear_resumen`.
6. `main`.

Corre las pruebas de una función antes de pasar a la siguiente. Con el entorno activo, el comando es el mismo en macOS, Linux y Windows:

```text
pytest modulos/08-proyecto-final/test_ejercicios.py::test_crear_gasto_normaliza
```

## Cuando termine el curso

Si quieres seguir con este mismo programa, tres ampliaciones cortas y útiles: un comando para borrar un gasto, un filtro por mes y exportar a CSV. Ninguna está en las pruebas. El curso, con el resumen en verde, ya está completo.

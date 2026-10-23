# Semana 6. Funciones

Llevas seis semanas usando `def`. Esta semana se mira la herramienta con calma: qué es un parámetro, por qué `print` no sustituye a `return`, y el error de Python que más se repite en el mundo real.

## Anatomía

```python
def saludar(nombre: str, formal: bool = False) -> str:
    """Devuelve un saludo para nombre."""
    if formal:
        return f"Buenos días, {nombre}."
    return f"Hola, {nombre}."
```

- `nombre` y `formal` son **parámetros**: los nombres que usa la función por dentro.
- Al llamarla, `saludar("Evelyn", formal=True)`, esos valores son **argumentos**.
- `formal=False` es un valor por defecto. Quien llama puede omitirlo.
- `-> str` es una anotación: una nota de que el resultado es texto. Python no la exige al correr. Puedes pasar un número donde dice `str` y el programa no se detiene por la nota; se detendrá, si acaso, cuando intente usar ese número como texto.
- La docstring, entre comillas triples, es la explicación que ves al escribir `help(saludar)`.

Los argumentos se pueden pasar por posición o por nombre. Los que tienen nombre pueden ir en cualquier orden, detrás de los posicionales:

```python
saludar("Evelyn")
saludar("Evelyn", True)
saludar("Evelyn", formal=True)
```

## return no es print

```python
def duplicar(numero):
    print(numero * 2)

resultado = duplicar(4)
```

En pantalla se ve `8`. `resultado` vale `None`, porque no hubo `return`. Las pruebas de todo el curso miran el valor devuelto. Si una función "se ve bien" en la terminal y la prueba falla, casi siempre imprimiste en lugar de devolver.

Una función sin `return` devuelve `None`. A veces es lo correcto, cuando su trabajo es guardar un archivo (semana 7) y no hay nada que entregar.

## Alcance

Un nombre creado dentro de la función vive ahí. Afuera no existe.

```python
def cuota(total):
    parte = total / 2
    return parte

# parte, aquí, da NameError
```

Si quieres que el de afuera se entere, devuelve el valor. No vamos a usar `global`. Esconder un dato en una variable global hace que el programa dependa de un orden invisible.

## El valor por defecto se calcula una vez

Esto parece inocente y no lo es:

```python
def anotar(mensaje, notas=[]):
    notas.append(mensaje)
    return notas
```

El `[]` no se crea en cada llamada. Se crea **una vez**, cuando Python lee el `def`, y todas las llamadas que no pasen lista comparten esa misma lista.

```python
anotar("comprar café")  # ["comprar café"]
anotar("estudiar")      # ["comprar café", "estudiar"]  sorpresa
```

La forma segura es usar `None` como señal de "no me pasaron nada" y crear la lista adentro:

```python
def anotar(mensaje, notas=None):
    if notas is None:
        notas = []
    notas.append(mensaje)
    return notas
```

Compara con `is None`, no con `== None`. `None` es un solo objeto, y `is` pregunta si es ese mismo objeto.

Si quien llama sí pasa una lista, se modifica esa lista y se devuelve. Eso está bien: te la prestaron para que le agregues el mensaje. Lo que no está bien es compartir una lista que la persona nunca vio.

Cualquier valor mutable (`list`, `dict`, `set`) tiene este problema como valor por defecto. Los números, los textos y `None` no, porque no se modifican por dentro.

## *args y **kwargs

A veces no sabes cuántos textos vas a pegar:

```python
def unir(*palabras, separador=" "):
    return separador.join(palabras)

unir("hola", "Evelyn")                  # "hola Evelyn"
unir("2026", "10", "23", separador="-") # "2026-10-23"
```

`*palabras` junta los argumentos posicionales en una tupla. El parámetro que va después tiene que llamarse por su nombre, porque si no Python no sabe dónde termina la tupla.

`**datos` junta los argumentos con nombre en un diccionario. No hay un ejercicio que lo exija. Vas a verlo en código ajeno: `def f(*args, **kwargs)`.

## Las funciones son valores

Puedes guardar una función en una variable, pasarla a otra función y devolverla.

```python
def aplicar_a_cada(funcion, valores):
    return [funcion(valor) for valor in valores]

aplicar_a_cada(str.upper, ["hola", "eva"])  # ["HOLA", "EVA"]
```

`str.upper` sin paréntesis es la función. `str.upper("hola")` es la llamada. La diferencia es la misma de la semana 2.

Una función puede fabricar otra. La de adentro recuerda los nombres de la de afuera que necesita. A eso se le llama clausura, pero la idea cabe en una frase: la función devuelta se queda con el prefijo.

```python
def crear_saludo(prefijo):
    def saludar_con_prefijo(nombre):
        return f"{prefijo}, {nombre}"
    return saludar_con_prefijo

hola = crear_saludo("Hola")
hola("Evelyn")  # "Hola, Evelyn"
```

`hola` sigue funcionando aunque `crear_saludo` ya terminó. Se llevó `prefijo` consigo.

`Callable[[str], str]` en una anotación significa "una función que recibe un texto y devuelve un texto". `Callable[[], str]` no recibe nada y devuelve un texto. Es una nota, igual que `-> str`.

## Los ejercicios

| Función | Qué practica |
| --- | --- |
| `saludar` | Un parámetro con valor por defecto |
| `con_iva` | Otro valor por defecto, y una lista nueva |
| `estadisticas` | Devolver varios datos en un diccionario |
| `unir` | `*palabras` |
| `aplicar_a_cada` | Recibir una función |
| `crear_saludo` | Devolver una función |
| `elegir` | Sacar una función de un diccionario y llamarla |
| `anotar` | El defecto mutable, hecho bien |

# Semana 5. Listas y diccionarios

Hasta ahora cada dato tenía su nombre. Una lista guarda varios valores en orden. Un diccionario guarda pares de llave y valor: el nombre de una persona y su teléfono, una palabra y cuántas veces salió.

## Listas

```python
compra = ["pan", "leche", "huevos"]
compra[0]       # "pan"
compra[-1]      # "huevos"
len(compra)     # 3
"leche" in compra
```

Los índices y las rebanadas funcionan como en el texto. Una rebanada de lista es una **lista nueva**:

```python
compra[1:]   # ["leche", "huevos"]
```

`sin_extremos` es esa idea: quédate con el medio.

La lista sí se puede modificar:

```python
compra.append("café")   # agrega al final
ultimo = compra.pop()   # quita el último y lo devuelve
compra.insert(0, "agua")
```

## Dos nombres, la misma lista

Este es el bug que más confunde al principio:

```python
compra = ["pan", "leche"]
otra = compra
otra.append("huevos")
```

`compra` también tiene `"huevos"`. `otra = compra` no copia: las dos etiquetas apuntan a la misma lista.

```python
copia = compra.copy()
copia.append("tortillas")
# compra no cambia
```

`copy` es superficial. Si la lista guarda diccionarios, la lista nueva es otra, pero los diccionarios de adentro siguen siendo los mismos. En este módulo no vamos a anidar tanto. Sí vamos a cuidar de no modificar la lista que nos pasaron, salvo que la docstring lo pida. `agregar_unico` devuelve una copia y deja la original quieta.

## Tuplas

Una tupla es una secuencia ordenada que **no** se puede modificar.

```python
horario = (2, 15)
horas, minutos = horario
```

La semana 1 ya devolvió `(horas, minutos)`. Sirve para "estos dos datos van juntos". Una tupla de un solo elemento lleva coma: `(1,)`. Sin la coma, `(1)` es solo el número 1 entre paréntesis.

Puedes usar una tupla como llave de un diccionario. Una lista, no: la lista puede cambiar, y las llaves tienen que ser estables.

## Diccionarios

```python
telefono = {"ana": "555", "eva": "111"}
telefono["ana"]          # "555"
telefono["luz"] = "222"  # agrega o reemplaza
"ana" in telefono        # True. in mira las llaves, no los valores
telefono.get("luz", "no encontrado")
```

Si pides `telefono["nadie"]` y esa llave no está, obtienes `KeyError`. `.get` evita el golpe y te deja elegir qué devolver.

Desde Python 3.7 el diccionario recuerda el orden en que agregaste las llaves. Puedes confiar en eso.

Recorrerlo:

```python
for nombre, numero in telefono.items():
    print(nombre, numero)
```

`keys()` son las llaves. `values()`, los valores. Casi siempre quieres `items()`.

Para contar palabras, el patrón es: si la palabra ya está, súmale uno; si no, empieza en cero.

```python
conteo = {}
for palabra in frase.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
```

`lower` basta para el español de este curso. Existe `casefold`, un poco más estricto con otros idiomas. No lo necesitas aquí.

Unir dos diccionarios sin modificarlos, desde Python 3.9:

```python
base = {"a": 1, "b": 2}
extra = {"b": 9, "c": 3}
combinado = base | extra
# {"a": 1, "b": 9, "c": 3}
```

Si una llave está en los dos, gana el de la derecha. `base` sigue igual. `base |= extra` sí actualiza `base`.

## Comprensiones

Cuando el ciclo solo arma una lista nueva, se puede escribir en una línea. Es lo mismo que el ciclo, más corto:

```python
mayores = [numero for numero in numeros if numero > 5]
```

Léelo de izquierda a derecha: "qué guardo", "de dónde", "con qué condición". Si el filtro o el cálculo no caben en la cabeza de un vistazo, escribe el ciclo. Las dos formas son Python de verdad.

Un diccionario también se puede armar así:

```python
invertido = {valor: clave for clave, valor in original.items()}
```

Si dos llaves tenían el mismo valor, se queda la última. `invertir_diccionario` avisa de eso en la docstring.

## sorted

`sorted(nombres)` devuelve una lista nueva, ordenada, y no toca la original. El orden es el de Unicode: las mayúsculas y las tildes no salen como en un diccionario de papel. Para ignorar mayúsculas se usa `sorted(nombres, key=str.lower)`. No hay un ejercicio de ordenar, pero lo vas a querer.

## Los ejercicios

| Función | Idea |
| --- | --- |
| `primer_y_ultimo` | El primero y el último, también si solo hay uno |
| `sin_extremos` | La rebanada del medio |
| `agregar_unico` | Una copia que no repite el valor |
| `promedio` | La media, y un error si la lista está vacía |
| `contar_palabras` | Un diccionario de frecuencias |
| `invertir_diccionario` | Los valores pasan a ser llaves |
| `filtrar_mayores` | Una comprensión, o un ciclo |
| `combinar` | `base \| extra` |

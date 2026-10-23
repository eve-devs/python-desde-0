# Semana 4. Ciclos

Un ciclo repite un bloque mientras haga falta. Vas a sumar del 1 al n, armar la tabla del 2 y recorrer un texto letra por letra. A los ciclos también se les dice bucles.

## for y range

`for` camina por una secuencia: un texto, un rango de números, más adelante una lista.

```python
for numero in range(1, 4):
    print(numero)
```

Eso imprime 1, 2 y 3. **No imprime el 4.** `range(inicio, fin)` se detiene justo antes de `fin`. Es el mismo convenio que las rebanadas de texto.

Otras formas:

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 11)    # 1 al 10, útil para la tabla de multiplicar
range(0, 10, 2) # 0, 2, 4, 6, 8  (el tercer número es el paso)
```

`range(inicio, fin)` con `inicio > fin` no da error: simplemente no entra al ciclo. Por eso `contar_pares(5, 1)` puede devolver 0 sin un `if` extra.

## while

`while` repite mientras la condición sea verdadera. Sirve cuando no sabes cuántas vueltas serán.

```python
restante = 3
while restante > 0:
    restante = restante - 1
```

Si olvidas cambiar `restante`, el ciclo no termina. Para cortarlo: Ctrl+C, en macOS, Linux y Windows. En la terminal eso lanza `KeyboardInterrupt` y recuperas el control.

En estos ejercicios el `for` alcanza. Úsalo.

## break y continue

`break` sale del ciclo. `continue` salta a la vuelta siguiente.

```python
for numero in range(1, 10):
    if numero % 2 == 0:
        continue
    if numero > 7:
        break
    print(numero)
```

Eso imprime los impares 1, 3, 5 y 7, y se detiene al pasar de 7.

`primer_indice` es un buen lugar para `return` dentro del `for`: en cuanto encuentras el carácter, ya no hace falta seguir. Un `return` dentro de un ciclo termina la función entera, no solo la vuelta.

## enumerate

A veces necesitas el valor y también su posición. `enumerate` te da las dos cosas, empezando en 0:

```python
for indice, caracter in enumerate("hola"):
    print(indice, caracter)
```

```text
0 h
1 o
2 l
3 a
```

Si quieres empezar en 1: `enumerate(texto, start=1)`.

## Acumular

El patrón de esta semana es: crea un resultado vacío, y en cada vuelta agrégale algo.

```python
def suma_del_1_al(n):
    total = 0
    for numero in range(1, n + 1):
        total = total + numero
    return total
```

`total += numero` es lo mismo que `total = total + numero`.

Para armar un texto, no sumes letras una por una si la cadena va a crecer mucho. Junta los caracteres en una lista y al final usa `"".join(...)`. El `str` no se puede modificar, así que cada suma copia todo lo anterior. La semana 2 ya avisó de esto. `invertir` es un buen momento para practicarlo, aunque el texto del ejercicio sea corto.

## Recorrer un texto

```python
vocales = set("aeiouáéíóúü")
total = 0
for caracter in "Árbol".lower():
    if caracter in vocales:
        total += 1
```

`set` es una bolsa sin repetidos y sin orden. Preguntar `caracter in vocales` es directo. No hace falta estudiarlo a fondo: aquí solo es una forma clara de decir "estas son las vocales". Las listas llegan la semana que viene.

`contar_vocales` cuenta a, e, i, o, u, con tilde, y también la ü de "pingüino". La y no cuenta. Pasa el texto a minúsculas una vez, o cada carácter, antes de comparar.

## FizzBuzz

Es un juego de contar en voz alta:

- si el número es múltiplo de 3, dices "Fizz";
- si es múltiplo de 5, dices "Buzz";
- si es múltiplo de los dos (o sea, de 15), dices "FizzBuzz";
- si no, dices el número.

El orden de los `if` importa. 15 es múltiplo de 3, así que si preguntas primero por el 3 nunca llegas a "FizzBuzz". Pregunta por el 15 primero.

## Lo que este módulo no usa

Existe `for` / `else`: el `else` corre si el ciclo terminó sin `break`. Se malinterpreta con facilidad y no lo usamos.

Cuando un método ya hace el trabajo (`str.count`, `sum`, una rebanada al revés), en la vida real úsalo. En los ejercicios de esta semana el ciclo es el objetivo, aunque exista un atajo. La docstring te lo recuerda.

## Los ejercicios

| Función | Ciclo |
| --- | --- |
| `suma_del_1_al` | Acumula 1 + 2 + ... + n |
| `contar_pares` | Cuenta pares entre dos extremos, inclusive |
| `tabla_de_multiplicar` | Diez filas con un formato exacto |
| `contar_vocales` | Recorre el texto, vocales del español |
| `invertir` | Arma el texto al revés con un ciclo |
| `factorial` | 5! = 120, y 0! = 1 |
| `fizzbuzz` | El juego, hasta n |
| `primer_indice` | La primera posición de un carácter, o -1 |

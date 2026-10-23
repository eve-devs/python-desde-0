# Python desde cero

Cuaderno de estudio para aprender Python 3 por tu cuenta, desde la primera variable hasta un programa pequeño que sí puedes usar: un registro de gastos.

El curso está pensado como **una semana por módulo**. Si un tema te pide más tiempo, quédate ahí. El ritmo es tuyo. Las pruebas automáticas te dicen qué falta; no hay calificación.

Este material está escrito para **Python 3.12 y 3.13**. No uses tutoriales de Python 2: la división, `print` y muchas otras cosas cambiaron.

## Cómo está organizado

Cada semana vive en su carpeta, dentro de `modulos/`:

| Archivo | Para qué sirve |
| --- | --- |
| `notas.md` | La explicación. Léela antes de programar. |
| `ejercicios.py` | Las funciones que vas a completar. Busca los `# TODO`. |
| `test_ejercicios.py` | Las pruebas. Cuando pasan, el ejercicio está bien. |
| `solucion.py` | Una solución de referencia. Mírala después de intentar, no antes. |

Las funciones de la semana 1 ya tienen forma de función (`def ...`) aunque las funciones se explican a fondo en la semana 6. Al principio basta con completar el cuerpo y devolver un resultado con `return`.

La carpeta `soporte/` no es una lección: las pruebas la usan para elegir qué archivo cargar.

## Progreso

Cuando termines un módulo, cambia `☐` por `☑` en esta tabla.

| Semana | Módulo | Qué vas a aprender | Listo |
| --- | --- | --- | --- |
| 1 | [Variables y tipos](modulos/01-variables-y-tipos/notas.md) | Guardar datos y operar con números | ☐ |
| 2 | [Texto](modulos/02-strings/notas.md) | Leer, recortar y armar textos | ☐ |
| 3 | [Condicionales](modulos/03-condicionales/notas.md) | Tomar decisiones | ☐ |
| 4 | [Ciclos](modulos/04-ciclos/notas.md) | Repetir sin copiar y pegar | ☐ |
| 5 | [Listas y diccionarios](modulos/05-listas-y-diccionarios/notas.md) | Guardar varios datos juntos | ☐ |
| 6 | [Funciones](modulos/06-funciones/notas.md) | Encapsular una idea con calma | ☐ |
| 7 | [Archivos y errores](modulos/07-archivos-y-errores/notas.md) | Guardar información y reaccionar cuando algo falla | ☐ |
| 8 | [Proyecto final](modulos/08-proyecto-final/notas.md) | Un registro de gastos en la terminal | ☐ |

## Instalar Python 3.12+ en una Mac mini M4

La Mac mini M4 usa un chip Apple Silicon. El Python que instales tiene que ser la versión para ese chip (`arm64`), no la versión Intel.

macOS no trae un Python actual. Si al escribir `python3` la Mac te ofrece instalar las herramientas de Xcode, cancela: eso no es el Python de este curso.

Cierra y vuelve a abrir la Terminal después de instalar.

### Opción A. Instalador oficial

1. Entra a [python.org/downloads/macos](https://www.python.org/downloads/macos/).
2. Descarga el instalador **macOS 64-bit universal2** de Python 3.13 o, si prefieres, de 3.12. El instalador universal2 sirve para la Mac mini M4. No uses un instalador que diga solo "Intel".
3. Ábrelo y acepta los pasos.
4. Comprueba:

```bash
python3 --version
python3 -c "import platform; print(platform.machine())"
```

Tiene que decir `Python 3.12` o mayor, y `arm64`.

Si `platform.machine()` imprime `x86_64`, se está usando un Python de Intel bajo Rosetta. Reinstala el universal2 y revisa la Terminal: clic derecho en Terminal.app → Obtener información → la casilla **Abrir con Rosetta** debe estar desmarcada.

El instalador también deja un comando con el número de versión, por ejemplo `python3.13`. Si `python3 --version` no es el que acabas de instalar, usa ese comando con número en los pasos de abajo.

### Opción B. Homebrew

Si ya usas Homebrew:

```bash
brew install python@3.13
python3.13 --version
python3.13 -c "import platform; print(platform.machine())"
```

En una Mac con chip Apple, Homebrew instala los programas en `/opt/homebrew/bin` (no en `/usr/local`, que es la ruta de las Mac Intel). Si el comando no se encuentra, abre una terminal nueva. La primera vez, el instalador de Homebrew muestra dos líneas para agregar al `PATH`: cópialas si todavía no lo has hecho.

También aquí la arquitectura tiene que ser `arm64`.

## Crear el entorno virtual

Un entorno virtual es una carpeta del proyecto con su propio Python y sus propios paquetes. Así no mezclas este curso con otros programas.

Desde la carpeta del repositorio (cambia la ruta por la tuya):

```bash
cd ~/ruta/a/python-desde-0
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Si instalaste 3.12 y el comando se llama `python3.12`, usa ese en la línea de `venv`.

Cuando el entorno está activo, el prompt empieza con `(.venv)` y `python` apunta al Python del curso. Compruébalo:

```bash
python --version
```

Cada vez que abras una terminal nueva, vuelve a activarlo con `source .venv/bin/activate`. Para salir del entorno: `deactivate`.

La carpeta `.venv/` no se sube a GitHub. Ya está en `.gitignore`.

## Cómo estudiar un módulo

1. Lee `notas.md` y prueba los ejemplos en el intérprete.
2. Abre `ejercicios.py` y sustituye cada `# TODO`.
3. Corre las pruebas de ese módulo.
4. Cuando salgan en verde, marca la casilla de la tabla.
5. Si llevas un rato atorada, mira `solucion.py` y vuelve a explicar la idea con tus palabras. Copiarla sin leerla no enseña.

Para abrir el intérprete dentro de un módulo:

```bash
cd modulos/01-variables-y-tipos
python
```

```python
import ejercicios
ejercicios.suma(35, 18)
```

Hasta que completes la función, vas a ver `NotImplementedError`. Es la señal de que ahí falta tu código.

Puedes salir del intérprete con `exit()` o con Control+D.

## Cómo correr las pruebas

Con el entorno virtual activo, desde la raíz del repositorio:

```bash
pytest modulos/01-variables-y-tipos
```

Eso prueba **tus** ejercicios. Al principio fallan: el rojo es el mapa de lo que falta, no una regañada.

Para una sola prueba:

```bash
pytest modulos/03-condicionales/test_ejercicios.py::test_signo_cero
```

Para correr **todas** las pruebas del curso contra tus ejercicios:

```bash
pytest
```

### Correr las pruebas contra las soluciones

La variable de entorno `PYTHON_DESDE_0_SOLUCION` cambia el archivo que importan las pruebas. Estos valores activan `solucion.py`: `1`, `true`, `yes`, `si`, `sí`, `solucion`.

```bash
PYTHON_DESDE_0_SOLUCION=1 pytest modulos/01-variables-y-tipos
PYTHON_DESDE_0_SOLUCION=1 pytest
```

Sin la variable, o con cualquier otro valor, se usa `ejercicios.py`.

La elección se hace al arrancar `pytest`. No se puede cambiar a mitad de una misma corrida.

En GitHub Actions las pruebas corren solas, en Python 3.12 y 3.13, siempre con `PYTHON_DESDE_0_SOLUCION=1`. El workflow está en `.github/workflows/pruebas.yml`. Tú, en tu máquina, ves tus ejercicios. El repositorio, en la nube, comprueba que las soluciones sigan siendo válidas.

## Mapa del repositorio

```text
.
├── README.md
├── requirements-dev.txt
├── pytest.ini
├── .gitignore
├── .github/workflows/pruebas.yml
├── soporte/
│   ├── cargar.py
│   └── test_contrato.py
└── modulos/
    ├── 01-variables-y-tipos/
    ├── 02-strings/
    ├── 03-condicionales/
    ├── 04-ciclos/
    ├── 05-listas-y-diccionarios/
    ├── 06-funciones/
    ├── 07-archivos-y-errores/
    └── 08-proyecto-final/
```

## Una nota sobre el dinero y los decimales

En la semana 1 vas a ver que `0.1 + 0.2` no da exactamente `0.3`. No es un fallo tuyo. Los `float` de Python (y de casi todos los lenguajes) usan un formato binario. Para este curso alcanza con `round(numero, 2)` cuando hablamos de precios. Un sistema de cobros real suele guardar los centavos como enteros, o usar el módulo `decimal`. Eso puede esperar.

Buena semana 1.

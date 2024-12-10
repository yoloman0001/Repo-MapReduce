# Repo-MapReduce :elephant:

## :book: Descripción 

Este repositorio realiza varios ejercicios sobre un dataset de ventas usando clases `mapper.py` y `reducer.py` modificadas según los requisitos de cada ejercicio.

## :arrow_down: Trabajar en local con el repositorio

Clona este repositorio en tu máquina local usando la URL o usando una clave SSH.

Con URL
~~~
git clone https://github.com/yoloman0001/Repo-MapReduce.git
~~~

Con SSH key
~~~
git clone git@github.com:yoloman0001/Repo-MapReduce.git
~~~

## :open_file_folder: Estructura

El repositorio está dividido en carpetas; una por ejercicio, cada carpeta contiene el mapper, el reducer y un `.txt` con los resultados:
- `exercicio1_1`
- `exercicio1_2`
- `exercicio1_3`
- `exercicio1_4`
- `exercicio1_5`

## :speech_balloon: Enunciados

### Ejercicio 1.1

**Mejora el código de modo que si encuentra alguna línea con formato no adecuado la descarte y siga trabajando con la línea siguiente.**

### Ejercicio 1.2

**Redefine el mapper y el reducer de modo que devuelvan un archivo con el total de ventas por categoría.**

### Ejercicio 1.3

**Redefine el mapper y el reducer de modo que se obtenga la venta más alta para cada tipo de pago de las registradas en todo el archivo.**

**Consulta el resultado: ¿a qué puede deberse?**

Al ver los resultados, se ve que todos los valores son iguales. Con esto se puede deducir que; al generarse los datos originales, se puso un tope al coste de venta.

### Ejercicio 1.4

**Modifica el ejercicio anterior para que el resultado de la ejecución sea el máximo absoluto de todas las ventas registradas.**

### Ejercicio 1.5

**Redefine el mapper y el reducer de modo que se obtenga el total de ventas.**

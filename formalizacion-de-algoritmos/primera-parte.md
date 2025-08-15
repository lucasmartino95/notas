# Introducción
En este documento se detallan **temas fundamentales** de programación, como: 

- **Algoritmo**
- **Tipos de datos**
- **Variables y constantes** 
- **Operadores**
- **Estructuras condicionales**
- **Trabajar con porcentajes** 

Los ejemplos de código estarán escritos en **Python**.

## Algoritmo

Es un **conjunto de pasos lógicos y estructurados** que nos permiten dar solución a un problema.

### Estructura de un algoritmo

- **Entrada**: Es la introducción de datos para ser transformados.
- **Proceso**: Es el conjunto de operaciones a realizar para dar solución a un problema.
- **Salida**: Son los resultados obtenidos a través del proceso.

### Descomposición de un algoritmo

1. **Definición del problema**: Establecer resultados y objetivos para saber si los resultados que se tienen son suficientes para lograr los fines propuestos.
2. **Análisis**: Organizar los datos de manera tal que se puedan usar en los cálculos siguientes.
3. **Diseño**: Solucionar un problema, aplicando conocimientos y datos existentes.
4. **Verificación a prueba de escritorio**: Comprobar que el algoritmo sirve o requiere modificarse.

### Cómo representar un algoritmo

Se puede representar un algoritmo a través de diagramas o código.

- **Diagrama**: [De flujo (flowchart)](https://es.wikipedia.org/wiki/Diagrama_de_flujo) o [Nassi-Shneiderman](https://es.wikipedia.org/wiki/Diagrama_Nassi-Shneiderman).
- **Código**: [Pseudocódigo](https://es.wikipedia.org/wiki/Pseudoc%C3%B3digo) o lenguaje real.

## Tipos de datos

En programación existen diferentes tipos de datos, los cuales indican **qué tipo de información** representa un valor.

#### Numéricos
- **Entero**: 7815158, 17, -2
- **Punto flotante**: 148562.4, 3.141592, -1.5

#### Alfanuméricos
- **Carácter simple**: "a", "@", "2"
- **Cadena de caracteres**: "Hola", "@", "Lo que sea"

#### Lógicos
- **Verdadero**: true
- **Falso**: false

Para saber el tipo de dato de un valor, podemos usar la función `type()`:

```python
print(type(5)) # Devolvera <class 'int'>
print(type("Hola")) # Devolvera <class 'str'>
print(type(True)) # Devolvera <class 'bool'>
```

## Variables y constantes

Una **variable** es un espacio en la memoria que **guarda un valor que puede cambiar** durante la ejecución de un programa.

Una **constante** es un valor que **no cambia** durante la ejecución de un programa.

### Variables en Python

 ```python
 # Crea una variable llamada var y guarda el valor 1
var = 1
print(var) # Imprime el valor de var

# Toma el valor de var, sumale 1 y vuelvelo a guardar en la variable var
var = var + 1
print(var) # Imprime el nuevo valor de var
 ```

### Constantes en Python

En Python no existen las constantes, sin embargo se puede seguir una convención para mantener el código legible. Se trata de escribir el **nombre de la constante en mayúsculas**.

```python
TITULO_CURSO = "curso introducción"
```

#### Nota sobre variables y constantes

Si **no necesitamos** utilizar el valor de una variable o constante más de una vez, es recomendable **no crear variables** ya que nos ahorramos ocupar espacio en la memoria, lo cual hace que nuestro programa tenga mejor rendimiento.

## Operadores

### Aritméticos
Son los **símbolos** que representan las acciones fundamentales que se realizan con números:

```python
print(9 + 5) # Suma
print(9 - 5) # Resta
print(9 * 5) # Multiplicación
print(9 / 5) # División
print(9 // 5) # Devuelve el cociente entero de dos números
print(9 ** 5) # Potenciación
print(9 % 5) # Devuelve el resto del cociente entre números
```

Los **operadores aritméticos** siguen la [jerarquía de prioridades](https://edu.gcfglobal.org/es/algebra/orden-de-las-operaciones/1/), es decir, algunos operadores actúan antes que otros. Por ejemplo:

```python
2 + 3 * 5
```

Primero se realiza la multiplicación, y luego la suma, por lo que quedaría:

```python
2 + 15 # Resultado 17
```

### De cadena y de replicación

El signo + (más), al ser aplicado a dos cadenas, se convierte en un **operador de concatenación**:

```python
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + fnam + " " + lnam + ".")
```

El signo * (asterisco) al ser aplicado a una cadena y a un número, se convierte en un **operador de replicación**:

```python
print("James" * 3) # Imprimirá JamesJamesJames
print(3 * "an") # Imprimirá ananan
print(5 * "2") # Imprimirá "22222"
```

### De incremento - decremento

En Python no existe el operador ++ ni --, para lograr el mismo resultado, se utilizan **operadores compuestos**:

```python
x = 5
x = x + 1 # O bien se puede utilizar: x += 1
print(x)
```

[x] Falta completar

### Relacionales o de comparación

Los operadores relacionales **toman números y devuelven como resultado un valor lógico**, es decir, verdadero o falso.

[x] Falta completar

## Estructuras condicionales

[x] Falta completar

## Trabajar con porcentajes

Los **porcentajes** son una forma de **expresar un número como una fracción de 100**. Por ejemplo, el 50% es igual a 50/100 o 0.5.

```python
# Convertir un número a porcentaje
numero = 0.75
porcentaje = numero * 100
print(porcentaje)

# Encontrar el porcentaje de un número utilizando regla de tres simple
numero = 200
porcentaje = 15
resultado = (numero * porcentaje) / 100 # El 15% de 200 es 30
print(resultado) # 30

# Incrementar un número por un porcentaje
numero = 100
porcentaje = 20
incremento = (numero * porcentaje) / 100 # El 20% de 100 es 20
nuevo_numero = numero + incremento # 100 + 20 = 120
print(nuevo_numero) # 120
```
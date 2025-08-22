# Introducción

Una computadora es un **dispositvo electrónico** capaz de procesar enormes secuencias de instrucciones muy velozmente.

Las computadoras eran utilizadas para fines específicos y ocupaban grandes espacios físicos. Con el avance de la electrónica las computadoras **se volvieron más pequeñas y más poderosas**, también más accesibles economicamente ya que el coste de producción también se redujo.

Y el uso de las computadoras se volvió **más generalizado**.

Toda computadora está formada por dos componentes: **hardware** y **software**.

## Hardware

Son los **componentes electrónicos** que juntos forman lo que hoy conocemos como computadora.

## Software

Son los **programas** que se ejecutan en el hardware de una computadora.

#### Programa
Es una serie de instrucciones que realiza alguna tarea.

## Arquitectura actual de computadoras

Las computadoras convencionales siguen la arquitectura propuesta a principio de los años 40 por [Von Neumann](https://es.wikipedia.org/wiki/Arquitectura_de_Von_Neumann):

- El procesador central o CPU.
- La memoria en la que residen datos y programas.
- Los dispositivos de entrada y salida o periféricos.

Toda la información viaja a través de los distintos componentes en **sistema binario**, es decir con ceros y unos. También se puede referenciar el cero con "apagado" y el uno con "encendido".

## Procesador

Es el responsable de **ejecutar programas**.

El procesador tiene una **unidad de control** que es la responsable de procesar cada instrucción y transferir información entre la **unidad aritmética lógica (ALU en inglés)** y la **memoria RAM**.

La **unidad aritmética lógica** se encarga de realizar operaciones aritméticas, operaciones lógicas y operaciones de comparación. Recibe los datos de los registros del procesador, procesa las instrucciones y devuelve los resultados.

Los **registros** del procesador son un tipo de memoria interna. Es donde se almacena momentaneamente algún dato específico. Por ejemplo, guarda la dirección de la celda de memoria en donde se debe ejecutar una instrucción.

### Un procesador está compuesto por

#### Núcleos

Un núcleo es un bloque que ejecuta instrucciones

Podemos tener uno o más núcleos en nuestro procesador. Esto quiere decir que si tenemos por ejemplo cuatro núcleos, podemos ejecutar un programa en cada núcleo. Esto se llama **multitarea**.

#### Hilos

Los hilos son una versión virtual de un núcleo. Podemos definir un hilo de procesamiento como el **flujo de control de datos de un programa**. Es un medio que permite administrar las tareas de un procesador y de sus diferentes núcleos de una forma más eficiente. **Divide la tarea en porciones**, lo que quiere decir que cada hilo se encarga de una parte concreta de dicho programa. Estas porciones se llaman **subprocesos o threads**.

Por cada núcleo existen dos hilos, aunque puede haber excepciones.

Se puede decir que los hilos **convencen** al usuario y a la PC de que se pueden realizar más tareas al mismo tiempo.

Para utilizar múltiples núcleos y sus hilos **es necesario que los programas se comuniquen con cada uno de los núcleos**.

#### Reloj o clock

El reloj o clock es un **componente del microprocesador** que emite pulsos eléctricos a intervalos constantes llamados ciclos, estos **ciclos marcan el ritmo** que ha de seguirse para la realización de cada paso que consta la instrucción. La velocidad de reloj indica cuántos ciclos de procesamiento por segundo puede ejecutar una CPU teniendo en cuenta todas sus unidades de procesamiento (núcleos).

**Esta velocidad se mide en GHz**, los cuales  se traducen de esta manera, por ejemplo:

3.7GHz = 3.700 millones de instrucciones por segundo.

### Overlock

El overlock es una técnica utilizada para **aumentar la frecuencia de reloj** de un componente electrónico, en este caso del procesador.

Una desventaja de utilizar esta técnica es que **aumenta el calor que emite el procesador**, ya que lo estamos forzando a trabajar más velozmente. También **reduce la vida útil del componente**.

## Memoria RAM

La memoria RAM está hecha de celdas, donde cada celda está identificada con un número. Es donde **se guardan los datos e instrucciones de nuestro programa** para que luego el procesador ejecute nuestro programa.

## Dispositivos de entrada y salida

El fin último de una computadora es ingresarle datos, que haga el procesamiento
y nos devuelva un resultado. Para esto, contamos con dispositivos de entrada y de salida.

Dispositivos de entrada:

- Teclado
- Mouse
- Micrófono

Dispositivos de salida:

- Monitor
- Auriculares
- Impresora

Dispositivos de entrada y salida:

- Pendrive
- Disco rígido o de estado sólido
- Pantalla táctil
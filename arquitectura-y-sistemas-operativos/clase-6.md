## Crear directorios

Para crear directorios, podemos usar ```mkdir```. Por ejemplo

```bash
mkdir -p {dir1, dir2}/subdir{1..3}
```

Otro ejemplo

```bash
mkdir -p {dir1,dir2}/{subdir1,subdir2,subdir3}
```

Si luego utilizamos ```tree``` nos mostrará la estructura de los directorios que creamos.

## Ver archivos

Para ver archivos desde la terminal, podemos usar el caomando `cat`. Por ejemplo: `cat /etc/passwd`

## Buscar cadenas dentro de un archivo

Podemos usar el comando `grep`. Por ejemplo: `grep -i vagrant /etc/passwd`. La `-i` significa que no distinga entre mayúsculas y minúsculas.
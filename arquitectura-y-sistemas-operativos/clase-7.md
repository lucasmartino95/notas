# Linux

### Permisos

Para dar permisos a un usuario podemos usar: `chmod u-x archivo`. Esto le da al usuario permiso de ejecución de un archivo. También podemos usar la notación octal (es la que usaremos).

Cuando hacemos `ls -l` cada directorio o archivo tendra esta información, por ejemplo: `drwxrwxrwx` o `-rwxrwxrwx`

- d: significa que es un directorio
- rwx: r significa **read**, w significa **write**, y x significa **ejecución**
- si hay un **-** significa que no tiene tal permiso, por ejemplo `drwxrw-rwx`, significa que el grupo no tiene permiso de ejecución.

Por ultimo, el primer rwx indica los **permisos del dueño**, el segundo rwx indica los **permisos del grupo**, y el tercer rwx indica los **permisos de otros usuarios**.

`chmod 775 nombre_archivo` (notación octal) o para hacerlo de forma recursiva: `chmod -R 755 nombre_directorio`. Esto le da permiso al dueño de leer, escribir y ejecutar, y al grupo y a otros usuarios solo permiso de leer y ejecutar.

Para cambiar el propietario y el grupo de un archivo podemos usar: `sudo chown nombre_propietario:nombre_grupo archivo` o para hacerlo de forma recursiva a un directorio `chown -R nombre_propietario:nombre_grupo nombre_dir/`
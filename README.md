# Objetivos:

Estamos haciendo un reproductor de música, para esto se debe crear el modulo que permite crear las listas de canciones. En estas listas colaborativas de al menos 2 usuarios, cada usuario puede colocar una canción a la vez, la lista se debe ir almacenando en un archivo CSV. Solo un usuario puede insertar una canción a la vez, pero la lectura no está restringida a accesos concurrentes. Los atributos de cada canción son: Título, Interprete, Álbum, Fecha en que se agregó, usuario que agregó y duración.

## Se pide

* En esta versión  se deben usar procesos independientes desde consola. Para mostrar el comportamiento debe crear un proceso que muestre en línea el estado de la lista y las dos últimas canciones agregadas.
* No permitir canciones repetidas

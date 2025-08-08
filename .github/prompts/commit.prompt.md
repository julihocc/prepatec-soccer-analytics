Instrucciones Detalladas para Commits
====================================


Verifica los Cambios Stageados
===============================

* Antes de commitear, asegúrate de que solo los archivos relevantes estén en el área de staging
* Usa `git status` para revisar los archivos stageados


Escribe un Mensaje de Commit Detallado
=======================================

El mensaje debe describir claramente *qué* cambiaste y *por qué*.

Usa el siguiente formato recomendado:

[source]
----
[Tipo de cambio]: Descripción breve

Explicación detallada del cambio realizado, incluyendo:
- Qué archivos fueron modificados.
- Qué problema resuelve o qué funcionalidad agrega.
- Contexto adicional si es necesario (por ejemplo, referencias a tareas o bugs).
- Si aplica, describe el impacto en otras partes del proyecto.
----


Ejemplo
=======

[source]
----
feat: agrega análisis de goles por equipo en datos_futbol

Se añadió una nueva función en analisis_goles.py que calcula la suma de goles por equipo usando el dataset de la Champions League. Esto permite visualizar patrones de rendimiento de equipos como Barcelona, Real Madrid y Manchester City. Se actualizó el notebook de la Semana 2 para incluir este análisis.
----


Realiza el Commit
=================

Ejecuta el comando:

[source,bash]
----
git commit
----

Se abrirá tu editor de texto para que escribas el mensaje siguiendo el formato anterior.


Revisa el Commit
================

Después de commitear, usa `git log -1` para verificar que el mensaje sea claro y completo.

*Recuerda:* Solo se deben commitear los cambios que estén en el área de staging. Si tienes archivos sin stagear, agrégalos con `git add <archivo>` antes de repetir el proceso.
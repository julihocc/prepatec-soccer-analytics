
INSTRUCCIONES DETALLADAS PARA COMMITS (EJECUCIÓN OBLIGATORIA, NO SOLO MOSTRAR)
===============================================================================



1. VERIFICA LOS CAMBIOS STAGEADOS (EJECUTA, NO SOLO MUESTRES)
-------------------------------------------------------------

- Antes de commitear, el agente debe ejecutar el comando `git status` y mostrar el resultado.
- Si no hay archivos en staging, el agente debe ejecutar `git add <archivo>` para agregar los archivos relevantes.
- El agente debe asegurarse de que solo los archivos correctos estén en staging antes de continuar.



2. ESCRIBE Y USA UN MENSAJE DE COMMIT DETALLADO (EJECUTA, NO SOLO MUESTRES)
----------------------------------------------------------------------------

El mensaje debe describir claramente *qué* cambiaste y *por qué*.
El agente debe redactar el mensaje siguiendo el formato recomendado y luego ejecutar el commit con ese mensaje.

Formato recomendado:

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


git commit

3. REALIZA EL COMMIT (EJECUTA, NO SOLO MUESTRES)
-------------------------------------------------

El agente debe ejecutar el comando de commit directamente, usando el mensaje detallado generado en el paso anterior.
No solo mostrar el comando, sino ejecutarlo realmente.



4. REVISA EL COMMIT (EJECUTA, NO SOLO MUESTRES)
------------------------------------------------

Después de commitear, el agente debe ejecutar `git log -1` y mostrar el resultado para verificar que el mensaje sea claro y completo.

*Recuerda:* Solo se deben commitear los cambios que estén en el área de staging. Si tienes archivos sin stagear, el agente debe agregarlos con `git add <archivo>` antes de repetir el proceso.

---

NOTA PARA AGENTES AUTOMATIZADOS:
--------------------------------
No basta con mostrar los comandos o el flujo en el chat. Debes ejecutar cada paso de staging, commit y verificación de manera automática y secuencial, asegurando que el commit quede registrado en el repositorio. Si algún paso falla, debes informar y sugerir la corrección.
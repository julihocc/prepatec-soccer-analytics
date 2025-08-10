# Prompt para Actualizar la Versión del Repositorio

Tu tarea es actualizar la versión del repositorio siguiendo las mejores prácticas de control de versiones y documentación profesional. Considera el siguiente contexto y requerimientos:

## Contexto
- Este repositorio es parte de un curso de Ciencia de Datos aplicada al Fútbol para estudiantes de preparatoria en México.
- El proyecto utiliza versiones semánticas (por ejemplo, 1.2.0).
- Toda la documentación y mensajes deben estar en español profesional, sin emojis.

## Instrucciones detalladas

1. **Identifica la versión actual** del repositorio (por ejemplo, en `pyproject.toml`, `setup.py`, `package.json` o archivos equivalentes).
2. **Determina el tipo de actualización**:
    - **Mayor**: Cambios incompatibles o nuevas funcionalidades importantes.
    - **Menor**: Nuevas funciones compatibles o mejoras.
    - **Parche**: Correcciones menores o ajustes sin impacto en la funcionalidad.
3. **Actualiza el número de versión** en todos los archivos relevantes.
4. **Registra los cambios** en el archivo de historial de cambios (`CHANGELOG.md`), siguiendo el formato:
    - Fecha
    - Nueva versión
    - Lista breve y clara de cambios realizados
5. **Realiza un commit** con un mensaje descriptivo en español, por ejemplo:  
    `Actualizar versión a 1.3.0: mejoras en visualización de datos`
6. **Verifica que la documentación y los archivos de configuración** reflejen la nueva versión.
7. **No incluyas emojis** en ningún mensaje, archivo o comentario.

## Ejemplo de commit
Actualizar versión a 2.0.0: incorporación de análisis de predicción de goles y mejoras en la estructura de datos
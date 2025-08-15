# CHANGELOG

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere al [Versionado Semántico](https://semver.org/lang/es/).

## 4.12.0 (2025-08-15)

### Agregado

- Solución completa del caso práctico del Bloque 1 con código ejecutable y documentado
- Solución completa del caso práctico del Bloque 2 con análisis pandas y visualizaciones
- Archivos de solución para referencia docente y validación de ejercicios
- Implementaciones de referencia que cumplen todos los criterios de evaluación

### Mejorado

- Recursos pedagógicos completos para casos prácticos con soluciones oficiales
- Herramientas de validación para evaluación consistente de proyectos estudiantiles
- Documentación de referencia para instructores y asistentes de enseñanza

## 4.11.0 (2025-08-15)

### Agregado

- Archivo CLAUDE.md con guía completa para asistente Claude Code
- Documentación exhaustiva de arquitectura pedagógica y técnica del proyecto
- Guía de comandos de desarrollo y flujo de trabajo para mantenimiento
- Especificaciones técnicas completas del stack y metodología educativa

### Mejorado

- Unificación completa de estructura en casos prácticos de los tres bloques
- Estandarización de formato de encabezados con ponderaciones consistentes
- Integración obligatoria de enlaces de YouTube directamente en notebooks
- Refinamiento de rúbricas con criterios específicos para enlaces funcionales
- Optimización de cronogramas con distribución temporal apropiada por complejidad
- Elevación del nivel profesional del caso práctico Bloque 3 (25% ponderación)

### Corregido

- Corrección de duración del caso práctico Bloque 3 de 3 semanas a 2 semanas optimizadas
- Actualización de expectativas profesionales acordes al peso del 25% del curso
- Eliminación de referencias inconsistentes a entrega por Canvas vs notebook
- Estandarización de template de información del equipo en todos los bloques

### Cambiado

- Casos prácticos Bloque 1 y 2 mantienen 15% pero con estructura unificada
- Caso práctico Bloque 3 elevado a 25% con contexto profesional completo
- Metodología de evaluación consistente: Excelente/Suficiente/Insuficiente/No presentó
- Instrucciones específicas para inclusión de enlaces de video en entregables

## 4.10.0 (2025-08-15)

### Mejorado

- Refinamiento completo del caso práctico colaborativo del Bloque 1
- Reubicación de sección Reflexión Final para mayor visibilidad estudiantil
- Simplificación del sistema de calificación con porcentajes fijos y símbolos de aproximación
- Estandarización de niveles de calificación: Excelente/Suficiente/Insuficiente/No presentó
- Corrección de ponderación académica y especificación de fechas límite de entrega
- Mejora en claridad de instrucciones para entregables y criterios de evaluación

### Corregido

- Eliminación de emojis en documentación para cumplir política profesional del proyecto
- Corrección de notación matemática inapropiada en rúbricas de evaluación
- Aclaración de distribución de puntos en componente Reflexión y Documentación
- Simplificación de referencias metodológicas para evitar confusión terminológica

### Cambiado

- Estructura de rúbrica más clara con distribución explícita de puntos por componente
- Cronograma de entrega específico con fechas concretas (17 de noviembre de 2025)
- Formato de tabla resumen de calificación más legible y consistente

## 4.9.0 (2025-08-12)

### Agregado

- Suite completa de tests para herramienta py-to-marp con cobertura exhaustiva
- Tests diagnósticos para verificación de funcionalidad (test_diagnostics.py)
- Suite de tests principal con 4 casos de prueba (run_tests.py)
- Tests específicos para conversión py-to-marp (test_py_to_marp.py)
- Archivo de muestra para testing (test_sample.py)
- Generación automática de documentación en formato Markdown desde archivos py:percent

### Corregido

- Restauración completa de convert.py tras corrupción del archivo
- Funcionalidad CLI de py-to-marp completamente operativa
- Corrección de imports y dependencias en herramienta py-to-marp
- Simplificación de Makefile para evitar conflictos de targets

### Mejorado

- Proceso de conversión de archivos py:percent a presentaciones Marp más robusto
- Validación automática de todas las configuraciones disponibles (6 configuraciones)
- Documentación técnica y procesos de testing mejorados

## 4.8.0 (2025-08-12)

### Agregado

- Herramientas profesionales de conversión notebook-to-pdf en herramientas/notebook-to-pdf/
- Sistema de cache inteligente con verificación MD5 para conversiones optimizadas
- Suite completa de tests automatizados (14 casos de prueba)
- Documentación profesional: README, USAGE_GUIDE, TECHNICAL_DETAILS, INSTALLATION
- Scripts especializados: convert.py (básico), smart_convert.py (inteligente), convert.sh (bash)
- Integración completa con Makefile del proyecto principal (comandos notebook-*)
- Soporte para múltiples motores LaTeX: XeLaTeX, PDFLaTeX, LuaLaTeX

### Eliminado

- Carpeta scripts/ redundante - funcionalidad supersedida por herramientas/notebook-to-pdf/

### Mejorado

- Proceso de conversión de notebooks a PDF con detección automática de cambios
- Verificación de dependencias automatizada
- Interfaz unificada para conversión mediante comandos make

## 4.7.0 (2025-08-12)

- Se agrega banco de preguntas del Bloque 3 en formatos .md, .txt, .csv y script generar_qti.py para conversión automática a QTI Canvas.
- Limpieza de mensajes en la herramienta herramientas/txt-to-qti para eliminar emojis y mantener estilo profesional.
- Mejora la integración y consistencia documental para evaluaciones Canvas en bloque 3.

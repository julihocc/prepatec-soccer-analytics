# Instrucciones para GitHub Copilot

**Proyecto**: Curso de Ciencia de Datos aplicada al Fútbol (Preparatoria/Bachillerato)  
**Idioma**: Español completo (código, comentarios, documentación)  
**Contexto**: Análisis deportivo con datos reales de fútbol  
**Metodología**: Enfoque reflexivo + 3 sesiones de 50 minutos por semana

## CONTEXTO EDUCATIVO CRÍTICO

**CURSO INTRODUCTORIO PARA PREPARATORIA**: Este es un curso de NIVEL BÁSICO para estudiantes de 15-18 años SIN experiencia previa en programación.

### Características del Estudiante Objetivo:
- **Edad**: 15-18 años (preparatoria/bachillerato)
- **Experiencia previa**: CERO programación, CERO ciencia de datos
- **Nivel matemático**: Álgebra básica de preparatoria
- **Contexto cultural**: México, familiarizados con fútbol
- **Motivación**: Conectar tecnología con deportes

### Implicaciones Pedagógicas Obligatorias:
- **Explicar TODO desde cero**: No asumir conocimientos previos
- **Vocabulario accesible**: Profesional pero comprensible para la edad
- **Progresión gradual**: Conceptos simples antes que complejos
- **Analogías constantes**: Usar deportes y vida cotidiana
- **Motivación continua**: Mostrar aplicaciones inmediatas y relevantes
- **Paciencia pedagógica**: Repetir conceptos clave múltiples veces

### RESTRICCIÓN TEMPORAL CRÍTICA:
- **Duración máxima por sesión**: 50 minutos reales de contenido
- **Incluye**: Teoría + práctica + reflexiones + ejercicios
- **Planificación**: 15 min teoría + 25 min práctica + 10 min síntesis
- **Prueba obligatoria**: Cada notebook debe ejecutarse completamente en máximo 45 minutos
- **Principio rector**: "Si no cabe en 50 minutos, es demasiado para una sesión"  

## REGLA CRÍTICA: PROHIBIDOS LOS EMOJIS

**ESTRICTAMENTE PROHIBIDO**: No se permiten emojis en ninguna parte de este proyecto.
- SIN emojis en archivos de código (.py, .ipynb)
- SIN emojis en documentación (archivos .md)
- SIN emojis en comentarios o strings
- SIN emojis en print statements
- SIN emojis en mensajes de commit
- SIN emojis en outputs de código
- SIN emojis en markdown headers
- Mantener contenido profesional, limpio, sin emojis en todo momento
- ELIMINAR inmediatamente cualquier emoji encontrado durante revisiones

## Contexto Central del Proyecto

Este archivo contiene TODA la documentación necesaria para trabajar en este proyecto educativo.

## Arquitectura del Proyecto

### Estructura de Contenido
```
contenido/
├── bloque-1/ (Semanas 1-5: Fundamentos Python)
├── bloque-2/ (Semanas 6-10: Ciencia de Datos + Fútbol)  
└── bloque-3/ (Semanas 11-15: Predicciones ML)
```

# Instrucciones rápidas para agentes de codificación (repositorio: tec-data-science-topic)

Objetivo: ser productivo aquí en minutos. Reglas clave, comandos y ejemplos concretos del repositorio.

- Idioma y estilo: TODO en español. Prohibidos los emojis en código, documentación y mensajes de commit.
- Formato de contenidos: usar archivos `.py` en formato percent (jupytext). No versionar `.ipynb` en la raíz de `contenido/*/semana-*`.
- Unicidad por semana: cada carpeta `contenido/*/semana-X/` solo un `.ipynb` en el nivel raíz; material extra en `material-apoyo/`.

Dónde trabajar (ejemplos):
- Contenido principal: `contenido/bloque-*/semana-*/` (ej. `contenido/bloque-1/semana-1/configuracion-fundamentos.py`).
- Evaluaciones y rúbricas: `evaluaciones/` (ej. `evaluaciones/bloque-1/caso-practico/caso-bloque1.md`).
- Herramientas: `herramientas/py-to-marp/`, `herramientas/notebook-to-pdf/` (usa los scripts allí para conversiones).

Comandos concretos (verificados en repo):
- Instalar dependencias: `pip install -r requirements.txt` (usa el entorno del repo).
- Convertir .py -> .ipynb y ejecutar para validar duración y errores:
    `jupytext --to notebook archivo.py && jupyter nbconvert --execute archivo.ipynb --ExecutePreprocessor.timeout=600`
- Generar slides: `cd herramientas/py-to-marp && python3 convert.py ../../contenido/archivo.py --config educativo`
- Generar PDFs (repositorio tiene `herramientas/notebook-to-pdf/convert.py`).

Reglas operativas para cambios en contenido/ evaluaciones:
- Si modificas `contenido/` o `evaluaciones/`, actualiza el `README.md` de la carpeta local en el mismo commit. Si cambias políticas globales, añade entrada en `evaluaciones/README.md`.
- Mensajes de commit en español; prefijo recomendado: `docs(...)`, `feat(...)`, `refactor(...)`.

Validaciones mínimas antes de crear PR:
- Ejecutar conversión y ejecutar notebook completo (ver comando arriba).
- Revisar que la sesión encaje en 50 min (prueba de ejecución o revisar el número de celdas/ejercicios).
- Comprobar que no se añadieron `.ipynb` no documentados en la raíz de una semana.

Patrones específicos del código educativo:
- Variables y nombres en español (ej. `datos_futbol`, `goles_por_equipo`).
- Visualización: usar `sns.set_theme(style="whitegrid", palette="viridis")` como estándar.
- Mantener explicaciones pedagógicas: introducir con una pregunta, luego código, luego reflexión.

Dónde buscar tests y utilidades:
- Tests de herramientas: `herramientas/*/tests/`.
- Scripts de conversión y helpers: `herramientas/py-to-marp/`, `herramientas/notebook-to-pdf/`.

Si necesitas cambios de formato (p. ej. renombrar una categoría en rúbrica):
1) editar `evaluaciones/bloque-X/caso-practico/*.md`; 2) actualizar `evaluaciones/bloque-X/README.md`; 3) añadir nota en `evaluaciones/README.md` — todo en un commit.

Preguntas frecuentes para agentes:
- "¿Dónde pongo material extra?" → `contenido/.../semana-X/material-apoyo/`.
- "¿Cómo pruebo un notebook rápidamente?" → ver comando `jupytext` + `nbconvert` arriba.

Fin: actualiza este archivo si encuentras patrones nuevos; pide revisión humana para cambios pedagógicos importantes. ¿Te hago un PR con estas modificaciones o prefieres ajustar algo? 
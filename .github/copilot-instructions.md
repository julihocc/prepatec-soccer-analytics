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
# Guía breve para agentes AI — repositorio "tec-data-science-topic"

Objetivo: instrucciones mínimas y accionables para editar, convertir y validar contenido educativo en este repo.

Reglas obligatorias
- Idioma: español en código, comentarios, commits y docs.
- Contenido interactivo: usar archivos `.py` en formato percent (# %% / # %% [markdown]). No commitear `.ipynb` en la raíz de una carpeta `semana/`.
- Prohibido: emojis en cualquier archivo, comentario o commit.

Estructura clave
- `contenido/` — materiales por bloque/semana (ej.: `contenido/bloque-1/semana-1/configuracion-fundamentos.py`).
- `evaluaciones/` — bancos, canvas, casos; actualizar README del bloque si se cambian evaluaciones.
- `herramientas/` — scripts de conversión: `py-to-marp/`, `notebook-to-pdf/`.

Comandos y flujos concretos
- Convertir .py a notebook on-demand: `jupytext --to notebook path/archivo.py`.
- Ejecutar notebook para pruebas: `jupyter nbconvert --execute path/archivo.ipynb`.
- Generar presentación (ejemplo): `python3 herramientas/py-to-marp/convert.py ../../contenido/..../archivo.py --config educativo`.

Patterns detectados (usar siempre)
- Un archivo `.py` por semana; los materiales adicionales van en `material-apoyo/` dentro de la semana.
- Variables y nombres en español, estilo snake_case; clases en PascalCase.
- Visuales: preferir seaborn/sns.set_theme(style="whitegrid", palette="viridis").

Checklist mínimo antes de abrir PR (agent checklist)
1. ¿El cambio mantiene español y formato percent? (sí/no)
2. ¿No agregaste `.ipynb` en la raíz de `semana/`? (si hace falta, mover a `material-apoyo/`)
3. ¿Actualizaste `contenido/.../README.md` o `evaluaciones/.../README.md` si cambias evaluaciones? (sí/no)
4. ¿Commit message en español y con prefijo recomendado (`docs(...)`, `feat(...)`, `refactor(...)`)?
5. ¿No añadiste emojis? (sí/no)

Dónde mirar para contexto rápido
- Archivo ejemplo de semana: `contenido/bloque-1/semana-1/configuracion-fundamentos.py`.
- Conversión/slide tooling: `herramientas/py-to-marp/convert.py` y `herramientas/notebook-to-pdf/`.
- Políticas de evaluación: `evaluaciones/README.md`.

Si vas a efectuar una reestructuración amplia, publica aquí un resumen de 3 puntos: qué cambias, por qué, y qué READMEs actualizarás — yo generaré la checklist y los comandos de prueba.

- Reforzar transferencia: del concepto aislado al contexto futbolístico.
- Mantener progresión cognitiva visible para curación y análisis.

### Tamaño y Segmentación
- Tamaño recomendado por bloque: 70–120 preguntas totales.
- Dividir explícitamente en:
    - Núcleo (Core): 60–75 preguntas esenciales (cobertura mínima necesaria para evaluaciones regulares).
    - Ampliación (Extended): Resto para variabilidad y reforzamiento.
- No renumerar al agregar Ampliación: preservar estabilidad para LMS.

### Etiquetas Cognitivas (OBLIGATORIAS)
- [R] Recuerdo básico (definición, sintaxis mínima, función directa).
- [C] Comprensión/Concepto (interpretar ejemplo, explicar diferencia, clasificar caso).
- [A] Aplicación (resolver mini‑situación con datos simples o ajuste de código mental).
- [S] (Opcional sugerido) Socrática/Interpretativa: justificar decisión, inferir implicación de salida, explicar causa futbolística de patrón observado.

Distribución sugerida en Núcleo: ~35–40% [R], ~35–40% [C], ~20–25% [A], opcional 5–10% [S] conforme avance el curso. En semanas iniciales priorizar [R]/[C]; introducir [A] y luego [S] gradualmente.

### Formatos de Pregunta
- 70% opción múltiple (3–4 distractores claros, 1 correcta).
- 30% numéricas (respuesta corta calculable; definir tolerancia si aplica).
- Evitar preguntas Sí/No (baja discriminación) salvo transición entre conceptos.

### Plantilla Recomendada
1. Micro‑escenario futbolístico (1 frase): "En una tabla con goles de Barcelona y Real Madrid..."
2. Enfoque cognitivo: "¿Cuál.../¿Por qué.../¿Qué pasaría si...?"
3. Opciones: ordenadas lógicamente (no alfabético arbitrario) o rango numérico.
4. (Si [S]) Sub‑prompt de justificación: "¿Qué te indica esto sobre..." (si la plataforma permite campo abierto adicional).

### Patrones de Calidad
- Evitar duplicados literales: reescribir cambiando dimensión (de sintaxis a interpretación / de estructura a salida esperada).
- Introducir progresión suave: secuencia interna de filtros simples → múltiples condiciones → agregaciones.
- Contextualizar con dominios constantes (equipos conocidos, métricas de goles, edad, minutos jugados) para reducir carga extrínseca.
- Balancear verbos: detectar exceso de "¿Cuál es...?" e inyectar "¿Por qué...?", "¿Qué implica...?", "¿Qué cambiaría si...?".
- Limitar carga numérica: operaciones aritméticas ≤ 2 pasos mentales.

### Proceso Iterativo Estandarizado
1. Borrador inicial (sin etiquetas) basado en temario semanal.
2. Etiquetado cognitivo y clasificación Core vs candidata a Ampliación.
3. Detección y reescritura de redundancias (mantener número; agregar nota *Reescrita* si se ajusta tras uso inicial).
4. Inyección de contexto futbolístico en preguntas abstractas (>10% del banco si faltan escenarios).
5. Revisión de distribución (tabla rápida: conteo por etiqueta y formato) y ajuste final.

### Checklist de Publicación
- [ ] Cobertura de TODOS los conceptos mínimos declarados en semanas del bloque.
- [ ] Distribución formatos: 65–75% opción múltiple, 25–35% numérica.
- [ ] Distribución cognitiva dentro de rangos sugeridos.
- [ ] ≥80% de preguntas Core con contexto o aplicabilidad clara.
- [ ] Sin emojis, sin jerga avanzada no explicada.
- [ ] Numeración continua sin saltos ni renumeraciones tras revisiones.
- [ ] Cada pregunta evaluable independientemente (no dependencias encadenadas).
- [ ] Distractores plausibles (evitar respuestas obviamente absurdas que reduzcan discriminación).

### Reglas de Mantenimiento
- Nunca renumerar preguntas ya referenciadas en LMS; agregar nuevas al final.
- Marcar ajustes significativos con anotación *(Actualizada vX.Y)* si cambia respuesta correcta o nivel cognitivo.
- Mantener changelog por bloque (sección en README de evaluaciones) con: fecha, tipo de cambio (alta, corrección, reescritura), impacto.

### Métricas Futuras (Opcional)
Cuando existan datos de uso (resultados de estudiantes):
- Calcular tasa de acierto por pregunta (<35% o >90% revisar redacción/dificultad).
- Reclasificar etiqueta si desempeño contradice nivel esperado.
- Retirar o ajustar preguntas con discriminación pobre (todos aciertan o todos fallan).

### Ejemplos de Transformaciones de Calidad
- Duplicado potencial "¿Qué hace len(lista)?" → Transformar a [C]: "Si una lista de 18 jugadores pasa a 16 tras eliminar porteros suplentes, ¿qué indica la diferencia en len()?"
- Sintaxis seca de filtrado → Escenario [A]: "Tienes un DataFrame de tiros; ¿qué condición seleccionarías para quedarte con tiros a puerta del Barcelona en 2024?"

### Errores Comunes a Evitar
- Sobrecargar con código no visto aún (rompe progresión).
- Mezclar dos conceptos nuevos en una sola pregunta inicial.
- Colocar respuestas numéricas con unidades inconsistentes (estandarizar: sin 'goles' en la caja de respuesta, unidad en el enunciado).
- Distractores con diferencias microscópicas (aumenta frustración sin valor pedagógico).

### Integración con Rúbricas y Casos
Las etiquetas [A]/[S] sirven para enlazar con rúbricas de razonamiento: priorizar su muestreo en evaluaciones formativas antes de casos prácticos.

---

## POLÍTICA OBLIGATORIA DE DOCUMENTACIÓN DE CAMBIOS

Toda modificación que afecte contenido educativo, bancos de preguntas, casos prácticos, rúbricas, cronogramas o lineamientos metodológicos debe reflejarse inmediatamente en la documentación correspondiente. No se permite introducir cambios silentes.

### Alcance de la Política
- **Nivel Carpeta (Local):** Si el cambio ocurre dentro de `contenido/bloque-X`, `evaluaciones/bloque-X` o cualquier subcarpeta específica, actualizar el `README.md` de esa carpeta en el mismo commit.
- **Nivel Global (Repositorio):** Si el cambio altera:
    - Estructura de bancos (tamaño, segmentación Core/Extended, distribución cognitiva)
    - Formato o pesos de rúbricas (40/30/30 u otro)
    - Cronogramas semanales o de evaluación
    - Límites de complejidad o alcance de bloques
    - Procedimientos de muestreo (examen Canvas: número de ítems, tiempos, proporciones por etiqueta)
    Entonces también actualizar el `README.md` principal del repositorio añadiendo un ítem en "Actualizaciones Recientes".
- **Nivel Instruccional (Este archivo):** Si el cambio introduce o modifica un proceso estándar (ej. nueva verificación previa a commit, ajuste en política de segmentación), añadir o editar la sección pertinente en este documento.

### Formato de Commits (Convenciones)
- Prefijo sugerido: `docs(...)` para cambios puramente de documentación; `feat(...)` si el contenido pedagógico nuevo añade capacidad evaluativa o instruccional; `refactor(...)` si reorganiza sin cambiar alcance.
- Ejemplos:
    - `docs(banco-bloque2): añadir 10 ítems Extended con etiquetas [S]`
    - `feat(rubrica-bloque3): incorporar métrica de precisión simplificada`

### Checklist Pre-Commit (Marcar mentalmente antes de confirmar)
1. ¿El cambio altera cómo un estudiante será evaluado? → Actualizar rúbrica y README(s).
2. ¿Afecta conteo, distribución o segmentación de preguntas? → Actualizar README del bloque y nota global si es política nueva.
3. ¿Modifica tiempos, duración de examen o número de ítems? → Actualizar README global y bloque implicado.
4. ¿Introduce una métrica, variable o término nuevo recurrente? → Añadir a estándares / glosario local si aplica.
5. ¿Se agregó contenido que impacta la progresión semanal? → Ajustar cronograma del bloque.
6. ¿Se tocaron notebooks que cambian alcance (más de 45 min)? → Recortar o documentar justificación y volver a validar tiempo.
7. ¿Se respetó prohibición de emojis y uso de español? → Verificación final.

### Criterios de Bloqueo (No Comitear si):
- Falta actualización de README donde el cambio es visible para docentes/estudiantes.
- Se modifica una rúbrica sin reflejar nuevos pesos en documentación del bloque.
- Se cambia distribución cognitiva sin tabla o nota explicativa.
- Se amplía banco sin añadir conteo actualizado o sin registrar si es Core o Extended.

### Registro de Cambios Sugerido
En cada README de bloque mantener sección "Actualizaciones Recientes" con entradas concisas:
```
AAAA-MM-DD: Cambio resumido (ej. Añadidas preguntas 76-90 Extended [S] interpretación de boxplots)
```

### Ejemplo de Flujo Correcto
1. Añadir 10 preguntas Extended [S] al banco Bloque 2.
2. Actualizar `evaluaciones/bloque-2/README.md` (nuevo total, distribución, nota de interpretación añadida).
3. Si se ajusta política general (ej. pasar de 22 a 24 ítems en examen), actualizar README principal + este archivo (sección de bancos) + bloque involucrado.
4. Commit único integrando banco + documentación: mensaje `feat(banco-bloque2): extender a 85 preguntas con primera capa [S] interpretación`.

### Principio Rector
"Ningún cambio evaluativo o metodológico es válido hasta que su documentación visible esté sincronizada en el mismo commit." 

---
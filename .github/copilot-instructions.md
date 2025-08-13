# Instrucciones para GitHub Copilot

**Proyecto**: Curso de Ciencia de Datos aplicada al Fútbol (Preparatoria/Bachillerato)  
**Idioma**: Español completo (código, comentarios, documentación)  
**Contexto**: Análisis deportivo con datos reales de fútbol  
**Metodología**: Socrática + 3 sesiones de 50 minutos por semana

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

### Sistema de Evaluación
```
evaluaciones/
├── canvas/ (Bancos de preguntas automáticas CON MÉTODO SOCRÁTICO)
├── casos-practicos/ (Proyectos colaborativos 3-4 estudiantes CON REFLEXIÓN GUIADA)
└── rubricas/ (40% técnico + 30% aplicación + 30% comunicación/RAZONAMIENTO)
```

#### Enfoque Socrático en Evaluaciones:
- **Canvas**: Preguntas que evalúan comprensión conceptual, no memorización
- **Casos prácticos**: Situaciones deportivas complejas que requieren análisis paso a paso
- **Rúbricas**: Valorar proceso de razonamiento y justificación de decisiones
- **Reflexión**: Incluir preguntas metacognitivas sobre el aprendizaje propio

## Convenciones Críticas

### Metodología Socrática Obligatoria
**APLICAR EN TODO EL PROYECTO**: Contenido educativo Y evaluaciones deben usar método socrático.

```python
# PATRÓN: Pregunta → Reflexión → Descubrimiento → Código
print("¿Te has preguntado alguna vez cómo un entrenador decide su alineación?")
print("¡Vamos a descubrirlo usando datos!")

# Generar curiosidad ANTES de mostrar resultados
equipos = ['Barcelona', 'Real Madrid', 'Manchester City']
print(f"¿Cuántos equipos tenemos? Descubrámoslo: {len(equipos)}")

# Preguntas reflexivas DESPUÉS del código
print("¿Qué patrones observas en estos datos?")
```

#### Aplicación en Contenido:
- Comenzar cada concepto con pregunta motivadora
- Usar analogías deportivas antes de explicaciones técnicas
- Incluir reflexiones intermedias durante el código
- Terminar con síntesis que conecte aprendizajes

#### Aplicación en Evaluaciones:
- Preguntas que requieren razonamiento, no memorización

### PARADIGMA ARQUITECTÓNICO: FORMATO PY:PERCENT (OBLIGATORIO)

**DECISIÓN CRÍTICA**: El contenido educativo utiliza archivos `.py` con formato percent en lugar de notebooks `.ipynb` para mejorar mantenibilidad y colaboración.

#### Beneficios del formato PY:PERCENT:
- **✅ Control de versiones superior**: Diffs legibles, no conflictos JSON
- **✅ Colaboración mejorada**: Editores completos con syntax highlighting 
- **✅ Mantenimiento simplificado**: Sin conflictos JSON de notebooks
- **✅ Compatibilidad total**: Conversión bidireccional automática con jupytext

#### Estructura del proyecto:
- **Un archivo `.py` por semana**: Formato percent con metadata automático
- **Exclusión de `.ipynb`**: Están en .gitignore, no se versionan
- **Conversión on-demand**: `jupytext --to notebook` cuando necesario

#### Flujo de trabajo:
1. **Editar contenido**: Trabajar directamente en archivos `.py`
2. **Generar notebooks**: `jupytext --to notebook archivo.py` cuando necesario  
3. **Generar PDFs**: Usar herramientas/notebook-to-pdf/ para conversión masiva

#### Reglas obligatorias:
- **Formato único**: Solo percent format (# %% [markdown] y # %%)
- **Sin notebooks**: Los `.ipynb` están excluidos del control de versiones
- **Conversión on-demand**: Generar notebooks solo cuando se requiera ejecución interactiva
- Escenarios deportivos que demanden análisis crítico
- Casos prácticos que integren múltiples conceptos
- Evaluación del proceso de pensamiento, no solo resultados

### Estructura de Notebook (OBLIGATORIA)
```markdown
# Semana X: ¿[Pregunta que genera curiosidad]?

## SESIÓN 1: ¿[Pregunta específica]? (50 min)
**Pregunta guía**: ¿Cómo...?
**Contenido máximo**: 15 min teoría + 25 min práctica + 10 min reflexión
- Conceptos fundamentales (máximo 2-3 conceptos por sesión)
- Teoría con analogías deportivas (explicaciones breves y claras)
- Preguntas reflexivas intermedias (máximo 3-4 preguntas)
- Práctica inmediata (ejercicios que tomen máximo 20 minutos)

## SESIÓN 2: ¿[Pregunta práctica]? (50 min)  
**Pregunta guía**: ¿Por qué...?
**Contenido máximo**: 10 min repaso + 30 min práctica + 10 min conexiones
- Ejercicios aplicados (progresión lógica desde sesión anterior)
- Práctica con datos (datasets pequeños y manejables)
- Conexiones con fútbol real (ejemplos concretos y familiares)
- Validación de comprensión (preguntas de verificación)

## SESIÓN 3: ¿[Pregunta de aplicación]? (50 min)
**Pregunta guía**: ¿Cómo podríamos...?
**Contenido máximo**: 5 min repaso + 35 min aplicación + 10 min síntesis
- Aplicación a datos deportivos reales (problema completo pero acotado)
- Integración de conceptos (máximo 3 conceptos de sesiones anteriores)
- Síntesis reflexiva final (consolidación y conexión con próxima semana)
- Autoevaluación del aprendizaje (reflexión metacognitiva)
```

### REGLAS DE TEMPORIZACIÓN:
- **Total por semana**: 150 minutos distribuidos en 3 sesiones de 50 minutos exactos
- **Margen de seguridad**: Planificar contenido para 45 minutos, reservar 5 para preguntas
- **Prueba obligatoria**: Ejecutar notebook completo en tiempo real antes de finalizar
- **Principio de edición**: Si excede tiempo, ELIMINAR contenido, no comprimir explicaciones

### Código Estándar
```python
# Variables descriptivas en español
datos_futbol = pd.DataFrame(...)
goles_por_equipo = datos_futbol.groupby('equipo')['goles'].sum()

# Configuración visual SIEMPRE
sns.set_theme(style="whitegrid", palette="viridis")

# Comentarios educativos y preguntas
# ¿Por qué usamos esta función específica?
print("Este análisis nos muestra los patrones de goles!")
```

## Flujos de Trabajo Específicos

### Política de Unicidad de Notebooks por Carpeta (NUEVA)
**Regla específica**: Cada carpeta de semana (por ejemplo: `contenido/bloque-1/semana-1/`) debe contener **solo un (1) notebook principal `.ipynb`** en el nivel raíz de esa carpeta.

**Motivación pedagógica y operativa**:
- Evita que el docente/estudiante se confunda sobre cuál es “el flujo oficial” de la semana.
- Facilita la validación estricta de tiempo (cronómetro sobre un único notebook).
- Simplifica control de versiones y seguimiento de cambios (changelog más claro).
- Reduce riesgo de duplicación parcial de contenido que rompa la progresión gradual.

**Si se requiere material adicional** (apoyo opcional, soluciones extendidas, datasets exploratorios, borradores):
1. Crear un subfolder dentro de la misma semana, por ejemplo: `material-apoyo/`, `exploraciones/` o `soluciones/`.
2. Colocar ahí archivos alternativos (`.ipynb`, `.md`, `.py`).
3. Referenciar explícitamente ese subfolder desde una sección “Recursos opcionales” del notebook principal (sin obligar su apertura para el flujo básico de 50 minutos).
4. Documentar en el `README.md` del bloque la existencia de esos recursos (fecha + propósito). 

**Alternativas recomendadas antes de crear un segundo notebook**:
- Convertir contenido extendido a `.md` (lectura) o `.py` (script demostrativo) si no precisa ejecución interactiva paso a paso.
- Integrar fragmentos como sección opcional al final (marcada claramente como “Extensión (no obligatoria)”), siempre validando que su exclusión mantiene la duración comprometida.

**Checklist previo a añadir un segundo `.ipynb` (debería normalmente evitarse)**:
- [ ] ¿El contenido extra es indispensable para los objetivos mínimos? (Si NO, mover a subfolder opcional.)
- [ ] ¿Rompe la regla de tiempo (sumado al principal excede 50 min)? (Si SÍ, descartar o resumir.)
- [ ] ¿Se actualizó README del bloque con nota de recurso adicional? (Obligatorio.)
- [ ] ¿Se explicó en la sección de “Recursos opcionales” por qué existe y su uso sugerido? (Claridad.)

**Criterio de bloqueo**: Un commit que agrega un segundo notebook en el nivel raíz de una carpeta de semana sin crear subfolder y sin documentación asociada debe ser rechazado hasta corregir la estructura.

> Nota: Esta política sustituye cualquier interpretación previa ambigua sobre “no múltiples archivos”; la restricción aplica únicamente a múltiples notebooks `.ipynb` en el mismo nivel raíz de una carpeta de semana.

### Creación de Contenido Semanal
1. **Comenzar con pregunta socrática** ("¿Alguna vez te has preguntado...?")
2. **Estructurar en 3 sesiones exactas** de 50 minutos
3. **Usar datos futbolísticos reales** (Barcelona, Real Madrid, equipos europeos)
4. **Incluir reflexiones intermedias** ("¿Qué patrones observas?")
5. **Terminar con síntesis** ("¿Qué hemos descubierto?")
6. **VALIDAR TEMPORIZACIÓN**: Probar cada sesión completa en tiempo real
7. **RECORTAR SI EXCEDE**: Eliminar contenido extra, mantener lo esencial

### METODOLOGÍA DE VALIDACIÓN TEMPORAL:
```python
# Antes de finalizar cualquier notebook:
# 1. Ejecutar sesión completa con cronómetro
# 2. Incluir tiempo para preguntas de estudiantes
# 3. Si excede 45 minutos, ELIMINAR contenido
# 4. Priorizar comprensión sobre cantidad de temas
```

### Evaluación y Testing
```python
# Probar notebooks COMPLETOS antes de finalizar
jupyter nbconvert --execute notebook.ipynb

# Usar equipos reconocibles en ejemplos
equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']

# CRÍTICO: Verificar que cada sesión tome máximo 50 minutos
# Cronometrar ejecución completa incluyendo explicaciones
```

### VALIDACIÓN TEMPORAL OBLIGATORIA:
- **Sesión 1**: Máximo 50 minutos (15 teoría + 25 práctica + 10 reflexión)
- **Sesión 2**: Máximo 50 minutos (10 repaso + 30 práctica + 10 conexiones)  
- **Sesión 3**: Máximo 50 minutos (5 repaso + 35 aplicación + 10 síntesis)
- **Margen de error**: Planificar para 45 minutos, reservar 5 para preguntas

#### Principios de Evaluación Socrática:
1. **Preguntas abiertas**: "¿Por qué crees que...?" en lugar de "¿Cuál es...?"
2. **Análisis de casos**: Presentar situaciones deportivas para analizar
3. **Justificación obligatoria**: Estudiantes deben explicar su razonamiento
4. **Conexión conceptual**: Evaluar capacidad de relacionar conceptos
5. **Aplicación práctica**: Resolver problemas deportivos reales con datos

## Patterns Específicos del Proyecto

### Datos Deportivos Simulados
```python
# Generación de datasets realistas para aprendizaje
partidos = []
for i in range(30):
    equipo_local = random.choice(equipos)
    equipo_visitante = random.choice([e for e in equipos if e != equipo_local])
    partidos.append({
        'Equipo_Local': equipo_local,
        'Goles_Local': random.randint(0, 3),
        'Temporada': random.choice(['2023-24', '2024-25'])
    })
```

### Integración Canvas
- **Formato**: 70% opción múltiple + 30% numérica
- **Bancos**: 70-75 preguntas por bloque con selección aleatoria
- **Importación**: Directa desde archivos markdown estructurados

## Comandos del Proyecto

```bash
# Verificar entorno de desarrollo
python -c "import pandas as pd; print('Pandas ready!')"

# Ejecutar notebook completo para testing
jupyter nbconvert --execute --to notebook contenido/bloque-1/semana-1/configuracion-fundamentos.ipynb

# Commit con estándares del proyecto (mensajes en español)
git commit -m "Actualizar Semana X: mejorar metodología socrática"
```

## Referencias Clave

- **Dataset principal**: [Champs - Kaggle](https://www.kaggle.com/datasets/julihocc/champs)
- **Notebook referencia**: [La Remontada](https://www.kaggle.com/code/julihocc/la-remontada)

## Estándares de Desarrollo

### Variables y Nomenclatura
- **Nombres en español**: `datos_futbol`, `equipos_europeos`, `promedio_goles`
- **Descriptivos y claros**: `goles_por_equipo` no `gpe`
- **Consistencia**: snake_case para variables, PascalCase para clases

### Contexto Deportivo Obligatorio
- **Equipos reales**: Barcelona, Real Madrid, Manchester City, Bayern Munich
- **Situaciones familiares**: Análisis de rendimiento, fichajes, alineaciones
- **Datos realistas**: Rangos de goles (0-4), edades (17-40), etc.

### Patrones de Código Educativo
```python
# Siempre incluir contexto deportivo
jugadores = ['Messi', 'Cristiano', 'Mbappé', 'Haaland']

# Preguntas antes de mostrar código
print("¿Cómo calcularíamos el promedio de edad del equipo?")
promedio_edad = sum(edades) / len(edades)
print(f"Promedio: {promedio_edad} años")

# Reflexión después del resultado
print("¿Qué nos dice este promedio sobre la experiencia del equipo?")
```

### Flujo de Trabajo de Contenido
1. **Pregunta motivadora inicial** (genera curiosidad)
2. **Analogía deportiva** (conecta con experiencia previa)
3. **Código progresivo** (construir paso a paso)
4. **Reflexiones intermedias** (conectar conceptos)
5. **Aplicación práctica** (problema deportivo real)
6. **Síntesis final** (¿qué descubrimos?)

## LÍMITES DE COMPLEJIDAD PARA PREPARATORIA

### LO QUE SÍ incluir (apropiado para nivel introductorio):
- **Python básico**: variables, operadores, listas, diccionarios, if/else, bucles simples
- **Pandas básico**: leer datos, filtrar, agrupar, promedios simples
- **Visualización simple**: gráficos de barras, líneas, dispersión básicos
- **Estadística descriptiva**: promedio, moda, mediana, rangos
- **Predicciones simples**: regresión lineal básica con interpretación clara

### LO QUE NO incluir (demasiado avanzado):
- **Algoritmos complejos**: clustering, redes neuronales, SVM avanzado
- **Estadística avanzada**: inferencia estadística, pruebas de hipótesis complejas
- **Programación avanzada**: clases, herencias, decoradores, manejo de errores complejo
- **Matemáticas universitarias**: cálculo, álgebra lineal, estadística bayesiana
- **Big Data**: Spark, bases de datos complejas, APIs avanzadas

### LÍMITES ESPECÍFICOS PARA BLOQUE 3 (Machine Learning):
- **Algoritmos permitidos**: Regresión lineal, regresión logística, Random Forest básico
- **Conceptos ML básicos**: train/test split, accuracy, overfitting (explicado con analogías)
- **Vocabulario simplificado**: "modelo" en lugar de "algoritmo", "predicción" en lugar de "inferencia"
- **Validación simple**: accuracy, confusion matrix básica (sin métricas avanzadas como F1, AUC)
- **Feature engineering básico**: crear variables simples (suma, promedio), NO transformaciones complejas

### Principio Rector:
"Si un estudiante de preparatoria no puede entender el concepto en 10 minutos con analogías deportivas, es demasiado complejo para este curso"

### REGLA DE VERIFICACIÓN:
Antes de incluir cualquier concepto de ML, preguntarse:
1. ¿Puede explicarse con analogía deportiva en 5 minutos?
2. ¿Requiere matemáticas más allá de álgebra básica?
3. ¿Puede implementarse en menos de 10 líneas de código?
4. ¿Genera valor práctico inmediato para análisis deportivo?

Si cualquier respuesta es NO, el concepto es demasiado avanzado.

**CRÍTICO**: Nunca usar emojis - mantener contenido profesional para preparatoria.

## ESTÁNDARES ESPECÍFICOS PARA BLOQUE 3 (MACHINE LEARNING)

### VOCABULARIO OBLIGATORIO SIMPLIFICADO:
- **"Modelo"** en lugar de "algoritmo"
- **"Predicción"** en lugar de "inferencia" 
- **"Entrenamiento"** en lugar de "fitting"
- **"Precisión"** en lugar de "accuracy score"
- **"Datos de prueba"** en lugar de "test set"

### ANALOGÍAS DEPORTIVAS OBLIGATORIAS:
- **Modelo = Entrenador**: "El modelo aprende patrones como un entrenador aprende tácticas"
- **Entrenamiento = Temporada de práctica**: "Entrenamos el modelo con datos del pasado"
- **Predicción = Pronóstico**: "Como pronosticar quién ganará el próximo partido"
- **Overfitting = Memorizar jugadas**: "Cuando el modelo memoriza en lugar de entender"

### LÍMITES TÉCNICOS ESTRICTOS:
- **Máximo 3 algoritmos**: Regresión lineal, regresión logística, Random Forest
- **Métricas básicas únicamente**: Accuracy, matriz de confusión simple
- **Sin matemáticas complejas**: Solo conceptos explicables con aritmética básica
- **Código máximo por sesión**: 20-25 líneas efectivas de programación

### PROGRESIÓN TEMPORAL OBLIGATORIA:
- **Semana 11**: Solo conceptos, sin código complejo (fundamentos ML)
- **Semana 12**: Un algoritmo a la vez, comparación simple
- **Semana 13**: Evaluación básica, conceptos de calidad
- **Semana 14**: Mejoras simples, variables nuevas
- **Semana 15**: Integración y proyecto final acotado

## PATRONES PARA DISEÑO DE BANCOS DE PREGUNTAS (Canvas/Moodle)

Esta sección estandariza la construcción de bancos evaluativos alineados con la metodología socrática y el nivel preparatoria. Aplicar en los tres bloques.

### Objetivos del Banco
- Medir comprensión real, no memorización literal.
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
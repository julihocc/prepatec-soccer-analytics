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

## REGLA CRÍTICA: PROHIBIDOS LOS EMOJIS

**ESTRICTAMENTE PROHIBIDO**: No se permiten emojis en ninguna parte de este proyecto.
- SIN emojis en archivos de código (.py, .ipynb)
- SIN emojis en documentación (archivos .md)
- SIN emojis en comentarios o strings
- SIN emojis en mensajes de commit
- Mantener contenido profesional, limpio, sin emojis en todo momento

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
- Escenarios deportivos que demanden análisis crítico
- Casos prácticos que integren múltiples conceptos
- Evaluación del proceso de pensamiento, no solo resultados

### Estructura de Notebook (OBLIGATORIA)
```markdown
# Semana X: ¿[Pregunta que genera curiosidad]?

## SESIÓN 1: ¿[Pregunta específica]? (50 min)
**Pregunta guía**: ¿Cómo...?
- Conceptos fundamentales
- Teoría con analogías deportivas
- Preguntas reflexivas intermedias

## SESIÓN 2: ¿[Pregunta práctica]? (50 min)  
**Pregunta guía**: ¿Por qué...?
- Ejercicios aplicados
- Práctica con datos
- Conexiones con fútbol real

## SESIÓN 3: ¿[Pregunta de aplicación]? (50 min)
**Pregunta guía**: ¿Cómo podríamos...?
- Aplicación a datos deportivos reales
- Integración de conceptos
- Síntesis reflexiva final
```

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

### Creación de Contenido Semanal
1. **Comenzar con pregunta socrática** ("¿Alguna vez te has preguntado...?")
2. **Estructurar en 3 sesiones exactas** de 50 minutos
3. **Usar datos futbolísticos reales** (Barcelona, Real Madrid, equipos europeos)
4. **Incluir reflexiones intermedias** ("¿Qué patrones observas?")
5. **Terminar con síntesis** ("¿Qué hemos descubierto?")

### Evaluación y Testing
```python
# Probar notebooks COMPLETOS antes de finalizar
jupyter nbconvert --execute notebook.ipynb

# Usar equipos reconocibles en ejemplos
equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']

# Verificar que ejercicios tomen ~60 minutos máximo
```

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
- **Algoritmos complejos**: clustering, redes neuronales, SVM
- **Estadística avanzada**: inferencia estadística, pruebas de hipótesis complejas
- **Programación avanzada**: clases, herencias, decoradores, manejo de errores complejo
- **Matemáticas universitarias**: cálculo, álgebra lineal, estadística bayesiana
- **Big Data**: Spark, bases de datos complejas, APIs avanzadas

### Principio Rector:
"Si un estudiante de preparatoria no puede entender el concepto en 10 minutos con analogías deportivas, es demasiado complejo para este curso"

**CRÍTICO**: Nunca usar emojis - mantener contenido profesional para preparatoria.
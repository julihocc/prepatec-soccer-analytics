# Instrucciones para GitHub Copilot

**Proyecto**: Curso de Ciencia de Datos aplicada al Fútbol (Preparatoria/Bachillerato)  
**Idioma**: Español completo (código, comentarios, documentación)  
**Contexto**: Análisis deportivo con datos reales de fútbol  
**Metodología**: Socrática + 3 sesiones de 50 minutos por semana  

## Contexto Central del Proyecto

**LEER PRIMERO**: [`.ai/AI-CONTEXT.md`](../.ai/AI-CONTEXT.md) - Contiene toda la documentación detallada, metodología socrática, patrones de código y estándares educativos.

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
├── canvas/ (Bancos de preguntas automáticas)
├── casos-practicos/ (Proyectos colaborativos 3-4 estudiantes)
└── rubricas/ (40% técnico + 30% aplicación + 30% comunicación)
```

## Convenciones Críticas

### Metodología Socrática Obligatoria
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

### Estructura de Notebook (OBLIGATORIA)
```python
# 1. Título con pregunta socrática
# Semana X: ¿[Pregunta que genera curiosidad]?

# 2. Sesión 1: Conceptos (50 min) - Preguntas guía + teoría
# 3. Sesión 2: Práctica (50 min) - Ejercicios + aplicación  
# 4. Sesión 3: Aplicación real (50 min) - Datos deportivos reales

# 5. SIEMPRE: Reflexiones finales socráticas
print("¿Qué hemos descubierto juntos?")
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
- **Documentación completa**: `.ai/AI-CONTEXT.md`

**CRÍTICO**: Nunca usar emojis - mantener contenido profesional para preparatoria.
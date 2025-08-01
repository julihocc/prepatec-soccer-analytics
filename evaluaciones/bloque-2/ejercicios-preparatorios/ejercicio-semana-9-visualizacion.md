# Ejercicio Semana 9: Visualización Avanzada de Datos

## Información General

**Bloque:** 2 - Fundamentos de Data Science  
**Semana:** 9  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 9  
**Archivo entrega:** `[matricula]-ejercicio-semana-9.ipynb`

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:
- Crear visualizaciones avanzadas específicas para análisis deportivo
- Aplicar principios de diseño visual para comunicación efectiva de datos
- Desarrollar dashboards coherentes para análisis futbolístico
- Implementar storytelling visual con datos deportivos
- Personalizar gráficos para diferentes audiencias y contextos

## Prerrequisitos

- Ejercicios de las Semanas 6-8 completados exitosamente  
- Dominio de matplotlib y seaborn básico
- Conocimiento de estadística descriptiva aplicada
- Comprensión de principios de visualización de datos

## Contexto del Ejercicio

Eres el **director de visualización de datos** del Liverpool FC. El club necesita un sistema visual integral para:

- Presentar análisis de rendimiento a diferentes audiencias
- Crear reportes visuales para medios de comunicación
- Desarrollar dashboards para el cuerpo técnico
- Comunicar insights de forma clara y atractiva

---

# Ejercicio Integrador: Centro Visual Liverpool FC

## Parte 1: Gráficos Especializados para Análisis Deportivo (25 puntos)

### Objetivo
Crear visualizaciones especializadas que comuniquen efectivamente el rendimiento del Liverpool FC.

### Instrucciones Detalladas

**Paso 1:** Configura el centro visual del Liverpool:

```python
# Configuración del centro visual Liverpool FC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi
import matplotlib.patches as patches
import warnings
warnings.filterwarnings('ignore')

# Configuración visual del Liverpool (colores oficiales)
colores_liverpool = ['#C8102E', '#F6EB61', '#00B2A9', '#212121']
sns.set_theme(style="whitegrid", palette=colores_liverpool)
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12

print("=== CENTRO VISUAL LIVERPOOL FC ===")
print("Sistema de visualización avanzada iniciado")
print("¡Herramientas gráficas listas!")

# Cargar datos de equipos europeos
df_equipos = pd.read_csv('equipos-europa-2023-24.csv')
print(f"Visualizando datos de {len(df_equipos)} equipos europeos")
```

**Paso 2:** Crea gráfico radar para análisis multidimensional:

```python
# Gráfico radar para análisis integral del Liverpool

# TU CÓDIGO AQUÍ:
# 1. Seleccionar métricas clave: Puntos, Goles_Favor, Goles_Contra, Presupuesto
# 2. Normalizar todas las métricas a escala 0-10
# 3. Crear función para gráfico radar del Liverpool vs promedio de liga
# 4. Incluir líneas para Liverpool, promedio Premier League y mejor equipo
# 5. Personalizar colores, etiquetas y leyenda
# 6. Añadir valores específicos en cada eje

def crear_radar_liverpool(datos_equipo, datos_referencia, metricas):
    """
    Crea gráfico radar comparativo para el Liverpool
    
    Parámetros:
    datos_equipo: Series con datos del Liverpool
    datos_referencia: DataFrame con datos de comparación
    metricas: Lista de métricas a incluir
    """
    # Tu implementación aquí
    
    # Configurar radar
    angulos = [n / float(len(metricas)) * 2 * pi for n in range(len(metricas))]
    angulos += angulos[:1]  # Cerrar el círculo
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    # Implementar radar aquí
    
    plt.title("Análisis Radar: Liverpool FC vs Competencia", size=16, fontweight='bold')
    return fig, ax

print("=== GRÁFICO RADAR LIVERPOOL FC ===")
# Implementar y mostrar radar
```

### Criterios de Evaluación
- **Gráfico radar funcional y preciso** (15 puntos)
- **Personalización visual efectiva** (10 puntos)

---

## Parte 2: Dashboard Comparativo de Rendimiento (25 puntos)

### Objetivo
Desarrollar un dashboard visual completo para comparar el Liverpool con la competencia europea.

### Instrucciones Detalladas

**Paso 3:** Crea visualizaciones comparativas múltiples:

```python
# Dashboard de comparación Liverpool vs élite europea

# TU CÓDIGO AQUÍ:
# 1. Crear subplot con 6 visualizaciones:
#    - Gráfico de barras: Top 10 equipos por puntos (destacar Liverpool)
#    - Scatter plot: Eficiencia presupuestaria (Puntos vs Presupuesto)
#    - Boxplot: Distribución de goles por liga (destacar Liverpool)
#    - Heatmap: Correlación entre métricas (solo equipos top)
#    - Pie chart: Proporción de victorias/empates/derrotas Liverpool
#    - Line plot: Progresión temporal simulada del Liverpool

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Panel 1: Top 10 equipos por puntos
ax1 = axes[0, 0]
# Implementar gráfico de barras

# Panel 2: Eficiencia presupuestaria
ax2 = axes[0, 1]  
# Implementar scatter plot

# Panel 3: Distribución goles por liga
ax3 = axes[0, 2]
# Implementar boxplot

# Panel 4: Heatmap correlaciones
ax4 = axes[1, 0]
# Implementar heatmap

# Panel 5: Distribución resultados Liverpool
ax5 = axes[1, 1]
# Implementar pie chart

# Panel 6: Tendencia temporal
ax6 = axes[1, 2]
# Implementar line plot

plt.suptitle("Dashboard Liverpool FC: Análisis Comparativo Temporada 2023-24", 
             fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("Dashboard comparativo Liverpool FC generado")
```

**Paso 4:** Crea visualización de rendimiento por competición:

```python
# Análisis de rendimiento Liverpool por tipo de competición

# TU CÓDIGO AQUÍ:
# 1. Simular datos de Liverpool en diferentes competiciones:
#    - Premier League, Champions League, FA Cup, Carabao Cup
# 2. Crear gráfico de barras agrupadas por competición
# 3. Mostrar goles favor, goles contra, puntos por partido
# 4. Incluir líneas de promedio general
# 5. Personalizar con colores del Liverpool
# 6. Añadir anotaciones explicativas

competiciones_liverpool = {
    'Premier League': {'partidos': 38, 'puntos': 82, 'goles_favor': 86, 'goles_contra': 41},
    'Champions League': {'partidos': 8, 'puntos': 18, 'goles_favor': 24, 'goles_contra': 12},
    'FA Cup': {'partidos': 6, 'puntos': 15, 'goles_favor': 18, 'goles_contra': 8},
    'Carabao Cup': {'partidos': 4, 'puntos': 9, 'goles_favor': 12, 'goles_contra': 5}
}

print("=== RENDIMIENTO LIVERPOOL POR COMPETICIÓN ===")
# Implementar visualización por competición
```

### Criterios de Evaluación
- **Dashboard completo y coherente** (15 puntos)
- **Visualizaciones especializadas efectivas** (10 puntos)

---

## Parte 3: Storytelling Visual con Datos (25 puntos)

### Objetivo
Crear una narrativa visual que cuente la historia del Liverpool a través de datos.

### Instrucciones Detalladas

**Paso 5:** Desarrolla narrativa visual progresiva:

```python
# Storytelling: La temporada del Liverpool en datos

# TU CÓDIGO AQUÍ:
# 1. Crear secuencia de 4 gráficos que cuenten una historia:
#    - Gráfico 1: "El Punto de Partida" (posición inicial vs objetivos)
#    - Gráfico 2: "El Camino" (evolución durante la temporada)
#    - Gráfico 3: "Los Desafíos" (comparación con rivales)
#    - Gráfico 4: "El Resultado" (logros y áreas de mejora)
# 2. Usar anotaciones, flechas y texto explicativo
# 3. Colores consistentes y progresión visual clara
# 4. Cada gráfico debe tener un mensaje principal

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Historia 1: El Punto de Partida
ax1 = axes[0, 0]
# Crear visualización de objetivos vs realidad inicial
ax1.set_title("1. El Punto de Partida", fontsize=14, fontweight='bold')

# Historia 2: El Camino  
ax2 = axes[0, 1]
# Mostrar evolución durante temporada
ax2.set_title("2. El Camino Recorrido", fontsize=14, fontweight='bold')

# Historia 3: Los Desafíos
ax3 = axes[1, 0]
# Comparar con principales rivales
ax3.set_title("3. Los Desafíos Enfrentados", fontsize=14, fontweight='bold')

# Historia 4: El Resultado
ax4 = axes[1, 1]
# Mostrar logros y áreas de mejora
ax4.set_title("4. El Resultado Final", fontsize=14, fontweight='bold')

plt.suptitle("La Temporada del Liverpool FC: Una Historia en Datos", 
             fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("=== NARRATIVA VISUAL LIVERPOOL ===")
print("Historia de la temporada contada a través de datos")
```

**Paso 6:** Crea infografía ejecutiva:

```python
# Infografía ejecutiva: Liverpool FC en números

# TU CÓDIGO AQUÍ:
# 1. Crear infografía estilo "fact sheet" con métricas clave
# 2. Usar iconos, colores y tipografía atractiva
# 3. Incluir comparaciones clave (vs temporada anterior, vs rivales)
# 4. Métricas destacadas: puntos, posición, goles, eficiencia
# 5. Sección de logros y reconocimientos
# 6. Proyecciones para próxima temporada

fig, ax = plt.subplots(figsize=(12, 16))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

# Título principal
ax.text(5, 13, "LIVERPOOL FC", fontsize=32, fontweight='bold', 
        ha='center', color='#C8102E')
ax.text(5, 12.5, "TEMPORADA 2023-24 EN NÚMEROS", fontsize=16, 
        ha='center', color='#212121')

# Implementar secciones de la infografía
# Sección 1: Métricas principales
# Sección 2: Comparaciones
# Sección 3: Logros destacados
# Sección 4: Proyecciones

plt.savefig('liverpool_infografia_2023-24.png', dpi=300, bbox_inches='tight')
plt.show()

print("Infografía ejecutiva Liverpool FC generada")
```

### Criterios de Evaluación
- **Narrativa visual coherente y efectiva** (15 puntos)
- **Infografía profesional y atractiva** (10 puntos)

---

## Parte 4: Visualización para Diferentes Audiencias (25 puntos)

### Objetivo
Adaptar visualizaciones para diferentes stakeholders del Liverpool FC.

### Instrucciones Detalladas

**Paso 7:** Crea visualizaciones específicas por audiencia:

```python
# Visualizaciones adaptadas por audiencia objetivo

# TU CÓDIGO AQUÍ:
# 1. Audiencia 1: Junta Directiva (métricas financieras y estratégicas)
# 2. Audiencia 2: Cuerpo Técnico (métricas tácticas y rendimiento)
# 3. Audiencia 3: Medios de Comunicación (métricas atractivas y destacadas)
# 4. Audiencia 4: Aficionados (métricas emocionales y comparativas)

def visualizacion_junta_directiva():
    """Gráficos enfocados en ROI, eficiencia presupuestaria, valor de marca"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Gráfico 1: ROI presupuestario
    # Gráfico 2: Comparación financiera vs rivales
    # Gráfico 3: Valor de marca y proyecciones
    
    plt.suptitle("Liverpool FC - Reporte Ejecutivo Junta Directiva", fontweight='bold')
    return fig

def visualizacion_cuerpo_tecnico():
    """Gráficos enfocados en táctica, rendimiento individual, patrones de juego"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Gráfico 1: Mapa de calor posicional
    # Gráfico 2: Eficiencia por zona del campo
    # Gráfico 3: Rendimiento individual por posición
    # Gráfico 4: Patrones tácticos vs rivales
    
    plt.suptitle("Liverpool FC - Análisis Técnico Avanzado", fontweight='bold')
    return fig

def visualizacion_medios():
    """Gráficos atractivos, fáciles de entender, con cifras impactantes"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Gráfico principal: Comparación visual impactante
    # Elementos destacados, colores llamativos, cifras grandes
    
    plt.title("Liverpool FC - Los Números que Impresionan", fontweight='bold')
    return fig

def visualizacion_aficionados():
    """Gráficos emotivos, comparaciones históricas, logros destacados"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Gráfico 1: Evolución histórica del club
    # Gráfico 2: Comparación con el pasado glorioso
    # Gráfico 3: Jugadores estrella del equipo
    # Gráfico 4: Próximos objetivos y sueños
    
    plt.suptitle("Liverpool FC - Para Nuestros Fieles Seguidores", fontweight='bold')
    return fig

print("=== VISUALIZACIONES POR AUDIENCIA ===")
# Generar cada tipo de visualización
```

**Paso 8:** Evalúa la efectividad de las visualizaciones:

```python
# Sistema de evaluación de efectividad visual

# TU CÓDIGO AQUÍ:
# 1. Crear criterios de evaluación por audiencia:
#    - Claridad del mensaje
#    - Relevancia de la información
#    - Atractivo visual
#    - Facilidad de comprensión
# 2. Autoevaluar cada visualización creada
# 3. Proponer mejoras específicas
# 4. Crear checklist de buenas prácticas
# 5. Documentar lecciones aprendidas

criterios_evaluacion = {
    'Junta Directiva': {
        'enfoque': 'Estratégico y financiero',
        'metricas_clave': ['ROI', 'Eficiencia', 'Competitividad'],
        'estilo': 'Profesional, sobrio, preciso'
    },
    'Cuerpo Técnico': {
        'enfoque': 'Táctico y rendimiento',
        'metricas_clave': ['Rendimiento', 'Patrones', 'Mejoras'],
        'estilo': 'Detallado, técnico, actionable'
    },
    'Medios': {
        'enfoque': 'Impacto y simplicidad',
        'metricas_clave': ['Highlights', 'Comparaciones', 'Records'],
        'estilo': 'Atractivo, simple, memorable'
    },
    'Aficionados': {
        'enfoque': 'Emocional y aspiracional',
        'metricas_clave': ['Historia', 'Orgullo', 'Futuro'],
        'estilo': 'Emotivo, inspirador, accesible'
    }
}

print("=== EVALUACIÓN DE EFECTIVIDAD VISUAL ===")
print("\n📊 RESUMEN DE VISUALIZACIONES CREADAS:")
for audiencia, criterios in criterios_evaluacion.items():
    print(f"\n{audiencia.upper()}:")
    print(f"  Enfoque: {criterios['enfoque']}")
    print(f"  Métricas: {', '.join(criterios['metricas_clave'])}")
    print(f"  Estilo: {criterios['estilo']}")

print("\n🎯 LECCIONES APRENDIDAS:")
print("1. [Tu reflexión sobre audiencias específicas]")
print("2. [Tu reflexión sobre diseño efectivo]")
print("3. [Tu reflexión sobre storytelling visual]")
```

### Criterios de Evaluación
- **Adaptación efectiva por audiencia** (15 puntos)
- **Reflexión y evaluación crítica** (10 puntos)

## Criterios de Evaluación General

### Correctitud Técnica (40 puntos)
- Visualizaciones ejecutan sin errores
- Uso correcto de librerías de visualización
- Implementación adecuada de gráficos especializados
- Personalización efectiva de estilos y colores

### Aplicación Práctica (30 puntos)
- Visualizaciones relevantes para análisis deportivo
- Adaptación apropiada para diferentes audiencias
- Storytelling efectivo con datos
- Insights comunicados claramente

### Claridad y Documentación (30 puntos)
- Gráficos profesionales y bien diseñados
- Etiquetas, títulos y leyendas claros
- Código bien comentado en español
- Narrativa visual coherente y atractiva

## Instrucciones de Entrega

1. **Completa todas las visualizaciones** con calidad profesional
2. **Incluye reflexiones** sobre decisiones de diseño
3. **Verifica legibilidad** en diferentes tamaños de pantalla
4. **Guarda como:** `[matricula]-ejercicio-semana-9.ipynb`
5. **Entrega antes del final de Semana 9**

## Recursos de Apoyo

- Notebook de la Semana 9: `visualizacion-datos.ipynb`
- Dataset: `equipos-europa-2023-24.csv`
- Paletas de colores: Colores oficiales de equipos
- Guía de visualización efectiva en deportes

---

**¡Transforma los datos del Liverpool FC en historias visuales que inspiren y informen!** ⚽🎨

```python
# Crear visualización tipo radar para comparar equipos

def crear_radar_equipos(equipos_data, equipos_seleccionados, metricas):
    """
    Crea gráfico de radar para comparar múltiples equipos
    
    Parámetros:
    equipos_data (DataFrame): Datos de equipos
    equipos_seleccionados (list): Lista de nombres de equipos
    metricas (list): Lista de métricas a incluir
    """
    # Tu código aquí:
    # 1. Filtrar datos para equipos seleccionados
    # 2. Normalizar métricas a escala 0-100
    # 3. Crear gráfico de radar con matplotlib/plotly
    # 4. Personalizar colores por equipo
    # 5. Agregar leyenda y títulos apropiados
    # 6. Incluir anotaciones explicativas
    pass

# Métricas para comparar
metricas_equipos = ['Puntos', 'Goles_Favor', 'Victorias', 'Presupuesto']
equipos_comparar = ['Barcelona', 'Real Madrid', 'Manchester City']

# crear_radar_equipos(df_equipos, equipos_comparar, metricas_equipos)
```

### Mapa de Calor de Rendimiento Temporal

```python
# Crear heatmap de rendimiento por semanas/meses
# Simular datos temporales para demostración

np.random.seed(42)
semanas = list(range(1, 39))  # 38 jornadas de liga
equipos_liga = ['Barcelona', 'Real Madrid', 'Atletico', 'Valencia', 'Sevilla']

# Simular puntos por jornada
datos_temporal = []
for equipo in equipos_liga:
    for semana in semanas:
        puntos = np.random.choice([0, 1, 3], p=[0.2, 0.3, 0.5])  # Derrota, empate, victoria
        datos_temporal.append({
            'Equipo': equipo,
            'Jornada': semana,
            'Puntos': puntos
        })

df_temporal = pd.DataFrame(datos_temporal)

# Tu código aquí:
# 1. Crear pivot table con equipos vs jornadas
# 2. Generar heatmap con seaborn
# 3. Personalizar colores para representar rendimiento
# 4. Agregar líneas divisorias por meses
# 5. Incluir anotaciones para rachas importantes
# 6. Crear versión interactiva con plotly
```

### Respuesta

*Completa las visualizaciones deportivas especializadas.*

## Ejercicio 2: Dashboard Interactivo de Análisis (20 puntos)

### Panel de Control de Liga

```python
# Crear dashboard multi-panel usando plotly

def crear_dashboard_liga(df_equipos, df_jugadores):
    """
    Crea dashboard interactivo para análisis de liga
    """
    # Tu código aquí:
    # 1. Panel 1: Clasificación actual (barplot horizontal)
    # 2. Panel 2: Distribución de goles por equipo (boxplot)
    # 3. Panel 3: Eficiencia económica (scatter: presupuesto vs puntos)
    # 4. Panel 4: Top jugadores por valor (treemap o barplot)
    # 5. Conectar paneles con filtros interactivos
    # 6. Agregar controles para seleccionar liga
    # 7. Incluir métricas resumen en texto
    
    # Usar plotly.subplots para layout
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Clasificación', 'Distribución Goles', 
                       'Eficiencia Económica', 'Top Jugadores'),
        specs=[[{"type": "bar"}, {"type": "box"}],
               [{"type": "scatter"}, {"type": "bar"}]]
    )
    
    # Agregar cada gráfico al subplot correspondiente
    # ...
    
    return fig

# dashboard = crear_dashboard_liga(df_equipos, df_jugadores)
# dashboard.show()
```

### Visualización de Redes de Transferencias

```python
# Crear visualización de red simulando transferencias entre ligas

# Simular datos de transferencias
transferencias_data = {
    'Liga_Origen': ['La Liga', 'Premier League', 'Serie A', 'Bundesliga', 'Ligue 1'] * 4,
    'Liga_Destino': ['Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Premier League'] * 4,
    'Numero_Transferencias': np.random.randint(1, 8, 20),
    'Valor_Total_Millones': np.random.randint(50, 500, 20)
}

df_transferencias = pd.DataFrame(transferencias_data)

# Tu código aquí:
# 1. Crear matriz de transferencias entre ligas
# 2. Generar gráfico de cuerdas (chord diagram) o red
# 3. Usar grosor de líneas para representar volumen
# 4. Colorear por liga de origen
# 5. Agregar información de hover con detalles
# 6. Crear versión estática con matplotlib
# 7. Implementar versión interactiva con plotly
```

### Respuesta

*Completa el dashboard interactivo y visualización de redes.*

## Ejercicio 3: Storytelling con Datos Deportivos (20 puntos)

### Narrativa Visual de Temporada

```python
# Crear historia visual de una temporada ficticia

# Simular evolución de puntos a lo largo de la temporada
jornadas = list(range(1, 39))
equipos = ['Equipo A', 'Equipo B', 'Equipo C']

# Crear tres historias diferentes:
# Equipo A: Líder constante
# Equipo B: Remontada épica
# Equipo C: Colapso final

puntos_acumulados = {
    'Equipo A': np.cumsum([3, 3, 1, 3, 3, 0, 3, 1] + [np.random.choice([0,1,3], p=[0.1,0.2,0.7]) for _ in range(30)]),
    'Equipo B': np.cumsum([0, 1, 0, 1, 0, 3] + [np.random.choice([0,1,3], p=[0.05,0.15,0.8]) for _ in range(32)]),
    'Equipo C': np.cumsum([3, 3, 3, 3, 1, 3] + [np.random.choice([0,1,3], p=[0.4,0.3,0.3]) for _ in range(32)])
}

# Tu código aquí:
# 1. Crear gráfico de línea con evolución temporal
# 2. Agregar anotaciones para momentos clave
# 3. Usar colores y estilos para destacar narrativa
# 4. Incluir zonas sombreadas para diferentes fases
# 5. Agregar elementos visuales (flechas, círculos) para enfasis
# 6. Crear múltiples vistas de la misma historia
# 7. Implementar animación básica de la evolución
```

### Infografía de Comparación de Jugadores

```python
# Crear infografía estilo deportivo para comparar jugadores

def crear_infografia_jugador(jugador_data, metricas_importantes):
    """
    Crea infografía estilo deportivo para un jugador
    """
    # Tu código aquí:
    # 1. Diseñar layout con información del jugador
    # 2. Crear gráficos pequeños (sparklines) para tendencias
    # 3. Usar iconos y elementos gráficos deportivos
    # 4. Implementar escalas visuales (medidores, barras)
    # 5. Agregar comparación con promedio de liga/posición
    # 6. Usar tipografía y colores llamativos
    # 7. Exportar como imagen de alta calidad
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle(f"Perfil de Rendimiento: {jugador_data['Nombre']}", 
                 fontsize=20, fontweight='bold')
    
    # Implementar cada sección de la infografía
    # ...
    
    return fig

# Crear infografías para jugadores destacados
# jugadores_destacados = ['Messi', 'Haaland', 'Mbappé']
# for jugador in jugadores_destacados:
#     datos_jugador = df_jugadores[df_jugadores['Nombre'] == jugador].iloc[0]
#     crear_infografia_jugador(datos_jugador, ['Goles', 'Asistencias', 'Valor_Mercado'])
```

### Respuesta

*Completa el storytelling visual y las infografías deportivas.*

## Ejercicio 4: Visualizaciones Personalizadas (20 puntos)

### Gráfico de Campo de Fútbol con Datos

```python
# Crear visualización en forma de campo de fútbol

def crear_campo_futbol_datos(datos_posiciones, metricas):
    """
    Crea visualización de campo de fútbol con datos de jugadores
    """
    # Tu código aquí:
    # 1. Dibujar campo de fútbol usando matplotlib patches
    # 2. Posicionar jugadores según su posición real
    # 3. Usar tamaño de puntos para representar una métrica
    # 4. Usar colores para representar otra métrica
    # 5. Agregar leyendas explicativas
    # 6. Incluir líneas de conexión para pases/asistencias
    # 7. Animar movimientos básicos
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Dibujar campo
    campo = Rectangle((0, 0), 100, 60, linewidth=2, 
                     edgecolor='white', facecolor='green', alpha=0.8)
    ax.add_patch(campo)
    
    # Agregar líneas del campo
    # ... líneas centrales, áreas, etc.
    
    # Posicionar jugadores con datos
    # ...
    
    return fig

# Simular datos de posiciones
posiciones_data = {
    'Jugador': ['Portero', 'Defensa1', 'Defensa2', 'Medio1', 'Medio2', 'Delantero'],
    'X': [10, 25, 25, 50, 50, 80],  # Posición horizontal
    'Y': [30, 15, 45, 20, 40, 30],  # Posición vertical
    'Goles': [0, 2, 1, 5, 3, 15],
    'Pases': [80, 60, 55, 85, 70, 45]
}

# crear_campo_futbol_datos(posiciones_data, ['Goles', 'Pases'])
```

### Gráfico de Densidad de Rendimiento

```python
# Crear visualización de densidad para analizar zonas de rendimiento

# Tu código aquí:
# 1. Crear gráfico de densidad 2D (goles vs asistencias)
# 2. Identificar zonas de alto/bajo rendimiento
# 3. Sobreponer puntos de jugadores específicos
# 4. Usar contornos para delimitar categorías de rendimiento
# 5. Agregar líneas de referencia (promedios, percentiles)
# 6. Crear versión interactiva con hover information
# 7. Implementar filtros por posición/liga
```

### Gráfico de Evolución de Carrera

```python
# Visualizar evolución hipotética de carrera de jugadores

# Simular datos de carrera
edades = list(range(18, 36))
jugadores_carrera = {
    'Messi': [5, 8, 12, 16, 25, 28, 31, 45, 38, 36, 41, 54, 46, 37, 32, 28, 22, 12],
    'Ronaldo': [3, 6, 9, 15, 21, 26, 31, 42, 48, 44, 51, 55, 44, 34, 28, 25, 20, 15],
    'Benzema': [2, 5, 8, 11, 15, 18, 21, 24, 27, 30, 32, 30, 27, 24, 21, 18, 12, 8]
}

# Tu código aquí:
# 1. Crear gráfico de área apilada para múltiples jugadores
# 2. Marcar picos de rendimiento y declines
# 3. Agregar eventos importantes (transferencias, lesiones)
# 4. Usar degradados de color para mostrar evolución
# 5. Incluir líneas de tendencia
# 6. Crear animación de la evolución temporal
# 7. Agregar predicciones para años futuros
```

### Respuesta

*Completa las visualizaciones personalizadas y creativas.*

## Ejercicio 5: Optimización y Mejores Prácticas (20 puntos)

### Análisis de Audiencia y Adaptación

```python
# Crear diferentes versiones de la misma visualización para diferentes audiencias

def crear_version_ejecutiva(datos):
    """Versión simplificada para ejecutivos"""
    # Tu código aquí:
    # 1. Enfocarse en métricas clave de negocio
    # 2. Usar colores corporativos
    # 3. Incluir solo insights principales
    # 4. Formato de presentación limpio
    pass

def crear_version_tecnica(datos):
    """Versión detallada para analistas"""
    # Tu código aquí:
    # 1. Incluir todas las métricas disponibles
    # 2. Mostrar intervalos de confianza
    # 3. Agregar anotaciones técnicas
    # 4. Incluir datos estadísticos detallados
    pass

def crear_version_publica(datos):
    """Versión atractiva para redes sociales"""
    # Tu código aquí:
    # 1. Diseño llamativo y colorido
    # 2. Elementos gráficos deportivos
    # 3. Mensajes claros y directos
    # 4. Formato optimizado para compartir
    pass

# Aplicar a un mismo dataset
datos_ejemplo = df_equipos[df_equipos['Liga'] == 'La Liga']
# crear_version_ejecutiva(datos_ejemplo)
# crear_version_tecnica(datos_ejemplo)
# crear_version_publica(datos_ejemplo)
```

### Sistema de Evaluación de Visualizaciones

```python
def evaluar_visualizacion(fig, criterios_evaluacion):
    """
    Evalúa calidad de una visualización según criterios específicos
    
    Criterios:
    - Claridad del mensaje
    - Apropiado para audiencia
    - Uso efectivo de color
    - Accesibilidad
    - Impacto visual
    """
    # Tu código aquí:
    # 1. Definir métricas de evaluación
    # 2. Crear checklist de mejores prácticas
    # 3. Evaluar accesibilidad (daltonismo, contraste)
    # 4. Verificar que el gráfico responda la pregunta planteada
    # 5. Generar score de calidad
    # 6. Proponer mejoras específicas
    # 7. Documentar proceso de evaluación
    pass

# Criterios estándar para visualizaciones deportivas
criterios_deportivos = {
    'mensaje_claro': 'El gráfico comunica un insight específico',
    'contexto_deportivo': 'Relevante para análisis futbolístico',
    'precision_datos': 'Representación fiel de los datos',
    'estetica': 'Visualmente atractivo y profesional',
    'interactividad': 'Permite exploración de datos'
}

# evaluar_visualizacion(mi_grafico, criterios_deportivos)
```

### Automatización de Reportes Visuales

```python
def generar_reporte_automatico(df_equipos, df_jugadores, liga_seleccionada):
    """
    Genera reporte visual automático para una liga específica
    """
    # Tu código aquí:
    # 1. Filtrar datos por liga seleccionada
    # 2. Generar automáticamente 6-8 visualizaciones clave
    # 3. Crear narrativa automática basada en datos
    # 4. Formatear como presentación o PDF
    # 5. Incluir conclusiones generadas automáticamente
    # 6. Agregar recomendaciones basadas en análisis
    # 7. Exportar en múltiples formatos
    
    # Template de reporte
    figuras_reporte = []
    
    # Gráfico 1: Clasificación actual
    # Gráfico 2: Análisis de goles
    # Gráfico 3: Eficiencia económica
    # Gráfico 4: Jugadores destacados
    # Gráfico 5: Tendencias temporales
    # Gráfico 6: Comparaciones
    
    return figuras_reporte

# Generar reportes para diferentes ligas
# ligas_disponibles = df_equipos['Liga'].unique()
# for liga in ligas_disponibles:
#     reporte = generar_reporte_automatico(df_equipos, df_jugadores, liga)
#     # Guardar reporte
```

### Respuesta

*Completa la optimización y sistema de mejores prácticas.*

## Ejercicio Bonus: Visualización en Tiempo Real (10 puntos extra)

### Dashboard en Vivo Simulado

**Ejercicio opcional para puntos adicionales:**

```python
# Simular dashboard que se actualiza en tiempo real

import time
from IPython.display import clear_output

def simular_dashboard_vivo():
    """
    Simula dashboard que se actualiza durante un partido
    """
    # Tu código aquí:
    # 1. Crear estructura de dashboard base
    # 2. Simular datos que cambian cada minuto
    # 3. Actualizar visualizaciones automáticamente
    # 4. Agregar alertas para eventos importantes
    # 5. Incluir cronómetro del partido
    # 6. Mostrar estadísticas acumulativas
    # 7. Implementar notificaciones de goles/tarjetas
    
    for minuto in range(0, 91, 5):  # Partido de 90 minutos, actualizar cada 5
        clear_output(wait=True)
        
        # Actualizar datos
        # Regenerar gráficos
        # Mostrar dashboard actualizado
        
        print(f"Minuto {minuto} del partido")
        time.sleep(1)  # Simular tiempo real

# simular_dashboard_vivo()
```

### Respuesta Bonus

*Ejercicio opcional: Crea sistema de visualización en tiempo real.*

## Criterios de Evaluación

### Técnica de Visualización (40%)

- [ ] Dominio de herramientas (matplotlib, seaborn, plotly) (15%)
- [ ] Implementación correcta de gráficos especializados (15%)
- [ ] Uso efectivo de interactividad (10%)

### Diseño y Comunicación (35%)

- [ ] Principios de diseño visual aplicados correctamente (15%)
- [ ] Storytelling efectivo con datos (10%)
- [ ] Adaptación apropiada para audiencia (10%)

### Innovación y Creatividad (25%)

- [ ] Originalidad en visualizaciones personalizadas (15%)
- [ ] Aplicación creativa a contexto deportivo (10%)

## Instrucciones de Entrega

1. **Completa todos los ejercicios** con visualizaciones funcionales
2. **Incluye interpretaciones** para cada gráfico creado
3. **Documenta decisiones de diseño** visual
4. **Guarda como:** `ejercicio-semana-9-[tu-apellido].ipynb`
5. **Entrega antes del final de Semana 9**

## Recursos de Apoyo

- Notebook de la Semana 9: `visualizacion-datos.ipynb`
- Plotly documentation: <https://plotly.com/python/>
- Matplotlib gallery: <https://matplotlib.org/stable/gallery/>
- Seaborn tutorial: <https://seaborn.pydata.org/tutorial.html>
- Color palettes: <https://colorbrewer2.org/>

---

**¡Transforma números en historias visuales que cautiven y comuniquen!** ⚽🎨

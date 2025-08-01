# Ejercicio Semana 9: Visualización Avanzada de Datos Deportivos

## Información del Ejercicio

**Bloque:** 2 - Fundamentos de Data Science  
**Peso:** 12% de la calificación del bloque (60% ÷ 5 ejercicios)  
**Tiempo estimado:** 3-3.5 horas  
**Entrega:** Final de Semana 9

## Objetivos

Al completar este ejercicio, serás capaz de:

- Crear visualizaciones avanzadas específicas para análisis deportivo
- Aplicar principios de diseño visual para comunicación efectiva
- Desarrollar dashboards interactivos básicos para análisis futbolístico
- Implementar storytelling con datos usando visualizaciones
- Crear gráficos personalizados para métricas deportivas específicas
- Optimizar visualizaciones para diferentes audiencias

## Configuración Inicial

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

# Configurar estilos
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12

# Cargar datos
df_equipos = pd.read_csv('equipos-europa-2023-24.csv')
df_jugadores = pd.read_csv('jugadores-estrellas-2024.csv')

print("¡Herramientas de visualización avanzada listas!")
```

## Ejercicio 1: Visualizaciones Deportivas Especializadas (20 puntos)

### Gráfico de Radar para Análisis de Equipos

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

---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.2
  kernelspec:
    display_name: .venv
    language: python
    name: python3
---

# Semana 5: ¿Cómo convierten los datos en historias visuales los medios deportivos?

## SESIÓN 1: ¿Por qué una imagen vale más que mil números? (50 min)
**Pregunta guía**: ¿Qué es más impactante: una tabla con estadísticas o un gráfico que muestra tendencias?

## SESIÓN 2: ¿Cómo crean visualizaciones profesionales como ESPN? (50 min)  
**Pregunta guía**: ¿Qué elementos hacen que una visualización sea profesional e impactante?

## SESIÓN 3: ¿Cómo integras múltiples gráficos en un dashboard ejecutivo? (50 min)
**Pregunta guía**: ¿Cómo crearías un panel de control que comunique insights complejos instantáneamente?

---

### Pregunta Central de la Semana
**¿Te has preguntado por qué los comentaristas deportivos usan gráficos en lugar de solo mencionar números durante las transmisiones?**

### Tu descubrimiento esta semana
Vas a aprender por qué la visualización de datos es fundamental en el análisis deportivo:
- **Comunicación instantánea**: El cerebro procesa imágenes 60,000 veces más rápido que texto
- **Identificación de patrones**: Tendencias invisibles en números se vuelven obvias
- **Impacto profesional**: Tus análisis rivalizarán con medios deportivos profesionales

### Conexión con tu experiencia
¿Recuerdas algún gráfico deportivo que te haya impactado en TV? ¿Qué lo hacía especial?

---


# SESIÓN 1: ¿Por qué necesitas comunicar visualmente en lugar de solo con números?
**(50 minutos)**

## Pregunta Central de la Sesión
**¿Te has preguntado por qué los analistas deportivos en TV usan gráficos en lugar de solo leer estadísticas?**

### Tu situación actual
Imagina que debes explicar el rendimiento goleador de 5 jugadores a un entrenador que tiene solo 30 segundos para entender la información.

### Reflexión inicial
¿Qué funcionaría mejor?
- **Opción A**: "Messi tiene 25 goles, Benzema 20, Lewandowski 22, Griezmann 15, Morata 13"
- **Opción B**: Un gráfico de barras que muestre visualmente las diferencias

### Analogía deportiva
**Piensa en esto**: ¿Por qué crees que los marcadores en TV muestran barras de progreso en lugar de solo números cuando comparan estadísticas?

### Tu descubrimiento fundamental
El cerebro humano procesa información visual 60,000 veces más rápido que texto. Por eso los medios deportivos profesionales nunca presentan solo números.

---

## Descubriendo Matplotlib: Tu herramienta profesional

### ¿Qué es Matplotlib?
La librería estándar que usan científicos de datos en todo el mundo para crear visualizaciones profesionales.

### Primera pregunta práctica
¿Cómo crees que se vería la diferencia entre comunicar datos con números versus con gráficos profesionales?


# Importando matplotlib - La herramienta estándar para gráficos
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Configuración para gráficos más profesionales
plt.style.use('default')  # Estilo limpio y profesional

print("Matplotlib importado exitosamente")
print("Listo para crear visualizaciones profesionales")
print()

# ===============================
# PRIMER GRÁFICO: Goles por Jugador
# ===============================

# Datos de goleadores de La Liga
jugadores = ['Lewandowski', 'Benzema', 'Griezmann', 'Aspas', 'Morata']
goles = [23, 19, 15, 14, 13]

# Creando nuestro primer gráfico de barras
plt.figure(figsize=(10, 6))  # Tamaño del gráfico
plt.bar(jugadores, goles, color='skyblue', edgecolor='navy', linewidth=1.2)

# Personalizando el gráfico
plt.title('Top 5 Goleadores de La Liga 2023-24', fontsize=16, fontweight='bold')
plt.xlabel('Jugadores', fontsize=12)
plt.ylabel('Goles Anotados', fontsize=12)

# Añadiendo valores sobre las barras
for i, v in enumerate(goles):
    plt.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

# Rotando nombres para mejor legibilidad
plt.xticks(rotation=45)
plt.tight_layout()  # Ajusta automáticamente el espaciado

plt.show()

print("¿Notas cómo el gráfico comunica la información instantáneamente?")
print("¿Qué patrones puedes identificar que serían difíciles de ver en una tabla?")


## Gráficos de Líneas: Mostrando Evolución en el Tiempo

**Pregunta clave**: ¿Cómo mostrarías el progreso de un equipo a lo largo de una temporada?

Los gráficos de líneas son perfectos para mostrar **cambios a través del tiempo**.

```python
# ===============================
# GRÁFICO DE LÍNEAS: Evolución de Puntos
# ===============================

# Simulando evolución de puntos a lo largo de 15 jornadas
jornadas = list(range(1, 16))
real_madrid = [3, 6, 7, 10, 13, 16, 19, 22, 25, 28, 31, 32, 35, 38, 41]
barcelona = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 37, 38, 40]
atletico = [1, 4, 7, 8, 11, 14, 17, 20, 23, 26, 27, 30, 33, 36, 37]

plt.figure(figsize=(12, 7))

# Creando líneas para cada equipo
plt.plot(jornadas, real_madrid, marker='o', linewidth=2.5, label='Real Madrid', color='purple')
plt.plot(jornadas, barcelona, marker='s', linewidth=2.5, label='Barcelona', color='blue')
plt.plot(jornadas, atletico, marker='^', linewidth=2.5, label='Atletico Madrid', color='red')

# Personalizando el gráfico
plt.title('Evolución de Puntos por Jornada - La Liga', fontsize=16, fontweight='bold')
plt.xlabel('Jornada', fontsize=12)
plt.ylabel('Puntos Acumulados', fontsize=12)

# Añadiendo cuadrícula para mejor lectura
plt.grid(True, alpha=0.3, linestyle='--')

# Leyenda para identificar equipos
plt.legend(fontsize=11)

# Resaltando la posición actual
plt.axhline(y=40, color='gold', linestyle=':', alpha=0.7, label='Línea de Liderato')

plt.tight_layout()
plt.show()

print("=== INSIGHTS VISUALES ===")
print("¿Qué patrones puedes identificar que serían invisibles en una tabla?")
print("• ¿En qué jornada se separó más el Real Madrid?")
print("• ¿Cuándo tuvo Barcelona su peor racha?")
print("• ¿El Atletico mantuvo un crecimiento constante?")
print("• ¿En qué momento la competencia fue más cerrada?")
```

## Gráficos de Dispersión: Descubriendo Relaciones

**Pregunta analítica**: ¿Existe relación entre los goles anotados por un equipo y los puntos que obtiene?

Los gráficos de dispersión nos ayudan a **visualizar correlaciones** entre dos variables.

```python
# ===============================
# GRÁFICO DE DISPERSIÓN: Goles vs Puntos
# ===============================

# Datos de equipos de La Liga (simulados pero realistas)
equipos = ['Real Madrid', 'Barcelona', 'Atletico', 'Sevilla', 'Valencia', 
           'Real Sociedad', 'Villarreal', 'Athletic', 'Betis', 'Osasuna',
           'Celta', 'Rayo', 'Espanyol', 'Getafe', 'Mallorca']

goles_favor = [68, 70, 55, 48, 42, 51, 45, 38, 47, 35, 
               39, 41, 33, 31, 29]
puntos_obtenidos = [78, 76, 66, 58, 53, 60, 55, 48, 54, 42,
                    44, 46, 37, 35, 33]

plt.figure(figsize=(11, 8))

# Creando gráfico de dispersión
scatter = plt.scatter(goles_favor, puntos_obtenidos, 
                     s=100, alpha=0.7, c=puntos_obtenidos, 
                     cmap='viridis', edgecolors='black', linewidth=1)

# Añadiendo línea de tendencia
z = np.polyfit(goles_favor, puntos_obtenidos, 1)
p = np.poly1d(z)
plt.plot(goles_favor, p(goles_favor), "r--", alpha=0.8, linewidth=2, 
         label=f'Tendencia: y={z[0]:.2f}x+{z[1]:.1f}')

# Etiquetando puntos importantes
for i, equipo in enumerate(equipos):
    if equipos[i] in ['Real Madrid', 'Barcelona', 'Atletico']:
        plt.annotate(equipo, (goles_favor[i], puntos_obtenidos[i]), 
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=9, fontweight='bold')

# Personalizando
plt.title('Relación entre Goles Anotados y Puntos Obtenidos', 
          fontsize=14, fontweight='bold')
plt.xlabel('Goles Anotados', fontsize=12)
plt.ylabel('Puntos Obtenidos', fontsize=12)

# Añadiendo barra de colores
cbar = plt.colorbar(scatter)
cbar.set_label('Puntos', fontsize=10)

# Grid y leyenda
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

# Calculando correlación
correlacion = np.corrcoef(goles_favor, puntos_obtenidos)[0, 1]
print(f"=== ANÁLISIS DE CORRELACIÓN ===")
print(f"Correlación goles-puntos: {correlacion:.3f}")
print(f"Interpretación: {'Correlación fuerte' if correlacion > 0.8 else 'Correlación moderada' if correlacion > 0.5 else 'Correlación débil'}")
print("¿Confirma esto tu intuición sobre la importancia del ataque en el fútbol?")
```

<!-- #region -->
### Actividad Práctica: Crea tu Primer Dashboard

**Tiempo estimado: 12 minutos**

**Tu desafío**: Crear un gráfico de barras que compare las asistencias de 5 mediocampistas.

**Datos sugeridos**:
```python
mediocampistas = ['Modric', 'Pedri', 'De Jong', 'Koke', 'Parejo']
asistencias = [12, 8, 6, 10, 7]
```

**Tareas**:
1. Crear gráfico de barras personalizado
2. Añadir título descriptivo
3. Incluir valores sobre las barras
4. Usar colores que representen los equipos
5. Interpretar qué insight comunica el gráfico

---

## Resumen de la Sesión 1 (50 minutos)

**¿Qué hemos descubierto sobre visualización de datos?**

### Tipos de Gráficos Aprendidos:
- **Gráficos de barras**: Para comparar valores entre categorías
- **Gráficos de líneas**: Para mostrar evolución temporal
- **Gráficos de dispersión**: Para descubrir relaciones entre variables

### Conceptos Clave:
- **Comunicación visual**: Las imágenes comunican más rápido que números
- **Personalización**: Títulos, colores y etiquetas mejoran la comprensión
- **Insights**: Los patrones visuales revelan información oculta en datos
- **Correlaciones**: Las relaciones entre variables se vuelven evidentes

### Aplicaciones Futbolísticas:
- Comparación de rendimiento entre jugadores
- Evolución de equipos a lo largo de la temporada
- Análisis de factores de éxito (goles vs puntos)
- Identificación de tendencias y patrones

**Pregunta para reflexionar**: ¿Cómo cambiaría tu capacidad de comunicar análisis deportivos si dominaras la visualización profesional?

---

**Próxima sesión**: Visualizaciones avanzadas - Múltiples series, subgráficos y personalización profesional para crear presentaciones impactantes.
<!-- #endregion -->

# Sesión 2: Visualizaciones Avanzadas - Comunicación Profesional
**(50 minutos)**

## Objetivo de la Sesión
Crear visualizaciones complejas y profesionales que comuniquen múltiples insights simultáneamente.

### Pregunta Central
**¿Cómo crearías visualizaciones que rivalizan con las que ves en ESPN o Sky Sports?**

**Desafío profesional**: Los analistas deportivos necesitan mostrar:
- Múltiples equipos en el mismo gráfico
- Comparaciones complejas entre estadísticas
- Visualizaciones que cuenten historias completas
- Gráficos que mantengan la atención del público

### ¿Qué Hace Profesional una Visualización?

**Elementos clave**:
- **Múltiples series de datos**: Varios equipos o jugadores simultáneamente
- **Subgráficos organizados**: Múltiples perspectivas en una sola imagen
- **Personalización avanzada**: Colores corporativos, estilos únicos
- **Narrativa visual**: Cada gráfico cuenta una historia específica

---

## Subgráficos: Múltiples Perspectivas en Una Vista

**Pregunta estratégica**: ¿Cómo mostrarías el rendimiento ofensivo y defensivo de un equipo simultáneamente?

```python
# ===============================
# SUBGRÁFICOS: Panel de Control Múltiple
# ===============================

# Datos para análisis completo
equipos = ['Real Madrid', 'Barcelona', 'Atletico', 'Sevilla', 'Valencia']
goles_favor = [68, 70, 55, 48, 42]
goles_contra = [32, 35, 40, 45, 50]
puntos = [78, 76, 66, 58, 53]
posesion = [58, 64, 52, 55, 49]

# Creando figura con múltiples subgráficos
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Análisis Integral de Equipos - La Liga 2023-24', fontsize=16, fontweight='bold')

# Subgráfico 1: Goles Favor vs Contra
x_pos = np.arange(len(equipos))
width = 0.35

ax1.bar(x_pos - width/2, goles_favor, width, label='Goles Favor', color='lightgreen', edgecolor='darkgreen')
ax1.bar(x_pos + width/2, goles_contra, width, label='Goles Contra', color='lightcoral', edgecolor='darkred')
ax1.set_title('Rendimiento Ofensivo vs Defensivo')
ax1.set_xlabel('Equipos')
ax1.set_ylabel('Goles')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(equipos, rotation=45)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Subgráfico 2: Evolución de Puntos (simulada)
jornadas = list(range(1, 16))
madrid_puntos = np.cumsum([3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3])
barca_puntos = np.cumsum([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1])

ax2.plot(jornadas, madrid_puntos, marker='o', linewidth=3, label='Real Madrid', color='purple')
ax2.plot(jornadas, barca_puntos, marker='s', linewidth=3, label='Barcelona', color='blue')
ax2.set_title('Evolución de Puntos')
ax2.set_xlabel('Jornada')
ax2.set_ylabel('Puntos Acumulados')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Subgráfico 3: Correlación Posesión vs Puntos
ax3.scatter(posesion, puntos, s=150, alpha=0.7, c=puntos, cmap='viridis', edgecolors='black')
ax3.set_title('Posesión vs Rendimiento')
ax3.set_xlabel('Posesión Promedio (%)')
ax3.set_ylabel('Puntos Totales')
ax3.grid(True, alpha=0.3)

# Añadir línea de tendencia
z = np.polyfit(posesion, puntos, 1)
p = np.poly1d(z)
ax3.plot(posesion, p(posesion), "r--", alpha=0.8)

# Subgráfico 4: Eficiencia Goleadora
eficiencia = [g/p*10 for g, p in zip(goles_favor, puntos)]  # Goles por cada 10 puntos
colors = ['gold', 'silver', '#CD7F32', 'lightblue', 'lightgray']

ax4.pie(eficiencia, labels=equipos, autopct='%1.1f%%', colors=colors, startangle=90)
ax4.set_title('Distribución de Eficiencia Goleadora')

plt.tight_layout()
plt.show()

print("=== INSIGHTS DEL PANEL MÚLTIPLE ===")
print("• ¿Qué equipo tiene mejor balance ofensivo-defensivo?")
print("• ¿Cuándo se definió la lucha por el título?")
print("• ¿La posesión garantiza mejores resultados?")
print("• ¿Qué equipo es más eficiente convirtiendo goles en puntos?")
```

## Personalización Profesional: Marca y Estilo

**Pregunta de identidad**: ¿Cómo harías que tus gráficos sean instantáneamente reconocibles como tuyos?

Los profesionales crean **identidad visual consistente** con colores, fuentes y estilos únicos.

```python
# ===============================
# PERSONALIZACIÓN AVANZADA: Gráfico de Marca
# ===============================

# Configurando estilo personalizado profesional
plt.style.use('seaborn-v0_8-darkgrid')

# Datos de rendimiento de jugadores
jugadores = ['Messi', 'Mbappé', 'Haaland', 'Benzema', 'Lewandowski']
goles = [30, 29, 36, 24, 33]
asistencias = [16, 8, 5, 11, 8]
valoracion = [8.2, 7.8, 8.5, 7.9, 8.1]

# Colores personalizados (paleta profesional)
colores_personalizados = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Configuración general de la figura
fig.patch.set_facecolor('#F8F9FA')
fig.suptitle('ANÁLISIS DE SUPERESTRELLAS MUNDIALES', 
             fontsize=20, fontweight='bold', color='#2C3E50', y=0.95)

# Gráfico 1: Rendimiento Goleador con estilo avanzado
ax1.bar(jugadores, goles, color=colores_personalizados, 
        edgecolor='white', linewidth=2, alpha=0.8)

# Añadiendo efectos visuales
for i, (jugador, gol) in enumerate(zip(jugadores, goles)):
    ax1.text(i, gol + 1, f'{gol}', ha='center', va='bottom', 
             fontweight='bold', fontsize=12, color='#2C3E50')
    
    # Añadiendo bandera emojis (simulado con colores)
    if jugador == 'Messi':
        ax1.text(i, -2, '🇦🇷', ha='center', fontsize=16)
    elif jugador == 'Mbappé':
        ax1.text(i, -2, '🇫🇷', ha='center', fontsize=16)

ax1.set_title('Goles por Temporada', fontsize=16, fontweight='bold', 
              color='#34495E', pad=20)
ax1.set_ylabel('Goles Anotados', fontsize=12, color='#34495E')
ax1.set_ylim(0, max(goles) + 5)

# Personalizando el eje
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color('#BDC3C7')
ax1.spines['bottom'].set_color('#BDC3C7')
ax1.set_facecolor('#FFFFFF')

# Gráfico 2: Goles vs Asistencias (Bubble Chart)
sizes = [v*50 for v in valoracion]  # Tamaño basado en valoración

scatter = ax2.scatter(goles, asistencias, s=sizes, c=valoracion, 
                     cmap='viridis', alpha=0.7, edgecolors='white', 
                     linewidth=2)

# Etiquetando cada punto
for i, jugador in enumerate(jugadores):
    ax2.annotate(jugador, (goles[i], asistencias[i]), 
                xytext=(5, 5), textcoords='offset points',
                fontsize=10, fontweight='bold', color='#2C3E50')

ax2.set_title('Goles vs Asistencias\n(Tamaño = Valoración)', 
              fontsize=16, fontweight='bold', color='#34495E', pad=20)
ax2.set_xlabel('Goles', fontsize=12, color='#34495E')
ax2.set_ylabel('Asistencias', fontsize=12, color='#34495E')

# Barra de colores personalizada
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Valoración Promedio', fontsize=10, color='#34495E')

# Grid personalizado
ax2.grid(True, alpha=0.3, color='#BDC3C7', linestyle='--')
ax2.set_facecolor('#FFFFFF')

# Añadiendo marca de agua (simulada)
fig.text(0.02, 0.02, 'Análisis Deportivo Pro © 2024', 
         fontsize=8, alpha=0.5, color='#7F8C8D')

plt.tight_layout()
plt.show()

print("=== ELEMENTOS DE PERSONALIZACIÓN PROFESIONAL ===")
print("✓ Paleta de colores consistente")
print("✓ Tipografía jerarquizada")
print("✓ Espaciado y márgenes optimizados")
print("✓ Marca de agua para identidad")
print("✓ Efectos visuales sutiles")
print("✓ Información contextual integrada")
```

---

## Actividades Prácticas - Sesión 2 (45 minutos)

### Ejercicio 1: Dashboard Personalizado (20 minutos)
1. **Datos del equipo**: Crea un conjunto de datos de tu equipo favorito con: 
   - Posiciones de jugadores
   - Minutos jugados
   - Goles y asistencias
   
2. **Visualización múltiple**: Diseña un dashboard con 4 gráficos:
   - Distribución de posiciones (gráfico de barras)
   - Rendimiento por jugador (scatter plot)
   - Evolución temporal (líneas)
   - Comparación de estadísticas (subplots)

### Ejercicio 2: Estilo de Marca (15 minutos)
- Aplica colores de tu equipo favorito
- Añade título profesional
- Incluye grids y etiquetas descriptivas
- Personaliza tipografía y espaciado

### Ejercicio 3: Análisis de Correlación (10 minutos)
- Investiga relación entre minutos jugados y goles
- Crea scatter plot con línea de tendencia
- Interpreta los resultados encontrados

**Entregable**: Archivo `.png` con tu dashboard personalizado y análisis escrito de 100 palabras sobre los hallazgos.


# SESIÓN 3: DASHBOARDS Y PRESENTACIÓN PROFESIONAL
**Duración**: 50 minutos | **Objetivo**: Crear sistemas completos de visualización

## ¿Por qué los Dashboards son Importantes?

En el análisis deportivo profesional, los **dashboards** son herramientas fundamentales que permiten:

### Ventajas Estratégicas:
- **Visión integral**: Múltiples métricas en una sola pantalla
- **Toma de decisiones rápida**: Información procesada y lista para usar
- **Comunicación efectiva**: Presentaciones claras para cuerpo técnico
- **Seguimiento temporal**: Evolución de rendimiento a lo largo del tiempo

### Aplicaciones en el Fútbol:
1. **Análisis pre-partido**: Fortalezas y debilidades del rival
2. **Monitoreo en vivo**: Estadísticas actualizadas durante el juego
3. **Evaluación post-partido**: Rendimiento individual y colectivo
4. **Planificación estratégica**: Tendencias de temporada para fichajes

---

## Componentes de un Dashboard Profesional

### 1. Estructura Lógica
- **Jerarquía visual**: Información más importante primero
- **Flujo de lectura**: De izquierda a derecha, arriba hacia abajo
- **Agrupación temática**: Métricas relacionadas juntas

### 2. Elementos Técnicos
- **Títulos descriptivos**: Claridad en cada sección
- **Leyendas completas**: Explicación de colores y símbolos
- **Escalas apropiadas**: Rangos que faciliten comparación
- **Anotaciones clave**: Destacar hallazgos importantes

### 3. Diseño Visual
- **Paleta consistente**: Máximo 4-5 colores principales
- **Espaciado uniforme**: Respiración visual entre elementos
- **Tipografía legible**: Tamaños apropiados para cada nivel
- **Balance compositivo**: Distribución equilibrada de elementos

```python
# ===============================
# DASHBOARD COMPLETO: ANÁLISIS INTEGRAL DE EQUIPO
# ===============================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle
import matplotlib.patches as patches

# Configuración global profesional
plt.style.use('default')
plt.rcParams.update({
    'font.size': 10,
    'font.family': 'sans-serif',
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 16
})

# DATOS DEL EQUIPO COMPLETOS
datos_equipo = {
    'jugadores': ['Ter Stegen', 'Piqué', 'Alba', 'Busquets', 'De Jong', 
                  'Pedri', 'Gavi', 'Dembélé', 'Messi', 'Griezmann', 'Ansu Fati'],
    'posiciones': ['Portero', 'Defensa', 'Defensa', 'Medio', 'Medio', 
                   'Medio', 'Medio', 'Delantero', 'Delantero', 'Delantero', 'Delantero'],
    'minutos': [3420, 2850, 2940, 3150, 2760, 2100, 1800, 2580, 3300, 2460, 1980],
    'goles': [0, 3, 1, 2, 4, 3, 2, 6, 25, 8, 5],
    'asistencias': [0, 1, 4, 8, 6, 4, 3, 9, 12, 4, 2],
    'tarjetas': [2, 8, 6, 4, 3, 1, 2, 3, 1, 2, 1],
    'valoracion': [7.2, 7.8, 7.5, 8.1, 7.9, 8.3, 7.6, 7.4, 9.2, 7.7, 7.8]
}

df_equipo = pd.DataFrame(datos_equipo)

# Datos temporales de rendimiento del equipo
jornadas = list(range(1, 19))
puntos_acumulados = [3, 6, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52]
goles_favor = [2, 4, 5, 8, 12, 15, 19, 23, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62]
goles_contra = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# ===============================
# CREACIÓN DEL DASHBOARD COMPLETO
# ===============================

fig = plt.figure(figsize=(20, 16))
fig.suptitle('DASHBOARD PROFESIONAL - FC BARCELONA TEMPORADA 2023/24', 
             fontsize=22, fontweight='bold', color='#004D98', y=0.98)

# Configuración de la grilla del dashboard
gs = fig.add_gridspec(4, 4, hspace=0.3, wspace=0.3, 
                      left=0.05, right=0.95, top=0.93, bottom=0.05)

# ===============================
# PANEL 1: DISTRIBUCIÓN POR POSICIONES
# ===============================
ax1 = fig.add_subplot(gs[0, 0])
posicion_counts = df_equipo['posiciones'].value_counts()
colores_posicion = ['#004D98', '#DC143C', '#FFD700', '#228B22']

wedges, texts, autotexts = ax1.pie(posicion_counts.values, 
                                   labels=posicion_counts.index,
                                   colors=colores_posicion,
                                   autopct='%1.1f%%',
                                   startangle=90,
                                   explode=(0.05, 0.05, 0.05, 0.05))

ax1.set_title('Distribución por Posiciones', fontweight='bold', color='#004D98')

# ===============================
# PANEL 2: TOP GOLEADORES
# ===============================
ax2 = fig.add_subplot(gs[0, 1])
top_goleadores = df_equipo.nlargest(5, 'goles')

barras = ax2.bar(range(len(top_goleadores)), top_goleadores['goles'], 
                 color=['#DC143C' if g > 15 else '#004D98' for g in top_goleadores['goles']])

ax2.set_xticks(range(len(top_goleadores)))
ax2.set_xticklabels(top_goleadores['jugadores'], rotation=45, ha='right')
ax2.set_title('Top Goleadores', fontweight='bold', color='#004D98')
ax2.set_ylabel('Goles')

# Añadiendo valores en las barras
for i, barra in enumerate(barras):
    altura = barra.get_height()
    ax2.text(barra.get_x() + barra.get_width()/2., altura + 0.5,
             f'{int(altura)}', ha='center', va='bottom', fontweight='bold')

# ===============================
# PANEL 3: EVOLUCIÓN DE PUNTOS
# ===============================
ax3 = fig.add_subplot(gs[0, 2:])
ax3.plot(jornadas, puntos_acumulados, marker='o', linewidth=3, 
         color='#004D98', markersize=6, markerfacecolor='#DC143C')
ax3.fill_between(jornadas, puntos_acumulados, alpha=0.3, color='#004D98')

ax3.set_title('Evolución de Puntos por Jornada', fontweight='bold', color='#004D98')
ax3.set_xlabel('Jornadas')
ax3.set_ylabel('Puntos Acumulados')
ax3.grid(True, alpha=0.3)
ax3.set_xlim(0, 19)

# Línea de objetivo (proyección para Champions)
objetivo_champions = [j * 2.8 for j in jornadas]
ax3.plot(jornadas, objetivo_champions, '--', color='#228B22', 
         alpha=0.7, label='Objetivo Champions (68 pts)')
ax3.legend()

# ===============================
# PANEL 4: RENDIMIENTO OFENSIVO VS DEFENSIVO
# ===============================
ax4 = fig.add_subplot(gs[1, :2])

ax4_twin = ax4.twinx()

# Gráfico de barras para goles a favor
barras_favor = ax4.bar(jornadas, goles_favor, alpha=0.7, 
                       color='#228B22', label='Goles a Favor')

# Línea para goles en contra
linea_contra = ax4_twin.plot(jornadas, goles_contra, color='#DC143C', 
                            marker='s', linewidth=2, markersize=4, 
                            label='Goles en Contra')

ax4.set_title('Rendimiento Ofensivo vs Defensivo', fontweight='bold', color='#004D98')
ax4.set_xlabel('Jornadas')
ax4.set_ylabel('Goles a Favor', color='#228B22')
ax4_twin.set_ylabel('Goles en Contra', color='#DC143C')

# Configurando colores de los ejes
ax4.tick_params(axis='y', labelcolor='#228B22')
ax4_twin.tick_params(axis='y', labelcolor='#DC143C')

# Leyenda combinada
lines1, labels1 = ax4.get_legend_handles_labels()
lines2, labels2 = ax4_twin.get_legend_handles_labels()
ax4.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# ===============================
# PANEL 5: RENDIMIENTO INDIVIDUAL (SCATTER AVANZADO)
# ===============================
ax5 = fig.add_subplot(gs[1, 2:])

# Tamaño basado en minutos jugados
tamaños = [(m/100) for m in df_equipo['minutos']]

scatter = ax5.scatter(df_equipo['goles'], df_equipo['asistencias'], 
                     s=tamaños, c=df_equipo['valoracion'], 
                     cmap='RdYlBu_r', alpha=0.8, edgecolors='white', linewidth=2)

# Etiquetando jugadores clave
for i, jugador in enumerate(df_equipo['jugadores']):
    if df_equipo.iloc[i]['goles'] + df_equipo.iloc[i]['asistencias'] > 10:
        ax5.annotate(jugador, (df_equipo.iloc[i]['goles'], df_equipo.iloc[i]['asistencias']),
                    xytext=(5, 5), textcoords='offset points', fontsize=9, 
                    fontweight='bold', alpha=0.8)

ax5.set_title('Rendimiento Individual\n(Tamaño = Minutos, Color = Valoración)', 
              fontweight='bold', color='#004D98')
ax5.set_xlabel('Goles')
ax5.set_ylabel('Asistencias')
ax5.grid(True, alpha=0.3)

# Barra de colores
cbar = plt.colorbar(scatter, ax=ax5, shrink=0.8)
cbar.set_label('Valoración', rotation=270, labelpad=15)

# ===============================
# PANEL 6: HEATMAP DE DISCIPLINA
# ===============================
ax6 = fig.add_subplot(gs[2, :2])

# Preparando datos para heatmap
posiciones_unicas = df_equipo['posiciones'].unique()
disciplina_por_posicion = []

for pos in posiciones_unicas:
    jugadores_pos = df_equipo[df_equipo['posiciones'] == pos]
    promedio_tarjetas = jugadores_pos['tarjetas'].mean()
    disciplina_por_posicion.append(promedio_tarjetas)

# Creando heatmap manual
y_pos = np.arange(len(posiciones_unicas))
colores_disciplina = plt.cm.Reds(np.linspace(0.2, 0.8, len(posiciones_unicas)))

barras_disciplina = ax6.barh(y_pos, disciplina_por_posicion, 
                            color=colores_disciplina, alpha=0.8)

ax6.set_yticks(y_pos)
ax6.set_yticklabels(posiciones_unicas)
ax6.set_title('Disciplina por Posición\n(Promedio de Tarjetas)', 
              fontweight='bold', color='#004D98')
ax6.set_xlabel('Tarjetas Promedio')

# Añadiendo valores
for i, v in enumerate(disciplina_por_posicion):
    ax6.text(v + 0.1, i, f'{v:.1f}', va='center', fontweight='bold')

# ===============================
# PANEL 7: PROYECCIÓN FINAL
# ===============================
ax7 = fig.add_subplot(gs[2, 2:])

# Calculando proyecciones
jornadas_restantes = 38 - len(jornadas)
puntos_por_jornada = puntos_acumulados[-1] / len(jornadas)
proyeccion_puntos = puntos_acumulados[-1] + (puntos_por_jornada * jornadas_restantes)

# Escenarios
escenarios = ['Actual', 'Optimista\n(+20%)', 'Pesimista\n(-20%)', 'Objetivo\nChampions']
puntos_escenarios = [proyeccion_puntos, 
                    proyeccion_puntos * 1.2, 
                    proyeccion_puntos * 0.8, 
                    68]

colores_escenarios = ['#004D98', '#228B22', '#DC143C', '#FFD700']

barras_proyeccion = ax7.bar(escenarios, puntos_escenarios, 
                           color=colores_escenarios, alpha=0.8)

ax7.set_title('Proyección Final de Temporada', fontweight='bold', color='#004D98')
ax7.set_ylabel('Puntos Proyectados')
ax7.axhline(y=68, color='#FFD700', linestyle='--', alpha=0.7, 
           label='Límite Champions')

# Añadiendo valores en las barras
for barra in barras_proyeccion:
    altura = barra.get_height()
    ax7.text(barra.get_x() + barra.get_width()/2., altura + 1,
             f'{int(altura)}', ha='center', va='bottom', fontweight='bold')

# ===============================
# PANEL 8: RESUMEN ESTADÍSTICO
# ===============================
ax8 = fig.add_subplot(gs[3, :])
ax8.axis('off')

# Creando tabla de resumen
estadisticas_clave = [
    ['Métrica', 'Valor Actual', 'Objetivo', 'Estado'],
    ['Puntos por Partido', f'{puntos_acumulados[-1]/len(jornadas):.2f}', '2.00', 
     'APROBADO' if puntos_acumulados[-1]/len(jornadas) >= 2.0 else 'MEJORAR'],
    ['Goles por Partido', f'{goles_favor[-1]/len(jornadas):.2f}', '2.50', 
     'APROBADO' if goles_favor[-1]/len(jornadas) >= 2.5 else 'MEJORAR'],
    ['Defensa (Goles/Partido)', f'{goles_contra[-1]/len(jornadas):.2f}', '< 1.00', 
     'APROBADO' if goles_contra[-1]/len(jornadas) < 1.0 else 'MEJORAR'],
    ['Diferencia de Goles', f'+{goles_favor[-1] - goles_contra[-1]}', '> +30', 
     'APROBADO' if (goles_favor[-1] - goles_contra[-1]) > 30 else 'MEJORAR']
]

# Dibujando tabla
for i, fila in enumerate(estadisticas_clave):
    for j, celda in enumerate(fila):
        color_fondo = '#F0F0F0' if i == 0 else 'white'
        peso_fuente = 'bold' if i == 0 else 'normal'
        
        rect = Rectangle((j*0.2, 0.8-i*0.15), 0.2, 0.15, 
                        facecolor=color_fondo, edgecolor='black', linewidth=1)
        ax8.add_patch(rect)
        
        ax8.text(j*0.2 + 0.1, 0.8-i*0.15 + 0.075, celda, 
                ha='center', va='center', fontweight=peso_fuente, fontsize=11)

ax8.set_xlim(0, 0.8)
ax8.set_ylim(0, 1)
ax8.set_title('Resumen de Objetivos de Temporada', 
              fontweight='bold', color='#004D98', y=0.95)

# ===============================
# MARCA DE AGUA Y METADATOS
# ===============================
fig.text(0.99, 0.01, 'Generado con Python • Análisis Deportivo Pro', 
         ha='right', va='bottom', fontsize=8, alpha=0.6, style='italic')

fig.text(0.01, 0.01, f'Actualizado: Jornada {len(jornadas)} de 38', 
         ha='left', va='bottom', fontsize=8, alpha=0.6, fontweight='bold')

plt.show()

print("=== DASHBOARD COMPLETADO EXITOSAMENTE ===")
print(f"✓ 8 paneles de análisis integrados")
print(f"✓ {len(df_equipo)} jugadores analizados")
print(f"✓ {len(jornadas)} jornadas procesadas")
print(f"✓ Proyección final: {int(proyeccion_puntos)} puntos")
print(f"✓ Estado Champions: {'CLASIFICADO' if proyeccion_puntos >= 68 else 'EN RIESGO'}")
```

---

## Proyecto Final - Sesión 3 (40 minutos)

### RETO: Creación de Dashboard Personalizado

**Objetivo**: Desarrollar un sistema completo de visualización para tu equipo preferido

#### Fase 1: Recolección de Datos (10 minutos)
Investiga y recopila datos reales de tu equipo:
- **Jugadores actuales**: Nombres, posiciones, edad
- **Estadísticas de temporada**: Goles, asistencias, minutos
- **Resultados recientes**: Últimos 10 partidos
- **Comparación con rivales**: Datos de equipos competidores

#### Fase 2: Diseño del Dashboard (25 minutos)
Crea un dashboard profesional que incluya:

1. **Panel Principal** (2x2 grid):
   - Gráfico de barras: Top goleadores del equipo
   - Scatter plot: Rendimiento individual (goles vs asistencias)
   - Línea temporal: Evolución de puntos
   - Pie chart: Distribución por posiciones

2. **Elementos de Personalización**:
   - Colores oficiales del equipo
   - Logo o escudo (simulado con texto)
   - Tipografía consistente y profesional
   - Grids y espaciado optimizado

3. **Información Contextual**:
   - Títulos descriptivos en cada panel
   - Leyendas completas y claras
   - Anotaciones de hallazgos importantes
   - Metadatos (fecha, fuente, autor)

#### Fase 3: Análisis e Interpretación (5 minutos)
Redacta un análisis de 150 palabras que incluya:
- **Fortalezas identificadas**: ¿Qué revela el dashboard sobre el equipo?
- **Áreas de mejora**: ¿Dónde puede optimizar el rendimiento?
- **Decisiones estratégicas**: ¿Qué recomendarías al entrenador?
- **Comparación competitiva**: ¿Cómo se posiciona frente a rivales?

---

## Criterios de Evaluación

### Técnico (40 puntos)
- **Código funcional**: Ejecuta sin errores
- **Estructura correcta**: Uso apropiado de subplots y matplotlib
- **Datos coherentes**: Información realista y bien organizada
- **Personalización avanzada**: Aplicación de estilos profesionales

### Visual (35 puntos)
- **Claridad**: Información fácil de interpretar
- **Estética**: Diseño atractivo y profesional
- **Consistencia**: Paleta de colores y tipografía uniforme
- **Organización**: Layout lógico y bien distribuido

### Análisis (25 puntos)
- **Interpretación correcta**: Conclusiones basadas en datos
- **Pensamiento crítico**: Identificación de patrones y tendencias
- **Aplicación práctica**: Recomendaciones viables
- **Comunicación efectiva**: Redacción clara y concisa

---

## Entregables

1. **Archivo Python** (`.py` o `.ipynb`): Código completo del dashboard
2. **Imagen PNG**: Captura de alta resolución del dashboard final
3. **Análisis escrito**: Documento PDF con interpretación y recomendaciones
4. **Presentación breve**: 2 minutos explicando hallazgos principales

**Fecha límite**: Próxima clase  
**Formato de entrega**: Carpeta comprimida con todos los archivos

---

## Recursos Adicionales

### Sitios Web de Datos Futbolísticos:
- **FIFA.com**: Estadísticas oficiales de selecciones
- **Transfermarkt**: Valores de mercado y estadísticas de jugadores
- **ESPN**: Resultados y análisis de ligas principales
- **SofaScore**: Datos detallados de rendimiento individual

### Herramientas Complementarias:
- **Matplotlib Gallery**: Ejemplos avanzados de visualización
- **Seaborn**: Biblioteca para gráficos estadísticos
- **Plotly**: Visualizaciones interactivas (opcional)
- **Color Hunt**: Paletas de colores profesionales

### Consejos Profesionales:
1. **Menos es más**: No satures el dashboard con información
2. **Historia coherente**: Cada gráfico debe contribuir al mensaje general
3. **Audiencia específica**: Adapta el nivel de detalle a quien lo va a usar
4. **Actualización regular**: Diseña pensando en datos que cambiarán


---

# 🎯 RESUMEN SEMANAL Y PRÓXIMOS PASOS

## ¿Qué Hemos Logrado Esta Semana?

### Sesión 1: Fundamentos de Matplotlib
- **Configuración del entorno**: Instalación y configuración de matplotlib
- **Gráficos básicos**: Barras, líneas y scatter plots con datos futbolísticos
- **Personalización inicial**: Colores, títulos y etiquetas descriptivas
- **Práctica hands-on**: Creación de visualizaciones de equipos reales

### Sesión 2: Visualizaciones Avanzadas
- **Subplots profesionales**: Múltiples gráficos en una sola figura
- **Personalización avanzada**: Paletas de colores, tipografía y espaciado
- **Correlaciones y tendencias**: Análisis de relaciones entre variables
- **Elementos de marca**: Aplicación de identidad visual consistente

### Sesión 3: Dashboards Completos
- **Sistemas integrados**: Combinación de múltiples tipos de visualización
- **Layout profesional**: Organización lógica y jerárquica de información
- **Análisis interpretativo**: Extracción de insights para toma de decisiones
- **Proyecto final**: Desarrollo de dashboard personalizado completo

---

## Habilidades Técnicas Desarrolladas

### Visualización de Datos
- Creación de gráficos de barras, líneas y dispersión
- Configuración avanzada de subplots y layouts
- Personalización profesional de elementos visuales
- Aplicación de principios de diseño efectivo

### Análisis Deportivo
- Interpretación de estadísticas futbolísticas
- Identificación de patrones de rendimiento
- Correlación entre diferentes métricas de juego
- Presentación de hallazgos para stakeholders

### 🐍 Programación Python
- Uso avanzado de matplotlib y pandas
- Estructuración de código para análisis repetible
- Gestión de datos complejos con múltiples variables
- Optimización de rendimiento en visualizaciones

### 🎨 Diseño Visual
- Aplicación de paletas de colores profesionales
- Jerarquización visual de información
- Balance compositivo en dashboards
- Comunicación efectiva a través del diseño

---

## Preparación para la Próxima Semana

### Semana 6: Introducción a la Exploración de Datos
**Objetivos de aprendizaje**:
- Técnicas de exploración inicial de datasets
- Limpieza y preparación de datos reales
- Identificación de patrones y anomalías
- Formulación de hipótesis basadas en datos

### Conocimientos Previos Necesarios:
1. **Matplotlib básico**: COMPLETADO (esta semana)
2. **Pandas fundamentals**: COMPLETADO (Semana 4)
3. **Estructuras de control**: COMPLETADO (Semana 2)
4. **Funciones y módulos**: COMPLETADO (Semana 3)

### Tareas de Preparación:
- [ ] **Revisar proyecto final**: Asegurar que el dashboard esté completado
- [ ] **Investigar datasets**: Buscar fuentes de datos futbolísticos para próxima semana
- [ ] **Practicar interpretación**: Analizar gráficos de medios deportivos
- [ ] **Explorar herramientas**: Familiarizarse con Jupyter Notebooks si no se ha hecho

---

## Recursos para Profundización

### 📚 Documentación Técnica
- **Matplotlib Documentation**: Referencia completa de funciones y parámetros
- **Pandas Plotting**: Integración directa entre pandas y matplotlib
- **Seaborn Gallery**: Ejemplos de visualizaciones estadísticas avanzadas

### Casos de Estudio Deportivos
- **Analytics FC**: Blog de análisis futbolístico con Python
- **FiveThirtyEight Soccer**: Metodologías de análisis deportivo
- **Football Analytics**: Casos prácticos de visualización en fútbol

### 💡 Inspiración Visual
- **Information is Beautiful**: Principios de visualización efectiva
- **Flowing Data**: Tutoriales de visualización avanzada
- **Visual Capitalist**: Ejemplos de infografías profesionales

---

## Autoevaluación Semanal

### Nivel de Comprensión (1-5)
- **Conceptos básicos de matplotlib**: Nivel 5
- **Creación de subplots complejos**: Nivel 5
- **Personalización avanzada**: Nivel 5
- **Interpretación de visualizaciones**: Nivel 5

### Preguntas de Reflexión
1. **¿Qué tipo de gráfico es más efectivo para mostrar evolución temporal?**
2. **¿Cómo decides la paleta de colores para un dashboard profesional?**
3. **¿Qué elementos son esenciales en un dashboard para entrenadores?**
4. **¿Cómo identificas correlaciones interesantes en datos deportivos?**

### Áreas para Reforzar
- [ ] Práctica adicional con correlaciones complejas
- [ ] Exploración de datasets más grandes
- [ ] Integración con fuentes de datos en tiempo real
- [ ] Optimización de código para mejor rendimiento

---

**¡Excelente trabajo esta semana!** Has desarrollado habilidades fundamentales en visualización de datos que serán la base para análisis más avanzados. La combinación de técnicas de programación con conocimiento deportivo te permitirá crear análisis únicos y valiosos.

**Próximo desafío**: En la Semana 6 trabajaremos con datasets reales y aprenderemos a extraer insights que no son obvios a simple vista. ¡Prepárate para descubrir patrones ocultos en el fútbol!

```python
# ¿Qué crees que sucede cuando "despertamos" estas herramientas de visualización?
# Experimenta ejecutando este código y observa:

import seaborn as sns
import matplotlib.pyplot as plt

# ¿Qué cambio crees que hace esta línea en el estilo de nuestros gráficos?
sns.set_theme()

print("¡Herramientas de visualización activadas!")
print("Seaborn: Tu diseñador gráfico automático")
print("Matplotlib: El motor de renderizado")

# Reflexión: ¿Por qué crees que necesitamos ambas herramientas trabajando juntas?
```

## 3. Gráficos de Barras - ¿Cómo hacer comparaciones visuales instantáneas?

### Pregunta conceptual: ¿Cuándo tu ojo necesita comparar?

**Escenario práctico**: Eres el entrenador de una liga juvenil. Quieres saber rápidamente qué equipos están marcando más goles para ajustar tu estrategia.

**Tu desafío**: ¿Cómo representarías visualmente esta información para que cualquiera pueda entender el ranking en 3 segundos?

### Descubrimiento: Los gráficos de barras como comparadores instantáneos

**Pregunta de diseño**: ¿Por qué crees que las barras verticales son tan efectivas para mostrar "quién va ganando"?

**Analogía deportiva**: ¿Es como ver un podium olímpico, donde la altura representa el rendimiento?

¡Vamos a crear nuestro primer "podium de datos"!

```python
# ¿Cómo crees que Python convertirá estos números en un gráfico visual?
# Experimenta y observa la magia:

# Nuestros datos: ¿Puedes predecir qué equipo tendrá la barra más alta?
equipos = ['Barcelona', 'Madrid', 'Valencia']
goles = [25, 20, 15]

# La línea mágica: ¿Qué crees que hace sns.barplot()?
sns.barplot(x=equipos, y=goles)

# ¿Qué diferencia crees que hace agregar un título?
plt.title('Goles por Equipo')

# El momento de la revelación:
plt.show()

print("¡Acabas de crear tu primer insight visual!")
print("Pregunta de reflexión: ¿Qué información captas instantáneamente del gráfico")
print("que sería más difícil de ver solo con los números?")

# Tu turno: ¿Qué preguntas puedes responder mirando este gráfico?
```

### Reflexión: ¿Por qué Seaborn es como tener un diseñador gráfico personal?

**Pregunta de comparación**: ¿Notaste algo especial en el estilo de tu gráfico comparado con otros que hayas visto?

**Descubrimiento guiado**: Seaborn tiene "súper poderes" automáticos:

- **Estética profesional**: ¿Crees que es importante que tus visualizaciones se vean serias y confiables?
- **Colores inteligentes**: ¿Qué ventaja tiene que Python elija colores que funcionen bien juntos?
- **Menos código, más impacto**: ¿Prefieres escribir 10 líneas o 1 línea para el mismo resultado?

**Pregunta estratégica**: ¿En qué situaciones deportivas sería crucial que tus gráficos se vean profesionales?

```python
# ¿Cómo crees que podemos hacer nuestro gráfico aún más impactante?
# Experimenta con estas mejoras visuales:

equipos = ['Barcelona', 'Madrid', 'Valencia']
goles = [25, 20, 15]

# Pregunta: ¿Qué diferencia visual esperas con esta paleta de colores?
sns.barplot(x=equipos, y=goles, hue=equipos, palette='viridis', legend=False)

# ¿Cómo crees que estos detalles afectan la profesionalidad del gráfico?
plt.title('Goles por Equipo', fontsize=16)
plt.xlabel('Equipos')
plt.ylabel('Número de Goles')

plt.show()

print("¡Observa la transformación!")
print("Reflexión: ¿Qué elementos hacen que este gráfico se vea más profesional?")
print("¿Cómo crees que reaccionaría un entrenador al ver esta visualización?")

# Experimenta: ¿Qué otras paletas te gustaría probar? 'Set2', 'plasma', 'coolwarm'
```

## 4. Gráficos de Líneas - ¿Cómo revelar patrones y tendencias?

### Pregunta temporal: ¿Cuándo el tiempo cuenta la historia?

**Escenario de análisis**: Un equipo parece estar mejorando, pero ¿cómo demostrarías esta evolución de manera convincente?

**Tu desafío**: ¿Qué tipo de visualización usarías para mostrar si un jugador está en racha goleadora o en declive?

### Descubrimiento: Las líneas como narrativas visuales

**Analogía médica**: ¿Has visto los monitores cardíacos en las películas? ¿Por qué crees que usan líneas y no barras?

**Pregunta clave**: ¿Qué información adicional proporciona la **conexión** entre puntos que no tendrías con puntos aislados?

**Reflexión deportiva**: ¿En qué situaciones deportivas sería crucial ver la "tendencia" además de los valores individuales?

```python
# ¿Cómo crees que Python "conectará" estos puntos para contar una historia?
# Observa la narrativa visual que se revela:

# Los datos: ¿Puedes predecir si Barcelona está mejorando o empeorando?
meses = ['Enero', 'Febrero', 'Marzo', 'Abril']
goles_barcelona = [5, 8, 6, 10]

# La magia de las conexiones: ¿Qué historia crees que revelará la línea?
sns.lineplot(x=meses, y=goles_barcelona, marker='o', linewidth=3, markersize=10)

plt.title('Goles de Barcelona por Mes')
plt.xlabel('Mes')
plt.ylabel('Goles')

plt.show()

print("¡Observa cómo la línea cuenta una historia!")
print("Pregunta de análisis: ¿Qué patrón ves en el rendimiento de Barcelona?")
print("¿Hay una tendencia general hacia arriba o hacia abajo?")
print("¿En qué mes tuvieron el peor rendimiento? ¿Y el mejor?")

# Reflexión: ¿Qué insights obtienes de la línea que no verías en una tabla de números?
```

## 5. Tu Laboratorio de Visualización - ¿Puedes crear tu propia narrativa visual?

### Desafío personal: Conviértete en analista de tu equipo favorito

**Tu misión**: Usar las herramientas que acabas de descubrir para crear una visualización que cuente la historia de rendimiento de tu equipo.

**Preguntas guía para tu análisis**:
- ¿Qué historia quieres contar con tus datos?
- ¿Tu equipo está en una buena racha o necesita mejorar?
- ¿Qué insights podrías compartir con otros fanáticos?

**Reflexión creativa**: ¿Cómo personalizarías el gráfico para que refleje la identidad de tu equipo?

```python
# ¡Tu turno de ser analista deportivo!
# Personaliza estos datos para contar la historia de tu equipo favorito:

# Pregunta de personalización: ¿Cuál es tu equipo favorito?
mi_equipo = "Mi Equipo Favorito"  # Cambia esto por tu equipo real

# Tu análisis: ¿Qué datos reales o hipotéticos usarías?
partidos = ['Partido 1', 'Partido 2', 'Partido 3', 'Partido 4']
goles_por_partido = [2, 1, 3, 0]  # Experimenta con diferentes patrones

# Creación de tu narrativa visual:
sns.lineplot(x=partidos, y=goles_por_partido, marker='o', linewidth=3, markersize=8, color='green')

plt.title(f'Goles de {mi_equipo}', fontsize=14)
plt.xlabel('Partidos')
plt.ylabel('Goles')

plt.show()

print(f"¡Excelente análisis de {mi_equipo}!")
print("Preguntas de reflexión:")
print("- ¿Qué historia cuenta tu línea?")
print("- ¿Hay una tendencia que te preocupe o te emocione?")
print("- ¿Qué recomendaciones darías basándote en esta visualización?")

# Experimenta: ¿Qué sucede si cambias los números? ¿Y el color?
```

## 6. Reflexiones sobre tu transformación en analista visual

### Autoevaluación: ¿Qué descubriste sobre el poder de la visualización?

**Pregunta de síntesis**: ¿Cómo cambió tu forma de ver los datos después de convertirlos en gráficos?

#### Tus nuevas habilidades como visualizador de datos

**Seaborn**: ¿Comprendes por qué es tu "diseñador gráfico automático"?  
**Gráficos de barras**: ¿Puedes identificar cuándo usar `sns.barplot()` para comparaciones?  
**Gráficos de líneas**: ¿Entiendes cuándo `sns.lineplot()` revela tendencias importantes?  
**Paletas de colores**: ¿Aprecias cómo los colores profesionales mejoran el impacto?  

### Reflexión estratégica: ¿Por qué Seaborn es revolucionario?

**Tu experiencia**: ¿Qué te sorprendió más de crear gráficos profesionales con tan poco código?

- **Estética automática**: ¿Cómo afecta tu confianza saber que tus gráficos se ven profesionales?
- **Eficiencia**: ¿Qué podrías hacer con el tiempo que ahorras no configurando colores manualmente?
- **Impacto**: ¿Cómo mejora tu capacidad de comunicar insights deportivos?

### Conexiones con el análisis deportivo real

**Pregunta integradora**: ¿Dónde has visto gráficos similares en deportes profesionales?

**Tu evolución**: ¿Cómo usarías estas habilidades para analizar datos deportivos reales?

### Preparación para aventuras más avanzadas

**Anticipación**: ¿Qué tipos de visualizaciones más complejas te gustaría crear?

**Tu caja de herramientas esencial**:
- `sns.barplot()` → Tu comparador instantáneo
- `sns.lineplot()` → Tu revelador de tendencias  
- `palette='viridis'` → Tu generador de colores profesionales
- `plt.title()` → Tu narrador de historias
- `plt.show()` → Tu momento de revelación

**Logro desbloqueado**: ¡Ya puedes transformar números en narrativas visuales impactantes!

### Reflexión final

¿Cómo crees que estas habilidades de visualización cambiarán tu forma de entender y comunicar información deportiva?

---

*Acabas de adquirir el súper poder de hacer que los datos "hablen" visualmente.*

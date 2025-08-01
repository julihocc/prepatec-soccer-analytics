# Ejercicio Semana 5: Visualización Básica

## 📋 Información General

**Bloque:** 1 - Prerrequisitos de Programación  
**Semana:** 5  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 5

## 🎯 Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

- Crear visualizaciones básicas con matplotlib y seaborn
- Diseñar gráficos informativos para análisis deportivo
- Personalizar y formatear visualizaciones profesionales
- Interpretar y comunicar insights a través de gráficos

## 📚 Conocimientos Previos Requeridos

- Manipulación de datos con pandas
- Operaciones básicas con NumPy
- Fundamentos de matplotlib y seaborn
- Análisis estadístico básico

## 🚀 Ejercicio: Dashboard Visual de La Liga

### Contexto

Como analista de datos deportivos, necesitas crear un dashboard visual que presente los hallazgos más importantes de La Liga española. Tus visualizaciones serán utilizadas en una presentación ejecutiva, por lo que deben ser claras, profesionales y fáciles de interpretar.

### Parte 1: Configuración y Gráficos Básicos (25 puntos)

**Instrucciones:**
Configura el entorno de visualización y crea gráficos básicos:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo para visualizaciones profesionales
plt.style.use('default')
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14

print("🎨 DASHBOARD VISUAL DE LA LIGA ESPAÑOLA")
print("=" * 60)

# Datos actualizados para visualización
equipos_data = {
    'equipo': ['Barcelona', 'Real Madrid', 'Atletico Madrid', 'Sevilla', 'Real Sociedad', 
               'Villarreal', 'Athletic Bilbao', 'Valencia', 'Real Betis', 'Osasuna'],
    'puntos': [88, 85, 78, 65, 62, 58, 55, 49, 47, 44],
    'goles_favor': [76, 75, 58, 48, 51, 44, 42, 38, 45, 37],
    'goles_contra': [20, 31, 33, 35, 36, 40, 38, 48, 52, 46],
    'partidos_ganados': [28, 26, 23, 18, 17, 16, 15, 13, 12, 12],
    'partidos_empatados': [4, 7, 9, 11, 11, 10, 10, 10, 11, 8],
    'partidos_perdidos': [6, 5, 6, 9, 10, 12, 13, 15, 15, 18],
    'presupuesto_millones': [1350, 1200, 350, 200, 120, 180, 150, 90, 110, 45]
}

df_liga = pd.DataFrame(equipos_data)

# Calcular métricas adicionales
df_liga['diferencia_goles'] = df_liga['goles_favor'] - df_liga['goles_contra']
df_liga['eficiencia_goles'] = df_liga['goles_favor'] / df_liga['partidos_ganados']
df_liga['puntos_por_millon'] = df_liga['puntos'] / df_liga['presupuesto_millones']

print("📊 Dataset preparado para visualización")
print(f"Equipos: {len(df_liga)}")
print(f"Métricas disponibles: {list(df_liga.columns)}")

# 1. Gráfico de barras básico - Puntos por equipo
print("\n📈 Creando gráfico de puntos por equipo...")

# Tu código aquí
plt.figure(figsize=(14, 8))
bars = plt.bar(# Tu código - equipos en eje x, puntos en eje y)

# Personalizar el gráfico
plt.title('🏆 Clasificación de La Liga 2023-24\nPuntos por Equipo', 
          fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Equipos', fontsize=14, fontweight='bold')
plt.ylabel('Puntos', fontsize=14, fontweight='bold')

# Rotar etiquetas del eje x para mejor legibilidad
plt.xticks(rotation=45, ha='right')

# Añadir valores sobre las barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')

# Añadir línea de promedio
promedio_puntos = df_liga['puntos'].mean()
plt.axhline(y=promedio_puntos, color='red', linestyle='--', alpha=0.7, 
            label=f'Promedio: {promedio_puntos:.1f} puntos')

plt.legend()
plt.tight_layout()
plt.show()

# 2. Gráfico de dispersión - Goles a favor vs en contra
print("\n🎯 Creando gráfico de goles a favor vs en contra...")

# Tu código aquí
plt.figure(figsize=(12, 8))
scatter = plt.scatter(# Tu código - goles_contra en x, goles_favor en y, 
                     # usar puntos como tamaño de los puntos)

# Personalizar
plt.title('⚽ Rendimiento Ofensivo vs Defensivo\nGoles a Favor vs Goles en Contra', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Goles en Contra', fontsize=14, fontweight='bold')
plt.ylabel('Goles a Favor', fontsize=14, fontweight='bold')

# Añadir línea diagonal de referencia (equilibrio)
min_goles = min(df_liga['goles_contra'].min(), df_liga['goles_favor'].min())
max_goles = max(df_liga['goles_contra'].max(), df_liga['goles_favor'].max())
plt.plot([min_goles, max_goles], [min_goles, max_goles], 
         'r--', alpha=0.5, label='Línea de equilibrio')

# Añadir etiquetas de equipos
for i, equipo in enumerate(df_liga['equipo']):
    plt.annotate(equipo, 
                (df_liga['goles_contra'].iloc[i], df_liga['goles_favor'].iloc[i]),
                xytext=(5, 5), textcoords='offset points', fontsize=10)

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Parte 2: Visualizaciones con Seaborn (30 puntos)

**Instrucciones:**
Crea visualizaciones más avanzadas usando seaborn:

```python
print("\n" + "="*60)
print("🎨 VISUALIZACIONES AVANZADAS CON SEABORN")
print("="*60)

# 1. Heatmap de correlaciones
print("\n🔥 Creando heatmap de correlaciones...")

# Tu código aquí
# Seleccionar columnas numéricas para la correlación
columnas_numericas = ['puntos', 'goles_favor', 'goles_contra', 'diferencia_goles', 
                     'partidos_ganados', 'presupuesto_millones', 'eficiencia_goles']

correlacion_matrix = # Tu código para calcular correlaciones

plt.figure(figsize=(12, 10))
heatmap = sns.heatmap(# Tu código - matriz de correlación,
                      # annot=True para mostrar valores
                      # cmap='RdYlBu_r' para colores
                      # center=0 para centrar en cero
                      # fmt='.2f' para formato de números
                      )

plt.title('🔍 Matriz de Correlaciones\nRelaciones entre Métricas de Rendimiento', 
          fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

# 2. Boxplot de distribución de goles
print("\n📦 Creando boxplot de distribución de goles...")

# Preparar datos para boxplot (formato largo)
datos_goles = pd.melt(df_liga[['equipo', 'goles_favor', 'goles_contra']], 
                      id_vars=['equipo'], 
                      var_name='tipo_gol', 
                      value_name='cantidad')

# Tu código aquí
plt.figure(figsize=(12, 8))
boxplot = sns.boxplot(# Tu código - tipo_gol en x, cantidad en y)

plt.title('📊 Distribución de Goles por Tipo\nGoles a Favor vs Goles en Contra', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Tipo de Gol', fontsize=14)
plt.ylabel('Cantidad de Goles', fontsize=14)

# Personalizar etiquetas
plt.xticks([0, 1], ['Goles a Favor', 'Goles en Contra'])

# Añadir puntos individuales
sns.stripplot(data=datos_goles, x='tipo_gol', y='cantidad', 
              color='black', alpha=0.6, size=8)

plt.tight_layout()
plt.show()

# 3. Barplot horizontal - Eficiencia por presupuesto
print("\n💰 Creando gráfico de eficiencia por presupuesto...")

# Tu código aquí
# Ordenar equipos por puntos_por_millon
df_ordenado = df_liga.sort_values('puntos_por_millon', ascending=True)

plt.figure(figsize=(12, 10))
barplot = sns.barplot(# Tu código - puntos_por_millon en x, equipo en y)

plt.title('💡 Eficiencia por Presupuesto\nPuntos obtenidos por Millón de Euros', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Puntos por Millón de Euros', fontsize=14)
plt.ylabel('Equipos', fontsize=14)

# Añadir valores al final de las barras
for i, v in enumerate(df_ordenado['puntos_por_millon']):
    plt.text(v + 0.001, i, f'{v:.3f}', va='center', fontweight='bold')

plt.tight_layout()
plt.show()

# 4. Violinplot - Distribución de métricas de rendimiento
print("\n🎻 Creando violinplot de métricas de rendimiento...")

# Preparar datos para violinplot
metricas_rendimiento = df_liga[['puntos', 'goles_favor', 'diferencia_goles']].copy()
# Normalizar para comparar en la misma escala
metricas_normalizadas = pd.DataFrame()
for col in metricas_rendimiento.columns:
    metricas_normalizadas[col] = (metricas_rendimiento[col] - metricas_rendimiento[col].min()) / \
                                (metricas_rendimiento[col].max() - metricas_rendimiento[col].min())

# Convertir a formato largo
datos_violin = pd.melt(metricas_normalizadas, var_name='metrica', value_name='valor_normalizado')

# Tu código aquí
plt.figure(figsize=(12, 8))
violinplot = sns.violinplot(# Tu código - metrica en x, valor_normalizado en y)

plt.title('🎵 Distribución de Métricas de Rendimiento\n(Valores Normalizados 0-1)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Métricas', fontsize=14)
plt.ylabel('Valor Normalizado', fontsize=14)

# Personalizar etiquetas
plt.xticks([0, 1, 2], ['Puntos', 'Goles a Favor', 'Diferencia de Goles'])

plt.tight_layout()
plt.show()
```

### Parte 3: Dashboard Integrado (25 puntos)

**Instrucciones:**
Crea un dashboard integrado con múltiples subgráficos:

```python
print("\n" + "="*60)
print("📊 DASHBOARD INTEGRADO DE LA LIGA")
print("="*60)

# Tu código aquí
# Crear figura con subplots
fig, axes = plt.subplots(2, 2, figsize=(20, 16))
fig.suptitle('🏈 Dashboard Completo - La Liga Española 2023-24', 
             fontsize=24, fontweight='bold', y=0.98)

# Subplot 1: Top 5 equipos por puntos
ax1 = axes[0, 0]
top_5_equipos = df_liga.nlargest(5, 'puntos')
bars1 = ax1.bar(# Tu código)
ax1.set_title('🏆 Top 5 Equipos por Puntos', fontsize=16, fontweight='bold')
ax1.set_xlabel('Equipos', fontweight='bold')
ax1.set_ylabel('Puntos', fontweight='bold')
ax1.tick_params(axis='x', rotation=45)

# Añadir valores sobre las barras
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')

# Subplot 2: Relación presupuesto vs puntos
ax2 = axes[0, 1]
scatter2 = ax2.scatter(# Tu código - presupuesto en x, puntos en y, 
                      # tamaño proporcional a diferencia_goles)
ax2.set_title('💰 Presupuesto vs Rendimiento', fontsize=16, fontweight='bold')
ax2.set_xlabel('Presupuesto (Millones €)', fontweight='bold')
ax2.set_ylabel('Puntos', fontweight='bold')

# Añadir línea de tendencia
z = np.polyfit(df_liga['presupuesto_millones'], df_liga['puntos'], 1)
p = np.poly1d(z)
ax2.plot(df_liga['presupuesto_millones'], p(df_liga['presupuesto_millones']), 
         "r--", alpha=0.8, label='Tendencia')
ax2.legend()

# Subplot 3: Distribución de goles por posición en la tabla
ax3 = axes[1, 0]
# Dividir equipos en grupos según posición
df_liga_sorted = df_liga.sort_values('puntos', ascending=False).reset_index(drop=True)
df_liga_sorted['posicion_grupo'] = pd.cut(df_liga_sorted.index, 
                                         bins=3, 
                                         labels=['Top (1-3)', 'Medio (4-7)', 'Bajo (8-10)'])

box3 = sns.boxplot(data=df_liga_sorted, x='posicion_grupo', y='goles_favor', ax=ax3)
ax3.set_title('⚽ Goles por Posición en Tabla', fontsize=16, fontweight='bold')
ax3.set_xlabel('Posición en la Tabla', fontweight='bold')
ax3.set_ylabel('Goles a Favor', fontweight='bold')

# Subplot 4: Heatmap simplificado de métricas clave
ax4 = axes[1, 1]
metricas_clave = df_liga[['equipo', 'puntos', 'goles_favor', 'diferencia_goles']].set_index('equipo')
# Normalizar para el heatmap
metricas_norm = (metricas_clave - metricas_clave.min()) / (metricas_clave.max() - metricas_clave.min())

heatmap4 = sns.heatmap(metricas_norm.T, # Transponer para equipos en columnas
                       annot=True, 
                       cmap='RdYlGn', 
                       center=0.5,
                       ax=ax4,
                       fmt='.2f')
ax4.set_title('🔥 Heatmap de Rendimiento', fontsize=16, fontweight='bold')
ax4.set_xlabel('Equipos', fontweight='bold')
ax4.set_ylabel('Métricas (Normalizadas)', fontweight='bold')

plt.tight_layout()
plt.show()

# Crear un segundo dashboard con análisis temporal simulado
print("\n📈 Dashboard de tendencias temporales...")

# Simular datos de progresión durante la temporada
jornadas = list(range(1, 39))  # 38 jornadas de La Liga
np.random.seed(42)

# Tu código aquí
# Simular puntos acumulados para top 3 equipos
fig, axes = plt.subplots(2, 1, figsize=(16, 12))

# Subplot 1: Evolución de puntos durante la temporada
ax_temp1 = axes[0]

for i, equipo in enumerate(['Barcelona', 'Real Madrid', 'Atletico Madrid']):
    puntos_finales = df_liga[df_liga['equipo'] == equipo]['puntos'].iloc[0]
    # Simular progresión realista
    progresion = np.cumsum(np.random.choice([0, 1, 3], 38, p=[0.2, 0.3, 0.5]))
    # Escalar para llegar a puntos finales
    progresion = (progresion / progresion[-1]) * puntos_finales
    
    ax_temp1.plot(jornadas, progresion, marker='o', linewidth=3, 
                  label=equipo, markersize=6)

ax_temp1.set_title('📈 Evolución de Puntos Durante la Temporada\nTop 3 Equipos', 
                   fontsize=16, fontweight='bold')
ax_temp1.set_xlabel('Jornada', fontweight='bold')
ax_temp1.set_ylabel('Puntos Acumulados', fontweight='bold')
ax_temp1.legend(fontsize=12)
ax_temp1.grid(True, alpha=0.3)

# Subplot 2: Promedio de goles por mes (simulado)
ax_temp2 = axes[1]
meses = ['Sep', 'Oct', 'Nov', 'Dec', 'Ene', 'Feb', 'Mar', 'Abr', 'May']
goles_por_mes = np.random.randint(15, 35, len(meses))

bars_temp = ax_temp2.bar(meses, goles_por_mes, color='skyblue', alpha=0.8)
ax_temp2.set_title('📊 Goles Totales por Mes\n(Todos los Equipos)', 
                   fontsize=16, fontweight='bold')
ax_temp2.set_xlabel('Mes', fontweight='bold')
ax_temp2.set_ylabel('Total de Goles', fontweight='bold')

# Añadir valores sobre las barras
for bar in bars_temp:
    height = bar.get_height()
    ax_temp2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                  f'{int(height)}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()
```

### Parte 4: Análisis Visual Final y Reportes (20 puntos)

**Instrucciones:**
Crea visualizaciones interpretativas y genera un reporte visual:

```python
print("\n" + "="*60)
print("📋 ANÁLISIS VISUAL FINAL Y REPORTE")
print("="*60)

# 1. Gráfico de radar/polar para comparar equipos top
print("\n🎯 Creando gráfico de radar para comparación...")

# Tu código aquí
# Preparar datos para gráfico radar de top 3 equipos
top_3 = df_liga.nlargest(3, 'puntos')

# Métricas para el radar (normalizar a escala 0-1)
metricas_radar = ['puntos', 'goles_favor', 'diferencia_goles', 'eficiencia_goles', 'puntos_por_millon']
datos_radar = top_3[metricas_radar].copy()

# Normalizar cada métrica
for col in metricas_radar:
    datos_radar[col] = (datos_radar[col] - df_liga[col].min()) / (df_liga[col].max() - df_liga[col].min())

# Crear gráfico polar
fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(projection='polar'))

# Ángulos para cada métrica
angulos = np.linspace(0, 2 * np.pi, len(metricas_radar), endpoint=False).tolist()
angulos += angulos[:1]  # Cerrar el círculo

# Colores para cada equipo
colores = ['#1f77b4', '#ff7f0e', '#2ca02c']

for i, (idx, equipo_data) in enumerate(top_3.iterrows()):
    valores = datos_radar.iloc[i].tolist()
    valores += valores[:1]  # Cerrar el círculo
    
    ax.plot(angulos, valores, 'o-', linewidth=3, label=equipo_data['equipo'], 
            color=colores[i], markersize=8)
    ax.fill(angulos, valores, alpha=0.25, color=colores[i])

# Personalizar el gráfico
ax.set_xticks(angulos[:-1])
ax.set_xticklabels(['Puntos', 'Goles Favor', 'Dif. Goles', 'Eficiencia', 'Efic. Presup.'])
ax.set_ylim(0, 1)
ax.set_title('🎯 Comparación Multidimensional\nTop 3 Equipos de La Liga', 
             fontsize=16, fontweight='bold', pad=30)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
ax.grid(True)

plt.tight_layout()
plt.show()

# 2. Gráfico de flujo/sankey simplificado para análisis de rendimiento
print("\n🌊 Creando análisis de categorías de rendimiento...")

# Categorizar equipos por rendimiento
def categorizar_rendimiento(fila):
    if fila['puntos'] >= 80:
        return 'Elite'
    elif fila['puntos'] >= 65:
        return 'Muy Bueno'
    elif fila['puntos'] >= 50:
        return 'Bueno'
    else:
        return 'Regular'

def categorizar_presupuesto(presupuesto):
    if presupuesto >= 500:
        return 'Alto'
    elif presupuesto >= 150:
        return 'Medio'
    else:
        return 'Bajo'

df_liga['categoria_rendimiento'] = df_liga.apply(categorizar_rendimiento, axis=1)
df_liga['categoria_presupuesto'] = df_liga['presupuesto_millones'].apply(categorizar_presupuesto)

# Tu código aquí
# Crear gráfico de barras apiladas para mostrar relación presupuesto-rendimiento
tabla_cruzada = pd.crosstab(df_liga['categoria_presupuesto'], df_liga['categoria_rendimiento'])

fig, ax = plt.subplots(figsize=(12, 8))
tabla_cruzada.plot(kind='bar', stacked=True, ax=ax, colormap='viridis')

ax.set_title('💰 Relación Presupuesto vs Rendimiento\nDistribución de Equipos por Categoría', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Categoría de Presupuesto', fontweight='bold')
ax.set_ylabel('Número de Equipos', fontweight='bold')
ax.legend(title='Rendimiento', title_fontsize=12, fontsize=11)

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 3. Crear reporte final con insights clave
print("\n📊 Generando reporte visual final...")

# Tu código aquí
fig, axes = plt.subplots(2, 2, figsize=(20, 16))
fig.suptitle('📋 REPORTE EJECUTIVO VISUAL - LA LIGA 2023-24', 
             fontsize=24, fontweight='bold', y=0.98)

# Panel 1: Métricas clave en texto
ax1 = axes[0, 0]
ax1.axis('off')
ax1.text(0.1, 0.9, '🏆 MÉTRICAS CLAVE', fontsize=20, fontweight='bold', 
         transform=ax1.transAxes)

metricas_texto = f"""
📊 Total de equipos analizados: {len(df_liga)}
⚽ Promedio de goles por equipo: {df_liga['goles_favor'].mean():.1f}
🥅 Promedio de goles en contra: {df_liga['goles_contra'].mean():.1f}
🏅 Equipo líder: {df_liga.loc[df_liga['puntos'].idxmax(), 'equipo']}
📈 Puntos del líder: {df_liga['puntos'].max()}
💰 Presupuesto promedio: {df_liga['presupuesto_millones'].mean():.0f}M €
🎯 Mejor eficiencia: {df_liga.loc[df_liga['puntos_por_millon'].idxmax(), 'equipo']}
"""

ax1.text(0.1, 0.7, metricas_texto, fontsize=14, transform=ax1.transAxes, 
         verticalalignment='top', fontfamily='monospace')

# Panel 2: Top 5 equipos más eficientes
ax2 = axes[0, 1]
top_eficientes = df_liga.nlargest(5, 'puntos_por_millon')
bars2 = ax2.barh(top_eficientes['equipo'], top_eficientes['puntos_por_millon'])
ax2.set_title('💡 Top 5 Más Eficientes\n(Puntos por Millón €)', fontweight='bold')
ax2.set_xlabel('Puntos/Millón €')

# Panel 3: Correlación presupuesto-puntos
ax3 = axes[1, 0]
scatter3 = ax3.scatter(df_liga['presupuesto_millones'], df_liga['puntos'], 
                       s=100, alpha=0.7, c=df_liga['diferencia_goles'], 
                       cmap='RdYlGn')
ax3.set_title('💰 Presupuesto vs Puntos\n(Color = Diferencia de Goles)', fontweight='bold')
ax3.set_xlabel('Presupuesto (Millones €)')
ax3.set_ylabel('Puntos')

# Añadir colorbar
plt.colorbar(scatter3, ax=ax3, label='Diferencia de Goles')

# Panel 4: Distribución de categorías
ax4 = axes[1, 1]
conteo_categorias = df_liga['categoria_rendimiento'].value_counts()
wedges, texts, autotexts = ax4.pie(conteo_categorias.values, 
                                   labels=conteo_categorias.index,
                                   autopct='%1.0f%%',
                                   startangle=90)
ax4.set_title('📊 Distribución por\nCategoría de Rendimiento', fontweight='bold')

plt.tight_layout()
plt.show()

# 4. Generar conclusiones finales
print("\n" + "="*60)
print("🎯 CONCLUSIONES DEL ANÁLISIS VISUAL")
print("="*60)

# Tu código aquí para generar insights basados en las visualizaciones
print(f"\n📈 INSIGHTS PRINCIPALES:")

# Correlación presupuesto-rendimiento
correlacion_presup_puntos = df_liga['presupuesto_millones'].corr(df_liga['puntos'])
print(f"1. Correlación presupuesto-puntos: {correlacion_presup_puntos:.3f}")

# Equipo más eficiente
equipo_eficiente = df_liga.loc[df_liga['puntos_por_millon'].idxmax()]
print(f"2. Equipo más eficiente: {equipo_eficiente['equipo']} ({equipo_eficiente['puntos_por_millon']:.3f} puntos/M€)")

# Análisis defensivo
mejor_defensa = df_liga.loc[df_liga['goles_contra'].idxmin()]
print(f"3. Mejor defensa: {mejor_defensa['equipo']} ({mejor_defensa['goles_contra']} goles en contra)")

# Análisis ofensivo
mejor_ataque = df_liga.loc[df_liga['goles_favor'].idxmax()]
print(f"4. Mejor ataque: {mejor_ataque['equipo']} ({mejor_ataque['goles_favor']} goles a favor)")

print(f"\n🔍 PATRONES IDENTIFICADOS:")
print(f"- Los equipos con mayor presupuesto tienden a obtener más puntos")
print(f"- La eficiencia por presupuesto varía considerablemente entre equipos")
print(f"- Existe una clara segmentación entre equipos top, medios y bajos")
print(f"- La diferencia de goles es un buen predictor de la posición final")

print(f"\n{'='*60}")
print("✅ ANÁLISIS VISUAL COMPLETADO")
print(f"{'='*60}")
```

## 📤 Instrucciones de Entrega

1. **Formato:** Archivo `.py` o notebook `.ipynb`
2. **Nombre del archivo:** `apellido_nombre_ejercicio_semana05.py`
3. **Contenido mínimo:**
   - Todas las visualizaciones generadas correctamente
   - Código bien comentado explicando cada gráfico
   - Personalización profesional de los gráficos
   - Análisis e interpretación de los resultados visuales

4. **Documentación adicional:**
   - Lista de 5 insights principales encontrados en las visualizaciones
   - Explicación de cuál fue la visualización más reveladora y por qué
   - Reflexión sobre la importancia de la visualización en el análisis de datos

## 🏆 Criterios de Evaluación

### Correctitud Técnica (40 puntos)

- **Excelente (36-40):** Todas las visualizaciones se generan correctamente, código sin errores
- **Competente (28-35):** Visualizaciones correctas con errores menores
- **En desarrollo (20-27):** Algunas visualizaciones fallan, errores en el código
- **Insuficiente (0-19):** Múltiples errores, visualizaciones no se generan

### Aplicación Práctica (30 puntos)

- **Excelente (27-30):** Visualizaciones muy informativas, insights relevantes, análisis profundo
- **Competente (21-26):** Visualizaciones apropiadas, algunos insights útiles
- **En desarrollo (15-20):** Visualizaciones básicas, análisis superficial
- **Insuficiente (0-14):** Visualizaciones poco informativas, falta de análisis

### Claridad y Documentación (30 puntos)

- **Excelente (27-30):** Gráficos muy bien personalizados, títulos claros, interpretación excelente
- **Competente (21-26):** Buena personalización, interpretación adecuada
- **En desarrollo (15-20):** Personalización básica, interpretación simple
- **Insuficiente (0-14):** Gráficos mal formateados, interpretación confusa

## 💡 Consejos para el Éxito

1. **Personaliza siempre:** Añade títulos, etiquetas y leyendas claras
2. **Elige colores apropiados:** Usa paletas profesionales y consistentes
3. **Interpreta los resultados:** No solo muestres gráficos, explica qué significan
4. **Usa el tamaño correcto:** Asegúrate de que los gráficos sean legibles
5. **Cuenta una historia:** Organiza las visualizaciones para contar una narrativa coherente

## 🔗 Recursos Adicionales

- [Documentación de matplotlib](https://matplotlib.org/stable/tutorials/index.html)
- [Galería de seaborn](https://seaborn.pydata.org/examples/index.html)
- [Principios de visualización](https://serialmentor.com/dataviz/)
- [Paletas de colores](https://colorbrewer2.org/)

---

*¿Preguntas? Contacta a tu instructor durante las horas de oficina o en el foro del curso.*

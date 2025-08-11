---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.2
---

# Semana 9: Análisis Básico de Jugadores de Fútbol

**Lo que aprenderemos hoy:**

- Explorar estadísticas básicas de jugadores
- Crear gráficos simples para comparar rendimiento
- Identificar patrones en los datos

**Tiempo estimado:** 60 minutos

**Contexto:** Imagina que eres analista de un equipo de fútbol y necesitas evaluar jugadores usando estadísticas básicas como goles, asistencias y partidos jugados.

---

## Objetivos de Aprendizaje

- Cargar y explorar datos de jugadores
- Calcular estadísticas básicas por posición
- Crear visualizaciones simples con pandas y seaborn
- Identificar los mejores jugadores por posición

```python
# Cargar los datos de jugadores
print("Cargando datos de jugadores de fútbol...")

# Dataset simplificado de jugadores
datos_jugadores = pd.read_csv('../datasets/jugadores_liga_juvenil.csv')
print(f"Datos cargados: {len(datos_jugadores)} jugadores")

# Veamos las primeras 5 filas
print("\n¡Echemos un vistazo a nuestros datos!")
print(datos_jugadores.head())
```

```python
# Cargar los datos de jugadores
print("Cargando datos de jugadores de fútbol...")

# Dataset simplificado de jugadores
datos_jugadores = pd.read_csv('../datasets/jugadores_liga_juvenil_simple.csv')
print(f"Datos cargados: {len(datos_jugadores)} jugadores")

# Veamos las primeras 5 filas
print("\n¡Echemos un vistazo a nuestros datos!")
print(datos_jugadores.head())
```

## 1. Exploración Básica de los Datos

¡Vamos a conocer mejor nuestros datos! Es importante entender qué información tenemos antes de hacer cualquier análisis.

```python
# Información básica sobre nuestros datos
print("=== INFORMACIÓN BÁSICA ===")
print(f"Cantidad de jugadores: {len(datos_jugadores)}")
print(f"Cantidad de columnas: {len(datos_jugadores.columns)}")

# Veamos qué columnas tenemos
print("\n¿Qué información tenemos de cada jugador?")
for columna in datos_jugadores.columns:
    print(f"  • {columna}")

# Información por posición
print("\n¿Cuántos jugadores hay por posición?")
jugadores_por_posicion = datos_jugadores['posicion'].value_counts()
print(jugadores_por_posicion)

# Estadísticas básicas
print("\n¿Cuántos goles han marcado en promedio?")
promedio_goles = datos_jugadores['goles'].mean()
print(f"Promedio de goles: {promedio_goles:.1f} goles por jugador")

print(f"El que más goles ha marcado: {datos_jugadores['goles'].max()} goles")
print(f"El que menos goles ha marcado: {datos_jugadores['goles'].min()} goles")
```

```python
# Crear nuestros primeros gráficos
print("¡Vamos a crear gráficos para entender mejor los datos!")

# Gráfico 1: ¿Cuántos jugadores hay por posición?
plt.figure(figsize=(10, 6))
sns.countplot(data=datos_jugadores, x='posicion', hue='posicion', palette='viridis', legend=False)
plt.title('¿Cuántos jugadores tenemos por posición?', fontsize=14, fontweight='bold')
plt.xlabel('Posición en el campo')
plt.ylabel('Cantidad de jugadores')
plt.show()

print("¡Este gráfico nos muestra que tenemos más delanteros y mediocampistas!")
```

```python
# Gráfico 2: ¿Quién marca más goles?
plt.figure(figsize=(10, 6))
sns.boxplot(data=datos_jugadores, x='posicion', y='goles', hue='posicion', palette='viridis', legend=False)
plt.title('¿Qué posición marca más goles?', fontsize=14, fontweight='bold')
plt.xlabel('Posición en el campo')
plt.ylabel('Cantidad de goles')
plt.show()

print("¡Como era de esperarse, los delanteros marcan más goles que las otras posiciones!")
```

```python
## 2. Análisis por Posición

¡Vamos a analizar cómo se desempeña cada posición!
```

# Calcular estadísticas básicas por posición

print("=== ESTADÍSTICAS POR POSICIÓN ===")

# Promedios por posición

estadisticas_por_posicion = datos_jugadores.groupby('posicion').agg({
    'goles': 'mean',
    'asistencias': 'mean',
    'partidos_jugados': 'mean'
}).round(1)

print("Promedios por posición:")
print(estadisticas_por_posicion)

# ¿Quién es el mejor de cada posición?

print("\n¿Quién es el mejor jugador de cada posición? (por goles)")
for posicion in datos_jugadores['posicion'].unique():
    jugadores_posicion = datos_jugadores[datos_jugadores['posicion'] == posicion]
    mejor_jugador = jugadores_posicion.loc[jugadores_posicion['goles'].idxmax()]
    print(f"{posicion}: {mejor_jugador['nombre']} con {mejor_jugador['goles']} goles")

```python
# Gráfico 3: ¿Hay relación entre goles y asistencias?
plt.figure(figsize=(10, 6))
sns.scatterplot(data=datos_jugadores, x='goles', y='asistencias', hue='posicion', s=100)
plt.title('¿Los jugadores que marcan goles también dan asistencias?', fontsize=12, fontweight='bold')
plt.xlabel('Cantidad de goles')
plt.ylabel('Cantidad de asistencias')
plt.show()

print("¡Interesante! Algunos jugadores son buenos en ambas cosas, otros se especializan en una sola.")
```

## 3. Los Mejores Jugadores

¡Vamos a encontrar a los jugadores más destacados!

```python
# Top 5 goleadores
print("=== TOP 5 GOLEADORES ===")
top_goleadores = datos_jugadores.nlargest(5, 'goles')
for i, (idx, jugador) in enumerate(top_goleadores.iterrows(), 1):
    print(f"{i}. {jugador['nombre']} ({jugador['posicion']}) - {jugador['goles']} goles")

print("\n=== TOP 5 ASISTENTES ===")
top_asistentes = datos_jugadores.nlargest(5, 'asistencias')
for i, (idx, jugador) in enumerate(top_asistentes.iterrows(), 1):
    print(f"{i}. {jugador['nombre']} ({jugador['posicion']}) - {jugador['asistencias']} asistencias")
```

# Gráfico final: Los mejores goleadores

plt.figure(figsize=(12, 6))
sns.barplot(data=top_goleadores, x='goles', y='nombre', hue='nombre', palette='viridis', legend=False)
plt.title('Los 5 jugadores que más goles han marcado', fontsize=14, fontweight='bold')
plt.xlabel('Cantidad de goles')
plt.ylabel('Jugador')
plt.show()

print("¡Estos son los jugadores que más goles han marcado en la temporada!")

```python
# Análisis final: ¿Qué aprendimos?

print("=== RESUMEN DE NUESTROS HALLAZGOS ===")

print("\n1. ¿Qué posición marca más goles en promedio?")
goles_por_posicion = datos_jugadores.groupby('posicion')['goles'].mean().sort_values(ascending=False)
mejor_posicion = goles_por_posicion.index[0]
promedio_mejor = goles_por_posicion.iloc[0]
print(f"   Respuesta: {mejor_posicion} con {promedio_mejor:.1f} goles en promedio")

print("\n2. ¿Cuál es la edad promedio por posición?")
edad_por_posicion = datos_jugadores.groupby('posicion')['edad'].mean().round(1)
for posicion, edad in edad_por_posicion.items():
    print(f"   {posicion}: {edad} años")

print("\n3. ¿Hay jugadores que son buenos tanto marcando como asistiendo?")
buenos_ambos = datos_jugadores[(datos_jugadores['goles'] >= 8) & (datos_jugadores['asistencias'] >= 8)]
if len(buenos_ambos) > 0:
    print(f"   Sí, encontramos {len(buenos_ambos)} jugadores:")
    for idx, jugador in buenos_ambos.iterrows():
        print(f"   - {jugador['nombre']}: {jugador['goles']} goles, {jugador['asistencias']} asistencias")
else:
    print("   No hay jugadores que destaquen mucho en ambas categorías")
```

### Lo que Aprendimos Hoy

¡Felicitaciones! Hoy aprendiste a:

- Cargar datos de jugadores de fútbol con pandas
- Explorar información básica usando `.head()`, `.value_counts()` y estadísticas simples  
- Crear gráficos con seaborn para visualizar patrones
- Comparar el rendimiento por posición
- Identificar a los mejores jugadores

### Próxima Semana

En la próxima clase aprenderemos a crear análisis más avanzados y combinar diferentes tipos de datos deportivos.

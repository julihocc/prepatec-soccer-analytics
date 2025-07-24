# Semana 1: Mis Primeros Datos de Fútbol

## Bloque 2: Explorando Datos Deportivos con Python

---

**Lo que aprenderemos hoy:**
- Abrir datos de fútbol en Python
- Ver información básica de equipos y partidos
- Crear gráficos bonitos con seaborn
- Hacer preguntas simples a los datos

**¿Por qué es emocionante?**
¡Vamos a usar Python para descubrir secretos del fútbol que no sabías!

---

## 1. ¿Qué Vamos a Hacer?

### Los Datos del Fútbol

En el fútbol, cada partido genera muchos datos:
- ⚽ **Goles**: Quién marcó y cuándo
- 🏟️ **Equipos**: Local vs Visitante
- 📅 **Fechas**: Cuándo se jugó cada partido
- 🏆 **Competiciones**: Champions League, ligas, etc.

### ¿Por Qué es Genial?

Con Python podemos:
- 📊 Ver patrones que no notamos viendo partidos
- 🔍 Descubrir qué equipos son realmente mejores
- 📈 Hacer gráficos que muestran la verdad sobre el fútbol
- 🎯 Responder preguntas como: "¿Es mejor jugar en casa?"

¡Es como ser detective del fútbol!

## 2. Preparando Nuestras Herramientas

Necesitamos importar las herramientas para trabajar con datos de fútbol.

**Lo que vamos a usar:**
- 📊 **pandas**: Para leer datos como si fuera Excel
- 🎨 **seaborn**: Para hacer gráficos súper bonitos

```python
# Importar las herramientas principales
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configurar seaborn para gráficos bonitos
sns.set_theme(style="whitegrid", palette="viridis")

print("✅ ¡Herramientas listas!")
print("📊 Pandas: Para leer datos de fútbol")
print("🎨 Seaborn: Para gráficos increíbles")
print("⚽ ¡Listos para explorar datos deportivos!")
```

### ¿Qué es Pandas?

Pandas es como Excel, pero más poderoso. Nos ayuda a:
- 📖 Leer datos de archivos
- 🔍 Buscar información específica
- 🧮 Hacer cálculos automáticamente

**Ejemplo simple:** Una tabla con equipos y sus goles

```python
# Una lista simple de equipos favoritos
equipos_favoritos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']

print("⚽ Mis equipos favoritos:")
for i, equipo in enumerate(equipos_favoritos, 1):
    print(f"{i}. {equipo}")

print(f"\n🔢 Total de equipos: {len(equipos_favoritos)}")
```

```python
# Crear una tabla simple con datos de equipos
datos_equipos = {
    'Equipo': ['Barcelona', 'Real Madrid', 'Manchester City'],
    'Goles': [68, 87, 95],
    'Partidos': [38, 38, 38]
}

tabla_equipos = pd.DataFrame(datos_equipos)
print("📊 Tabla de equipos:")
print(tabla_equipos)

print(f"\n✨ ¡Esta tabla tiene {len(tabla_equipos)} equipos y {len(tabla_equipos.columns)} columnas!")
```

## 3. ¡Datos Reales de Fútbol!

Ahora vamos a trabajar con datos reales de partidos.

**¿Qué contienen estos datos?**
- 🏟️ Equipos que jugaron
- ⚽ Goles marcados
- 📅 Cuándo se jugó
- 🏆 En qué competición

¡Vamos a crear datos de ejemplo que parecen reales!

```python
# Crear datos simples de partidos de fútbol
import random

equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich', 
          'Liverpool', 'Paris Saint-Germain', 'Chelsea', 'Juventus']

# Crear lista de partidos
partidos = []
for i in range(50):  # 50 partidos
    equipo_local = random.choice(equipos)
    equipo_visitante = random.choice([e for e in equipos if e != equipo_local])
    
    partidos.append({
        'Equipo_Local': equipo_local,
        'Equipo_Visitante': equipo_visitante,
        'Goles_Local': random.randint(0, 4),
        'Goles_Visitante': random.randint(0, 3),
        'Temporada': random.choice(['2022-23', '2023-24'])
    })

# Convertir a tabla
datos_futbol = pd.DataFrame(partidos)
print("⚽ ¡Datos de fútbol creados!")
print(f"📊 Tenemos {len(datos_futbol)} partidos")
print(f"🏟️ Con {len(equipos)} equipos diferentes")
```

### Echemos un Vistazo a Nuestros Datos

¡Vamos a ver qué partidos tenemos!

```python
# Ver los primeros 10 partidos
print("🔍 Los primeros 10 partidos:")
print(datos_futbol.head(10))

print(f"\n📈 Resumen rápido:")
print(f"• Total de partidos: {len(datos_futbol)}")
print(f"• Columnas de información: {list(datos_futbol.columns)}")
```

```python
# Calcular algunas estadísticas interesantes
total_goles = datos_futbol['Goles_Local'].sum() + datos_futbol['Goles_Visitante'].sum()
promedio_goles = total_goles / len(datos_futbol)

print("⚽ Estadísticas Básicas:")
print(f"• Total de goles en todos los partidos: {total_goles}")
print(f"• Promedio de goles por partido: {promedio_goles:.1f}")
print(f"• Gol máximo en un partido (local): {datos_futbol['Goles_Local'].max()}")
print(f"• Gol máximo en un partido (visitante): {datos_futbol['Goles_Visitante'].max()}")
```

## 4. ¡Hagamos Gráficos Bonitos con Seaborn!

Ahora viene lo divertido: convertir números en gráficos increíbles.

```python
# Gráfico 1: ¿Cuántos goles marcan los equipos locales?
plt.figure(figsize=(10, 6))
sns.countplot(data=datos_futbol, x='Goles_Local', palette='viridis')
plt.title('¿Cuántos Goles Marcan los Equipos Locales?', fontsize=16, fontweight='bold')
plt.xlabel('Goles Marcados')
plt.ylabel('Número de Partidos')
plt.show()

print("📊 ¡Este gráfico nos muestra qué tan seguido los equipos marcan 0, 1, 2, 3 o 4 goles en casa!")
```

```python
# Gráfico 2: ¿Es mejor jugar en casa?
datos_futbol['Total_Goles'] = datos_futbol['Goles_Local'] + datos_futbol['Goles_Visitante']

plt.figure(figsize=(10, 6))
sns.boxplot(data=datos_futbol, y='Total_Goles', palette='Set2')
plt.title('¿Cuántos Goles Hay por Partido?', fontsize=16, fontweight='bold')
plt.ylabel('Total de Goles en el Partido')
plt.show()

print("📈 ¡Este gráfico nos muestra si hay partidos con muchos o pocos goles!")
print(f"🎯 Promedio de goles por partido: {datos_futbol['Total_Goles'].mean():.1f}")
```

```python
# Gráfico 3: ¿Qué equipos juegan más partidos?
equipos_conteo = datos_futbol['Equipo_Local'].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=equipos_conteo.values, y=equipos_conteo.index, palette='plasma')
plt.title('¿Qué Equipos Aparecen Más Como Locales?', fontsize=16, fontweight='bold')
plt.xlabel('Número de Partidos como Local')
plt.ylabel('Equipos')
plt.show()

print("🏟️ ¡Este gráfico muestra qué equipos jugaron más partidos en casa!")
print(f"🎯 El equipo que más jugó en casa: {equipos_conteo.index[0]} con {equipos_conteo.iloc[0]} partidos")
```

```python
# ¿Es mejor jugar en casa? ¡Vamos a descubrirlo!
# Crear una nueva columna que diga quién ganó
def quien_gano(fila):
    if fila['Goles_Local'] > fila['Goles_Visitante']:
        return 'Ganó Local'
    elif fila['Goles_Local'] < fila['Goles_Visitante']:
        return 'Ganó Visitante'
    else:
        return 'Empate'

datos_futbol['Resultado'] = datos_futbol.apply(quien_gano, axis=1)

# Hacer gráfico con seaborn
plt.figure(figsize=(10, 6))
sns.countplot(data=datos_futbol, x='Resultado', palette='Set1')
plt.title('¿Es Mejor Jugar en Casa?', fontsize=16, fontweight='bold')
plt.xlabel('Resultado del Partido')
plt.ylabel('Número de Partidos')
plt.show()

# Mostrar porcentajes
resultados = datos_futbol['Resultado'].value_counts()
total = len(datos_futbol)
print("🏟️ Ventaja de jugar en casa:")
for resultado, cantidad in resultados.items():
    porcentaje = (cantidad / total) * 100
    print(f"• {resultado}: {cantidad} partidos ({porcentaje:.1f}%)")
```

## 5. ¡Tu Turno! Ejercicio Práctico

Ahora vamos a hacer algunos descubrimientos por nuestra cuenta.

```python
# Ejercicio 1: ¡Encuentra el partido con más goles!
datos_futbol['Total_Goles'] = datos_futbol['Goles_Local'] + datos_futbol['Goles_Visitante']
partido_mas_goles = datos_futbol.loc[datos_futbol['Total_Goles'].idxmax()]

print("🎯 El partido con más goles fue:")
print(f"⚽ {partido_mas_goles['Equipo_Local']} {partido_mas_goles['Goles_Local']} - {partido_mas_goles['Goles_Visitante']} {partido_mas_goles['Equipo_Visitante']}")
print(f"⚽ Total de goles: {partido_mas_goles['Total_Goles']}")

# Ejercicio 2: ¿Cuál es tu equipo favorito?
mi_equipo_favorito = "Barcelona"  # ¡Cambia esto por tu equipo favorito!

partidos_favorito = datos_futbol[
    (datos_futbol['Equipo_Local'] == mi_equipo_favorito) | 
    (datos_futbol['Equipo_Visitante'] == mi_equipo_favorito)
]

print(f"\n⚽ Partidos de {mi_equipo_favorito}:")
print(f"🎮 Total de partidos: {len(partidos_favorito)}")

if len(partidos_favorito) > 0:
    print("📋 Algunos partidos:")
    print(partidos_favorito[['Equipo_Local', 'Goles_Local', 'Goles_Visitante', 'Equipo_Visitante']].head())
else:
    print("😔 Tu equipo no está en estos datos. ¡Prueba con otro!")
```

```python
# Análisis más profundo de nuestros datos de fútbol
# Vamos a crear visualizaciones más interesantes

# Crear nuevas columnas para análisis
datos_futbol['diferencia_goles'] = datos_futbol['Goles_Local'] - datos_futbol['Goles_Visitante']

# Crear visualizaciones con subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. Distribución de goles por temporada
sns.boxplot(data=datos_futbol, x='Temporada', y='Total_Goles', ax=axes[0,0], palette='Set2')
axes[0,0].set_title('Distribución de Goles por Temporada', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Temporada')
axes[0,0].set_ylabel('Total de Goles')

# 2. Goles locales vs visitantes
sns.scatterplot(data=datos_futbol, x='Goles_Local', y='Goles_Visitante', 
                hue='Resultado', ax=axes[0,1], s=80, alpha=0.7)
axes[0,1].set_title('Goles Locales vs Visitantes', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Goles Equipo Local')
axes[0,1].set_ylabel('Goles Equipo Visitante')

# 3. Diferencia de goles por resultado
sns.violinplot(data=datos_futbol, x='Resultado', y='diferencia_goles', 
               ax=axes[1,0], palette='viridis')
axes[1,0].set_title('Diferencia de Goles por Resultado', fontsize=12, fontweight='bold')
axes[1,0].set_xlabel('Resultado del Partido')
axes[1,0].set_ylabel('Diferencia de Goles (Local - Visitante)')

# 4. Distribución de goles totales
sns.histplot(data=datos_futbol, x='Total_Goles', bins=8, 
             ax=axes[1,1], color='skyblue', alpha=0.7)
axes[1,1].axvline(datos_futbol['Total_Goles'].mean(), color='red', 
                  linestyle='--', label=f'Promedio: {datos_futbol["Total_Goles"].mean():.1f}')
axes[1,1].set_title('Distribución de Goles Totales por Partido', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Total de Goles')
axes[1,1].set_ylabel('Frecuencia')
axes[1,1].legend()

plt.tight_layout()
plt.show()

print("🎨 ¡Análisis visual completado!")
print("📊 Estas gráficas muestran patrones interesantes:")
print(f"⚽ Promedio de goles por partido: {datos_futbol['Total_Goles'].mean():.1f}")
print(f"🏟️ Diferencia promedio (local-visitante): {datos_futbol['diferencia_goles'].mean():.1f}")
print(f"📈 Rango de goles: {datos_futbol['Total_Goles'].min()} - {datos_futbol['Total_Goles'].max()}")
```

```python
# Verificación final de nuestros datos de fútbol
print("🔍 Información completa de nuestros datos:")
print(f"📊 Total de filas: {len(datos_futbol)}")
print(f"📋 Total de columnas: {len(datos_futbol.columns)}")

# Verificar datos faltantes
print("\n🔍 Verificación de datos faltantes:")
print(datos_futbol.isnull().sum())

# Mostrar tipos de datos
print("\n📋 Tipos de datos:")
print(datos_futbol.dtypes)

# Estadísticas por temporada
print("\n⚽ Estadísticas por temporada:")
stats_temporada = datos_futbol.groupby('Temporada').agg({
    'Total_Goles': ['mean', 'sum', 'count'],
    'Goles_Local': 'mean',
    'Goles_Visitante': 'mean'
}).round(2)

for temporada in datos_futbol['Temporada'].unique():
    temp_data = datos_futbol[datos_futbol['Temporada'] == temporada]
    print(f"\n🏆 Temporada {temporada}:")
    print(f"  • Partidos jugados: {len(temp_data)}")
    print(f"  • Promedio goles/partido: {temp_data['Total_Goles'].mean():.1f}")
    print(f"  • Total goles temporada: {temp_data['Total_Goles'].sum()}")
    
# Verificar valores únicos en columnas importantes
print("\n🔢 Valores únicos por columna:")
for col in ['Temporada', 'Resultado']:
    if col in datos_futbol.columns:
        valores_unicos = datos_futbol[col].value_counts()
        print(f"\n{col}:")
        for valor, cantidad in valores_unicos.items():
            print(f"  • {valor}: {cantidad} registros")

print("\n✅ ¡Verificación de datos completada!")
```

## 6. ¡Felicitaciones! 🎉

### Lo que Descubrimos Hoy

✅ **Datos de fútbol**: Aprendimos a leer información de partidos  
✅ **Pandas**: Usamos tablas como si fuera Excel, pero mejor  
✅ **Seaborn**: Hicimos gráficos súper bonitos automáticamente  
✅ **Preguntas interesantes**: ¿Es mejor jugar en casa? ¿Qué equipos marcan más?

### ¿Qué Descubrimos?

🏟️ **Ventaja de local**: Los datos nos dijeron si es mejor jugar en casa  
📊 **Goles por partido**: Vimos cuántos goles son normales en un partido  
⚽ **Equipos favoritos**: Encontramos información de nuestros equipos  

### ¿Por Qué es Genial?

- 🔍 **Descubrimos secretos**: Cosas que no sabíamos solo viendo partidos
- 📈 **Gráficos bonitos**: Seaborn hizo que todo se viera increíble
- 📚 **Fácil de entender**: Los datos complicados se volvieron simples

### Comandos Importantes para Recordar

- `pd.DataFrame()` → Crear tablas de datos
- `sns.countplot()` → Contar cosas con gráficos bonitos
- `sns.barplot()` → Comparar con barras coloridas
- `data.head()` → Ver los primeros datos
- `data.value_counts()` → Contar qué aparece más

**¡Ya sabes usar datos reales de fútbol con Python!** ⚽

---

*En la próxima semana aprenderemos más trucos para descubrir secretos del fútbol con datos.*

## 7. ¡Practica en Casa! 🏠

### Tu Misión (si decides aceptarla)

1. **Cambia tu equipo favorito**:
   - En el ejercicio, cambia `"Barcelona"` por tu equipo favorito
   - Ejecuta el código y ve qué encuentras

2. **Haz tu propia pregunta**:
   - ¿Qué temporada tuvo más goles?
   - ¿Qué equipo aparece más como visitante?
   - ¡Inventa tu propia pregunta y trata de responderla!

3. **Experimenta con seaborn**:
   - Cambia las paletas de colores: prueba `'plasma'`, `'Set3'`, `'husl'`
   - Cambia los títulos de los gráficos
   - ¡Haz que se vean aún más bonitos!

### Desafío Extra (Opcional)

- Crea un gráfico que muestre qué temporada tuvo más partidos
- Usa `sns.countplot()` con la columna `'Temporada'`

### ¿Tienes Preguntas?

¡Experimenta y diviértete! La mejor forma de aprender es jugando con los datos.

---

**¡Excelente trabajo en tu primera exploración de datos deportivos!** 🚀

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

# Semana 14: ¿Cómo crear mejores estadísticas para nuestros análisis?

## SESIÓN 1: ¿Qué información necesita un buen scout de fútbol? (50 min)
**Pregunta guía**: ¿Cómo podemos crear nuevas estadísticas que nos ayuden a entender mejor a los jugadores?

### ¿Has observado cómo trabajan los scouts profesionales?

Imagínate que eres un scout del Real Madrid y debes evaluar a un jugador del Barcelona para un posible fichaje.

**¿Qué observarías?**
- ¿Solo los goles que marca?
- ¿O también cómo se desempeña bajo presión?
- ¿Su consistencia a lo largo de la temporada?
- ¿Cómo juega contra rivales difíciles vs. rivales fáciles?

**Pregunta reflexiva**: ¿Crees que las estadísticas básicas (goles, asistencias) son suficientes para evaluar completamente a un jugador?

### El concepto de "estadísticas creadas"

A veces necesitamos crear nuevas medidas que no existen directamente en los datos:

- **Ejemplo 1**: Goles por partido = Total de goles ÷ Partidos jugados
- **Ejemplo 2**: Efectividad = Goles ÷ Disparos realizados  
- **Ejemplo 3**: Consistencia = ¿Qué tan parecido es su rendimiento cada partido?

¿Se te ocurren otras estadísticas útiles que podríamos crear?


### Práctica inmediata: Mejorando el análisis del Barcelona

Tenemos datos básicos de jugadores del Barcelona, pero queremos crear estadísticas más inteligentes para entender mejor su rendimiento.

**Datos básicos que tenemos:**
- Goles marcados en la temporada
- Partidos jugados
- Minutos totales en el campo
- Edad del jugador

**Estadísticas nuevas que crearemos:**
1. **Promedio de goles por partido**
2. **Minutos promedio por partido**  
3. **Eficiencia por minuto** (goles cada 90 minutos)
4. **Categoría de experiencia** (joven, experimentado, veterano)

**Pregunta guía**: ¿Cómo crees que estas nuevas estadísticas nos ayudarán a comparar mejor a los jugadores?

Vamos a descubrirlo creando y analizando estos datos.

```python
# Importamos las herramientas necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Datos básicos de jugadores del Barcelona (simulados pero realistas)
datos_basicos = {
    'Jugador': ['Lewandowski', 'Gavi', 'Pedri', 'De Jong', 'Raphinha', 
                'Ferran Torres', 'Ansu Fati', 'Balde', 'Araujo', 'Ter Stegen',
                'Kounde', 'Christensen', 'Sergi Roberto', 'Marcos Alonso'],
    'Goles_Temporada': [23, 4, 6, 2, 12, 8, 7, 1, 2, 0, 3, 1, 2, 3],
    'Partidos_Jugados': [35, 32, 38, 28, 34, 25, 18, 30, 33, 38, 36, 22, 15, 12],
    'Minutos_Totales': [3000, 2400, 3200, 2100, 2800, 1800, 1200, 2200, 2700, 3420, 3100, 1650, 900, 600],
    'Edad': [35, 19, 21, 26, 26, 24, 21, 20, 24, 31, 25, 27, 31, 30]
}

barcelona_datos = pd.DataFrame(datos_basicos)
print("📊 Datos básicos del Barcelona:")
print(barcelona_datos)
print(f"\n📈 Tenemos información de {len(barcelona_datos)} jugadores")
print("Ahora vamos a crear estadísticas más inteligentes con estos datos...")
```

```python
# Creamos nuevas estadísticas más útiles

# 1. Promedio de goles por partido
barcelona_datos['Goles_Por_Partido'] = barcelona_datos['Goles_Temporada'] / barcelona_datos['Partidos_Jugados']

# 2. Minutos promedio por partido
barcelona_datos['Minutos_Por_Partido'] = barcelona_datos['Minutos_Totales'] / barcelona_datos['Partidos_Jugados']

# 3. Eficiencia por cada 90 minutos (un partido completo)
barcelona_datos['Goles_Por_90min'] = (barcelona_datos['Goles_Temporada'] / barcelona_datos['Minutos_Totales']) * 90

# 4. Categoría de experiencia basada en la edad
def categorizar_edad(edad):
    if edad <= 22:
        return 'Joven'
    elif edad <= 28:
        return 'Experimentado'  
    else:
        return 'Veterano'

barcelona_datos['Categoria_Experiencia'] = barcelona_datos['Edad'].apply(categorizar_edad)

# Mostramos las nuevas estadísticas
print("🎯 Nuevas estadísticas creadas:")
print(barcelona_datos[['Jugador', 'Goles_Por_Partido', 'Minutos_Por_Partido', 
                       'Goles_Por_90min', 'Categoria_Experiencia']].round(2))

print("\n¿Qué nuevas perspectivas nos dan estas estadísticas?")
print("¿Quién es más eficiente: el que marca más goles totales o el que marca más goles por partido?")
```

## SESIÓN 2: ¿Cómo identificamos patrones ocultos en los datos? (50 min)
**Pregunta guía**: ¿Qué historias nos cuentan nuestras nuevas estadísticas?

### Comparando jugadores con diferentes enfoques

Ahora que tenemos estadísticas más sofisticadas, podemos hacer comparaciones más justas:

**Comparación tradicional:**
- Lewandowski: 23 goles
- Raphinha: 12 goles  
- Conclusión: Lewandowski es mejor

**Comparación con nuevas estadísticas:**
- Lewandowski: 0.66 goles por partido
- Raphinha: 0.35 goles por partido
- Pero... ¿qué pasa si consideramos minutos jugados?

**Pregunta reflexiva**: ¿Cómo cambia nuestra perspectiva cuando usamos diferentes métricas para comparar?

### Descubriendo patrones por categorías

¿Existen diferencias entre jugadores jóvenes, experimentados y veteranos?
¿Los defensores tienen patrones diferentes a los delanteros?

Vamos a investigar estos patrones usando nuestras nuevas estadísticas.

```python
# Analizamos patrones por categoría de experiencia

print("📊 Análisis por categoría de experiencia:")
print("="*50)

for categoria in ['Joven', 'Experimentado', 'Veterano']:
    jugadores_categoria = barcelona_datos[barcelona_datos['Categoria_Experiencia'] == categoria]
    
    if len(jugadores_categoria) > 0:
        promedio_goles_partido = jugadores_categoria['Goles_Por_Partido'].mean()
        promedio_minutos = jugadores_categoria['Minutos_Por_Partido'].mean()
        promedio_eficiencia = jugadores_categoria['Goles_Por_90min'].mean()
        
        print(f"\n🏷️ Jugadores {categoria}:")
        print(f"   Cantidad: {len(jugadores_categoria)} jugadores")
        print(f"   Goles por partido promedio: {promedio_goles_partido:.2f}")
        print(f"   Minutos por partido promedio: {promedio_minutos:.1f}")
        print(f"   Eficiencia (goles/90min): {promedio_eficiencia:.2f}")
        
        print(f"   Jugadores: {', '.join(jugadores_categoria['Jugador'].tolist())}")

print("\n🤔 Pregunta reflexiva:")
print("¿Qué patrones observas? ¿Los veteranos son más o menos eficientes que los jóvenes?")

# Creamos una nueva estadística: Regularidad de juego
barcelona_datos['Regularidad'] = barcelona_datos['Minutos_Por_Partido'] / 90  # Qué fracción del partido juega
print(f"\n📈 Nueva estadística: Regularidad de juego (0=nunca juega, 1=siempre completo)")
print(barcelona_datos[['Jugador', 'Regularidad', 'Categoria_Experiencia']].round(2))
```

```python
# Visualizamos nuestras nuevas estadísticas
plt.figure(figsize=(12, 8))

# Gráfico 1: Eficiencia por categoría de experiencia
plt.subplot(2, 2, 1)
sns.boxplot(data=barcelona_datos, x='Categoria_Experiencia', y='Goles_Por_90min')
plt.title('Eficiencia de Goles por Categoría de Experiencia')
plt.ylabel('Goles cada 90 minutos')
plt.xticks(rotation=45)

# Gráfico 2: Regularidad vs Goles por partido
plt.subplot(2, 2, 2)
plt.scatter(barcelona_datos['Regularidad'], barcelona_datos['Goles_Por_Partido'], 
           c=barcelona_datos['Edad'], cmap='viridis', s=100)
plt.xlabel('Regularidad (fracción del partido)')
plt.ylabel('Goles por partido')
plt.title('¿Más tiempo = Más goles?')
plt.colorbar(label='Edad')

# Gráfico 3: Distribución de nuevas estadísticas
plt.subplot(2, 2, 3)
barcelona_datos['Goles_Por_Partido'].hist(bins=8, alpha=0.7, color='skyblue')
plt.xlabel('Goles por partido')
plt.ylabel('Cantidad de jugadores')
plt.title('Distribución: Goles por Partido')

# Gráfico 4: Comparación por experiencia
plt.subplot(2, 2, 4)
categoria_stats = barcelona_datos.groupby('Categoria_Experiencia')['Goles_Por_90min'].mean()
categoria_stats.plot(kind='bar', color=['lightgreen', 'orange', 'lightcoral'])
plt.title('Eficiencia Promedio por Experiencia')
plt.ylabel('Goles por 90 minutos')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

print("🎯 ¿Qué conclusiones puedes sacar de estos gráficos?")
print("¿Las nuevas estadísticas revelan patrones que no veíamos antes?")
```

## SESIÓN 3: ¿Cómo mejoran nuestros modelos con mejores estadísticas? (50 min)
**Pregunta guía**: ¿Nuestras nuevas estadísticas hacen que las predicciones sean más precisas?

### Experimento: Comparando modelos

Vamos a comparar dos enfoques para predecir si un jugador será titular:

**Modelo Básico:**
- Solo usa: Goles totales, Edad, Minutos totales

**Modelo Mejorado:**  
- Usa nuestras nuevas estadísticas: Goles por partido, Eficiencia por 90min, Regularidad, Categoría de experiencia

**Hipótesis**: El modelo con mejores estadísticas debería ser más preciso.

**Pregunta reflexiva**: ¿Por qué crees que estadísticas más específicas podrían mejorar las predicciones?

### Creando etiquetas para nuestro experimento

Primero necesitamos definir qué hace a un jugador "titular regular" basándonos en nuestros datos.

```python
# Creamos una etiqueta para "titular regular" basada en regularidad de juego
# Un titular regular juega más del 70% del tiempo disponible
barcelona_datos['Es_Titular_Regular'] = (barcelona_datos['Regularidad'] > 0.7).astype(int)

print("🎯 Clasificación de jugadores:")
titulares = barcelona_datos[barcelona_datos['Es_Titular_Regular'] == 1]
suplentes = barcelona_datos[barcelona_datos['Es_Titular_Regular'] == 0]

print(f"✅ Titulares regulares ({len(titulares)}): {', '.join(titulares['Jugador'].tolist())}")
print(f"🔄 Suplentes/Rotación ({len(suplentes)}): {', '.join(suplentes['Jugador'].tolist())}")

# Preparamos datos para entrenar modelos
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Convertimos categorías de experiencia a números para el modelo
le = LabelEncoder()
barcelona_datos['Experiencia_Numerica'] = le.fit_transform(barcelona_datos['Categoria_Experiencia'])

# Modelo Básico: características originales
caracteristicas_basicas = ['Goles_Temporada', 'Edad', 'Minutos_Totales']
X_basico = barcelona_datos[caracteristicas_basicas]

# Modelo Mejorado: nuevas estadísticas
caracteristicas_mejoradas = ['Goles_Por_Partido', 'Goles_Por_90min', 'Regularidad', 'Experiencia_Numerica']
X_mejorado = barcelona_datos[caracteristicas_mejoradas]

# Variable objetivo
y = barcelona_datos['Es_Titular_Regular']

print(f"\n📊 Características del Modelo Básico: {caracteristicas_basicas}")
print(f"📈 Características del Modelo Mejorado: {caracteristicas_mejoradas}")
print(f"🎯 Objetivo: Predecir si es titular regular (1) o suplente (0)")
```

### Entrenando y comparando los modelos

**Nota importante**: Con pocos datos (14 jugadores), nuestro experimento es educativo. En análisis reales necesitaríamos cientos o miles de jugadores.

**¿Qué esperamos descubrir?**
- ¿Las estadísticas más específicas ayudan al modelo a entender mejor?
- ¿Hay diferencias significativas en la precisión?
- ¿Qué características son más importantes para determinar titularidad?

Vamos a entrenar ambos modelos y comparar sus resultados.

```python
# Entrenamos ambos modelos
# Nota: Con pocos datos, usamos todo el conjunto para demostración

# Modelo Básico
modelo_basico = LogisticRegression(random_state=42)
modelo_basico.fit(X_basico, y)
predicciones_basicas = modelo_basico.predict(X_basico)
precision_basica = accuracy_score(y, predicciones_basicas)

# Modelo Mejorado  
modelo_mejorado = LogisticRegression(random_state=42)
modelo_mejorado.fit(X_mejorado, y)
predicciones_mejoradas = modelo_mejorado.predict(X_mejorado)
precision_mejorada = accuracy_score(y, predicciones_mejoradas)

# Comparamos resultados
print("🏆 Resultados de la comparación:")
print("="*40)
print(f"📊 Modelo Básico - Precisión: {precision_basica*100:.1f}%")
print(f"📈 Modelo Mejorado - Precisión: {precision_mejorada*100:.1f}%")

diferencia = precision_mejorada - precision_basica
if diferencia > 0:
    print(f"✅ El modelo mejorado es {diferencia*100:.1f}% más preciso")
elif diferencia < 0:
    print(f"❌ El modelo básico es {abs(diferencia)*100:.1f}% más preciso")
else:
    print("🤝 Ambos modelos tienen la misma precisión")

# Mostramos predicciones lado a lado
comparacion_detallada = pd.DataFrame({
    'Jugador': barcelona_datos['Jugador'],
    'Realidad': y,
    'Prediccion_Basica': predicciones_basicas,
    'Prediccion_Mejorada': predicciones_mejoradas,
    'Acierto_Basico': (y == predicciones_basicas).astype(int),
    'Acierto_Mejorado': (y == predicciones_mejoradas).astype(int)
})

print(f"\n📋 Comparación detallada por jugador:")
print("(1 = Titular regular, 0 = Suplente/Rotación)")
print(comparacion_detallada)
```

### Síntesis de la Semana 14: ¿Qué hemos descubierto sobre crear mejores estadísticas?

**Pregunta final de reflexión**: ¿Por qué es importante pensar creativamente sobre qué información darle a nuestros modelos?

### Lo que aprendimos hoy:

1. **Las estadísticas derivadas pueden ser más útiles que las básicas**
   - Goles por partido vs. goles totales
   - Eficiencia por 90 minutos vs. minutos totales
   - Categorías de experiencia vs. edad exacta

2. **Los patrones emergen con mejores estadísticas**
   - Diferencias entre categorías de experiencia
   - Relaciones entre regularidad y rendimiento
   - Visualizaciones más reveladoras

3. **Los modelos mejoran con mejores características**
   - Estadísticas más específicas pueden mejorar predicciones
   - La calidad de la información importa más que la cantidad
   - Debemos pensar como scouts: ¿qué realmente importa?

### Aplicación práctica en el fútbol real

**Estas técnicas ayudan a:**
- Scouts: Crear métricas más precisas para evaluar jugadores
- Analistas: Descubrir patrones ocultos en el rendimiento
- Entrenadores: Tomar decisiones basadas en estadísticas más inteligentes
- Clubes: Optimizar fichajes y estrategias de juego

### Preparándose para el proyecto final

**Pregunta puente**: Ahora que sabemos crear modelos, combinarlos, evaluarlos y mejorar sus características... ¿estás listo para aplicar todo esto en un proyecto real?

La próxima semana integraremos todo lo aprendido en un análisis completo de datos futbolísticos reales.

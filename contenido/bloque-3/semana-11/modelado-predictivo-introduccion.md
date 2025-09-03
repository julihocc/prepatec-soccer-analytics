---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.3
  kernelspec:
    display_name: .venv
    language: python
    name: python3
---

# Semana 11: ¿Alguna vez has querido adivinar quién va a ganar antes del partido?

## ¿Te has preguntado cómo algunos entrenadores parecen "adivinar" siempre bien?

**Reflexión inicial**: Cuando ves a Pep Guardiola tomar decisiones que resultan perfectas, ¿crees que es solo suerte o que tiene algún método secreto? ¿Será que usa información del pasado para predecir qué va a pasar?

### Pregunta motivadora para la semana:
Si fueras entrenador del Barcelona y tuvieras que decidir la alineación para el Clásico contra el Real Madrid, ¿cómo usarías los datos de partidos anteriores para tomar la mejor decisión?

---

## ESTRUCTURA SEMANAL: 3 Sesiones de Descubrimiento

### SESIÓN 1: ¿Qué significa "predecir" usando datos? (50 min)
**Pregunta guía**: ¿Cómo pasamos de "esto pasó" a "esto va a pasar"?
**Contenido máximo**: 15 min teoría + 25 min práctica + 10 min reflexión
- ¿Qué es una predicción y por qué es útil en el fútbol?
- Diferencia entre adivinar y predecir con datos
- Primera predicción simple: ¿quién gana en casa vs visitante?

### SESIÓN 2: ¿Cómo le enseñamos a la computadora a predecir? (50 min)  
**Pregunta guía**: ¿Qué información necesita una computadora para hacer pronósticos?
**Contenido máximo**: 10 min repaso + 30 min práctica + 10 min conexiones
- Mi primer modelo de predicción con Python
- Entrenamiento vs predicción (como entrenar a un jugador)
- Probando nuestro modelo con datos nuevos

### SESIÓN 3: ¿Qué tan buenas son nuestras predicciones? (50 min)
**Pregunta guía**: ¿Cómo sabemos si nuestro modelo está funcionando bien?
**Contenido máximo**: 5 min repaso + 35 min aplicación + 10 min síntesis
- Midiendo qué tanto acertamos
- ¿Cuándo podemos confiar en nuestras predicciones?
- Aplicación: prediciendo resultados de partidos reales

---

## ¿Por qué aprender a predecir con datos?

**Pregunta reflexiva**: ¿Has notado que algunos equipos pequeños vencen a equipos grandes de manera "inesperada"? ¿Será realmente inesperado o podríamos haberlo predicho con datos?

### La magia detrás de las decisiones deportivas:
- **¿Sabías que...?** Los equipos profesionales usan computadoras para decidir alineaciones
- **¿Te imaginas que...?** Podemos predecir quién va a ganar un partido antes de que empiece
- **¿Has considerado que...?** Los datos del pasado nos ayudan a tomar mejores decisiones para el futuro

**Tu misión esta semana**: Aprender a hacer tus primeras predicciones deportivas usando Python.

¿Estás listo para descubrir cómo predecir el futuro del fútbol?


# SESIÓN 1: ¿Qué significa "predecir" usando datos? (50 minutos)

## Pregunta de apertura: ¿Qué tienen en común un meteorólogo y un entrenador de fútbol?

**Reflexiona antes de continuar**: Ambos usan información del pasado para predecir qué va a pasar en el futuro. El meteorólogo usa datos del clima, el entrenador usa datos de partidos anteriores.

---

## Momento de curiosidad: ¿Cómo saber quién va a ganar antes del partido?

Imagina que vas a ver el partido Barcelona vs Real Madrid. Tu amigo te dice: "Seguro gana el Barcelona". ¿En qué se basa para decir eso?

**Posibles respuestas:**
- "Porque siempre gana el Barcelona"
- "Porque tiene mejores jugadores" 
- "Porque juega en casa"
- "Porque ganó los últimos 3 partidos"

**Pregunta reflexiva**: ¿Cuál de estas razones usa datos reales y cuál es solo opinión?

### ¿Qué diferencia una opinión de una predicción con datos?

**Piensa en esto**: Cuando dices "va a llover", ¿te basas en datos (nubes oscuras, humedad) o solo en intuición?

En el fútbol es igual. ¿Podemos usar datos de partidos anteriores para predecir resultados futuros?

```python
# ¿Qué herramientas necesitamos para hacer predicciones?
# Piensa: ¿Qué usa un entrenador para analizar a su equipo?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Herramientas especiales para predicciones (¡La magia empieza aquí!)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Configuración visual (para que nuestros gráficos se vean profesionales)
sns.set_theme(style="whitegrid", palette="viridis")

print("¡Herramientas de predicción listas!")
print("¿Sabías que estas son las mismas herramientas que usan en el Real Madrid?")
print()
print("Pregunta: ¿Por qué crees que necesitamos bibliotecas especiales para predecir?")
```

## ¿Cómo funciona una predicción paso a paso?

**Analogía del entrenador**: Un entrenador experimentado predice resultados siguiendo estos pasos:

### Paso 1: Mirar el pasado (Datos históricos)
- "En los últimos 10 partidos en casa, ganamos 8"
- "Contra equipos similares, marcamos 2 goles en promedio"
- "Cuando llueve, nuestro rendimiento baja 20%"

### Paso 2: Buscar patrones (Entrenamiento)
- "Cuando jugamos en casa + tenemos a nuestro goleador = 90% de probabilidad de ganar"
- "Si el rival ha perdido sus últimos 2 partidos = más fácil ganar"

### Paso 3: Aplicar al futuro (Predicción)
- "Mañana jugamos en casa + tenemos al goleador + el rival perdió ayer"
- "Conclusión: Alta probabilidad de ganar"

**Pregunta clave**: ¿Ves cómo el entrenador usa datos del pasado para predecir el futuro?

### ¿Cómo hace esto una computadora?

Una computadora hace exactamente lo mismo, pero mucho más rápido y con muchos más datos.

```python
# Vamos a crear nuestro primer dataset para predicciones
# ¿Qué información necesitamos para predecir quién gana un partido?

import random

# Datos de partidos anteriores (como el historial de un equipo)
partidos_anteriores = []

equipos = ["Barcelona", "Real Madrid", "Manchester City", "Bayern Munich"]

# ¿Cómo generamos datos realistas de partidos?
for i in range(20):
    # Elegimos equipos al azar
    equipo_local = random.choice(equipos)
    equipo_visitante = random.choice([e for e in equipos if e != equipo_local])

    # ¿Quién tiene más probabilidad de ganar?
    # Pista: Los equipos locales tienen ventaja
    if random.random() > 0.3:  # 70% gana el local
        ganador = equipo_local
    else:
        ganador = equipo_visitante

    partidos_anteriores.append(
        {
            "Equipo_Local": equipo_local,
            "Equipo_Visitante": equipo_visitante,
            "Ganador": ganador,
            "Juega_En_Casa": ganador == equipo_local,
        }
    )

# Convertimos a DataFrame (tabla de datos)
datos_partidos = pd.DataFrame(partidos_anteriores)
print("Nuestros datos de partidos anteriores:")
print(datos_partidos.head())

print("\nPregunta: ¿Ves algún patrón en estos datos?")
```

```python
# ¿Cuántas veces gana el equipo local vs el visitante?
# Esta información nos ayudará a hacer predicciones

ventaja_local = datos_partidos["Juega_En_Casa"].sum()
total_partidos = len(datos_partidos)

print(f"De {total_partidos} partidos:")
print(f"- El equipo local ganó: {ventaja_local} veces")
print(f"- El equipo visitante ganó: {total_partidos - ventaja_local} veces")
print(f"- Porcentaje de victorias locales: {(ventaja_local/total_partidos)*100:.1f}%")

print("\n¿Qué descubrimos?")
if ventaja_local > total_partidos / 2:
    print("¡Existe ventaja de jugar en casa!")
else:
    print("No parece haber ventaja de jugar en casa")

print("\nPregunta reflexiva: ¿Por qué crees que los equipos ganan más en casa?")
```

## Síntesis de la Sesión 1: ¿Qué hemos descubierto?

### Lo que aprendimos:
1. **Predecir** = Usar datos del pasado para saber qué puede pasar en el futuro
2. **Diferencia clave**: Una predicción usa datos reales, una opinión solo usa intuición
3. **Patrón descubierto**: Los equipos locales tienen ventaja (dato real que podemos usar)

### Preguntas para reflexionar:
- ¿Cómo usarías este conocimiento si fueras entrenador?
- ¿Qué otros factores crees que influyen en el resultado de un partido?

**Próximo paso**: ¿Cómo le enseñamos a la computadora a usar estos patrones para hacer predicciones automáticas?

---

# SESIÓN 2: ¿Cómo le enseñamos a la computadora a predecir? (50 minutos)

## Pregunta de apertura: ¿Qué tienen en común entrenar a un jugador y entrenar a una computadora?

**Reflexiona**: Cuando entrenas a un jugador de fútbol, le muestras jugadas exitosas una y otra vez hasta que las aprende. ¿Crees que podemos hacer algo similar con una computadora?


## ¿Qué es un "modelo" de predicción?

**Analogía simple**: Un modelo es como un entrenador virtual que:

### 1. Aprende de la experiencia (Entrenamiento)
- Le mostramos muchos partidos del pasado
- Le decimos quién ganó en cada caso
- Busca patrones: "Ah, cuando juegan en casa, ganan más"

### 2. Hace predicciones nuevas
- Le damos información de un partido futuro
- Usa lo que aprendió para predecir quién ganará
- Nos da su respuesta con un nivel de confianza

**Pregunta clave**: ¿Es como tener un asistente técnico súper inteligente que nunca olvida nada?

### Tipos de predicciones simples en fútbol:

**Tipo 1: ¿Quién gana?** (Gana Local / Gana Visitante / Empate)
**Tipo 2: ¿Cuántos goles?** (0, 1, 2, 3, 4+)
**Tipo 3: ¿Será emocionante?** (Partido aburrido / Partido emocionante)

Hoy aprenderemos el Tipo 1: ¿Quién gana?

```python
# Mi primer modelo de predicción
# ¿Cómo preparamos los datos para que la computadora los entienda?

print("PASO 1: Preparar los datos")
print("=" * 30)

# La computadora no entiende "Barcelona" o "Real Madrid"
# Necesita números. ¿Cómo convertimos texto en números?

# Convertimos "jugar en casa" a números
datos_partidos["Es_Local"] = datos_partidos["Juega_En_Casa"].astype(int)

# 1 = Gana el local, 0 = Gana el visitante
datos_partidos["Gana_Local"] = (
    datos_partidos["Ganador"] == datos_partidos["Equipo_Local"]
).astype(int)

print("Datos preparados:")
print(datos_partidos[["Es_Local", "Gana_Local"]].head())

print("\n¿Ves cómo convertimos palabras en números?")
print("Es_Local: 1=juega en casa, 0=juega fuera")
print("Gana_Local: 1=ganó el local, 0=ganó el visitante")

print(
    "\nPregunta: ¿Por qué crees que la computadora prefiere números en lugar de palabras?"
)
```

```python
# PASO 2: Entrenar nuestro modelo
# Como enseñarle a un niño a reconocer patrones

print("PASO 2: Entrenando el modelo")
print("=" * 30)

# Separamos la información (X) del resultado (y)
X = datos_partidos[["Es_Local"]]  # Información que usamos para predecir
y = datos_partidos["Gana_Local"]  # Lo que queremos predecir

print("Información para predecir (X):")
print(X.head())
print("\nResultados reales (y):")
print(y.head())

# Creamos nuestro modelo (como contratar un entrenador)
modelo = LogisticRegression()

# Entrenamos el modelo (como enseñarle los patrones)
modelo.fit(X, y)

print("\n¡Modelo entrenado!")
print("El modelo ahora 'sabe' que jugar en casa es importante")

print("\nAnalogía: Es como si le hubiéramos mostrado 20 partidos a un entrenador")
print("y ahora él puede predecir resultados futuros basándose en esa experiencia")

print("\nPregunta: ¿Qué crees que aprendió el modelo de nuestros datos?")
```

```python
# PASO 3: ¡Hagamos nuestra primera predicción!
# El momento mágico: predecir el futuro

print("PASO 3: Predicciones")
print("=" * 30)

# Situación 1: Barcelona juega en casa contra Real Madrid
print("SITUACIÓN 1: Barcelona (casa) vs Real Madrid (visitante)")
situacion_1 = [[1]]  # 1 = juega en casa
prediccion_1 = modelo.predict(situacion_1)

if prediccion_1[0] == 1:
    print("CASA - Predicción: ¡Gana el equipo local (Barcelona)!")
else:
    print("VISITANTE - Predicción: ¡Gana el equipo visitante (Real Madrid)!")

# Situación 2: Real Madrid juega fuera contra Bayern Munich
print("\nSITUACIÓN 2: Bayern Munich (casa) vs Real Madrid (visitante)")
situacion_2 = [[1]]  # 1 = Bayern juega en casa
prediccion_2 = modelo.predict(situacion_2)

if prediccion_2[0] == 1:
    print("CASA - Predicción: ¡Gana el equipo local (Bayern Munich)!")
else:
    print("VISITANTE - Predicción: ¡Gana el equipo visitante (Real Madrid)!")

print("\n¿Ves el patrón? El modelo siempre predice que gana el equipo local")
print("Esto es porque aprendió que hay ventaja de jugar en casa")

print("\nPregunta reflexiva: ¿Te parece una predicción razonable? ¿Por qué?")
```

## Síntesis de la Sesión 2: ¿Qué hemos logrado?

### Lo que aprendimos:
1. **Modelo** = Un entrenador virtual que aprende patrones de datos pasados
2. **Entrenamiento** = Mostrarle muchos ejemplos para que aprenda
3. **Predicción** = Usar lo aprendido para predecir situaciones nuevas
4. **Patrón descubierto**: Nuestro modelo aprendió la ventaja de jugar en casa

### Conexiones con fútbol real:
- Los entrenadores reales hacen esto mentalmente todo el tiempo
- Los clubes profesionales usan modelos como este (pero más complejos)
- Nosotros acabamos de crear nuestro primer sistema de predicción deportiva

**Próximo paso**: ¿Cómo sabemos si nuestras predicciones son buenas o malas?

---

# SESIÓN 3: ¿Qué tan buenas son nuestras predicciones? (50 minutos)

## Pregunta de apertura: ¿Cómo evalúas si un entrenador toma buenas decisiones?

**Reflexiona**: Un entrenador que acierta 9 de cada 10 predicciones es mejor que uno que acierta 5 de cada 10. ¿Cómo podemos medir qué tan bueno es nuestro modelo?


## ¿Cómo medimos qué tan bueno es nuestro modelo?

**Analogía del examen**: Es como evaluar a un estudiante:

### Método 1: Porcentaje de aciertos (Precisión)
- Si hace 10 predicciones y acierta 8 = 80% de precisión
- Si hace 10 predicciones y acierta 5 = 50% de precisión

### ¿Qué es una buena precisión en fútbol?
- **90-100%**: ¡Imposible! (El fútbol siempre tiene sorpresas)
- **70-80%**: Excelente (Mejor que muchos expertos)
- **60-70%**: Bueno (Mejor que adivinar al azar)
- **50%**: Malo (Es como lanzar una moneda)

**Pregunta clave**: ¿Qué precisión crees que tiene nuestro modelo?

### ¿Cómo probamos nuestro modelo de manera justa?

**Problema**: Si uso los mismos datos para entrenar y para probar, ¡es trampa!

**Analogía**: Es como si un maestro enseñara las respuestas del examen y luego aplicara el mismo examen.

**Solución**: Separar datos en dos grupos:
- **Datos de entrenamiento**: Para que el modelo aprenda
- **Datos de prueba**: Para ver qué tan bien predice datos nuevos

```python
# Evaluemos nuestro modelo de manera justa
# Creando datos de prueba que el modelo nunca ha visto

print("EVALUACIÓN DEL MODELO")
print("=" * 30)

# Creamos nuevos partidos para probar (que el modelo no conoce)
partidos_prueba = []
for i in range(10):
    equipo_local = random.choice(equipos)
    equipo_visitante = random.choice([e for e in equipos if e != equipo_local])

    # Simulamos resultados reales
    if random.random() > 0.3:  # 70% gana el local (patrón real)
        ganador_real = equipo_local
    else:
        ganador_real = equipo_visitante

    partidos_prueba.append(
        {
            "Equipo_Local": equipo_local,
            "Equipo_Visitante": equipo_visitante,
            "Ganador_Real": ganador_real,
            "Es_Local": 1,  # Siempre evaluamos al equipo local
        }
    )

datos_prueba = pd.DataFrame(partidos_prueba)
print("Partidos de prueba creados:")
print(datos_prueba[["Equipo_Local", "Equipo_Visitante", "Ganador_Real"]].head())

# ¿Qué predice nuestro modelo para estos partidos?
X_prueba = datos_prueba[["Es_Local"]]
predicciones = modelo.predict(X_prueba)

# Convertimos las predicciones a nombres de equipos para entenderlas mejor
datos_prueba["Prediccion_Modelo"] = predicciones
datos_prueba["Gana_Local_Real"] = (
    datos_prueba["Ganador_Real"] == datos_prueba["Equipo_Local"]
).astype(int)

print("\nResultados vs Predicciones:")
print(datos_prueba[["Equipo_Local", "Gana_Local_Real", "Prediccion_Modelo"]].head())
```

```python
# Calculemos la precisión de nuestro modelo
# ¿Qué porcentaje de predicciones acertó?

print("CÁLCULO DE PRECISIÓN")
print("=" * 30)

# Comparamos predicciones con resultados reales
aciertos = (datos_prueba["Prediccion_Modelo"] == datos_prueba["Gana_Local_Real"]).sum()
total_predicciones = len(datos_prueba)
precision = (aciertos / total_predicciones) * 100

print(f"Resultados de nuestro modelo:")
print(f"- Total de predicciones: {total_predicciones}")
print(f"- Predicciones correctas: {aciertos}")
print(f"- Predicciones incorrectas: {total_predicciones - aciertos}")
print(f"- PRECISIÓN: {precision:.1f}%")

print(f"\n¿Cómo interpretar este resultado?")
if precision >= 70:
    print("¡EXCELENTE! Nuestro modelo es muy bueno")
elif precision >= 60:
    print("¡BUENO! Nuestro modelo es útil")
elif precision >= 50:
    print("REGULAR - El modelo es mejor que adivinar al azar")
else:
    print("MALO - El modelo necesita mejoras")

print(f"\nComparación con otros métodos:")
print(f"- Adivinar al azar: ~50%")
print(f"- Nuestro modelo: {precision:.1f}%")
print(f"- Expertos deportivos: ~65-75%")

print(f"\nPregunta reflexiva: ¿Te sorprende este resultado? ¿Por qué?")
```

## Síntesis Final: ¿Qué hemos logrado esta semana?

### Nuestro viaje completo:

#### SESIÓN 1: Entendimos qué es predecir
- ✓ Diferencia entre opinión y predicción con datos
- ✓ Descubrimos la ventaja de jugar en casa
- ✓ Aprendimos que los datos del pasado nos ayudan a predecir el futuro

#### SESIÓN 2: Creamos nuestro primer modelo
- ✓ Construimos un "entrenador virtual"
- ✓ Le enseñamos patrones de partidos anteriores
- ✓ Hicimos nuestras primeras predicciones

#### SESIÓN 3: Evaluamos qué tan bueno es
- ✓ Medimos la precisión de nuestro modelo
- ✓ Comparamos con métodos alternativos
- ✓ Entendimos cómo interpretar resultados

### ¿Qué significa esto para el fútbol real?

**Antes de este curso**: "Creo que va a ganar el Barcelona" (opinión)
**Después de este curso**: "Basándome en datos históricos, el Barcelona tiene 70% de probabilidad de ganar" (predicción con datos)

### Conexiones con el mundo profesional:
- Los clubes reales usan modelos similares (pero más complejos)
- Las casas de apuestas basan sus decisiones en estos análisis
- Los entrenadores usan esta información para tomar decisiones estratégicas

### Preguntas para reflexionar:
1. ¿Cómo usarías este conocimiento si fueras director deportivo?
2. ¿Qué otros factores agregarías para mejorar las predicciones?
3. ¿Crees que las máquinas pueden predecir mejor que los humanos?

**Próxima semana**: ¿Podemos combinar diferentes métodos para predecir mejor?

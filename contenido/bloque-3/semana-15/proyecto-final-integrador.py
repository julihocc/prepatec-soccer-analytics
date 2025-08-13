# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Semana 15: ¿Podemos crear nuestro propio sistema de análisis futbolístico?
#
# ## PROYECTO FINAL INTEGRADOR (150 min distribuidos en 3 sesiones)
#
# ### ¡El gran desafío final!
#
# **Misión**: Crear un sistema completo de análisis que ayude al FC Barcelona a tomar mejores decisiones sobre sus jugadores.
#
# **¿Te imaginas trabajando como analista de datos en el Barcelona?** Esta semana vas a experimentar exactamente eso, aplicando todo lo que has aprendido en las últimas 14 semanas.
#
# ### Tu rol: Analista Junior del Barcelona
#
# **Situación**: El cuerpo técnico del Barcelona te ha encargado crear un sistema que les ayude a:
# 1. **Evaluar el rendimiento** de los jugadores actuales
# 2. **Predecir qué jugadores** deberían ser titulares  
# 3. **Comparar diferentes estrategias** de análisis
# 4. **Presentar recomendaciones** claras y útiles
#
# **Pregunta motivadora**: ¿Estás listo para demostrar todo lo que has aprendido sobre ciencia de datos aplicada al fútbol?

# %% [markdown]
# ## SESIÓN 1: ¿Cómo empezaríamos nuestro análisis profesional? (50 min)
# **Pregunta guía**: ¿Qué pasos seguiría un analista profesional para evaluar un equipo completo?
#
# ### El proceso de un analista de datos deportivos
#
# **Imagínate este escenario**: Es lunes por la mañana en la Ciudad Deportiva del Barcelona. Xavi te llama a su oficina y te dice:
#
# *"Necesito tu ayuda para analizar a nuestros jugadores. Tenemos el Clásico el próximo fin de semana contra el Real Madrid, y quiero tomar las mejores decisiones basadas en datos."*
#
# **¿Por dónde empezarías?**
#
# ### Metodología profesional: Los 4 pasos fundamentales
#
# Como analista profesional, seguirías estos pasos:
#
# 1. **🔍 Exploración inicial**: ¿Qué datos tenemos disponibles?
# 2. **📊 Análisis descriptivo**: ¿Qué patrones básicos observamos?
# 3. **🤖 Modelado predictivo**: ¿Podemos predecir rendimientos futuros?
# 4. **💡 Recomendaciones**: ¿Qué decisiones sugieren los datos?
#
# **Pregunta reflexiva**: ¿Recuerdas haber aplicado estos pasos en las semanas anteriores? ¿Cuáles fueron los más desafiantes para ti?
#
# ### Nuestro dataset: La temporada del Barcelona
#
# Vamos a trabajar con datos realistas de la temporada actual del Barcelona, aplicando todo lo que hemos aprendido.

# %%
# Importamos todas las herramientas que hemos aprendido
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import warnings

warnings.filterwarnings("ignore")

# Dataset completo del Barcelona - Temporada 2024-25
datos_barcelona_completos = {
    "Jugador": [
        "Ter Stegen",
        "Lewandowski",
        "Gavi",
        "Pedri",
        "De Jong",
        "Raphinha",
        "Balde",
        "Araujo",
        "Kounde",
        "Cancelo",
        "Ferran Torres",
        "Ansu Fati",
        "Christensen",
        "Sergi Roberto",
        "Marcos Alonso",
        "Oriol Romeu",
        "Joao Felix",
        "Lamine Yamal",
        "Inigo Martinez",
        "Inaki Pena",
    ],
    "Posicion": [
        "Portero",
        "Delantero",
        "Centrocampista",
        "Centrocampista",
        "Centrocampista",
        "Extremo",
        "Lateral",
        "Defensa",
        "Defensa",
        "Lateral",
        "Extremo",
        "Extremo",
        "Defensa",
        "Centrocampista",
        "Lateral",
        "Centrocampista",
        "Delantero",
        "Extremo",
        "Defensa",
        "Portero",
    ],
    "Edad": [
        31,
        35,
        19,
        21,
        26,
        26,
        20,
        24,
        25,
        29,
        24,
        21,
        27,
        31,
        30,
        27,
        24,
        16,
        32,
        25,
    ],
    "Partidos_Jugados": [
        38,
        35,
        32,
        38,
        28,
        34,
        30,
        33,
        36,
        25,
        25,
        18,
        22,
        15,
        12,
        20,
        28,
        30,
        28,
        5,
    ],
    "Minutos_Totales": [
        3420,
        3000,
        2400,
        3200,
        2100,
        2800,
        2200,
        2700,
        3100,
        1800,
        1800,
        1200,
        1650,
        900,
        600,
        1200,
        2000,
        2100,
        2000,
        400,
    ],
    "Goles": [0, 23, 4, 6, 2, 12, 1, 2, 3, 3, 8, 7, 1, 2, 3, 1, 10, 5, 0, 0],
    "Asistencias": [0, 8, 6, 12, 4, 10, 4, 1, 2, 8, 3, 2, 0, 3, 1, 2, 6, 8, 0, 0],
    "Tarjetas_Amarillas": [2, 4, 8, 3, 5, 6, 3, 7, 4, 2, 1, 1, 3, 2, 1, 4, 2, 1, 5, 0],
    "Tarjetas_Rojas": [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Titular_Habitual": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        0,
    ],  # 1=Sí, 0=No
}

# Creamos nuestro DataFrame principal
barcelona_df = pd.DataFrame(datos_barcelona_completos)

print("🏆 Dataset del FC Barcelona - Temporada 2024-25")
print("=" * 50)
print(f"📊 Jugadores analizados: {len(barcelona_df)}")
print(f"📈 Variables disponibles: {len(barcelona_df.columns)}")
print("\n🔍 Primeros 10 jugadores:")
print(barcelona_df.head(10))

# %% [markdown]
# ### Paso 1: Exploración inicial de nuestros datos
#
# **Pregunta de análisis**: ¿Qué información básica necesitamos entender sobre nuestro equipo?
#
# Como analista profesional, siempre empezamos preguntándonos:
# - ¿Cuántos jugadores tenemos por posición?
# - ¿Cuál es la distribución de edades?
# - ¿Quiénes son los jugadores más utilizados?
# - ¿Hay patrones evidentes en el rendimiento?
#
# **Tu misión**: Realiza una exploración básica que te ayude a entender el perfil general del Barcelona.
#
# **Pregunta reflexiva**: ¿Qué aspectos consideras más importantes para entender un equipo de fútbol?

# %%
# PASO 1: Análisis exploratorio básico

print("🔍 ANÁLISIS EXPLORATORIO DEL FC BARCELONA")
print("=" * 60)

# 1. Distribución por posiciones
print("\n📋 Distribución de jugadores por posición:")
distribucion_posiciones = barcelona_df["Posicion"].value_counts()
print(distribucion_posiciones)

# 2. Estadísticas básicas de edad
print(f"\n👥 Perfil de edades del equipo:")
print(f"   Edad promedio: {barcelona_df['Edad'].mean():.1f} años")
print(f"   Jugador más joven: {barcelona_df['Edad'].min()} años")
print(f"   Jugador más veterano: {barcelona_df['Edad'].max()} años")

# 3. Top jugadores por minutos jugados
print(f"\n⏱️ Jugadores con más minutos en la temporada:")
top_minutos = barcelona_df.nlargest(5, "Minutos_Totales")[
    ["Jugador", "Minutos_Totales", "Posicion"]
]
for idx, jugador in top_minutos.iterrows():
    print(
        f"   {jugador['Jugador']}: {jugador['Minutos_Totales']} min ({jugador['Posicion']})"
    )

# 4. Top goleadores
print(f"\n⚽ Top goleadores del equipo:")
top_goles = barcelona_df.nlargest(5, "Goles")[["Jugador", "Goles", "Posicion"]]
for idx, jugador in top_goles.iterrows():
    print(f"   {jugador['Jugador']}: {jugador['Goles']} goles ({jugador['Posicion']})")

# 5. Resumen de titulares habituales
titulares = barcelona_df[barcelona_df["Titular_Habitual"] == 1]
print(f"\n👑 Titulares habituales ({len(titulares)} jugadores):")
print(f"   {', '.join(titulares['Jugador'].tolist())}")

print(f"\n🔄 Jugadores de rotación ({len(barcelona_df) - len(titulares)} jugadores)")

print("\n🤔 Pregunta para reflexionar:")
print("¿Qué patrones iniciales observas en estos datos del Barcelona?")

# %% [markdown]
# ## SESIÓN 2: ¿Cómo creamos estadísticas avanzadas para el análisis? (50 min)
# **Pregunta guía**: ¿Qué estadísticas personalizadas necesitamos para evaluar mejor a nuestros jugadores?
#
# ### Aplicando lo aprendido: Creación de métricas inteligentes
#
# Recordando la **Semana 14**, aprendimos que las estadísticas básicas no siempre cuentan toda la historia. Como analista del Barcelona, necesitas crear métricas más sofisticadas.
#
# **Tu desafío**: Crear estadísticas que respondan preguntas específicas:
# - ¿Quién es más eficiente por minuto jugado?
# - ¿Qué jugadores tienen mejor balance entre goles y asistencias?
# - ¿Quién tiene mejor disciplina (menos tarjetas)?
# - ¿Cómo se comparan jugadores de diferentes posiciones?
#
# **Pregunta estratégica**: Si fueras Xavi, ¿qué métricas te ayudarían más para decidir tu alineación contra el Real Madrid?
#
# ### Paso 2: Ingeniería de características (Feature Engineering)
#
# Vamos a crear nuevas variables que nos den insights más profundos sobre el rendimiento de cada jugador.

# %%
# PASO 2: Creando estadísticas avanzadas del Barcelona

print("📈 CREACIÓN DE MÉTRICAS AVANZADAS")
print("=" * 50)

# 1. Eficiencia ofensiva
barcelona_df["Goles_Por_Partido"] = (
    barcelona_df["Goles"] / barcelona_df["Partidos_Jugados"]
)
barcelona_df["Asistencias_Por_Partido"] = (
    barcelona_df["Asistencias"] / barcelona_df["Partidos_Jugados"]
)
barcelona_df["Contribucion_Ofensiva"] = (
    barcelona_df["Goles"] + barcelona_df["Asistencias"]
)
barcelona_df["Contribucion_Por_Partido"] = (
    barcelona_df["Contribucion_Ofensiva"] / barcelona_df["Partidos_Jugados"]
)

# 2. Eficiencia por tiempo
barcelona_df["Minutos_Por_Partido"] = (
    barcelona_df["Minutos_Totales"] / barcelona_df["Partidos_Jugados"]
)
barcelona_df["Goles_Por_90min"] = (
    barcelona_df["Goles"] / barcelona_df["Minutos_Totales"]
) * 90
barcelona_df["Contribucion_Por_90min"] = (
    barcelona_df["Contribucion_Ofensiva"] / barcelona_df["Minutos_Totales"]
) * 90

# 3. Disciplina
barcelona_df["Tarjetas_Totales"] = barcelona_df["Tarjetas_Amarillas"] + (
    barcelona_df["Tarjetas_Rojas"] * 2
)
barcelona_df["Indice_Disciplina"] = 1 / (
    barcelona_df["Tarjetas_Totales"] + 1
)  # Más alto = más disciplinado

# 4. Regularidad
barcelona_df["Regularidad"] = (
    barcelona_df["Minutos_Por_Partido"] / 90
)  # Fracción del partido que juega


# 5. Categorías de experiencia
def categorizar_experiencia(edad):
    if edad <= 21:
        return "Joven"
    elif edad <= 28:
        return "Experimentado"
    else:
        return "Veterano"


barcelona_df["Categoria_Experiencia"] = barcelona_df["Edad"].apply(
    categorizar_experiencia
)

# 6. Puntuación integral de rendimiento (combinando múltiples métricas)
# Normalizamos las métricas principales para crear un índice compuesto
from sklearn.preprocessing import MinMaxScaler

metricas_principales = ["Contribucion_Por_90min", "Regularidad", "Indice_Disciplina"]
scaler = MinMaxScaler()
barcelona_df["Indice_Rendimiento"] = scaler.fit_transform(
    barcelona_df[metricas_principales]
).mean(axis=1)

print("✅ Nuevas métricas creadas:")
print("   - Contribución ofensiva por partido")
print("   - Eficiencia por 90 minutos")
print("   - Índice de disciplina")
print("   - Regularidad de juego")
print("   - Índice de rendimiento integral")

# Mostramos las métricas más importantes
metricas_importantes = [
    "Jugador",
    "Posicion",
    "Contribucion_Por_Partido",
    "Goles_Por_90min",
    "Regularidad",
    "Indice_Rendimiento",
]
print(f"\n🎯 Top 10 jugadores por índice de rendimiento:")
top_rendimiento = barcelona_df.nlargest(10, "Indice_Rendimiento")[metricas_importantes]
print(top_rendimiento.round(3))

# %% [markdown]
# ### Visualizando nuestras métricas avanzadas
#
# **Como analista profesional**, necesitas crear visualizaciones que comuniquen insights claramente al cuerpo técnico.
#
# **Tu objetivo**: Crear gráficos que respondan:
# - ¿Cuáles son los patrones de rendimiento por posición?
# - ¿Hay correlación entre edad y eficiencia?
# - ¿Los titulares habituales realmente tienen mejores métricas?
# - ¿Qué jugadores destacan en áreas específicas?
#
# **Pregunta estratégica**: ¿Cómo presentarías estos datos a Xavi de manera que pueda tomar decisiones rápidas y informadas?

# %%
# PASO 2B: Visualizaciones profesionales para el cuerpo técnico

plt.figure(figsize=(16, 12))

# Gráfico 1: Rendimiento por posición
plt.subplot(2, 3, 1)
sns.boxplot(data=barcelona_df, x="Posicion", y="Indice_Rendimiento")
plt.title("Índice de Rendimiento por Posición")
plt.xticks(rotation=45)
plt.ylabel("Índice de Rendimiento")

# Gráfico 2: Eficiencia ofensiva vs Regularidad
plt.subplot(2, 3, 2)
colors = {"Joven": "lightgreen", "Experimentado": "orange", "Veterano": "lightcoral"}
for categoria in barcelona_df["Categoria_Experiencia"].unique():
    data_categoria = barcelona_df[barcelona_df["Categoria_Experiencia"] == categoria]
    plt.scatter(
        data_categoria["Regularidad"],
        data_categoria["Contribucion_Por_90min"],
        c=colors[categoria],
        label=categoria,
        s=100,
        alpha=0.7,
    )

plt.xlabel("Regularidad (fracción del partido)")
plt.ylabel("Contribución por 90 min")
plt.title("Regularidad vs Contribución Ofensiva")
plt.legend()

# Gráfico 3: Comparación titulares vs suplentes
plt.subplot(2, 3, 3)
titulares_data = barcelona_df[barcelona_df["Titular_Habitual"] == 1][
    "Indice_Rendimiento"
]
suplentes_data = barcelona_df[barcelona_df["Titular_Habitual"] == 0][
    "Indice_Rendimiento"
]

plt.boxplot([titulares_data, suplentes_data], labels=["Titulares", "Suplentes"])
plt.title("Rendimiento: Titulares vs Suplentes")
plt.ylabel("Índice de Rendimiento")

# Gráfico 4: Top 10 por contribución ofensiva
plt.subplot(2, 3, 4)
top_contribucion = barcelona_df.nlargest(10, "Contribucion_Ofensiva")
plt.barh(top_contribucion["Jugador"], top_contribucion["Contribucion_Ofensiva"])
plt.title("Top 10: Contribución Ofensiva Total")
plt.xlabel("Goles + Asistencias")

# Gráfico 5: Disciplina vs Edad
plt.subplot(2, 3, 5)
plt.scatter(
    barcelona_df["Edad"],
    barcelona_df["Indice_Disciplina"],
    c=barcelona_df["Minutos_Totales"],
    cmap="viridis",
    s=100,
)
plt.xlabel("Edad")
plt.ylabel("Índice de Disciplina")
plt.title("¿Los veteranos son más disciplinados?")
plt.colorbar(label="Minutos jugados")

# Gráfico 6: Distribución de índices de rendimiento
plt.subplot(2, 3, 6)
barcelona_df["Indice_Rendimiento"].hist(
    bins=8, alpha=0.7, color="skyblue", edgecolor="black"
)
plt.xlabel("Índice de Rendimiento")
plt.ylabel("Número de jugadores")
plt.title("Distribución del Rendimiento en el Equipo")

plt.tight_layout()
plt.show()

print("📊 Análisis visual completado")
print("🤔 ¿Qué patrones interesantes observas en estos gráficos?")
print("💡 ¿Qué recomendaciones harías basándote en estas visualizaciones?")

# %% [markdown]
# ## SESIÓN 3: ¿Podemos predecir quién debería jugar el Clásico? (50 min)
# **Pregunta guía**: ¿Cómo usamos machine learning para ayudar a Xavi a decidir su alineación?
#
# ### El gran desafío: Modelado predictivo para el Clásico
#
# **Situación crítica**: Es jueves, dos días antes del Clásico contra el Real Madrid. Xavi te pide que uses todos tus conocimientos de machine learning para recomendar quién debería ser titular.
#
# **Tu misión final**: Crear y evaluar modelos predictivos que determinen quién debería jugar basándose en:
# - Las métricas avanzadas que creaste
# - Los patrones de rendimiento descubiertos
# - La importancia del partido (Clásico = máxima exigencia)
#
# **Pregunta estratégica**: ¿Recuerdas los diferentes tipos de modelos que aprendiste? ¿Cuál crees que funcionaría mejor para esta decisión?
#
# ### Paso 3: Aplicando machine learning profesional
#
# Vamos a usar todo lo aprendido en las semanas 11-14:
# - **Múltiples modelos** (Semana 12)
# - **Evaluación rigurosa** (Semana 13)  
# - **Características optimizadas** (Semana 14)
# - **Metodología profesional** (Semana 11)

# %%
# PASO 3: Modelado predictivo para la alineación del Clásico

print("🤖 CREANDO MODELOS PREDICTIVOS PARA EL CLÁSICO")
print("=" * 60)

# Preparamos los datos para machine learning
# Excluimos porteros del análisis (diferentes criterios)
jugadores_campo = barcelona_df[barcelona_df["Posicion"] != "Portero"].copy()

print(f"👥 Jugadores de campo analizados: {len(jugadores_campo)}")

# Seleccionamos las mejores características para nuestros modelos
caracteristicas_modelo = [
    "Contribucion_Por_90min",
    "Regularidad",
    "Indice_Disciplina",
    "Edad",
    "Minutos_Totales",
]

X = jugadores_campo[caracteristicas_modelo]
y = jugadores_campo["Titular_Habitual"]

print(f"📊 Características utilizadas: {caracteristicas_modelo}")
print(f"🎯 Objetivo: Predecir si debe ser titular (1) o suplente (0)")

# Creamos nuestro "equipo de especialistas" (recordando Semana 12)
modelos = {
    "Especialista_Rendimiento": LogisticRegression(random_state=42),
    "Estratega_Integral": RandomForestClassifier(n_estimators=10, random_state=42),
    "Analista_Experiencia": LogisticRegression(random_state=42),
}

# Entrenamos todos los modelos
print(f"\n🏋️ Entrenando modelos especialistas...")
resultados_modelos = {}

for nombre, modelo in modelos.items():
    # Entrenamos el modelo
    modelo.fit(X, y)

    # Hacemos predicciones
    predicciones = modelo.predict(X)
    precision = accuracy_score(y, predicciones)

    # Guardamos resultados
    resultados_modelos[nombre] = {
        "modelo": modelo,
        "predicciones": predicciones,
        "precision": precision,
    }

    print(f"✅ {nombre}: {precision*100:.1f}% de precisión")


# Implementamos votación combinada (recordando Semana 12)
def votacion_especialistas(pred1, pred2, pred3):
    votos = pred1 + pred2 + pred3
    return (votos >= 2).astype(int)


pred1 = resultados_modelos["Especialista_Rendimiento"]["predicciones"]
pred2 = resultados_modelos["Estratega_Integral"]["predicciones"]
pred3 = resultados_modelos["Analista_Experiencia"]["predicciones"]

prediccion_combinada = votacion_especialistas(pred1, pred2, pred3)
precision_combinada = accuracy_score(y, prediccion_combinada)

print(f"🏆 Decisión Combinada: {precision_combinada*100:.1f}% de precisión")
print(f"\n📋 El modelo combinado es nuestro 'cuerpo técnico digital'")

# %% [markdown]
# ### Análisis final y recomendaciones para Xavi
#
# **El momento de la verdad**: Basándote en todo tu análisis, ¿qué le dirías a Xavi sobre la alineación para el Clásico?
#
# **Tu análisis debe incluir:**
# 1. **Alineación recomendada** por tu modelo combinado
# 2. **Justificación** basada en métricas
# 3. **Jugadores sorpresa** que el modelo recomienda
# 4. **Advertencias** sobre limitaciones del análisis
#
# **Pregunta final**: ¿Te sentirías cómodo presentando estas recomendaciones al cuerpo técnico del Barcelona?

# %%
# RECOMENDACIONES FINALES PARA EL CLÁSICO

print("🏆 REPORTE FINAL: RECOMENDACIONES PARA EL CLÁSICO")
print("=" * 70)

# Creamos el reporte final combinando predicciones con datos originales
reporte_final = jugadores_campo.copy()
reporte_final["Prediccion_Combinada"] = prediccion_combinada
reporte_final["Recomendacion"] = reporte_final["Prediccion_Combinada"].map(
    {1: "TITULAR", 0: "SUPLENTE"}
)

# 1. ALINEACIÓN RECOMENDADA
titulares_recomendados = reporte_final[
    reporte_final["Prediccion_Combinada"] == 1
].sort_values("Indice_Rendimiento", ascending=False)

print(f"⭐ ALINEACIÓN RECOMENDADA PARA EL CLÁSICO:")
print(f"   (Basada en análisis de datos y machine learning)")
print()

for posicion in ["Defensa", "Lateral", "Centrocampista", "Extremo", "Delantero"]:
    jugadores_posicion = titulares_recomendados[
        titulares_recomendados["Posicion"] == posicion
    ]
    if len(jugadores_posicion) > 0:
        print(f"🔹 {posicion}:")
        for _, jugador in jugadores_posicion.iterrows():
            print(
                f"   • {jugador['Jugador']} (Rendimiento: {jugador['Indice_Rendimiento']:.3f})"
            )

# 2. ANÁLISIS DE DECISIONES
print(f"\n📊 ANÁLISIS DE DECISIONES DEL MODELO:")
cambios_sugeridos = reporte_final[
    reporte_final["Titular_Habitual"] != reporte_final["Prediccion_Combinada"]
]

if len(cambios_sugeridos) > 0:
    print(f"\n🔄 Cambios sugeridos respecto a la alineación habitual:")
    for _, jugador in cambios_sugeridos.iterrows():
        status_actual = (
            "titular habitual"
            if jugador["Titular_Habitual"] == 1
            else "suplente habitual"
        )
        recomendacion = (
            "TITULAR" if jugador["Prediccion_Combinada"] == 1 else "SUPLENTE"
        )
        print(
            f"   • {jugador['Jugador']} ({status_actual}) → Recomendado como {recomendacion}"
        )
        print(
            f"     Justificación: Índice rendimiento {jugador['Indice_Rendimiento']:.3f}"
        )

# 3. MÉTRICAS DE CONFIANZA
print(f"\n🎯 CONFIANZA EN LAS RECOMENDACIONES:")
print(f"   • Precisión del modelo combinado: {precision_combinada*100:.1f}%")
print(f"   • Jugadores analizados: {len(jugadores_campo)}")
print(f"   • Características consideradas: {len(caracteristicas_modelo)}")

# 4. TOP PERFORMERS PARA EL CLÁSICO
print(f"\n🌟 JUGADORES CON MAYOR POTENCIAL PARA EL CLÁSICO:")
top_performers = reporte_final.nlargest(5, "Indice_Rendimiento")[
    ["Jugador", "Posicion", "Indice_Rendimiento", "Recomendacion"]
]
for _, jugador in top_performers.iterrows():
    print(
        f"   {jugador['Jugador']} ({jugador['Posicion']}) - Rendimiento: {jugador['Indice_Rendimiento']:.3f} - {jugador['Recomendacion']}"
    )

print(f"\n💡 RECOMENDACIÓN ESTRATÉGICA:")
print(f"   Basar la alineación en estas métricas objetivas puede optimizar")
print(f"   el rendimiento del equipo en el partido más importante del año.")

print(f"\n⚠️  LIMITACIONES IMPORTANTES:")
print(f"   • Los datos reflejan rendimiento pasado, no garantizan futuro")
print(f"   • Factores como lesiones y estado de forma no están incluidos")
print(f"   • La química del equipo y tácticas específicas son igualmente importantes")
print(f"   • Este análisis debe complementar, no reemplazar, el criterio técnico")

# %% [markdown]
# ### 🎓 SÍNTESIS FINAL: ¡Tu jornada como analista de datos deportivos!
#
# **¡Felicidades!** Has completado un proyecto real de análisis deportivo aplicando ciencia de datos profesional.
#
# ### ¿Qué has logrado en este proyecto?
#
# ✅ **Exploración de datos**: Analizaste 20 jugadores del Barcelona con múltiples variables  
# ✅ **Ingeniería de características**: Creaste 8 métricas avanzadas de rendimiento  
# ✅ **Visualización profesional**: Generaste 6 gráficos para comunicar insights  
# ✅ **Machine Learning**: Entrenaste 3 modelos y los combinaste inteligentemente  
# ✅ **Evaluación rigurosa**: Mediste precisión y validaste resultados  
# ✅ **Comunicación efectiva**: Presentaste recomendaciones claras y justificadas
#
# ### ¿Qué has aprendido en todo el curso? (15 semanas)
#
# **BLOQUE 1 (Semanas 1-5): Fundamentos de Programación**
# - Python desde cero hasta análisis básico
# - Estructuras de datos y control de flujo
# - Funciones, módulos y buenas prácticas
# - Pandas y NumPy para manipulación de datos
# - Visualización básica con matplotlib
#
# **BLOQUE 2 (Semanas 6-10): Ciencia de Datos + Fútbol**
# - Exploración y limpieza de datos deportivos
# - Tipos de datos específicos del fútbol
# - Estadística descriptiva aplicada al deporte
# - Visualizaciones avanzadas con seaborn
# - Interpretación y comunicación de resultados
#
# **BLOQUE 3 (Semanas 11-15): Machine Learning Aplicado**
# - Conceptos fundamentales de predicción
# - Combinación de múltiples modelos
# - Evaluación y métricas de calidad
# - Optimización de características
# - Proyecto integral real
#
# ### ¿Estás preparado para el siguiente nivel?
#
# **Como analista junior**, ahora podrías:
# - Trabajar con datasets deportivos reales
# - Crear dashboards para equipos profesionales
# - Colaborar en proyectos de scouting digital
# - Continuar aprendiendo técnicas más avanzadas
#
# **Pregunta final de reflexión**: ¿Qué aspecto de la ciencia de datos deportivos te resulta más emocionante para seguir explorando?

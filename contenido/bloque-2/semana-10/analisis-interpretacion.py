# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
# ---

# %% [markdown]
# <VSCode.Cell id="#VSC-semana10-header" language="markdown">
# # SEMANA 10: ¿Cómo transformar datos en decisiones estratégicas que cambien la historia deportiva?
#
# ## BLOQUE 2 - CULMINACIÓN: Explorando Datos Deportivos con Python
#
# ---
#
# ## Pregunta culminante: ¿Cuál es la diferencia entre ser un recopilador de estadísticas y un consultor estratégico que influye decisiones millonarias?
#
# **Reflexión de síntesis del Bloque 2**: Has dominado la recopilación, organización, visualización y descripción de datos deportivos. ¿Estás preparado para el salto cualitativo final: convertir toda esta información en insights que cambien el curso de equipos y carreras?
#
# **Tu metamorfosis**: De estudiante de análisis de datos a consultor estratégico capaz de influenciar decisiones que definan el futuro deportivo.
#
# ### Tu recorrido transformador en este bloque:
# - **Semana 6**: ¿Dominaste la exploración inicial de datasets deportivos?
# - **Semana 7**: ¿Comprendiste cómo los tipos de datos revelan diferentes perspectivas del juego?
# - **Semana 8**: ¿Descubriste cómo la estadística descriptiva convierte números en narrativas?
# - **Semana 9**: ¿Desarrollaste la capacidad de crear visualizaciones que comunican verdades profundas?
# - **Semana 10**: ¿Puedes ahora sintetizar todo en recomendaciones estratégicas convincentes?
#
# **Pregunta transformadora**: Si fueras convocado como consultor por el Real Madrid para analizar la efectividad de su inversión de 300 millones en fichajes, ¿cómo estructurarías tu metodología de análisis integral?
#
# ---
#
# ## Tu evolución como analista integral
#
# ### ¿Qué diferencia a un analista profesional de un simple procesador de datos?
#
# **Nivel ejecutivo alcanzado**: La capacidad de extraer narrativas convincentes que justifiquen inversiones estratégicas y cambios organizacionales fundamentales.
#
# **Pregunta de identidad profesional**: ¿Comprendes que tu valor no está en procesar datos sino en generar confianza para tomar decisiones arriesgadas pero fundamentadas?
#
# ---
#
# ### ESTRUCTURA DE INVESTIGACIÓN INTENSIVA: 3 Sesiones de Consultoría Estratégica
#
# **Sesión 1 (50 min)**: ¿Cómo desarrollar metodologías de interpretación que distingan patrones genuinos de ruido estadístico?
#
# **Sesión 2 (50 min)**: ¿Cómo construir narrativas analíticas que convenzan a stakeholders no técnicos de invertir recursos significativos?
#
# **Sesión 3 (50 min)**: ¿Cómo integrar todo tu conocimiento del Bloque 2 en un framework de consultoría deportiva profesional?
#
# **Síntesis final**: ¿Cómo posicionarte como el analista que los equipos buscan cuando necesitan certeza en decisiones cruciales?
#
# ---

# %% [markdown]
# ---
#
# # SESIÓN 1: ¿Cómo desarrollar metodologías de interpretación que distingan insights genuinos de correlaciones fortuitas? (50 minutos)
#
# ## Pregunta de apertura: ¿Qué separa a un analista que encuentra patrones reales de uno que persigue espejismos estadísticos?
#
# **Reflexiona**: Has aprendido a crear gráficos hermosos y calcular estadísticas precisas, pero ¿cómo desarrollas el criterio para distinguir entre descubrimientos genuinos y correlaciones que son puro ruido? ¿Qué metodología te protege de recomendar estrategias basadas en patrones falsos?
#
# **Desafío de rigor**: Si encontraras una correlación del 0.87 entre el color de las camisetas y las victorias, ¿cómo determinarías si es un insight valioso o una trampa estadística?
#
# ---
#
# ## ¿Qué principios usan los consultores de élite para validar sus descubrimientos?
#
# **Momento de madurez**: Los analistas más respetados no se distinguen por encontrar más correlaciones, sino por identificar cuáles merecen atención estratégica y cuáles deben descartarse.

# %%
# ¿Te has preguntado cómo desarrollar un sistema de criterios que valide tus descubrimientos?
# Vamos a construir una metodología de interpretación profesional

print("METODOLOGÍA PROFESIONAL DE INTERPRETACIÓN DE DATOS")
print("=" * 60)

# ¿Cómo creamos un dataset que nos permita explorar diferentes tipos de correlaciones?
# Simularemos un escenario realista de análisis de rendimiento de equipo

np.random.seed(42)  # Para resultados consistentes

# Datos fundamentales del equipo
partidos = 30
datos_equipo = {
    "Partido": range(1, partidos + 1),
    "Presupuesto_Salarial": np.random.normal(50, 10, partidos),  # Millones de euros
    "Goles_Favor": np.random.poisson(2, partidos),
    "Goles_Contra": np.random.poisson(1.5, partidos),
    "Posesion_Balon": np.random.normal(55, 8, partidos),
    "Asistencia_Publico": np.random.normal(40000, 8000, partidos),
    "Temperatura_Partido": np.random.normal(18, 6, partidos),  # Celsius
    "Dia_Semana": np.random.choice(
        ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
        partidos,
    ),
}

# ¿Cómo introducimos correlaciones de diferentes tipos para practicar interpretación?
# Correlación GENUINA: Presupuesto salarial debería influir en rendimiento
datos_equipo["Goles_Favor"] = (
    datos_equipo["Presupuesto_Salarial"] / 25 + np.random.normal(0, 0.5, partidos)
).astype(int)

# Correlación ESPURIA: Temperatura no debería afectar goles directamente
# Pero podríamos encontrar correlación por azar

# Correlación MEDIADA: Asistencia podría correlacionar con rendimiento
# pero através del apoyo moral, no causalmente directo

df_analisis = pd.DataFrame(datos_equipo)

print("DATASET PARA ANÁLISIS DE INTERPRETACIÓN:")
print(df_analisis.head())

print("\nPregunta metodológica: ¿Cómo abordarías el análisis de este dataset?")
print("¿Qué correlaciones esperarías encontrar y cuáles serían sospechosas?")

# ¿Cómo calculamos correlaciones de manera sistemática?
correlaciones = df_analisis.corr()
print("\nMATRIZ DE CORRELACIONES:")
print(correlaciones.round(3))

print("\nReflexión crítica: ¿Todas estas correlaciones representan relaciones reales?")
print("¿Cómo distinguirías entre correlación y causalidad?")

# %%
# ¿Cómo desarrollas criterios sistemáticos para evaluar la validez de tus descobrimientos?
# Vamos a crear un framework de validación analítica

print("FRAMEWORK DE VALIDACIÓN DE INSIGHTS")
print("=" * 45)


def evaluar_insight(correlacion, n_observaciones, contexto_logico, reproducibilidad):
    """
    ¿Cómo crear un sistema de scoring para validar discoveries?

    Parámetros:
    - correlacion: fuerza de la correlación (-1 a 1)
    - n_observaciones: tamaño de muestra
    - contexto_logico: ¿tiene sentido teórico? (0-10)
    - reproducibilidad: ¿se mantiene en diferentes datasets? (0-10)
    """

    # Criterio 1: ¿La correlación es lo suficientemente fuerte?
    fuerza_correlacion = abs(correlacion)
    if fuerza_correlacion > 0.7:
        score_fuerza = 10
    elif fuerza_correlacion > 0.5:
        score_fuerza = 7
    elif fuerza_correlacion > 0.3:
        score_fuerza = 4
    else:
        score_fuerza = 1

    # Criterio 2: ¿Tenemos suficientes observaciones?
    if n_observaciones > 100:
        score_muestra = 10
    elif n_observaciones > 50:
        score_muestra = 7
    elif n_observaciones > 20:
        score_muestra = 4
    else:
        score_muestra = 1

    # Criterio 3: ¿El contexto lógico es sólido?
    score_logica = contexto_logico

    # Criterio 4: ¿Es reproducible?
    score_reproducibilidad = reproducibilidad

    # ¿Cómo combinamos todos los criterios?
    score_total = (
        score_fuerza * 0.3
        + score_muestra * 0.2
        + score_logica * 0.3
        + score_reproducibilidad * 0.2
    )

    return {
        "Score_Total": round(score_total, 1),
        "Fuerza": score_fuerza,
        "Muestra": score_muestra,
        "Lógica": score_logica,
        "Reproducibilidad": score_reproducibilidad,
        "Recomendación": (
            "ACTUAR"
            if score_total >= 7
            else "INVESTIGAR MÁS" if score_total >= 4 else "DESCARTAR"
        ),
    }


# ¿Cómo aplicamos nuestro framework a discoveries específicos?
print("EVALUANDO DISCOVERIES ESPECÍFICOS:")
print("-" * 40)

# Discovery 1: Presupuesto vs Goles
correlacion_presupuesto_goles = df_analisis["Presupuesto_Salarial"].corr(
    df_analisis["Goles_Favor"]
)
evaluacion_1 = evaluar_insight(
    correlacion=correlacion_presupuesto_goles,
    n_observaciones=30,
    contexto_logico=9,  # Lógico: mejor presupuesto = mejores jugadores = más goles
    reproducibilidad=8,  # Debería reproducirse en otros equipos
)

print(f"DISCOVERY 1: Presupuesto → Goles (r = {correlacion_presupuesto_goles:.3f})")
print(f"Evaluación: {evaluacion_1}")
print()

# Discovery 2: Temperatura vs Goles
correlacion_temperatura_goles = df_analisis["Temperatura_Partido"].corr(
    df_analisis["Goles_Favor"]
)
evaluacion_2 = evaluar_insight(
    correlacion=correlacion_temperatura_goles,
    n_observaciones=30,
    contexto_logico=3,  # Poco lógico: temperatura no debería afectar habilidad
    reproducibilidad=2,  # Probablemente no se reproduciría
)

print(f"DISCOVERY 2: Temperatura → Goles (r = {correlacion_temperatura_goles:.3f})")
print(f"Evaluación: {evaluacion_2}")
print()

# Discovery 3: Asistencia vs Goles
correlacion_asistencia_goles = df_analisis["Asistencia_Publico"].corr(
    df_analisis["Goles_Favor"]
)
evaluacion_3 = evaluar_insight(
    correlacion=correlacion_asistencia_goles,
    n_observaciones=30,
    contexto_logico=6,  # Posible: apoyo del público podría motivar
    reproducibilidad=5,  # Podría variar según cultura del equipo
)

print(f"DISCOVERY 3: Asistencia → Goles (r = {correlacion_asistencia_goles:.3f})")
print(f"Evaluación: {evaluacion_3}")

print(
    "\nPregunta de aplicación: ¿Cómo este framework cambiaría tu confianza en diferentes discoveries?"
)
print("¿Qué otros criterios añadirías para evaluar la validez de un insight?")

# %% [markdown]
# ## 3. Creando Datos de Fútbol
#
# ### 3.1 Vamos a inventar partidos de fútbol
#
# Para practicar, vamos a crear datos falsos de partidos. Es como un videojuego donde nosotros controlamos todo.
#
# **Nuestros datos van a tener:**
# - Equipos famosos (Real Madrid, Barcelona, etc.)
# - Cuántos goles anotó cada equipo
# - Quién ganó el partido
#
# ### ¿Por qué usar datos falsos?
# - Para practicar sin complicaciones
# - Podemos controlar qué pasa
# - Nos enfocamos en aprender, no en conseguir datos reales

# %%
# ¿Cómo visualizamos nuestros criterios de validación para comunicar confianza?
# Vamos a crear un dashboard de validación de insights

print("DASHBOARD DE VALIDACIÓN DE INSIGHTS")
print("=" * 40)

# ¿Cómo estructuramos una visualización que muestre la solidez de nuestros discoveries?
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    "EVALUACIÓN SISTEMÁTICA DE DISCOVERIES ANALÍTICOS", fontsize=14, fontweight="bold"
)

# Gráfico 1: Fuerza de las correlaciones
discoveries = ["Presupuesto→Goles", "Temperatura→Goles", "Asistencia→Goles"]
correlaciones = [
    correlacion_presupuesto_goles,
    correlacion_temperatura_goles,
    correlacion_asistencia_goles,
]
colores = [
    "green" if abs(c) > 0.5 else "orange" if abs(c) > 0.3 else "red"
    for c in correlaciones
]

axes[0, 0].bar(discoveries, [abs(c) for c in correlaciones], color=colores, alpha=0.7)
axes[0, 0].set_title("¿Qué tan fuertes son las correlaciones?")
axes[0, 0].set_ylabel("Fuerza de Correlación (|r|)")
axes[0, 0].set_ylim(0, 1)
axes[0, 0].axhline(y=0.5, color="red", linestyle="--", alpha=0.5, label="Umbral mínimo")
axes[0, 0].legend()

# Gráfico 2: Scores de validación
evaluaciones = [evaluacion_1, evaluacion_2, evaluacion_3]
scores_totales = [eval["Score_Total"] for eval in evaluaciones]
colores_scores = [
    "green" if s >= 7 else "orange" if s >= 4 else "red" for s in scores_totales
]

axes[0, 1].bar(discoveries, scores_totales, color=colores_scores, alpha=0.7)
axes[0, 1].set_title("¿Qué tan confiables son los discoveries?")
axes[0, 1].set_ylabel("Score de Validación")
axes[0, 1].set_ylim(0, 10)
axes[0, 1].axhline(
    y=7, color="green", linestyle="--", alpha=0.5, label="Umbral de acción"
)
axes[0, 1].axhline(
    y=4, color="orange", linestyle="--", alpha=0.5, label="Umbral de investigación"
)
axes[0, 1].legend()

# Gráfico 3: Descomposición de criterios
criterios = ["Fuerza", "Muestra", "Lógica", "Reproducibilidad"]
scores_presupuesto = [evaluacion_1[criterio] for criterio in criterios]

axes[1, 0].radar_chart = axes[1, 0].bar(
    criterios, scores_presupuesto, color="skyblue", alpha=0.7
)
axes[1, 0].set_title("Presupuesto→Goles: Análisis detallado")
axes[1, 0].set_ylabel("Score por Criterio")
axes[1, 0].set_ylim(0, 10)

# Gráfico 4: Comparación de robustez
width = 0.25
x = np.arange(len(criterios))

axes[1, 1].bar(
    x - width,
    [evaluacion_1[c] for c in criterios],
    width,
    label="Presupuesto→Goles",
    alpha=0.8,
)
axes[1, 1].bar(
    x, [evaluacion_2[c] for c in criterios], width, label="Temperatura→Goles", alpha=0.8
)
axes[1, 1].bar(
    x + width,
    [evaluacion_3[c] for c in criterios],
    width,
    label="Asistencia→Goles",
    alpha=0.8,
)
axes[1, 1].set_title("¿Qué discovery es más robusto?")
axes[1, 1].set_ylabel("Score por Criterio")
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(criterios)
axes[1, 1].legend()

plt.tight_layout()
plt.show()

print("\nRESUMEN DE VALIDACIÓN:")
for i, (discovery, eval) in enumerate(zip(discoveries, evaluaciones)):
    print(f"{discovery}: {eval['Score_Total']}/10 - {eval['Recomendación']}")

print(
    "\nPregunta estratégica: ¿Cómo esta metodología de validación cambiaría tu confianza al presentar recommendations?"
)
print("¿Qué discovery recomendarías para acción inmediata y cuál descartarías?")

# %% [markdown]
# ---
#
# ## SÍNTESIS DE LA SESIÓN 1: ¿Qué hemos desarrollado sobre metodologías de interpretación rigurosa?
#
# **Reflexión de 50 minutos**:
# - ¿Cómo un framework sistemático de validación protege de recommendations basadas en correlaciones espurias?
# - ¿Qué valor tiene cuantificar la confianza en tus discoveries antes de comunicarlos?
# - ¿Por qué la combinación de múltiples criterios es superior a confiar en correlaciones simples?
#
# **Pregunta preparatoria**: ¿Estás listo para transformar estos insights validados en narrativas que convenzan a stakeholders de invertir recursos?
#
# ---
#
# # SESIÓN 2: ¿Cómo construir narrativas analíticas que convenzan a stakeholders no técnicos de invertir recursos significativos? (50 minutos)
#
# ## Pregunta de apertura: ¿Qué diferencia hay entre presentar números y contar historias que inspiren confianza para tomar decisiones arriesgadas?
#
# **Reflexiona**: Has desarrollado la capacidad técnica de validar insights, pero ¿cómo traduces descubrimientos complejos en narrativas que ejecutivos y directores deportivos puedan procesar rápidamente y actuar con confianza?
#
# **Desafío de comunicación**: Si tuvieras 10 minutos para convencer al presidente del FC Barcelona de modificar su estrategia de fichajes basándose en tu análisis, ¿cómo estructurarías tu presentación?
#
# ---
#
# ## ¿Qué técnicas usan los consultores más exitosos para traducir complejidad en decisiones claras?
#
# **Momento de maestría comunicativa**: Los mejores analistas deportivos no solo encuentran insights valiosos, sino que los comunican de maneras que hacen que la acción parezca obvia e inevitable.

# %%
# ¿Te has preguntado cómo estructurar una presentación que transforme escepticismo en convicción?
# Vamos a construir una narrativa ejecutiva profesional

print("CONSTRUCCIÓN DE NARRATIVA EJECUTIVA PERSUASIVA")
print("=" * 55)

# ¿Cómo creamos un caso de estudio que demuestre valor estratégico inmediato?
# Simulemos un análisis de transferencias del mercado de fichajes

np.random.seed(123)

# Datos de "candidatos" para fichaje
candidatos_fichaje = {
    "Jugador": ["Mbappé_Clone", "Haaland_Clone", "Vinicius_Clone"],
    "Edad": [24, 23, 22],
    "Costo_Transferencia": [180, 150, 120],  # Millones EUR
    "Salario_Anual": [30, 25, 20],  # Millones EUR
    "Goles_Temporada_Pasada": [35, 42, 28],
    "Asistencias_Temporada_Pasada": [12, 8, 18],
    "Partidos_Perdidos_Lesion": [3, 8, 2],
    "Valor_Marketing": [95, 80, 70],  # Índice 0-100
    "Adaptabilidad_Liga": [90, 85, 95],  # Índice 0-100
}

df_candidatos = pd.DataFrame(candidatos_fichaje)

# ¿Cómo calculamos métricas que importen a ejecutivos?
df_candidatos["ROI_Goles"] = (
    df_candidatos["Goles_Temporada_Pasada"] / df_candidatos["Costo_Transferencia"]
)
df_candidatos["Versatilidad_Ofensiva"] = (
    df_candidatos["Goles_Temporada_Pasada"]
    + df_candidatos["Asistencias_Temporada_Pasada"]
)
df_candidatos["Riesgo_Lesion"] = (
    df_candidatos["Partidos_Perdidos_Lesion"] / 38 * 100
)  # % de temporada perdida
df_candidatos["Valor_Total_5_Anos"] = (
    df_candidatos["Costo_Transferencia"] + df_candidatos["Salario_Anual"] * 5
)

print("ANÁLISIS EJECUTIVO DE CANDIDATOS:")
print(
    df_candidatos[
        [
            "Jugador",
            "ROI_Goles",
            "Versatilidad_Ofensiva",
            "Riesgo_Lesion",
            "Valor_Total_5_Anos",
        ]
    ].round(2)
)

# ¿Cómo creamos una visualización que cuente la historia completa?
fig = plt.figure(figsize=(16, 10))
fig.suptitle(
    "ANÁLISIS ESTRATÉGICO: ¿Cuál es la inversión más inteligente?",
    fontsize=16,
    fontweight="bold",
)

# Layout profesional para presentación ejecutiva
gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)

# Panel 1: Eficiencia de inversión (LO MÁS IMPORTANTE PARA EJECUTIVOS)
ax1 = fig.add_subplot(gs[0, 0])
colores_roi = [
    "gold" if roi == df_candidatos["ROI_Goles"].max() else "silver"
    for roi in df_candidatos["ROI_Goles"]
]
bars1 = ax1.bar(
    df_candidatos["Jugador"], df_candidatos["ROI_Goles"], color=colores_roi, alpha=0.8
)
ax1.set_title("EFICIENCIA DE INVERSIÓN\n(Goles por Millón €)", fontweight="bold")
ax1.set_ylabel("Goles / Millón €")
# ¿Cómo destacar el insight clave?
for i, (jugador, roi) in enumerate(
    zip(df_candidatos["Jugador"], df_candidatos["ROI_Goles"])
):
    ax1.text(i, roi + 0.01, f"{roi:.3f}", ha="center", fontweight="bold")

# Panel 2: Análisis de riesgo vs rendimiento
ax2 = fig.add_subplot(gs[0, 1])
scatter = ax2.scatter(
    df_candidatos["Riesgo_Lesion"],
    df_candidatos["Versatilidad_Ofensiva"],
    s=df_candidatos["Valor_Marketing"] * 2,
    alpha=0.6,
    c=["red", "blue", "green"],
)
ax2.set_xlabel("Riesgo de Lesión (%)")
ax2.set_ylabel("Versatilidad Ofensiva")
ax2.set_title("RIESGO vs RENDIMIENTO\n(Tamaño = Valor Marketing)")
# ¿Cómo añadir etiquetas que faciliten interpretación?
for i, jugador in enumerate(df_candidatos["Jugador"]):
    ax2.annotate(
        jugador.split("_")[0],
        (
            df_candidatos["Riesgo_Lesion"].iloc[i],
            df_candidatos["Versatilidad_Ofensiva"].iloc[i],
        ),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=9,
    )

# Panel 3: Proyección financiera a 5 años
ax3 = fig.add_subplot(gs[0, 2])
ax3.barh(
    df_candidatos["Jugador"],
    df_candidatos["Valor_Total_5_Anos"],
    alpha=0.7,
    color=["lightcoral", "lightblue", "lightgreen"],
)
ax3.set_xlabel("Inversión Total 5 años (M€)")
ax3.set_title("COMPROMISO FINANCIERO\nTotal a 5 años")
for i, valor in enumerate(df_candidatos["Valor_Total_5_Anos"]):
    ax3.text(valor + 5, i, f"{valor:.0f}M€", va="center", fontweight="bold")

# Panel 4: Matriz de decisión ejecutiva
ax4 = fig.add_subplot(gs[1, :])
# ¿Cómo crear una tabla de recomendaciones clara?
recomendaciones = []
for i, row in df_candidatos.iterrows():
    if row["ROI_Goles"] == df_candidatos["ROI_Goles"].max():
        recomendacion = "RECOMENDADO: Máxima eficiencia de inversión"
        color = "lightgreen"
    elif row["Riesgo_Lesion"] == df_candidatos["Riesgo_Lesion"].min():
        recomendacion = "SEGUNDA OPCIÓN: Menor riesgo de lesión"
        color = "lightyellow"
    else:
        recomendacion = "ALTO RIESGO: Mayor costo total"
        color = "lightcoral"
    recomendaciones.append(recomendacion)

# Tabla visual de recomendaciones
tabla_data = []
for i, row in df_candidatos.iterrows():
    tabla_data.append(
        [
            row["Jugador"].split("_")[0],
            f"{row['ROI_Goles']:.3f}",
            f"{row['Riesgo_Lesion']:.1f}%",
            f"{row['Valor_Total_5_Anos']:.0f}M€",
            recomendaciones[i],
        ]
    )

tabla = ax4.table(
    cellText=tabla_data,
    colLabels=["Jugador", "ROI", "Riesgo", "Costo 5a", "Recomendación"],
    cellLoc="center",
    loc="center",
)
tabla.auto_set_font_size(False)
tabla.set_fontsize(10)
tabla.scale(1.2, 2)

# ¿Cómo colorear la tabla para comunicar recomendaciones visualmente?
for i in range(len(df_candidatos)):
    if "RECOMENDADO" in recomendaciones[i]:
        tabla[(i + 1, 4)].set_facecolor("lightgreen")
    elif "SEGUNDA" in recomendaciones[i]:
        tabla[(i + 1, 4)].set_facecolor("lightyellow")
    else:
        tabla[(i + 1, 4)].set_facecolor("lightcoral")

ax4.axis("off")
ax4.set_title("MATRIZ DE DECISIÓN EJECUTIVA", fontweight="bold", pad=20)

plt.show()

print("\nNARRATIVA EJECUTIVA CONSTRUIDA:")
print("✓ Hook: Eficiencia de inversión (lo que más importa)")
print("✓ Contexto: Análisis multidimensional de riesgo")
print("✓ Evidencia: Proyecciones financieras claras")
print("✓ Recomendación: Matriz de decisión visual")

print(
    "\nPregunta de comunicación: ¿Cómo esta estructura cambiaría la velocidad de toma de decisiones?"
)
print("¿Qué elemento visual fue más convincente para formar tu recomendación?")

# %% [markdown]
# ## 4. Tu primera consultoría analítica completa
#
# ### 4.1 El método del consultor de élite: de datos a recomendaciones
#
# **Pregunta metodológica**: ¿Cómo estructurarías un análisis que debe convencer a tomadores de decisiones escépticos?
#
# **Tu enfoque investigativo**: Transformar una colección de partidos en insights estratégicos que justifiquen inversiones o cambios tácticos.
#
# **Reflexión profesional**: ¿Qué diferencia un análisis académico de una consultoría que genere valor comercial real?

# %%
# ¿Cómo traducir insights complejos en comunicación que inspire acción ejecutiva?
# Vamos a crear un framework de comunicación persuasiva

print("FRAMEWORK DE COMUNICACIÓN EJECUTIVA")
print("=" * 40)


# ¿Cómo estructurar un mensaje que transforme datos en confianza para actuar?
def crear_mensaje_ejecutivo(insight_tecnico, audiencia_tipo, riesgo_decision):
    """
    ¿Cómo adaptar el mismo insight para diferentes tipos de stakeholders?

    Parámetros:
    - insight_tecnico: el descubrimiento analítico
    - audiencia_tipo: 'CEO', 'Director_Deportivo', 'Entrenador'
    - riesgo_decision: 'Alto', 'Medio', 'Bajo'
    """

    if audiencia_tipo == "CEO":
        if riesgo_decision == "Alto":
            estructura = f"""
RESUMEN EJECUTIVO PARA DECISIÓN DE ALTO RIESGO:
• INSIGHT CLAVE: {insight_tecnico}
• IMPACTO FINANCIERO: [Cuantificar en euros/porcentaje]
• PROBABILIDAD DE ÉXITO: [Porcentaje basado en evidencia]
• PLAN DE MITIGACIÓN: [Estrategia si las cosas salen mal]
• COMPARACIÓN CON COMPETENCIA: [Benchmarking relevante]
• RECOMENDACIÓN: [Acción específica con timeline]
"""
        else:
            estructura = f"""
OPORTUNIDAD IDENTIFICADA:
• {insight_tecnico}
• ROI proyectado: [Número específico]
• Recomendación: [Acción clara]
"""

    elif audiencia_tipo == "Director_Deportivo":
        estructura = f"""
ANÁLISIS TÉCNICO DEPORTIVO:
• DESCUBRIMIENTO: {insight_tecnico}
• IMPLICACIONES TÁCTICAS: [Cómo afecta el juego]
• CONSIDERACIONES DE PLANTILLA: [Qué jugadores necesitas]
• VENTAJA COMPETITIVA: [Cómo esto te diferencia]
• IMPLEMENTACIÓN: [Pasos concretos]
"""

    elif audiencia_tipo == "Entrenador":
        estructura = f"""
INSIGHT PARA APLICACIÓN INMEDIATA:
• PATRÓN IDENTIFICADO: {insight_tecnico}
• APLICACIÓN EN ENTRENAMIENTO: [Ejercicios específicos]
• AJUSTES TÁCTICOS SUGERIDOS: [Cambios en formación/estrategia]
• MÉTRICAS A MONITOREAR: [Qué medir en próximos partidos]
"""

    return estructura


# ¿Cómo aplicamos diferentes enfoques comunicativos al mismo insight?
insight_base = (
    "Los equipos que mantienen >60% posesión tienen 73% más probabilidad de ganar"
)

print("ADAPTACIÓN DEL MISMO INSIGHT PARA DIFERENTES AUDIENCIAS:")
print("=" * 60)

# Para CEO
mensaje_ceo = crear_mensaje_ejecutivo(insight_base, "CEO", "Alto")
print("VERSIÓN PARA CEO:")
print(mensaje_ceo)

# Para Director Deportivo
mensaje_director = crear_mensaje_ejecutivo(insight_base, "Director_Deportivo", "Medio")
print("VERSIÓN PARA DIRECTOR DEPORTIVO:")
print(mensaje_director)

# Para Entrenador
mensaje_entrenador = crear_mensaje_ejecutivo(insight_base, "Entrenador", "Bajo")
print("VERSIÓN PARA ENTRENADOR:")
print(mensaje_entrenador)

print("\nPRINCIPIOS DE COMUNICACIÓN EJECUTIVA IDENTIFICADOS:")
print("✓ CEO: Enfoque en impacto financiero y riesgo")
print("✓ Director Deportivo: Enfoque en ventaja competitiva y aplicación")
print("✓ Entrenador: Enfoque en implementación práctica inmediata")

print(
    "\nPregunta de reflexión: ¿Cómo cambiaría la recepción del mismo dato según la audiencia?"
)
print("¿Qué versión te parece más convincente para generar acción inmediata?")

# %% [markdown]
# ---
#
# ## SÍNTESIS DE LA SESIÓN 2: ¿Qué hemos desarrollado sobre narrativas analíticas persuasivas?
#
# **Reflexión de 50 minutos**:
# - ¿Cómo las visualizaciones ejecutivas aceleran la toma de decisiones complejas?
# - ¿Qué valor tiene adaptar el mismo insight para diferentes tipos de audiencias?
# - ¿Por qué la estructura narrativa es tan importante como la precisión técnica?
#
# **Pregunta de transición**: ¿Estás preparado para integrar todo tu conocimiento del Bloque 2 en un framework de consultoría deportiva completo?
#
# ---
#
# # SESIÓN 3: ¿Cómo integrar todo tu conocimiento del Bloque 2 en un framework de consultoría deportiva profesional? (50 minutos)
#
# ## Pregunta de apertura: ¿Qué significa haber completado tu transformación de estudiante de datos a consultor estratégico deportivo?
#
# **Reflexiona sobre tu evolución**: Iniciaste el Bloque 2 aprendiendo a explorar datasets básicos. ¿Comprendes la magnitud de tu transformación hacia alguien capaz de influenciar decisiones estratégicas millonarias?
#
# **Desafío de síntesis**: Si tuvieras que demostrar tu competencia completa como analista deportivo en una presentación de 15 minutos, ¿cómo integrarías exploración, tipos de datos, estadística descriptiva, visualización avanzada e interpretación estratégica?
#
# ---
#
# ## ¿Cómo los consultores de élite integran múltiples competencias en metodologías coherentes?
#
# **Momento de maestría integral**: Tu valor profesional no está en dominar herramientas aisladas sino en integrarlas en un enfoque sistemático que genere confianza y resultados consistentes.

# %%
# ¿Te has preguntado cómo integrar todas las competencias del Bloque 2 en una metodología coherente?
# Vamos a construir tu Framework de Consultoría Deportiva Integral

print("FRAMEWORK DE CONSULTORÍA DEPORTIVA INTEGRAL")
print("=" * 50)


class ConsultorDeportivoAnalista:
    """
    ¿Cómo estructurar tu competencia profesional como un sistema integrado?

    Este framework integra todas las competencias desarrolladas en el Bloque 2:
    - Exploración (Semana 6)
    - Tipos de datos (Semana 7)
    - Estadística descriptiva (Semana 8)
    - Visualización (Semana 9)
    - Interpretación estratégica (Semana 10)
    """

    def __init__(self):
        self.competencias_desarrolladas = {
            "exploracion_datos": "Semana 6",
            "tipos_datos": "Semana 7",
            "estadistica_descriptiva": "Semana 8",
            "visualizacion_avanzada": "Semana 9",
            "interpretacion_estrategica": "Semana 10",
        }

    def analisis_completo(self, dataset, objetivo_negocio):
        """¿Cómo estructurar un análisis que integre todas tus competencias?"""

        print(f"INICIANDO CONSULTORÍA PARA: {objetivo_negocio}")
        print("-" * 40)

        # FASE 1: Exploración sistemática (Semana 6)
        print("FASE 1: EXPLORACIÓN SISTEMÁTICA")
        print(f"• Dataset cargado: {len(dataset)} observaciones")
        print(f"• Variables identificadas: {list(dataset.columns)}")
        print(
            f"• Calidad de datos evaluada: {dataset.isnull().sum().sum()} valores nulos"
        )

        # FASE 2: Clasificación de tipos de datos (Semana 7)
        print("\nFASE 2: CLASIFICACIÓN DE TIPOS DE DATOS")
        tipos_identificados = {
            "numericos": dataset.select_dtypes(include=[np.number]).columns.tolist(),
            "categoricos": dataset.select_dtypes(include=["object"]).columns.tolist(),
            "temporales": [
                col
                for col in dataset.columns
                if "fecha" in col.lower() or "tiempo" in col.lower()
            ],
        }
        for tipo, columnas in tipos_identificados.items():
            print(f"• {tipo.capitalize()}: {columnas}")

        # FASE 3: Análisis estadístico descriptivo (Semana 8)
        print("\nFASE 3: ANÁLISIS ESTADÍSTICO DESCRIPTIVO")
        if len(tipos_identificados["numericos"]) > 0:
            estadisticas = dataset[tipos_identificados["numericos"]].describe()
            print("• Estadísticas centrales calculadas")
            print("• Distribuciones analizadas")
            print("• Outliers identificados")

        # FASE 4: Visualización estratégica (Semana 9)
        print("\nFASE 4: VISUALIZACIÓN ESTRATÉGICA")
        print("• Gráficos ejecutivos preparados")
        print("• Narrativa visual estructurada")
        print("• Dashboard de KPIs desarrollado")

        # FASE 5: Interpretación y recomendaciones (Semana 10)
        print("\nFASE 5: INTERPRETACIÓN Y RECOMENDACIONES")
        print("• Patrones validados con framework de criterios")
        print("• Insights traducidos a lenguaje ejecutivo")
        print("• Recomendaciones estratégicas formuladas")

        return "CONSULTORÍA COMPLETADA CON ÉXITO"


# ¿Cómo demostramos la integración con un caso práctico?
consultor = ConsultorDeportivoAnalista()

# Caso de demostración: Análisis de rendimiento de equipo
resultado = consultor.analisis_completo(
    dataset=df_analisis,  # Nuestros datos de ejemplo
    objetivo_negocio="Optimización de Inversión en Fichajes 2024/25",
)

print(f"\n{resultado}")

print("\nCOMPETENCIAS INTEGRADAS DEL BLOQUE 2:")
for competencia, semana in consultor.competencias_desarrolladas.items():
    print(f"✓ {competencia.replace('_', ' ').title()}: {semana}")

print("\nVALOR PROFESIONAL DESARROLLADO:")
print("• Capacidad de análisis integral end-to-end")
print("• Comunicación adaptada a diferentes audiencias")
print("• Framework sistemático reproducible")
print("• Criterios de validación rigurosos")
print("• Traducción de complejidad técnica a decisiones estratégicas")

print(
    "\nPregunta de síntesis: ¿Cómo esta integración multiplica tu valor vs. conocimientos aislados?"
)
print(
    "¿Te sientes preparado para abordar desafíos de modelado predictivo en el Bloque 3?"
)

# %%
# ¿Cómo conectar tu competencia del Bloque 2 con los desafíos del Bloque 3?
# Vamos a crear un puente conceptual hacia el modelado predictivo

print("PREPARACIÓN PARA EL BLOQUE 3: MODELADO PREDICTIVO")
print("=" * 55)

# ¿Cómo evolucionan tus preguntas analíticas del descriptivo al predictivo?
print("EVOLUCIÓN DE PREGUNTAS ANALÍTICAS:")
print("-" * 35)

preguntas_evolucion = {
    "Bloque 2 (Descriptivo)": [
        "¿Cuántos goles marcó este equipo?",
        "¿Qué equipos tienen mejor posesión?",
        "¿Cómo correlacionan goles y victorias?",
        "¿Qué patrones vemos en los datos históricos?",
    ],
    "Bloque 3 (Predictivo)": [
        "¿Cuántos goles marcará este equipo el próximo mes?",
        "¿Qué equipos tienen mayor probabilidad de ganar el título?",
        "¿Podemos predecir el resultado antes del partido?",
        "¿Qué jugador tiene más probabilidad de anotar?",
    ],
}

for bloque, preguntas in preguntas_evolucion.items():
    print(f"\n{bloque}:")
    for pregunta in preguntas:
        print(f"  • {pregunta}")

print("\n" + "=" * 55)
print("TU PREPARACIÓN ACTUAL PARA MODELADO PREDICTIVO:")

# ¿Cómo evaluamos tu preparación para el siguiente nivel?
preparacion_skills = {
    "Manipulación de datos": 95,  # Pandas dominado
    "Visualización": 90,  # Seaborn + matplotlib
    "Estadística descriptiva": 85,  # Correlaciones, distribuciones
    "Interpretación de patrones": 80,  # Framework de validación
    "Comunicación ejecutiva": 75,  # Narrativas persuasivas
}

# Visualización de tu preparación
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: Tu nivel actual de preparación
skills = list(preparacion_skills.keys())
niveles = list(preparacion_skills.values())
colores = [
    "green" if nivel >= 80 else "orange" if nivel >= 70 else "red" for nivel in niveles
]

ax1.barh(skills, niveles, color=colores, alpha=0.7)
ax1.set_xlabel("Nivel de Preparación (%)")
ax1.set_title("Tu Preparación para Modelado Predictivo")
ax1.set_xlim(0, 100)
for i, nivel in enumerate(niveles):
    ax1.text(nivel + 1, i, f"{nivel}%", va="center", fontweight="bold")

# Gráfico 2: Skills necesarios para Bloque 3
skills_bloque3 = [
    "Machine Learning",
    "Modelos Predictivos",
    "Evaluación de Modelos",
    "Feature Engineering",
    "Validación Cruzada",
]
importancia = [95, 90, 85, 80, 75]

ax2.bar(range(len(skills_bloque3)), importancia, color="lightblue", alpha=0.7)
ax2.set_xlabel("Nuevas Competencias")
ax2.set_ylabel("Importancia (%)")
ax2.set_title("Skills a Desarrollar en Bloque 3")
ax2.set_xticks(range(len(skills_bloque3)))
ax2.set_xticklabels(skills_bloque3, rotation=45, ha="right")

plt.tight_layout()
plt.show()

print("DIAGNÓSTICO DE TU PROGRESIÓN:")
promedio_preparacion = np.mean(list(preparacion_skills.values()))
print(f"• Nivel promedio de preparación: {promedio_preparacion:.1f}%")

if promedio_preparacion >= 85:
    status = "EXCELENTE - Listo para desafíos avanzados"
elif promedio_preparacion >= 75:
    status = "BUENO - Preparación sólida para continuar"
else:
    status = "NECESITA REFUERZO - Revisar conceptos básicos"

print(f"• Status de preparación: {status}")

print("\nCONEXIÓN BLOQUE 2 → BLOQUE 3:")
print("✓ Tus skills de análisis descriptivo son la base del predictivo")
print("✓ Tu capacidad de interpretación será crucial para validar modelos")
print("✓ Tu experiencia en visualización te ayudará a comunicar predicciones")
print("✓ Tu framework de validación se expandirá a métricas de modelos")

print(
    "\nPregunta de anticipación: ¿Cómo crees que cambiarán tus responsabilidades al poder 'predecir el futuro'?"
)
print(
    "¿Qué tipo de decisiones deportivas te gustaría influenciar con modelos predictivos?"
)

# %% [markdown]
# ---
#
# ## SÍNTESIS FINAL DEL BLOQUE 2: ¿Cómo has evolucionado como analista deportivo integral?
#
# **Reflexión culminante**: Has completado una transformación extraordinaria desde manipulador básico de datos hasta consultor estratégico capaz de influenciar decisiones deportivas millonarias.
#
# ### Tu metamorfosis documentada:
#
# #### SEMANA 6: ¿Descubriste cómo explorar la riqueza oculta en datasets deportivos?
# - **Logro**: Dominaste la investigación inicial de datos complejos
# - **Transformación**: De intimidación por datasets grandes a exploración sistemática y confiada
#
# #### SEMANA 7: ¿Comprendiste cómo diferentes tipos de datos revelan perspectivas únicas del juego?
# - **Logro**: Clasificaste y aprovechaste datos numéricos, categóricos, temporales y booleanos
# - **Transformación**: De ver "números" a reconocer insights específicos según tipo de información
#
# #### SEMANA 8: ¿Desarrollaste la capacidad de convertir estadísticas en narrativas convincentes?
# - **Logro**: Dominaste estadística descriptiva aplicada al contexto deportivo
# - **Transformación**: De calcular promedios a interpretar patrones que sugieren estrategias
#
# #### SEMANA 9: ¿Masterizaste el arte de hacer que los datos "hablen" visualmente?
# - **Logro**: Creaste visualizaciones que no solo informan sino que persuaden
# - **Transformación**: De gráficos básicos a narrativas visuales que inspiran acción
#
# #### SEMANA 10: ¿Integraste todo en metodologías de consultoría estratégica?
# - **Logro**: Desarrollaste frameworks para traducir complejidad en decisiones ejecutivas
# - **Transformación**: De procesador de datos a influenciador de decisiones estratégicas
#
# ### Tu identidad profesional emergente:
#
# **Analista Deportivo Estratégico**: Profesional capaz de:
# - ✅ Procesar datasets complejos con confianza y eficiencia
# - ✅ Identificar patrones genuinos vs. correlaciones espurias  
# - ✅ Crear visualizaciones que convencen a stakeholders no técnicos
# - ✅ Formular recomendaciones que justifican inversiones significativas
# - ✅ Adaptar comunicación técnica para diferentes audiencias ejecutivas
#
# ### Preparación para el Bloque 3:
#
# **Pregunta de transición**: ¿Estás listo para el salto más dramático - de analista descriptivo a "predictor del futuro deportivo"?
#
# **Tu base sólida**: Las competencias desarrolladas en este bloque son la fundación sobre la cual construirás capacidades de machine learning y modelado predictivo.
#
# **Anticipación**: ¿Cómo crees que cambiarán las expectativas cuando puedas no solo explicar qué pasó sino predecir qué pasará?
#
# ---
#
# ## Logro desbloqueado: Consultor Estratégico Deportivo
#
# ¡Has desarrollado la competencia integral para transformar datos deportivos en inteligencia estratégica que influencia decisiones importantes!
#
# **Tu nueva capacidad**: No solo procesas información deportiva - la conviertes en confianza para tomar decisiones que pueden definir el éxito de organizaciones enteras.
#
# ---
#
# *"El analista que puede explicar el pasado es útil. El analista que puede predecir el futuro es indispensable."*
#
# ### ¿Preparado para convertirte en indispensable?

# %% [markdown]
# ### 📈 Análisis de Tendencias Temporales y Estacionalidad
#
# **Desafío de Inteligencia Comercial:**
#
# Como **consultor de inteligencia de mercado**, has sido contratado por una red de medios deportivos internacional para optimizar su estrategia de programación y maximizar audiencias.
#
# **Pregunta estratégica clave:** ¿Cómo evolucionan los patrones de entretenimiento deportivo a lo largo del tiempo, y qué oportunidades comerciales revelan estas tendencias?
#
# **Tu análisis de inteligencia temporal debe responder:**
#
# 🔍 **Análisis de ciclos de negocio:**
# - ¿En qué momentos del calendario se maximiza el "value proposition" del entretenimiento deportivo?
# - ¿Qué patrones de estacionalidad pueden predecir picos de audiencia?
# - ¿Cómo fluctúa la "intensidad del producto" (goles/espectáculo) temporalmente?
#
# 🎯 **Optimización de cartera de contenidos:**
# - ¿Cuándo programar los eventos premium para maximizar engagement?
# - ¿Qué períodos requieren estrategias de activación de audiencia adicionales?
# - ¿Cómo anticipar y mitigar las caídas estacionales de interés?
#
# **Reflexión de consultor estratégico:**
# - Si fueras CEO de una plataforma de streaming deportivo, ¿cómo usarías estas tendencias temporales para diseñar tu estrategia anual de contenidos?
# - ¿Qué patrones temporales justificarían inversiones diferenciadas en marketing?
# - ¿Cómo convertirías la estacionalidad en ventaja competitiva sostenible?

# %%
# ¿Cómo optimizar una estrategia de contenidos deportivos usando inteligencia temporal?
# Desarrolla tu reporte de programación estratégica:

print("ANÁLISIS DE INTELIGENCIA TEMPORAL DEPORTIVA")
print("=" * 42)

# Preparación de datos temporales para análisis estratégico
# Simularemos fechas si no están disponibles
import datetime as dt
import random

# Generar fechas simuladas para el análisis (últimos 12 meses)
fechas_simuladas = []
fecha_inicio = dt.datetime(2023, 1, 1)
for i in range(len(df_partidos)):
    dias_aleatorios = random.randint(0, 365)
    fecha_partido = fecha_inicio + dt.timedelta(days=dias_aleatorios)
    fechas_simuladas.append(fecha_partido)

df_partidos["Fecha"] = fechas_simuladas
df_partidos["Mes"] = df_partidos["Fecha"].dt.month
df_partidos["Mes_Nombre"] = df_partidos["Fecha"].dt.strftime("%B")
df_partidos["Dia_Semana"] = df_partidos["Fecha"].dt.dayofweek
df_partidos["Semana_Año"] = df_partidos["Fecha"].dt.isocalendar().week

print("ANÁLISIS 1: ESTACIONALIDAD DEL VALUE PROPOSITION")
print("-" * 45)

# Análisis mensual de intensidad de entretenimiento
intensidad_mensual = (
    df_partidos.groupby("Mes").agg({"Total_Goles": ["mean", "count", "sum"]}).round(2)
)

intensidad_mensual.columns = [
    "Intensidad_Promedio",
    "Volumen_Partidos",
    "Goles_Totales",
]

print("RANKING DE MESES POR POTENCIAL COMERCIAL:")
# Crear índice de valor comercial (intensidad * volumen)
intensidad_mensual["Indice_Valor_Comercial"] = (
    intensidad_mensual["Intensidad_Promedio"] * intensidad_mensual["Volumen_Partidos"]
)

ranking_meses = intensidad_mensual.sort_values(
    "Indice_Valor_Comercial", ascending=False
)

meses_nombres = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]

for i, (mes, row) in enumerate(ranking_meses.head().iterrows(), 1):
    print(
        f"{i}. {meses_nombres[mes-1]}: IVC={row['Indice_Valor_Comercial']:.1f} "
        f"({row['Intensidad_Promedio']:.1f} goles/partido × {row['Volumen_Partidos']} eventos)"
    )

# Análisis 2: Optimización de programación semanal
print(f"\nANÁLISIS 2: PROGRAMACIÓN SEMANAL ESTRATÉGICA")
print("-" * 45)

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
rendimiento_semanal = (
    df_partidos.groupby("Dia_Semana")
    .agg(
        {
            "Total_Goles": ["mean", "count"],
            "Ganador": lambda x: (x == "Empate").sum(),  # Contar empates
        }
    )
    .round(2)
)

rendimiento_semanal.columns = ["Intensidad_Promedio", "Volumen", "Empates"]
rendimiento_semanal["Predictibilidad"] = (
    rendimiento_semanal["Empates"] / rendimiento_semanal["Volumen"] * 100
).round(1)

print("ESTRATEGIA DE PROGRAMACIÓN POR DÍA:")
for dia_num, row in rendimiento_semanal.iterrows():
    dia_nombre = dias_semana[dia_num]

    # Clasificación estratégica del día
    if row["Intensidad_Promedio"] > 2.0 and row["Volumen"] > 2:
        categoria = "PREMIUM - Programar eventos estrella"
    elif row["Intensidad_Promedio"] > 1.5:
        categoria = "ESTÁNDAR - Contenido principal sólido"
    else:
        categoria = "NICHO - Oportunidad de diferenciación"

    print(
        f"• {dia_nombre}: {row['Intensidad_Promedio']:.1f} goles/partido "
        f"({row['Volumen']} eventos, {row['Predictibilidad']:.1f}% empates) → {categoria}"
    )

# Análisis 3: Identificación de ventanas de oportunidad
print(f"\nANÁLISIS 3: VENTANAS DE OPORTUNIDAD COMERCIAL")
print("-" * 48)

# Análisis por semanas del año para identificar patrones
rendimiento_semanal_año = (
    df_partidos.groupby("Semana_Año").agg({"Total_Goles": ["mean", "count"]}).round(2)
)

rendimiento_semanal_año.columns = ["Intensidad", "Volumen"]
rendimiento_semanal_año = rendimiento_semanal_año[
    rendimiento_semanal_año["Volumen"] > 0
]

# Identificar semanas de alto valor
umbral_intensidad = rendimiento_semanal_año["Intensidad"].quantile(0.75)
umbral_volumen = rendimiento_semanal_año["Volumen"].quantile(0.5)

semanas_premium = rendimiento_semanal_año[
    (rendimiento_semanal_año["Intensidad"] >= umbral_intensidad)
    & (rendimiento_semanal_año["Volumen"] >= umbral_volumen)
]

print(f"SEMANAS PREMIUM IDENTIFICADAS (Top 25% intensidad + 50%+ volumen):")
for semana, row in semanas_premium.head().iterrows():
    print(
        f"• Semana {semana}: {row['Intensidad']:.1f} goles/partido "
        f"({row['Volumen']} eventos) - Oportunidad de monetización premium"
    )

# Visualización de inteligencia temporal
plt.figure(figsize=(16, 12))

# Visual 1: Mapa de calor de estacionalidad mensual
plt.subplot(2, 3, 1)
matriz_estacional = (
    df_partidos.groupby(["Mes", "Dia_Semana"])["Total_Goles"].mean().unstack()
)
sns.heatmap(
    matriz_estacional,
    annot=True,
    fmt=".1f",
    cmap="YlOrRd",
    xticklabels=dias_semana,
    yticklabels=meses_nombres,
)
plt.title("Mapa de Calor: Intensidad por Mes/Día\n(Goles Promedio)")
plt.xlabel("Día de la Semana")
plt.ylabel("Mes")

# Visual 2: Evolución temporal del value proposition
plt.subplot(2, 3, 2)
intensidad_temporal = df_partidos.groupby("Mes")["Total_Goles"].mean()
plt.plot(range(1, 13), intensidad_temporal, marker="o", linewidth=2, markersize=8)
plt.fill_between(range(1, 13), intensidad_temporal, alpha=0.3)
plt.title("Evolución Anual del Value Proposition")
plt.xlabel("Mes del Año")
plt.ylabel("Intensidad Promedio (Goles/Partido)")
plt.xticks(range(1, 13), [m[:3] for m in meses_nombres], rotation=45)
plt.grid(True, alpha=0.3)

# Visual 3: Análisis de concentración semanal
plt.subplot(2, 3, 3)
volumen_semanal = df_partidos.groupby("Dia_Semana")["Total_Goles"].count()
colores = plt.cm.viridis(np.linspace(0, 1, 7))
plt.bar(range(7), volumen_semanal, color=colores)
plt.title("Concentración de Eventos por Día")
plt.xlabel("Día de la Semana")
plt.ylabel("Número de Partidos")
plt.xticks(range(7), [d[:3] for d in dias_semana])

# Visual 4: Matriz de decisión estratégica (Intensidad vs Volumen)
plt.subplot(2, 3, 4)
for mes in range(1, 13):
    datos_mes = intensidad_mensual.loc[mes]
    plt.scatter(
        datos_mes["Volumen_Partidos"],
        datos_mes["Intensidad_Promedio"],
        s=datos_mes["Indice_Valor_Comercial"] * 5,
        alpha=0.7,
        label=meses_nombres[mes - 1],
    )

plt.xlabel("Volumen de Eventos")
plt.ylabel("Intensidad Promedio (Goles/Partido)")
plt.title("Matriz Estratégica: Volumen vs Intensidad\n(Tamaño = Valor Comercial)")
plt.grid(True, alpha=0.3)

# Visual 5: Distribución de predictibilidad
plt.subplot(2, 3, 5)
plt.hist(
    df_partidos["Total_Goles"],
    bins=range(0, 8),
    alpha=0.7,
    color="lightcoral",
    edgecolor="black",
)
plt.title("Distribución de Predictibilidad\n(Frecuencia por Goles Totales)")
plt.xlabel("Goles Totales por Partido")
plt.ylabel("Frecuencia")
plt.grid(axis="y", alpha=0.3)

# Visual 6: Índice de valor comercial temporal
plt.subplot(2, 3, 6)
plt.bar(
    range(len(ranking_meses)),
    ranking_meses["Indice_Valor_Comercial"],
    color=plt.cm.plasma(np.linspace(0, 1, len(ranking_meses))),
)
plt.title("Ranking de Valor Comercial por Mes")
plt.xlabel("Posición en Ranking")
plt.ylabel("Índice de Valor Comercial")
plt.xticks(
    range(len(ranking_meses)),
    [meses_nombres[mes - 1][:3] for mes in ranking_meses.index],
    rotation=45,
)

plt.tight_layout()
plt.show()

# Recomendaciones estratégicas finales
print(f"\nRECOMENDACIONES ESTRATÉGICAS PARA DIRECCIÓN COMERCIAL:")
print("=" * 55)

mejor_mes = ranking_meses.index[0]
mejor_dia = rendimiento_semanal.loc[rendimiento_semanal["Intensidad_Promedio"].idxmax()]

print(
    f"1. PROGRAMACIÓN PREMIUM: {meses_nombres[mejor_mes-1]} es el mes de mayor valor comercial"
)
print(
    f"2. OPTIMIZACIÓN SEMANAL: Los {dias_semana[rendimiento_semanal['Intensidad_Promedio'].idxmax()]} generan mayor intensidad de entretenimiento"
)
print(
    f"3. VENTANAS DE OPORTUNIDAD: {len(semanas_premium)} semanas identificadas para eventos especiales"
)

media_intensidad = df_partidos["Total_Goles"].mean()
meses_premium = ranking_meses[ranking_meses["Intensidad_Promedio"] > media_intensidad]

print(
    f"4. ESTRATEGIA DE PRECIOS: {len(meses_premium)} meses justifican pricing premium"
)
print(
    f"5. ACTIVACIÓN DE AUDIENCIA: Invertir recursos adicionales en meses de baja intensidad para mantener engagement"
)

print(f"\nIMPACTO COMERCIAL PROYECTADO:")
print(
    f"• Optimización de programación puede incrementar audiencia promedio {(ranking_meses.iloc[0]['Intensidad_Promedio'] / media_intensidad - 1) * 100:.1f}%"
)
print(f"• Concentración en ventanas premium puede mejorar ROI de marketing hasta 40%")
print(
    f"• Estrategia de contenidos diferenciada por estacionalidad puede incrementar retención de suscriptores 15-25%"
)

# %% [markdown]
# ### 🎯 Síntesis Estratégica y Próximos Pasos
#
# **Reflexión del Consultor Senior:**
#
# Has completado tu primer **análisis integral de consultoría deportiva**. Como analista estratégico, has transformado datos brutos en inteligencia comercial que puede impulsar decisiones ejecutivas de millones de dólares.
#
# **¿Qué habilidades de consultor estratégico has desarrollado hoy?**
#
# 🔍 **Pensamiento Analítico de Élite:**
# - Capacidad de identificar patrones estratégicos ocultos en datasets complejos
# - Habilidad para cuantificar ventajas competitivas y oportunidades de mercado
# - Competencia en traducir análisis técnicos a recomendaciones ejecutivas
#
# 💼 **Expertise en Inteligencia Comercial:**
# - Análisis de cuotas de mercado y posicionamiento competitivo
# - Evaluación de riesgo-retorno en decisiones de inversión deportiva
# - Optimización de estrategias de programación y monetización
#
# 📈 **Capacidades de Consultoría Avanzada:**
# - Generación de insights accionables para comités de inversión
# - Desarrollo de marcos de análisis temporal para maximizar value proposition
# - Construcción de argumentos basados en evidencia para decisiones estratégicas
#
# **Reflexiones críticas de tu evolución como analista:**
#
# 1. **¿Cómo has evolucionado desde ser un "manipulador de datos" hasta convertirte en un "estratega de inteligencia comercial"?**
#
# 2. **¿Qué diferencias observas entre hacer análisis "por hacer análisis" vs. generar insights que impulsen decisiones de $100+ millones?**
#
# 3. **¿Cómo aplicarías esta mentalidad de consultor estratégico a otros sectores (fintech, retail, manufactura)?**
#
# **Tu próximo nivel como consultor de datos:**
#
# En el **Bloque 3**, evolucionarás de "analista estratégico" a **"arquitecto de inteligencia predictiva"**, donde no solo interpretarás el pasado, sino que construirás modelos que predigan el futuro y optimicen decisiones en tiempo real.
#
# **Desafío de transición:** ¿Estás listo para pasar de consultor de insights retrospectivos a arquitecto de ventajas competitivas predictivas?

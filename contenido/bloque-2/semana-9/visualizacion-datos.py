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
# # Semana 9: ¿Cómo transformar números fríos en historias visuales convincentes?
#
# ## ¿Alguna vez te has preguntado por qué una imagen deportiva comunica más que mil estadísticas?
#
# **Reflexión inicial**: Cuando ves las gráficas de rendimiento durante un partido de la Liga MX, tu cerebro procesa la información instantáneamente. ¿Pero qué pasaría si esos mismos datos fueran solo números en una tabla?
#
# ### Pregunta motivadora para la semana:
# Si fueras analista del América y tuvieras que convencer a la directiva de fichar a un jugador específico, ¿usarías tablas llenas de números o gráficos que cuenten una historia visual?
#
# ---
#
# ## ESTRUCTURA SEMANAL: 3 Sesiones de Descubrimiento
#
# ### SESIÓN 1: ¿Por qué nuestro cerebro prefiere ver que leer? (50 min)
# **Pregunta guía**: ¿Cómo los gráficos transforman nuestra capacidad de entender datos?
# - ¿Qué ventajas evolutivas tiene el procesamiento visual sobre el numérico?
# - ¿Por qué ciertos tipos de gráficos revelan patrones específicos?
# - ¿Cómo elegir la visualización correcta para cada tipo de insight?
#
# ### SESIÓN 2: ¿Qué técnicas crean visualizaciones irresistibles? (50 min)  
# **Pregunta guía**: ¿Cómo diseñar gráficos que no solo informen sino que persuadan?
# - ¿Qué elementos visuales capturan y mantienen la atención?
# - ¿Cómo el color y el diseño amplifican el mensaje de los datos?
# - ¿Cuándo la estética mejora vs distrae del contenido?
#
# ### SESIÓN 3: ¿Cómo crear dashboards que cambien decisiones? (50 min)
# **Pregunta guía**: ¿Qué diferencia un gráfico informativo de uno transformador?
# - ¿Cómo combinar múltiples visualizaciones en narrativas coherentes?
# - ¿Qué estrategias usan los equipos profesionales para comunicar insights?
# - ¿Cómo adaptar visualizaciones para diferentes audiencias?
#
# ---
#
# ## ¿Por qué dominar la visualización de datos deportivos?
#
# **Pregunta reflexiva**: ¿Has notado que los equipos más exitosos no solo generan datos, sino que los transforman en herramientas de decisión visual? ¿Será porque los humanos tomamos decisiones con los ojos, no con calculadoras?
#
# ### La revolución visual en el deporte moderno:
# - **¿Sabías que...?** Los entrenadores modernos toman decisiones tácticas en tiempo real basándose en visualizaciones dinámicas
# - **¿Te imaginas que...?** Una visualización mal diseñada puede costarte la comprensión de un patrón crucial de rendimiento
# - **¿Has considerado que...?** Los análisis visuales más efectivos combinan ciencia de datos con principios de comunicación visual
#
# **Tu misión esta semana**: Convertirte en un "narrador visual" que transforma datos complejos en historias irresistibles.
#
# ¿Estás listo para descubrir cómo hacer que los datos deportivos cobren vida a través de visualizaciones extraordinarias?

# %% [markdown]
# # SESIÓN 1: ¿Por qué nuestro cerebro prefiere ver que leer? (50 minutos)
#
# ## Pregunta de apertura: ¿Qué tienen en común un mapa y un gráfico deportivo?
#
# **Reflexiona antes de continuar**: Ambos transforman información compleja en patrones visuales que puedes entender en segundos. ¿Pero qué hace que tu cerebro procese imágenes 60,000 veces más rápido que texto?
#
# ---
#
# ## Momento de curiosidad: ¿Por qué los gráficos deportivos son tan adictivos?
#
# Imagina que te muestran una tabla con 20 filas de estadísticas de goleadores. Luego te muestran el mismo dato en un gráfico de barras colorido. ¿Cuál captó tu atención primero y por más tiempo?
#
# **Pregunta reflexiva**: ¿Será que nuestro cerebro evolucionó para detectar patrones visuales como estrategia de supervivencia, y ahora aplicamos esa misma habilidad a los datos deportivos?
#
# ### ¿Qué diferencia hay entre "ver números" y "visualizar patrones"?
#
# Antes de crear gráficos, necesitamos entender que existe una diferencia fundamental entre mostrar datos y revelar insights. ¿Has notado que algunos gráficos te hacen decir "¡Ahá!" inmediatamente, mientras otros solo te confunden?
#
# ## ¿Cómo exploramos los diferentes "idiomas" visuales del análisis deportivo?
#
# **Momento de reflexión**: En el mundo de la visualización, cada tipo de gráfico tiene su propio "superpoder". ¿Pero cómo elegir el tipo correcto para revelar el insight que buscas?
#
# **Pregunta clave**: Si quisieras mostrar la evolución del rendimiento de un jugador a lo largo de una temporada, ¿qué tipo de visualización elegiría tu intuición?
#
# ### ¡Vamos a ser "traductores" visuales de datos deportivos!
#
# Antes de crear visualizaciones complejas, necesitamos dominar el arte de elegir el tipo correcto de gráfico para cada historia que queremos contar. ¿Has notado que algunos datos "piden" ciertos tipos de visualización?
#
# ### ¿Qué herramientas necesitamos para nuestro estudio visual?
#
# **Pregunta instrumental**: Para crear visualizaciones que compitan con ESPN y Fox Sports, ¿qué capacidades técnicas serían esenciales?

# %% [markdown]
# ## ¿Cómo configuramos nuestro "estudio de diseño" visual deportivo?
#
# **Momento de reflexión**: Para crear visualizaciones que rivalen con las que ves en ESPN, necesitas las herramientas correctas. ¿Pero qué diferencia hay entre herramientas y maestría en su uso?
#
# **Pregunta clave**: Si tuvieras que elegir entre control total sobre cada detalle visual o resultados profesionales rápidos, ¿qué elegiría un analista bajo presión?
#
# ### ¡Vamos a ser "directores artísticos" de datos deportivos!
#
# **Tu arsenal creativo profesional**:
# - **Pandas**: ¿Tu organizador de información compleja?
# - **Seaborn**: ¿Tu director artístico con inteligencia estadística?
# - **Matplotlib**: ¿Tu lienzo infinito para creatividad visual?
# - **NumPy**: ¿Tu generador de escenarios futbolísticos realistas?
#
# ### ¿Por qué Seaborn es revolucionario para visualización deportiva?
#
# **Pregunta de eficiencia**: ¿Qué valorarías más como analista deportivo profesional: pasar horas perfeccionando detalles visuales o generar insights rápidamente con estética automática de nivel profesional?
#
# **Ventajas estratégicas**:
# - **Estética instantánea**: ¿Gráficos de calidad televisiva sin ser diseñador gráfico?
# - **Integración inteligente**: ¿Visualizaciones que "entienden" la naturaleza de tus datos?
# - **Escalabilidad creativa**: ¿De prototipos rápidos a presentaciones ejecutivas?
#
# **Pregunta anticipatoria**: ¿Crees que estas herramientas cambiarán tu velocidad para descubrir y comunicar insights deportivos?

# %%
# ¿Te has preguntado qué herramientas usan los creadores de gráficos deportivos profesionales?
# Vamos a configurar nuestro "estudio de producción visual" paso a paso

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# ¿Por qué necesitamos cada una de estas herramientas para visualización deportiva?
# pandas -> ¿Para qué crees que sirve cuando tenemos datos complejos de múltiples equipos?
# numpy -> ¿Qué ventajas tiene para crear datos realistas de análisis?
# seaborn -> ¿Cómo puede transformar números aburridos en visualizaciones fascinantes?
# matplotlib -> ¿Por qué necesitamos control creativo total sobre nuestros gráficos?

# ¿Qué transformación visual esperas con esta configuración profesional?
sns.set_theme(style="whitegrid", palette="Set2")
plt.rcParams["figure.figsize"] = (10, 6)

print("¡Estudio de visualización deportiva activado!")
print(
    "¿Te has preguntado alguna vez cómo ESPN crea esos gráficos impactantes durante los partidos?"
)
print("¡Exactamente con las mismas herramientas que acabamos de cargar!")
print()
print("pandas: Tu curador de datos deportivos complejos")
print("seaborn: Tu director artístico con inteligencia estadística")
print("matplotlib: Tu lienzo ilimitado para creatividad visual")
print("numpy: Tu simulador de realidades futbolísticas")
print()
print(
    "Pregunta de reflexión: ¿Cómo crees que estas herramientas cambiarán tu capacidad de contar historias visuales?"
)

# %% [markdown]
# ## ¿Cómo creamos nuestro "universo futbolístico" de visualización?
#
# **Momento de reflexión**: Para practicar visualizaciones efectivas, necesitamos datos que representen la riqueza y variabilidad del fútbol real. ¿Pero qué características debe tener un dataset ideal para contar historias visuales convincentes?
#
# **Pregunta clave**: Si tuvieras que crear datos sintéticos que capturen la emoción y complejidad de una temporada futbolística, ¿qué variables incluirías para que las visualizaciones sean realmente reveladoras?
#
# ### ¡Vamos a ser "productores" de datos deportivos cinematográficos!
#
# Antes de crear visualizaciones, necesitamos generar un dataset que tenga la diversidad y los patrones interesantes que hacen que los gráficos cobren vida. ¿Has notado que los mejores gráficos deportivos siempre tienen datos con historias intrínsecas?
#
# ### ¿Qué dimensiones del fútbol capturaremos para nuestras visualizaciones?
#
# **Pregunta de diseño**: Para que nuestras visualizaciones sean realmente instructivas, ¿qué aspectos del fútbol profesional deberíamos modelar?
#
# **Dimensiones narrativas**:
# - **Equipos icónicos**: ¿Nombres que generen engagement emocional?
# - **Variabilidad realista**: ¿Resultados que reflejen la impredecibilidad del deporte?
# - **Métricas multidimensionales**: ¿Variables que permitan análisis visuales complejos?
# - **Patrones temporales**: ¿Tendencias que revelen historias de temporada?
#
# **Pregunta metodológica**: ¿Prefieres datos perfectamente organizados o datos que reflejen el caos hermoso del fútbol real?

# %%
# ¿Te has preguntado cómo crear datos que capturen la épica del fútbol profesional?
# Vamos a construir nuestro dataset de "temporada cinematográfica" paso a paso

# ¿Por qué la reproducibilidad es crucial en visualización de datos?
np.random.seed(42)  # Consistencia: todos crearemos las mismas historias visuales

print("CREANDO NUESTRA TEMPORADA FUTBOLÍSTICA ÉPICA")
print("=" * 50)

# ¿Qué equipos europeos reconoces inmediatamente?
# Reflexiona: ¿Por qué elegimos estos equipos para máximo engagement visual?
equipos = [
    "Real Madrid",
    "Barcelona",
    "Manchester City",
    "Liverpool",
    "PSG",
    "Bayern Munich",
]

print(f"Equipos protagonistas: {len(equipos)} equipos élite")

# ¿Cuántos partidos representan una temporada interesante?
n_partidos = 50

# ¿Cómo generamos datos que cuenten historias visuales convincentes?
partidos_data = []

for i in range(n_partidos):
    # ¿Por qué elegir equipos aleatoriamente crea narrativas más interesantes?
    equipo_local = np.random.choice(equipos)
    equipo_visitante = np.random.choice([e for e in equipos if e != equipo_local])

    # ¿Qué hace realistas estos rangos de goles?
    goles_local = np.random.randint(0, 5)  # 0 a 4 goles
    goles_visitante = np.random.randint(0, 4)  # Ligera ventaja local

    # ¿Cómo agregamos variables que enriquezcan nuestras visualizaciones?
    posesion_local = np.random.randint(35, 75)  # Porcentaje de posesión
    tiros_local = np.random.randint(8, 25)  # Tiros al arco
    faltas_local = np.random.randint(5, 20)  # Faltas cometidas

    # ¿Qué insights visuales permitirán estas variables?
    partido = {
        "Equipo_Local": equipo_local,
        "Equipo_Visitante": equipo_visitante,
        "Goles_Local": goles_local,
        "Goles_Visitante": goles_visitante,
        "Total_Goles": goles_local + goles_visitante,
        "Posesion_Local": posesion_local,
        "Tiros_Local": tiros_local,
        "Faltas_Local": faltas_local,
        "Partido": i + 1,
    }
    partidos_data.append(partido)

# ¿Qué ventajas tiene estructurar estos datos en un DataFrame?
df_partidos = pd.DataFrame(partidos_data)

print(f"Temporada generada: {len(df_partidos)} partidos épicos")
print("\nPrimeros 5 partidos de nuestra temporada:")
print(df_partidos.head())

print(f"\nEquipos más activos como locales:")
print(df_partidos["Equipo_Local"].value_counts())

print(
    "\nPregunta de reflexión: ¿Estos datos tienen la variabilidad necesaria para crear visualizaciones impactantes?"
)
print("¿Qué patrones visuales crees que emergerán de este dataset?")

# %% [markdown]
# # ¿Qué tipos de gráficos revelan diferentes historias?
#
# ## Pregunta fundamental: ¿Cómo elegir el tipo de visualización que mejor cuente tu historia?
#
# **Reflexiona**: Tienes datos de 50 partidos con múltiples variables. ¿Pero cómo sabes qué tipo de gráfico revelará los insights más valiosos para cada pregunta específica?
#
# **Momento de descubrimiento**: Vamos a explorar cómo diferentes tipos de visualización destacan aspectos únicos de los mismos datos.
#
# ### ¿Qué diferencia hay entre "mostrar datos" y "revelar insights"?
#
# **Pregunta clave**: Si quisieras investigar si realmente existe "ventaja local" en el fútbol, ¿qué tipo de visualización sería más convincente: barras, líneas, o gráficos circulares?
#
# #### Los cuatro poderes básicos de la visualización:
# - **Comparación**: ¿Quién es mejor entre múltiples opciones?
# - **Distribución**: ¿Cómo se esparcen los valores?
# - **Relación**: ¿Dos variables están conectadas?
# - **Evolución**: ¿Cómo cambian las cosas en el tiempo?
#
# **Pregunta estratégica**: ¿Crees que un solo tipo de gráfico puede contar toda la historia de tus datos?

# %%
# ¿Te has preguntado qué gráfico es el más efectivo para comparar rendimientos?
# Vamos a crear nuestro primer "laboratorio visual" paso a paso

print("EXPLORANDO EL PODER DE LOS GRÁFICOS DE BARRAS")
print("="*50)

# ¿Cómo transformamos datos complejos en comparaciones visuales simples?
# Vamos a investigar: ¿Existe realmente la "ventaja local"?

# ¿Por qué reestructurar los datos de esta manera facilita la comparación?
datos_comparacion = []
for _, row in df_partidos.iterrows():
    datos_comparacion.append({'Tipo': 'Local', 'Goles': row['Goles_Local']})
    datos_comparacion.append({'Tipo': 'Visitante', 'Goles': row['Goles_Visitante']})

df_comparacion = pd.DataFrame(datos_comparacion)

# ¿Qué historia cuenta este gráfico que los números solos no pueden?
plt.figure(figsize=(10, 6))
sns.barplot(data=df_comparacion, x='Tipo', y='Goles', palette='Set2')
plt.title('¿Existe realmente la ventaja local en el fútbol?', size=16, pad=20)
plt.ylabel('Goles Promedio por Partido')
plt.xlabel('Tipo de Equipo')

# ¿Cómo agregamos información numérica que enriquezca la visualización?
for i, tipo in enumerate(['Local', 'Visitante']):
    promedio = df_comparacion[df_comparacion['Tipo'] == tipo]['Goles'].mean()
    plt.text(i, promedio + 0.05, f'{promedio:.2f}', ha='center', fontweight='bold')

plt.show()

# ¿Qué insights adicionales revelan los números?
print("\nAnálisis numérico de respaldo:")
promedio_local = df_partidos['Goles_Local'].mean()
promedio_visitante = df_partidos['Goles_Visitante'].mean()
diferencia = promedio_local - promedio_visitante

print(f"Promedio goles locales: {promedio_local:.2f}")
print(f"Promedio goles visitantes: {promedio_visitante:.2f}")
print(f"Diferencia: {diferencia:.2f} goles")

if diferencia > 0.1:
    print("✓ Los datos sugieren ventaja local")
elif diferencia < -0.1:
    print("✓ Los datos sugieren ventaja visitante")
else:
    print("≈ Los datos sugieren equilibrio")

print("\nPregunta de reflexión: ¿Este gráfico de barras te convence más que solo ver los números?")
print("¿Qué otros tipos de visualización podrían revelar patrones diferentes en estos mismos datos?")
axes[1, 1].set_title('¿Quién ataca más?')

<VSCode.Cell id="#VSC-sesión2-inicio" language="markdown">
---

## SÍNTESIS DE LA SESIÓN 1: ¿Qué hemos descubierto sobre visualizaciones básicas?

**Reflexión de 50 minutos**:
- ¿Cómo los gráficos de barras transforman comparaciones numéricas en insights visuales inmediatos?
- ¿Por qué nuestro cerebro procesa patrones visuales más rápido que tablas de números?
- ¿Cuándo un tipo específico de gráfico revela historias que otros tipos ocultan?

**Pregunta preparatoria**: ¿Estás listo para explorar técnicas avanzadas que transforman datos en narrativas visuales irresistibles?

---

# SESIÓN 2: ¿Qué técnicas crean visualizaciones irresistibles? (50 minutos)

## Pregunta de apertura: ¿Qué diferencia hay entre un gráfico que informa y uno que transforma percepciones?

**Reflexiona**: Has creado tu primer gráfico de barras, pero ¿cómo llevarlo al siguiente nivel? ¿Qué elementos visuales hacen que algunos gráficos se queden en tu memoria mientras otros se olvidan inmediatamente?

**Desafío creativo**: Si tuvieras que presentar tus hallazgos al presidente del Real Madrid, ¿cómo harías que tus visualizaciones fueran imposibles de ignorar?

---

## ¿Qué técnicas separan a los visualizadores amateur de los profesionales?

**Momento de elevación**: Los analistas de ESPN y Fox Sports no solo muestran datos, crean experiencias visuales que cautivan a millones. ¿Cuáles son sus secretos?

# %%
# ¿Te has preguntado qué hace que algunas visualizaciones sean verdaderamente memorables?
# Vamos a explorar técnicas que transforman datos en narrativas visuales impactantes

print("TÉCNICAS AVANZADAS DE VISUALIZACIÓN DEPORTIVA")
print("=" * 50)

# ¿Cómo crear un "dashboard" multidimensional que cuente una historia completa?
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle(
    "ANÁLISIS VISUAL MULTIDIMENSIONAL: Local vs Visitante",
    fontsize=16,
    fontweight="bold",
)

# Técnica 1: Gráficos de dispersión - ¿Revelando correlaciones ocultas?
axes[0, 0].scatter(
    df_partidos["Tiros_Local"],
    df_partidos["Goles_Local"],
    alpha=0.6,
    s=80,
    color="skyblue",
    label="Tiros vs Goles",
)
axes[0, 0].set_title("¿Más tiros garantizan más goles?")
axes[0, 0].set_xlabel("Tiros al Arco")
axes[0, 0].set_ylabel("Goles Anotados")

# ¿Cómo añadir una línea de tendencia para mayor claridad?
z = np.polyfit(df_partidos["Tiros_Local"], df_partidos["Goles_Local"], 1)
p = np.poly1d(z)
axes[0, 0].plot(
    df_partidos["Tiros_Local"],
    p(df_partidos["Tiros_Local"]),
    "r--",
    alpha=0.8,
    linewidth=2,
)

# Técnica 2: Histogramas - ¿Mostrando distribuciones de rendimiento?
axes[0, 1].hist(
    df_partidos["Total_Goles"], bins=8, color="lightgreen", alpha=0.7, edgecolor="black"
)
axes[0, 1].set_title('¿Cuál es la "normalidad" en goles por partido?')
axes[0, 1].set_xlabel("Total de Goles por Partido")
axes[0, 1].set_ylabel("Frecuencia")

# ¿Cómo añadir estadísticas visuales para mayor contexto?
promedio_goles = df_partidos["Total_Goles"].mean()
axes[0, 1].axvline(
    promedio_goles,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Promedio: {promedio_goles:.1f}",
)
axes[0, 1].legend()

# Técnica 3: Box plots - ¿Comparando distribuciones completas?
sns.boxplot(data=df_comparacion, x="Tipo", y="Goles", ax=axes[1, 0], palette="Set3")
axes[1, 0].set_title("¿Cómo varía la consistencia ofensiva?")
axes[1, 0].set_ylabel("Distribución de Goles")

# Técnica 4: Gráficos de línea temporal - ¿Mostrando evolución?
goles_acumulados = df_partidos["Total_Goles"].cumsum()
axes[1, 1].plot(
    range(1, len(goles_acumulados) + 1),
    goles_acumulados,
    marker="o",
    linewidth=2,
    markersize=4,
    color="orange",
)
axes[1, 1].set_title("¿Cómo evoluciona la emoción de la temporada?")
axes[1, 1].set_xlabel("Número de Partido")
axes[1, 1].set_ylabel("Goles Acumulados")

plt.tight_layout()
plt.show()

print("\nTÉCNICAS PROFESIONALES APLICADAS:")
print("✓ Correlaciones: Dispersión + línea de tendencia")
print("✓ Distribuciones: Histograma + promedio visual")
print("✓ Comparaciones: Box plots para variabilidad completa")
print("✓ Evolución temporal: Líneas para mostrar progresión")

print(
    "\nPregunta de reflexión: ¿Cuál de estas técnicas reveló el insight más sorprendente?"
)
print("¿Cómo combinarías múltiples técnicas para crear una narrativa visual única?")

# Agregar anotaciones emocionantes
plt.annotate(
    "¡Empezaron ganando!",
    xy=(40, 3),
    xytext=(45, 3.5),
    arrowprops=dict(arrowstyle="->", color="red"),
)
plt.annotate(
    "¡REMONTADA!",
    xy=(85, 4),
    xytext=(70, 4.5),
    arrowprops=dict(arrowstyle="->", color="blue"),
    fontsize=12,
    fontweight="bold",
)

plt.show()

# Contar la historia
print("\nLA HISTORIA DEL PARTIDO:")
print("Minuto 10: ¡Gol del visitante! 0-1")
print("Minuto 25: ¡Segundo gol visitante! 0-2")
print("Minuto 40: ¡Tercer gol visitante! 0-3")
print("Minuto 50: ¡Primer gol local! 1-3")
print("Minuto 65: ¡Segundo gol local! 2-3")
print("Minuto 75: ¡Empate! 3-3")
print("Minuto 85: ¡GOL DE LA VICTORIA! 4-3")

print("\n¡Remontada histórica! De 0-3 a 4-3")

# %% [markdown]
# ---
#
# ## SÍNTESIS DE LA SESIÓN 2: ¿Qué hemos revelado sobre técnicas avanzadas?
#
# **Reflexión de 50 minutos**:
# - ¿Cómo los gráficos multidimensionales revelan relaciones que análisis unidimensionales ocultan?
# - ¿Qué ventajas tienen las visualizaciones compuestas sobre gráficos individuales?
# - ¿Por qué combinar diferentes técnicas visuales enriquece la narrativa de los datos?
#
# **Pregunta preparatoria**: ¿Estás listo para crear visualizaciones que no solo impresionen sino que transformen decisiones deportivas?
#
# ---
#
# # SESIÓN 3: ¿Cómo crear dashboards que cambien decisiones? (50 minutos)
#
# ## Pregunta de apertura: ¿Qué diferencia hay entre mostrar datos y contar historias transformadoras?
#
# **Reflexiona**: Has dominado técnicas visuales individuales, pero ¿cómo combinarlas en narrativas que convenzan a directivos de invertir millones de euros? ¿Qué hace que una presentación visual sea imposible de ignorar?
#
# **Desafío profesional**: Si fueras el analista principal del Manchester City y tuvieras que justificar el fichaje de un jugador de 100 millones de euros usando solo visualizaciones, ¿cómo estructurarías tu presentación?
#
# ---
#
# ## ¿Qué estrategias usan los equipos élite para visualizar decisiones cruciales?
#
# **Momento de maestría**: Los equipos más exitosos no solo analizan datos, los transforman en herramientas de decisión visual que alinean a toda la organización.

# %%
# ¿Te has preguntado cómo crear un dashboard que cambie percepciones y decisiones?
# Vamos a construir una visualización de "impacto ejecutivo"

print("CREANDO UN DASHBOARD EJECUTIVO PROFESIONAL")
print("=" * 60)

# ¿Cómo simular una situación de análisis de fichaje realista?
# Vamos a crear el perfil visual de dos "candidatos" para contratación

# Generamos perfiles de jugadores hipotéticos
np.random.seed(123)  # Nuevos datos para la comparación

jugador_a_stats = {
    "Goles": np.random.normal(15, 3, 20),
    "Asistencias": np.random.normal(8, 2, 20),
    "Pases_Exitosos": np.random.normal(85, 5, 20),
    "Duelos_Ganados": np.random.normal(65, 8, 20),
}

jugador_b_stats = {
    "Goles": np.random.normal(12, 4, 20),
    "Asistencias": np.random.normal(12, 3, 20),
    "Pases_Exitosos": np.random.normal(90, 3, 20),
    "Duelos_Ganados": np.random.normal(70, 6, 20),
}

# ¿Cómo crear un dashboard que cuente una historia convincente?
fig = plt.figure(figsize=(16, 12))
fig.suptitle(
    "ANÁLISIS DE FICHAJE: ¿Quién tiene el perfil más prometedor?",
    fontsize=18,
    fontweight="bold",
    y=0.95,
)

# Dashboard con 6 perspectivas diferentes
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# 1. Comparación de rendimiento ofensivo
ax1 = fig.add_subplot(gs[0, 0])
categorias = ["Goles", "Asistencias"]
jugador_a_ofensivo = [
    np.mean(jugador_a_stats["Goles"]),
    np.mean(jugador_a_stats["Asistencias"]),
]
jugador_b_ofensivo = [
    np.mean(jugador_b_stats["Goles"]),
    np.mean(jugador_b_stats["Asistencias"]),
]

x = np.arange(len(categorias))
width = 0.35
ax1.bar(
    x - width / 2,
    jugador_a_ofensivo,
    width,
    label="Candidato A",
    alpha=0.8,
    color="skyblue",
)
ax1.bar(
    x + width / 2,
    jugador_b_ofensivo,
    width,
    label="Candidato B",
    alpha=0.8,
    color="lightcoral",
)
ax1.set_title("Impacto Ofensivo")
ax1.set_xticks(x)
ax1.set_xticklabels(categorias)
ax1.legend()

# 2. Consistencia temporal
ax2 = fig.add_subplot(gs[0, 1])
partidos = range(1, 21)
ax2.plot(
    partidos,
    jugador_a_stats["Goles"],
    marker="o",
    label="Candidato A",
    alpha=0.7,
    linewidth=2,
)
ax2.plot(
    partidos,
    jugador_b_stats["Goles"],
    marker="s",
    label="Candidato B",
    alpha=0.7,
    linewidth=2,
)
ax2.set_title("Consistencia en Goles")
ax2.set_xlabel("Partido")
ax2.set_ylabel("Goles")
ax2.legend()
ax2.grid(True, alpha=0.3)

# 3. Distribución de rendimiento técnico
ax3 = fig.add_subplot(gs[0, 2])
ax3.boxplot(
    [jugador_a_stats["Pases_Exitosos"], jugador_b_stats["Pases_Exitosos"]],
    labels=["Candidato A", "Candidato B"],
)
ax3.set_title("Precisión de Pases (%)")
ax3.set_ylabel("Porcentaje de Éxito")

# 4. Correlación habilidades
ax4 = fig.add_subplot(gs[1, 0])
ax4.scatter(
    jugador_a_stats["Goles"],
    jugador_a_stats["Asistencias"],
    alpha=0.6,
    s=60,
    label="Candidato A",
    color="skyblue",
)
ax4.scatter(
    jugador_b_stats["Goles"],
    jugador_b_stats["Asistencias"],
    alpha=0.6,
    s=60,
    label="Candidato B",
    color="lightcoral",
)
ax4.set_xlabel("Goles por Partido")
ax4.set_ylabel("Asistencias por Partido")
ax4.set_title("Versatilidad Ofensiva")
ax4.legend()

# 5. Radar comparativo
ax5 = fig.add_subplot(gs[1, 1], projection="polar")
categorias_radar = ["Goles", "Asistencias", "Pases", "Duelos"]
valores_a = [
    np.mean(jugador_a_stats["Goles"]) / 20 * 100,
    np.mean(jugador_a_stats["Asistencias"]) / 15 * 100,
    np.mean(jugador_a_stats["Pases_Exitosos"]),
    np.mean(jugador_a_stats["Duelos_Ganados"]),
]
valores_b = [
    np.mean(jugador_b_stats["Goles"]) / 20 * 100,
    np.mean(jugador_b_stats["Asistencias"]) / 15 * 100,
    np.mean(jugador_b_stats["Pases_Exitosos"]),
    np.mean(jugador_b_stats["Duelos_Ganados"]),
]

angulos = np.linspace(0, 2 * np.pi, len(categorias_radar), endpoint=False).tolist()
valores_a += valores_a[:1]
valores_b += valores_b[:1]
angulos += angulos[:1]

ax5.plot(angulos, valores_a, "o-", linewidth=2, label="Candidato A")
ax5.fill(angulos, valores_a, alpha=0.25)
ax5.plot(angulos, valores_b, "s-", linewidth=2, label="Candidato B")
ax5.fill(angulos, valores_b, alpha=0.25)
ax5.set_xticks(angulos[:-1])
ax5.set_xticklabels(categorias_radar)
ax5.set_title("Perfil Completo")

# 6. Resumen ejecutivo
ax6 = fig.add_subplot(gs[1:, 2])
ax6.axis("off")

# ¿Cómo presentar insights clave de manera visual?
resumen_texto = f"""
RESUMEN EJECUTIVO

CANDIDATO A:
• Goleador más consistente
• {np.mean(jugador_a_stats['Goles']):.1f} goles promedio
• Especialista ofensivo
• Riesgo: Menor versatilidad

CANDIDATO B:
• Más equilibrado
• {np.mean(jugador_b_stats['Asistencias']):.1f} asistencias promedio
• Mayor precisión técnica
• Ventaja: Versatilidad total

RECOMENDACIÓN:
Basado en análisis visual
multidimensional...
"""

ax6.text(
    0.05,
    0.95,
    resumen_texto,
    transform=ax6.transAxes,
    fontsize=11,
    verticalalignment="top",
    bbox=dict(boxstyle="round", facecolor="lightgray", alpha=0.8),
)

plt.show()

print("\nCOMPONENTES DEL DASHBOARD EJECUTIVO:")
print("✓ Comparación directa (barras)")
print("✓ Análisis temporal (líneas)")
print("✓ Distribuciones (box plots)")
print("✓ Correlaciones (dispersión)")
print("✓ Perfil integral (radar)")
print("✓ Síntesis ejecutiva (texto)")

print(
    "\nPregunta de reflexión: ¿Esta combinación de visualizaciones te daría confianza para tomar una decisión de 100M€?"
)
print("¿Qué elemento visual fue más convincente para formar tu opinión?")

# %%
# ¿Cómo crear una secuencia visual que cuente una historia completa?
# Vamos a diseñar una "presentación ejecutiva" con narrativa progresiva

print("CREANDO UNA NARRATIVA VISUAL PROGRESIVA")
print("=" * 50)

# Historia: "La evolución de un equipo durante una temporada"
temporada_datos = {
    "Mes": ["Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre", "Enero"],
    "Puntos": [8, 12, 18, 22, 28, 35],
    "Goles_Favor": [12, 18, 25, 30, 38, 45],
    "Goles_Contra": [8, 10, 12, 15, 16, 18],
    "Asistencia_Promedio": [25000, 27000, 32000, 35000, 38000, 42000],
}

# ¿Cómo estructurar una presentación que convenza progresivamente?
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle(
    "LA TRANSFORMACIÓN DE UN EQUIPO: Una Historia en 4 Actos",
    fontsize=16,
    fontweight="bold",
)

# Acto 1: "El Despertar" - Evolución de puntos
axes[0, 0].plot(
    temporada_datos["Mes"],
    temporada_datos["Puntos"],
    marker="o",
    linewidth=3,
    markersize=8,
    color="green",
)
axes[0, 0].set_title("ACTO 1: ¿Cómo creció la ambición?")
axes[0, 0].set_ylabel("Puntos Acumulados")
axes[0, 0].grid(True, alpha=0.3)
# ¿Cómo añadir drama visual?
for i, (mes, puntos) in enumerate(
    zip(temporada_datos["Mes"], temporada_datos["Puntos"])
):
    if i == len(temporada_datos["Mes"]) - 1:
        axes[0, 0].annotate(
            "¡DESPEGUE!",
            xy=(mes, puntos),
            xytext=(mes, puntos + 3),
            arrowprops=dict(arrowstyle="->", color="red"),
            fontweight="bold",
            color="red",
        )

# Acto 2: "El Equilibrio" - Goles a favor vs contra
axes[0, 1].bar(
    temporada_datos["Mes"],
    temporada_datos["Goles_Favor"],
    alpha=0.7,
    label="Goles a Favor",
    color="lightblue",
)
axes[0, 1].bar(
    temporada_datos["Mes"],
    [-x for x in temporada_datos["Goles_Contra"]],
    alpha=0.7,
    label="Goles en Contra",
    color="lightcoral",
)
axes[0, 1].set_title("ACTO 2: ¿Se logró el equilibrio perfecto?")
axes[0, 1].set_ylabel("Goles (+/-)")
axes[0, 1].legend()
axes[0, 1].axhline(y=0, color="black", linestyle="-", alpha=0.3)

# Acto 3: "La Conexión" - Correlación entre rendimiento y apoyo
axes[1, 0].scatter(
    temporada_datos["Puntos"],
    temporada_datos["Asistencia_Promedio"],
    s=150,
    alpha=0.7,
    color="purple",
)
axes[1, 0].set_xlabel("Puntos Acumulados")
axes[1, 0].set_ylabel("Asistencia Promedio")
axes[1, 0].set_title("ACTO 3: ¿El éxito atrae pasión?")
# ¿Cómo mostrar la relación de manera visual?
z = np.polyfit(temporada_datos["Puntos"], temporada_datos["Asistencia_Promedio"], 1)
p = np.poly1d(z)
axes[1, 0].plot(
    temporada_datos["Puntos"],
    p(temporada_datos["Puntos"]),
    "r--",
    alpha=0.8,
    linewidth=2,
)

# Acto 4: "El Clímax" - Efectividad ofensiva
efectividad = [
    gf / (gf + gc) * 100
    for gf, gc in zip(temporada_datos["Goles_Favor"], temporada_datos["Goles_Contra"])
]
axes[1, 1].fill_between(temporada_datos["Mes"], efectividad, alpha=0.6, color="gold")
axes[1, 1].plot(
    temporada_datos["Mes"],
    efectividad,
    marker="s",
    linewidth=2,
    markersize=6,
    color="orange",
)
axes[1, 1].set_title("ACTO 4: ¿Cuál fue el momento de máxima efectividad?")
axes[1, 1].set_ylabel("Efectividad Ofensiva (%)")
axes[1, 1].set_ylim(50, 80)

plt.tight_layout()
plt.show()

print("\nESTRUCTURA DE NARRATIVA VISUAL PROFESIONAL:")
print("✓ Acto 1: Establecer el progreso (línea temporal)")
print("✓ Acto 2: Mostrar el equilibrio (barras comparativas)")
print("✓ Acto 3: Revelar relaciones (correlación)")
print("✓ Acto 4: Culminar con el mensaje clave (área + tendencia)")

print(
    "\nPregunta estratégica: ¿Cómo esta secuencia visual cambiaría tu percepción del equipo?"
)
print("¿Qué acto te convenció más de la transformación?")

# %%
# ¿Cuáles son las herramientas que distinguen a un visualizador profesional?
# Vamos a crear un "kit de supervivencia" para presentaciones ejecutivas

print("KIT DE HERRAMIENTAS DEL VISUALIZADOR PROFESIONAL")
print("=" * 55)


# Herramienta 1: Configuración profesional estándar
def configurar_estilo_profesional():
    """¿Cómo lograr que todos tus gráficos tengan apariencia corporativa?"""
    plt.style.use("seaborn-v0_8")  # Estilo limpio y profesional
    plt.rcParams["figure.figsize"] = (12, 8)
    plt.rcParams["font.size"] = 11
    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.alpha"] = 0.3
    return "✓ Estilo profesional activado"


# Herramienta 2: Paleta de colores ejecutivos
colores_corporativos = {
    "azul_ejecutivo": "#1f77b4",
    "rojo_accion": "#d62728",
    "verde_crecimiento": "#2ca02c",
    "naranja_energia": "#ff7f0e",
    "morado_innovacion": "#9467bd",
}


# Herramienta 3: Template de dashboard multimétrico
def crear_dashboard_metricas(datos_principales):
    """¿Cómo crear un dashboard que muestre múltiples KPIs simultáneamente?"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)

    # KPI Principal (grande)
    ax_principal = fig.add_subplot(gs[0, :2])

    # Métricas secundarias (medianas)
    ax_metrica1 = fig.add_subplot(gs[0, 2])
    ax_metrica2 = fig.add_subplot(gs[0, 3])

    # Análisis detallado (parte inferior)
    ax_tendencia = fig.add_subplot(gs[1:, :2])
    ax_comparacion = fig.add_subplot(gs[1:, 2:])

    return fig, (ax_principal, ax_metrica1, ax_metrica2, ax_tendencia, ax_comparacion)


# Ejemplo de implementación
configurar_estilo_profesional()

# Datos para demostración
rendimiento_equipo = {
    "Partidos": list(range(1, 11)),
    "Efectividad": [65, 68, 72, 70, 75, 78, 80, 82, 85, 88],
    "Goles_Promedio": [1.5, 1.8, 2.1, 1.9, 2.3, 2.5, 2.7, 2.8, 3.0, 3.2],
    "Posesion": [52, 54, 58, 56, 60, 62, 65, 68, 70, 72],
}

fig, axes = crear_dashboard_metricas(rendimiento_equipo)

# KPI Principal: Evolución de efectividad
axes[0].plot(
    rendimiento_equipo["Partidos"],
    rendimiento_equipo["Efectividad"],
    linewidth=4,
    marker="o",
    markersize=8,
    color=colores_corporativos["azul_ejecutivo"],
)
axes[0].set_title("EFECTIVIDAD DEL EQUIPO", fontsize=14, fontweight="bold")
axes[0].set_ylabel("Porcentaje de Efectividad")

# Métrica 1: Promedio actual
efectividad_actual = rendimiento_equipo["Efectividad"][-1]
axes[1].text(
    0.5,
    0.5,
    f"{efectividad_actual}%",
    ha="center",
    va="center",
    fontsize=24,
    fontweight="bold",
    color=colores_corporativos["verde_crecimiento"],
    transform=axes[1].transAxes,
)
axes[1].set_title("EFECTIVIDAD\nACTUAL", ha="center")
axes[1].axis("off")

# Métrica 2: Tendencia
tendencia = rendimiento_equipo["Efectividad"][-1] - rendimiento_equipo["Efectividad"][0]
axes[2].text(
    0.5,
    0.5,
    f"+{tendencia}%",
    ha="center",
    va="center",
    fontsize=24,
    fontweight="bold",
    color=colores_corporativos["rojo_accion"],
    transform=axes[2].transAxes,
)
axes[2].set_title("MEJORA\nTOTAL", ha="center")
axes[2].axis("off")

# Análisis de tendencia detallado
axes[3].fill_between(
    rendimiento_equipo["Partidos"],
    rendimiento_equipo["Goles_Promedio"],
    alpha=0.6,
    color=colores_corporativos["naranja_energia"],
)
axes[3].plot(
    rendimiento_equipo["Partidos"],
    rendimiento_equipo["Goles_Promedio"],
    linewidth=2,
    marker="s",
    color=colores_corporativos["naranja_energia"],
)
axes[3].set_title("EVOLUCIÓN DE GOLES PROMEDIO")
axes[3].set_xlabel("Número de Partido")
axes[3].set_ylabel("Goles por Partido")

# Comparación multivariable
axes[4].scatter(
    rendimiento_equipo["Posesion"],
    rendimiento_equipo["Efectividad"],
    s=100,
    alpha=0.7,
    color=colores_corporativos["morado_innovacion"],
)
axes[4].set_xlabel("Posesión del Balón (%)")
axes[4].set_ylabel("Efectividad General (%)")
axes[4].set_title("POSESIÓN vs EFECTIVIDAD")

plt.suptitle(
    "DASHBOARD EJECUTIVO: ANÁLISIS INTEGRAL DE RENDIMIENTO",
    fontsize=16,
    fontweight="bold",
)
plt.show()

print("\nHERRAMIENTAS PROFESIONALES IMPLEMENTADAS:")
print("✓ Configuración estándar corporativa")
print("✓ Paleta de colores ejecutivos")
print("✓ Layout de dashboard multimétrico")
print("✓ KPIs destacados visualmente")
print("✓ Análisis integrado multivariable")

print(
    "\nPregunta de maestría: ¿Cómo este enfoque profesional cambiaría la recepción de tus análisis?"
)
print("¿Qué elementos visuales aumentan la credibilidad de la presentación?")

# %% [markdown]
# ---
#
# ## SÍNTESIS DE LA SESIÓN 3: ¿Qué hemos dominado sobre comunicación visual ejecutiva?
#
# **Reflexión final de 50 minutos**:
# - ¿Cómo los dashboards integrados superan presentaciones de gráficos individuales?
# - ¿Qué rol juega la narrativa visual en la toma de decisiones deportivas?
# - ¿Por qué la presentación profesional amplifica el impacto de tus análisis?
#
# ---
#
# # SÍNTESIS INTEGRADA: ¿Cómo has evolucionado como comunicador visual?
#
# ## Tu transformación: De observador a narrador visual experto
#
# **Pregunta de cierre**: ¿Qué diferencia percibes entre tu capacidad inicial de "leer gráficos" y tu nueva habilidad de "crear narrativas visuales convincentes"?
#
# ### Tu arsenal profesional desarrollado:
#
# #### Nivel 1: Fundamentos visuales dominados
# - **Seaborn como acelerador**: ¿Comprendes cómo esta herramienta transforma datos complejos en comunicación clara?
# - **Tipología de gráficos**: ¿Puedes seleccionar el formato visual óptimo según el mensaje que deseas transmitir?
# - **Estética profesional**: ¿Aprecias cómo la presentación visual afecta la credibilidad de tus análisis?
#
# #### Nivel 2: Técnicas avanzadas integradas
# - **Visualizaciones multidimensionales**: ¿Puedes combinar múltiples perspectivas en análisis integrados?
# - **Correlaciones reveladas**: ¿Dominas técnicas para hacer visibles relaciones ocultas en los datos?
# - **Narrativa temporal**: ¿Puedes mostrar evoluciones y tendencias de manera convincente?
#
# #### Nivel 3: Comunicación ejecutiva masterizada
# - **Dashboards estratégicos**: ¿Puedes crear presentaciones que influencien decisiones importantes?
# - **Narrativa visual progresiva**: ¿Estructuras tus análisis como historias que construyen convicción?
# - **Herramientas profesionales**: ¿Utilizas configuraciones y estándares de nivel corporativo?
#
# ### Reflexión sobre tu impacto potencial
#
# **En el contexto deportivo profesional**: ¿Cómo tus nuevas habilidades podrían influir en decisiones de fichajes, estrategias de juego, o análisis de rendimiento?
#
# **Tu contribución única**: ¿Qué valor especial aportas al combinar pasión deportiva con competencia técnica en visualización?
#
# ### Tu próximo horizonte
#
# **Pregunta anticipatoria**: Con estas herramientas de comunicación visual, ¿qué tipos de análisis deportivos más complejos te gustaría abordar?
#
# **Tu evolución continua**: ¿Cómo planeas integrar estos conocimientos con futuras técnicas de análisis avanzado?
#
# ---
#
# ## Logro desbloqueado: Comunicador Visual Deportivo Experto
#
# ¡Has desarrollado la capacidad de transformar análisis deportivos complejos en narrativas visuales que no solo informan sino que inspiran acción y cambio!
#
# **Tu nueva identidad profesional**: Analista deportivo que domina el arte de hacer que los datos "hablen" persuasivamente a cualquier audiencia.
#
# ---
#
# *"La diferencia entre información y comunicación es la diferencia entre datos aislados y historias que transforman decisiones."*

# %% [markdown]
# ## 7. Resumen de lo que Aprendimos
#
# ### 7.1 ¿Qué Aprendimos Hoy?
#
# **Los gráficos son mejores que las tablas** - Se ven los patrones más fácil  
# **Seaborn hace gráficos bonitos** - Con muy poco código  
# **Diferentes tipos de gráficos** - Barras, líneas, puntos, histogramas  
# **Analizar datos deportivos** - Comparar locales vs visitantes  
# **Contar historias con gráficos** - Como la remontada épica  
#
# ### 7.2 Tipos de Gráficos que Usamos
#
# **sns.barplot()** - Para comparar categorías  
# **plt.plot()** - Para líneas de tiempo  
# **sns.scatterplot()** - Para ver relaciones  
# **sns.histplot()** - Para ver distribuciones  
# **sns.boxplot()** - Para comparar grupos  
#
# ### 7.3 ¡Lo Más Importante!
#
# **Seaborn hace todo más fácil** - Un comando, un gráfico bonito  
# **Los gráficos cuentan historias** - Mejor que solo números  
# **El fútbol es perfecto para aprender** - Datos interesantes y fáciles de entender

# %%
# Plantilla simple para hacer tus propios gráficos
print("PLANTILLA PARA PRACTICAR")
print("=" * 30)

print("FÓRMULA MÁGICA PARA GRÁFICOS:")
print(
    """
1. Importar seaborn: import seaborn as sns
2. Configurar tema: sns.set_theme()
3. Hacer gráfico: sns.barplot(data=df, x='columna1', y='columna2')
4. Mostrar: plt.show()

¡Solo 4 pasos para gráficos profesionales!
"""
)

print("EJEMPLOS SÚPER FÁCILES:")
print(
    """
# Gráfico de barras
sns.barplot(data=df_partidos, x='Resultado', y='Total_Goles')

# Gráfico de puntos  
sns.scatterplot(data=df_partidos, x='Tiros_Local', y='Goles_Local')

# Histograma
sns.histplot(data=df_partidos, x='Total_Goles')

# Gráfico de caja
sns.boxplot(data=df_comparacion, x='Tipo', y='Goles')
"""
)

print("CONSEJOS PRO:")
print("Usa colores: palette='Set2'")
print("Cambia tamaño: figsize=(10, 6)")
print("Agrega títulos: plt.title('Mi Gráfico')")
print("Usa seaborn para todo: ¡Es más fácil!")

# Ejemplo rápido
plt.figure(figsize=(8, 5))
resultados_df = df_partidos["Resultado"].value_counts().reset_index()
sns.barplot(data=resultados_df, x="Resultado", y="count", palette="Set2")
plt.title("¿Quién Gana Más Partidos?", fontweight="bold")
plt.xlabel("Tipo de Resultado")
plt.ylabel("Cantidad de Partidos")
plt.show()

print("\n¡Ahora ya sabes hacer gráficos profesionales con seaborn!")

# %% [markdown]
# ---
#
# ## Reflexiones sobre tu evolución como visualizador de datos deportivos
#
# ### Autoevaluación: ¿Cómo transformaste tu relación con la información deportiva?
#
# **Pregunta de síntesis**: ¿Qué diferencia encuentras entre "tener datos" y "comunicar insights" efectivamente?
#
# #### Tu nueva identidad como comunicador visual
#
# **Traducción instantánea**: ¿Comprendes cómo convertir números complejos en narrativas visuales claras?
#
# **Investigación multidimensional**: ¿Puedes usar múltiples tipos de gráficos para examinar un problema desde diferentes ángulos?
#
# **Comunicación persuasiva**: ¿Entiendes cómo la elección del gráfico afecta la interpretación del mensaje?
#
# **Eficiencia profesional**: ¿Aprecias el poder de herramientas como Seaborn para crear visualizaciones de nivel profesional?
#
# ### Reflexión metodológica: ¿Qué aprendiste sobre el proceso de investigación visual?
#
# **Tu experiencia**: ¿Qué fue más revelador: crear los gráficos o interpretar lo que revelan?
#
# #### Insights sobre herramientas y técnicas:
# - **Seaborn**: ¿Tu acelerador de productividad visual?
# - **Múltiples perspectivas**: ¿El valor de examinar datos desde diferentes ángulos gráficos?
# - **Estética profesional**: ¿Cómo la presentación visual afecta la credibilidad de tus análisis?
#
# ### Conexiones con el análisis deportivo profesional
#
# **Pregunta integradora**: ¿Cómo crees que las visualizaciones que aprendiste a crear se comparan con las que ves en medios deportivos profesionales?
#
# **Tu perspectiva evolucionada**: ¿Puedes ahora "decodificar" las intenciones detrás de los gráficos que ves en televisión deportiva?
#
# ### Preparación para comunicación avanzada
#
# **Anticipación**: ¿Qué tipos de historias deportivas más complejas te gustaría contar con visualizaciones?
#
# **Tu próximo nivel**: ¿Cómo combinarías múltiples datasets para crear narrativas visuales más ricas?
#
# ### Tu arsenal de comunicación visual
#
# ```python
# # Tu fórmula del éxito:
# import seaborn as sns
# sns.set_theme()
#
# # Tu kit de herramientas narrativas:
# sns.barplot(...)      # Para comparaciones decisivas
# sns.lineplot(...)     # Para revelar tendencias temporales  
# sns.scatterplot(...)  # Para descubrir relaciones ocultas
# sns.boxplot(...)      # Para análisis de distribuciones
# ```
#
# ### Logro desbloqueado
#
# ¡Ya puedes transformar análisis deportivos en comunicación visual impactante y crear presentaciones que no solo informan sino que inspiran acción!
#
# **Tu transformación**: De consumidor pasivo de gráficos deportivos a creador activo de narrativas visuales persuasivas.
#
# ---
#
# *Has desarrollado la capacidad de hacer que los datos deportivos "hablen" visualmente, una habilidad esencial en el mundo moderno del análisis deportivo.*

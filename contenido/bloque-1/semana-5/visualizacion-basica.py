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
# # Semana 5: ¿Cómo convierten los datos en historias visuales los medios deportivos?
#
# ## Enfoque semanal (3 sesiones de 50 min)
# - **Sesión 1 (Fundamentos)**: Gráficos básicos (barras, líneas, dispersión) para comunicar comparaciones, evolución y relaciones.
# - **Sesión 2 (Profundización)**: Subgráficos simples (2x2) y personalización básica (colores, títulos, etiquetas legibles).
# - **Sesión 3 (Integración)**: Combinar 2–3 gráficos adecuados para responder una pequeña pregunta analítica de fútbol.
#
# Cada sesión sigue: Pregunta guía → Micro‑teoría → Ejemplos → Breve reflexión.
#
# ---
#
# ### Pregunta central de la semana
# **¿Por qué los comentaristas deportivos usan gráficos en lugar de solo mencionar números durante las transmisiones?**
#
# ### Descubrimiento esperado
# - Patrones visibles rápido
# - Tendencias simples
# - Claridad para audiencias no técnicas
#
# ### Conexión personal
# Piensa en el último gráfico futbolístico que viste en una transmisión: ¿qué entendiste de inmediato que habría sido más lento leer en una tabla?
#
# ---

# %% [markdown]
# # SESIÓN 1 (50 min): Fundamentos de visualización
#
# Pregunta guía: ¿Por qué un gráfico comunica más rápido que una lista de números?
#
# Objetivo: Reconocer cuándo usar barras (comparar), líneas (evolución) y dispersión (relación simple).
#
# Micro‑teoría breve:
# - El ojo detecta alturas, pendientes y agrupamientos más rápido que leer cifras.
# - Un gráfico = una pregunta clara. Cualquier elemento que no responde la pregunta estorba.
#
# Conceptos clave:
# 1. Barras: comparar categorías (goles por equipo).
# 2. Línea: ver cambio a lo largo del tiempo (puntos por jornada).
# 3. Dispersión: explorar si dos variables se mueven juntas (goles vs puntos).
#
# Secuencia práctica:
# - Importar librerías.
# - Gráfico de barras simple.
# - Gráfico de línea de evolución.
# - Dispersión para relación.
#
# Reflexiona tras cada salida: ¿Qué aprendí más rápido que leyendo números?
#
# ---

# %% [markdown]
# # Primer contacto práctico
#
# A continuación comenzarás a crear tus primeras visualizaciones básicas paso a paso. Observa cómo un gráfico comunica más rápido que una lista de números y reflexiona después de cada salida.
#
# (El código de importación y configuración está en la primera celda de código para evitar confusiones.)

# %% [markdown]
# ## Gráficos de Líneas: Mostrando Evolución en el Tiempo
#
# **Pregunta clave**: ¿Cómo mostrarías el progreso de un equipo a lo largo de una temporada?
#
# Los gráficos de líneas son perfectos para mostrar **cambios a través del tiempo**.

# %%
# Importaciones básicas para toda la semana
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set_theme()
print("Librerías cargadas (matplotlib, seaborn, numpy, pandas)")

# %%
# BARRAS: comparación simple (Sesión 1)
equipos_basicos = ["Barcelona", "Real Madrid", "Valencia"]
goles_basicos = [25, 20, 15]

sns.barplot(x=equipos_basicos, y=goles_basicos)
plt.title("Goles por Equipo (Comparación)")
plt.ylabel("Goles")
plt.show()

print("Reflexión: ¿Qué ves en 1 segundo que tardarías más leyendo números?")

# %%
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
plt.plot(
    jornadas,
    real_madrid,
    marker="o",
    linewidth=2.5,
    label="Real Madrid",
    color="purple",
)
plt.plot(
    jornadas, barcelona, marker="s", linewidth=2.5, label="Barcelona", color="blue"
)
plt.plot(
    jornadas, atletico, marker="^", linewidth=2.5, label="Atletico Madrid", color="red"
)

# Personalizando el gráfico
plt.title("Evolución de Puntos por Jornada - La Liga", fontsize=16, fontweight="bold")
plt.xlabel("Jornada", fontsize=12)
plt.ylabel("Puntos Acumulados", fontsize=12)

# Añadiendo cuadrícula para mejor lectura
plt.grid(True, alpha=0.3, linestyle="--")

# Leyenda para identificar equipos
plt.legend(fontsize=11)

# Resaltando la posición actual
plt.axhline(y=40, color="gold", linestyle=":", alpha=0.7, label="Línea de Liderato")

plt.tight_layout()
plt.show()

print("=== INSIGHTS VISUALES ===")
print("¿Qué patrones puedes identificar que serían invisibles en una tabla?")
print("• ¿En qué jornada se separó más el Real Madrid?")
print("• ¿Cuándo tuvo Barcelona su peor racha?")
print("• ¿El Atletico mantuvo un crecimiento constante?")
print("• ¿En qué momento la competencia fue más cerrada?")

# %% [markdown]
# ## Gráficos de Dispersión: Descubriendo Relaciones
#
# **Pregunta analítica**: ¿Existe relación entre los goles anotados por un equipo y los puntos que obtiene?
#
# Los gráficos de dispersión nos ayudan a **visualizar correlaciones** entre dos variables.

# %%
# ===============================
# GRÁFICO DE DISPERSIÓN: Goles vs Puntos (Versión Básica)
# ===============================

# Datos de equipos de La Liga (simulados pero realistas)
equipos = ["Real Madrid", "Barcelona", "Atletico", "Sevilla", "Valencia"]

goles_favor = [68, 70, 55, 48, 42]
puntos_obtenidos = [78, 76, 66, 58, 53]

plt.figure(figsize=(8, 6))

# Gráfico de dispersión simple
plt.scatter(
    goles_favor,
    puntos_obtenidos,
    s=120,
    alpha=0.7,
    color="steelblue",
    edgecolors="black",
)

# Etiquetar solo equipos destacados (menos carga visual)
for i, equipo in enumerate(equipos):
    plt.annotate(
        equipo,
        (goles_favor[i], puntos_obtenidos[i]),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=9,
    )

plt.title("Relación Goles Anotados vs Puntos Obtenidos")
plt.xlabel("Goles Anotados")
plt.ylabel("Puntos Obtenidos")
plt.grid(alpha=0.3, linestyle="--")
plt.tight_layout()
plt.show()

print("Observa: cuando los goles aumentan, los puntos también parecen aumentar.")
print("Reflexión: ¿Siempre más goles significan más puntos o hay excepciones?")
print("Pregunta: ¿Qué otro factor podría influir (defensa, posesión, disciplina)?")

# %% [markdown]
# # SESIÓN 2 (50 min): Panel 2x2 y personalización mínima
#
# Repaso rápido: barras (comparar), línea (evolución), dispersión (relación).
#
# Objetivo: Combinar vistas distintas en un panel 2x2 y aplicar ajustes mínimos de legibilidad.
#
# Preguntas mientras observas el panel:
# - ¿Cada panel aporta un ángulo distinto?
# - ¿Cuál eliminarías si tuvieras solo 3?
# - ¿Título general que describa todo?
#
# ---

# %%
# ===============================
# SUBGRÁFICOS BÁSICOS (Versión Simplificada 2x2)
# ===============================

# Datos simples
equipos = ["Real Madrid", "Barcelona", "Atletico", "Sevilla", "Valencia"]
goles_favor = [68, 70, 55, 48, 42]
goles_contra = [32, 35, 40, 45, 50]
puntos = [78, 76, 66, 58, 53]
posesion = [58, 64, 52, 55, 49]

fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle("Panel Básico de Rendimiento (2x2)", fontsize=16, fontweight="bold")

# 1. Barras: Goles a Favor
axes[0, 0].bar(equipos, goles_favor, color="skyblue")
axes[0, 0].set_title("Goles a Favor")
axes[0, 0].set_ylabel("Goles")
axes[0, 0].tick_params(axis="x", rotation=45)

# 2. Barras: Goles en Contra
axes[0, 1].bar(equipos, goles_contra, color="salmon")
axes[0, 1].set_title("Goles en Contra")
axes[0, 1].tick_params(axis="x", rotation=45)

# 3. Línea: Evolución simple (simulada)
jornadas = list(range(1, 11))
barcelona = [3, 6, 9, 12, 15, 18, 20, 22, 25, 27]
axes[1, 0].plot(jornadas, barcelona, marker="o", color="navy")
axes[1, 0].set_title("Puntos Barcelona (10 Jornadas)")
axes[1, 0].set_xlabel("Jornada")
axes[1, 0].set_ylabel("Puntos")
axes[1, 0].grid(alpha=0.3)

# 4. Dispersión: Posesión vs Puntos (simple)
axes[1, 1].scatter(posesion, puntos, color="green", s=100, edgecolors="black")
axes[1, 1].set_title("Posesión vs Puntos")
axes[1, 1].set_xlabel("Posesión (%)")
axes[1, 1].set_ylabel("Puntos")
axes[1, 1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

print("Reflexión panel:")
print("1. ¿Qué equipo destaca en ataque?")
print("2. ¿Quién necesita mejorar defensa?")
print("3. ¿La evolución de puntos es estable?")
print("4. ¿Más posesión parece asociarse a más puntos?")

# %% [markdown]
# ## Personalización mínima
#
# Pregunta: ¿Qué pequeño ajuste mejora la lectura (título, rotación, etiqueta)?
#
# Objetivo: hacer el gráfico legible sin adornos innecesarios.
#
# ---

# %%
# ===============================
# PERSONALIZACIÓN BÁSICA (Colores y Etiquetas)
# ===============================

plt.style.use("default")  # Estilo simple

jugadores = ["Messi", "Mbappé", "Haaland", "Benzema", "Lewandowski"]
goles = [30, 29, 36, 24, 33]

plt.figure(figsize=(8, 5))
plt.bar(jugadores, goles, color="steelblue", edgecolor="black")
plt.title("Goles por Jugador (Ejemplo)")
plt.ylabel("Goles")
plt.xticks(rotation=30)

for i, v in enumerate(goles):
    plt.text(i, v + 0.5, v, ha="center", fontweight="bold")

plt.tight_layout()
plt.show()

print("Elementos de personalización básicos usados:")
print("- Color uniforme sencillo")
print("- Etiquetas numéricas sobre barras")
print("- Rotación leve para legibilidad")
print(
    "Reflexión: ¿Qué otro cambio simple mejoraría claridad (ordenar, cambiar color, agrupar)?"
)

# %% [markdown]
# # SESIÓN 3 (50 min): Integrar y sintetizar
#
# Pregunta guía: ¿Cuál combinación mínima responde tu pregunta?
#
# Recordatorio rápido:
# - Barras = comparación
# - Línea = evolución
# - Dispersión = relación
#
# Pasos sugeridos:
# 1. Formula una pregunta concreta (ej: ¿Ha mejorado el equipo A respecto a B?).
# 2. Elige el tipo que mejor responde (1 a 3 gráficos máximo).
# 3. Verifica que cada gráfico aporte algo distinto.
#
# Preguntas rápidas:
# - ¿Mi pregunta inicial sigue clara?
# - ¿Algún gráfico sobra?
# - ¿Puedo explicar cada gráfico en 1 frase?
#
# Síntesis (al final de la sesión): escribe 2 frases:
# - Hallazgo principal.
# - Gráfico que más ayudó y por qué.
#
# ---

# %%
# Ejemplo integrado (Sesión 3)
# Pregunta: ¿El equipo con más goles también lidera en posesión y puntos?

equipos = ["Real Madrid", "Barcelona", "Atletico", "Sevilla", "Valencia"]
goles_favor = [68, 70, 55, 48, 42]
posesion = [58, 64, 52, 55, 49]
puntos = [78, 76, 66, 58, 53]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Barras: goles
axes[0].bar(equipos, goles_favor, color="steelblue")
axes[0].set_title("Goles a Favor")
axes[0].tick_params(axis="x", rotation=35)

# Dispersión: posesión vs puntos
axes[1].scatter(posesion, puntos, s=100, color="darkgreen", edgecolors="black")
for i, e in enumerate(equipos):
    axes[1].annotate(
        e,
        (posesion[i], puntos[i]),
        xytext=(4, 4),
        textcoords="offset points",
        fontsize=8,
    )
axes[1].set_title("Posesión vs Puntos")
axes[1].set_xlabel("Posesión (%)")
axes[1].set_ylabel("Puntos")
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

print("Síntesis guiada:")
print("1. Hallazgo principal (1 frase): ...")
print("2. Gráfico más útil y por qué: ...")
print("3. ¿Algún gráfico sobrante? ...")

# %%
# ¿Cómo crees que Python convertirá estos números en un gráfico visual?
# Experimenta y observa la magia:

# Nuestros datos: ¿Puedes predecir qué equipo tendrá la barra más alta?
equipos = ["Barcelona", "Madrid", "Valencia"]
goles = [25, 20, 15]

# La línea mágica: ¿Qué crees que hace sns.barplot()?
sns.barplot(x=equipos, y=goles)

# ¿Qué diferencia crees que hace agregar un título?
plt.title("Goles por Equipo")

# El momento de la revelación:
plt.show()

print("¡Acabas de crear tu primer insight visual!")
print("Pregunta de reflexión: ¿Qué información captas instantáneamente del gráfico")
print("que sería más difícil de ver solo con los números?")

# Tu turno: ¿Qué preguntas puedes responder mirando este gráfico?

# %%
# ¿Cómo crees que Python "conectará" estos puntos para contar una historia?
# Observa la narrativa visual que se revela:

# Los datos: ¿Puedes predecir si Barcelona está mejorando o empeorando?
meses = ["Enero", "Febrero", "Marzo", "Abril"]
goles_barcelona = [5, 8, 6, 10]

# La magia de las conexiones: ¿Qué historia crees que revelará la línea?
sns.lineplot(x=meses, y=goles_barcelona, marker="o", linewidth=3, markersize=10)

plt.title("Goles de Barcelona por Mes")
plt.xlabel("Mes")
plt.ylabel("Goles")

plt.show()

print("¡Observa cómo la línea cuenta una historia!")
print("Pregunta de análisis: ¿Qué patrón ves en el rendimiento de Barcelona?")
print("¿Hay una tendencia general hacia arriba o hacia abajo?")
print("¿En qué mes tuvieron el peor rendimiento? ¿Y el mejor?")

# Reflexión: ¿Qué insights obtienes de la línea que no verías en una tabla de números?

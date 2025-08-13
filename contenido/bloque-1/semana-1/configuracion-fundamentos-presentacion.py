# ---
# marp: true
# theme: default
# paginate: true
# ---

# %% [markdown]
#

# %% [markdown]
# # Semana 1: ¿Cómo empieza el análisis de datos en el fútbol?
#
# **Programación Básica 1 – Prepa Tec**
#
# ---
#
# # SESIÓN 1: ¿Cómo le explico a la computadora lo que sé de fútbol? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Cómo le dirías a una computadora quién es tu jugador favorito y cuántos goles lleva?
#
# ---
#
# ## Teoría: ¿Qué es una variable en fútbol?
#
# Imagina que eres el director deportivo y necesitas registrar información básica de tus jugadores: nombre, edad, goles, altura, ¿está activo?
#
# ---
#
# ## Pregunta reflexiva
#
# ¿Por qué no basta con solo recordar los datos en tu cabeza?
#
# ---
#
# ## Práctica: Primer código en Python

# %%
jugador = "Lionel Messi"
edad = 37
goles = 10
altura = 1.70
es_activo = True
print(f"Nombre: {jugador}, Edad: {edad}, Goles: {goles}, Altura: {altura}, ¿Activo?: {es_activo}")

# %% [markdown]
# ---
#
# ## Tipos de datos en fútbol
#
# - **Texto**: nombres, equipos ("Barcelona")
# - **Números enteros**: goles, edad (10, 37)
# - **Números decimales**: altura (1.70)
# - **Booleanos**: ¿Está activo? (True/False)
#
# ---
#
# ## Práctica: Operaciones básicas
#
# ¿Cómo sumarías los goles que le faltan a Messi para llegar a 15?
#
# ---

# %%
goles_objetivo = 15
goles_faltantes = goles_objetivo - goles
altura_cm = altura * 100

# %% [markdown]
# ---
#
# ## Síntesis de la sesión 1
#
# - ¿Por qué es importante distinguir entre tipos de datos?
# - ¿Qué errores podrías cometer si mezclas texto y números?
# - ¿Cómo ayuda la computadora a organizar la información del equipo?
#
# ---
#
# # SESIÓN 2: ¿Cómo toma decisiones un entrenador usando datos? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Cómo decide un DT si un jugador debe ser titular o suplente?
#
# ---
#
# ## Teoría: Comparaciones y decisiones automáticas
#
# Los entrenadores comparan estadísticas para tomar decisiones. ¿Podemos enseñar a la computadora a comparar y decidir?
#
# ---
#
# ## Pregunta reflexiva
#
# ¿Qué datos compararías para decidir si un jugador es veterano o está en forma?
#
# ---
#
# ## Práctica: Comparaciones en Python

# %%
es_veterano = edad > 30
en_forma = goles > 8
partidos_jugados = 25
es_titular = partidos_jugados > 20

# %% [markdown]
# ---
#
# ## Práctica: Decisiones automáticas con if/elif/else
#
# ¿Cómo automatizarías la decisión de si un jugador es apto para alto rendimiento?
#
# ---

# %%
if edad < 35:
    print("Edad apropiada para alto rendimiento")
else:
    print("Jugador veterano - requiere evaluación especial")

# %% [markdown]
# ---
#
# ## Práctica: Asistente técnico automático
#
# ¿Cómo decidirías si un jugador debe ser convocado según edad, goles y altura?
#
# ---
#
# ## Síntesis de la sesión 2
#
# - ¿Qué significa que el resultado de una comparación sea True o False?
# - ¿Cómo ayuda la indentación a Python?
# - ¿Cómo automatizamos decisiones simples como un entrenador?
#
# ---
#
# # SESIÓN 3: ¿Cómo organiza un club profesional la información de su plantilla? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Cómo gestiona el Barcelona la información de sus 25 jugadores?
#
# ---
#
# ## Teoría: Listas y diccionarios en Python
#
# ¿Prefieres 25 variables separadas o una forma más inteligente de organizar la plantilla?
#
# ---
#
# ## Pregunta reflexiva
#
# ¿Por qué los índices de las listas empiezan en 0?
#
# ---
#
# ## Práctica: Listas en Python

# %%
jugadores_convocados = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Kylian Mbappé",
    "Erling Haaland",
    "Vinicius Jr"
]

# %% [markdown]
# ---
#
# ## Práctica: Diccionarios en Python

# %%
estadisticas_messi = {
    "nombre": "Lionel Messi",
    "edad": 37,
    "goles_temporada": 10,
    "asistencias": 8
}

# %% [markdown]
# ---
#
# ## Práctica: Mini sistema de gestión deportiva
#
# Combina listas, diccionarios y decisiones automáticas para clasificar jugadores según goles y edad.
#
# ---
#
# ## Ejemplo: Análisis de plantilla

# %%
plantilla_completa = [
    {"nombre": "Lionel Messi", "goles": 10, "edad": 37},
    {"nombre": "Cristiano Ronaldo", "goles": 12, "edad": 39},
    {"nombre": "Kylian Mbappé", "goles": 15, "edad": 25},
    {"nombre": "Erling Haaland", "goles": 18, "edad": 24}
]
for jugador in plantilla_completa:
    if jugador["goles"] >= 15:
        print(f"{jugador['nombre']}: ESTRELLA GOLEADORA")

# %% [markdown]
# ---
#
# ## Síntesis de la sesión 3
#
# - ¿Qué ventajas tiene organizar la información en listas y diccionarios?
# - ¿Cómo automatizarías el análisis de una plantilla completa?
# - ¿En qué otras áreas podrías usar este pensamiento lógico?
#
# ---
#
# # Preguntas para tu autoevaluación
#
# - ¿Qué fue lo más claro y lo más desafiante?
# - ¿Cómo aplicarías estos patrones fuera del fútbol?
# - ¿Qué te gustaría automatizar en tu vida diaria usando lógica similar?
#
# ---
#
# # Próxima semana
#
# - Estructuras de control más avanzadas
# - Bucles para analizar temporadas completas
# - Funciones para automatizar análisis
#
# **¿Listo para el siguiente nivel?**

# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: .venv (3.10.12)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Semana 3: ¿Cómo construyen los estrategas sistemas elegantes y reutilizables?
#
# ## ¿Te has preguntado cómo los entrenadores desarrollan un "manual de jugadas" que funciona en cualquier situación?
#
# **Pregunta central de la semana**: ¿Qué diferencia a un técnico principiante que improvisa cada situación, de un estratega maestro que tiene sistemas organizados para cualquier escenario?
#
# ### ¿Por qué los grandes entrenadores son tan efectivos?
#
# **Descubrimiento sorprendente**: Los entrenadores de élite no solo conocen muchas jugadas... tienen **sistemas organizados** que pueden:
# - Adaptarse a cualquier oponente
# - Reutilizarse en diferentes situaciones  
# - Combinarse para crear estrategias complejas
# - Transmitirse eficientemente a todo el cuerpo técnico
#
# **Conexión reveladora**: Los programadores profesionales trabajan exactamente igual. Esta semana descubrirás cómo crear tu propio "manual de jugadas programadas" usando funciones y módulos.
#
# ---
#
# ## Estructura del descubrimiento (3 sesiones × 50 minutos)
#
# ### SESIÓN 1: ¿Cómo crear "jugadas programadas" reutilizables? (50 min)
# **Pregunta guía**: ¿Por qué repetir código es como improvisar la misma jugada una y otra vez?
# - Funciones básicas: tus primeras "jugadas maestras"
# - Parámetros: adaptando jugadas a diferentes situaciones
# - Valores de retorno: obtener resultados útiles de tus estrategias
#
# ### SESIÓN 2: ¿Cómo organizan los técnicos de élite sus sistemas? (50 min)  
# **Pregunta guía**: ¿Cómo pasamos de jugadas individuales a manuales completos de estrategias?
# - Módulos: crear tu biblioteca personal de herramientas
# - Importaciones: acceder a sistemas creados por otros expertos
# - Organización de código: estructura como los grandes clubes
#
# ### SESIÓN 3: ¿Podrías crear un sistema de análisis como los usan los equipos profesionales? (50 min)
# **Pregunta guía**: ¿Cómo integramos todo en un sistema coherente y poderoso?
# - Proyecto integrador: Sistema completo de análisis de equipos
# - Integración de conceptos: desde variables hasta sistemas complejos
# - Reflexión sobre la evolución de tu pensamiento estratégico
#
# ---
#
# ### ¿Qué descubriremos esta semana?
#
# Al final de estos 150 minutos, habrás desarrollado la mentalidad de un **arquitecto de sistemas**, capaz de:
# - Diseñar soluciones elegantes y reutilizables como un entrenador de élite
# - Organizar código complejo de manera profesional y mantenible
# - Crear herramientas que otros puedan usar y entender
# - Construir sistemas integrados para análisis deportivo real
#
# **Pregunta motivadora**: ¿Estás listo para pensar como los grandes estrategas del fútbol moderno?

# %% [markdown]
# # SESIÓN 1: ¿Cómo crear "jugadas programadas" reutilizables? (50 minutos)
#
# ## ¿Alguna vez te has preguntado por qué los entrenadores practican la misma jugada cientos de veces?
#
# **Escenario reflexivo**: Imagínate en el banquillo del Real Madrid. Es el minuto 89 de la final de la Champions League, empate 1-1, y tienes un tiro libre a 25 metros del arco...
#
# **Pregunta crítica**: ¿Prefieres que Kroos improvise completamente, o que ejecute una jugada que ha perfeccionado miles de veces?
#
# ### ¿Qué hace especiales a las "jugadas maestras"?
#
# **Reflexiona antes de continuar**:
# - ¿Por qué los tiros libres de Messi siempre parecen tan precisos?
# - ¿Cómo logra el Barcelona que sus jugadas de corner sean tan efectivas?
# - ¿Qué permite que un equipo ejecute la misma estrategia contra diferentes oponentes?
#
# **Descubrimiento fundamental**: Las mejores jugadas tienen algo en común...
#
# ### Características de las jugadas de élite:
#
# 1. **Reproducibles**: Se pueden ejecutar múltiples veces con el mismo resultado
# 2. **Adaptables**: Funcionan contra diferentes oponentes modificando pequeños detalles
# 3. **Eficientes**: Logran el máximo resultado con el mínimo esfuerzo
# 4. **Transmisibles**: Otros jugadores pueden aprenderlas y ejecutarlas
# 5. **Combinables**: Se pueden conectar con otras jugadas para crear estrategias complejas
#
# **Revelación sorprendente**: En programación, las **funciones** funcionan exactamente igual que las jugadas maestras del fútbol.
#
# ---
#
# ## ¿Qué son las funciones en programación?
#
# **Analogía reveladora**: Si las variables son como los jugadores individuales, las funciones son como las jugadas ensayadas completas.
#
# **Pregunta de conexión**: Cuando Guardiola grita "¡Jugada 7!" desde la banda, ¿qué está pasando realmente?
#
# ### Anatomía de una jugada maestra vs. una función:
#
# | Jugada de Fútbol | Función de Programación |
# |------------------|-------------------------|
# | Nombre de la jugada | Nombre de la función |
# | Posiciones iniciales | Parámetros de entrada |
# | Secuencia de movimientos | Código interno |
# | Resultado esperado | Valor de retorno |
# | Manual táctico | Documentación |
#
# **Momento de descubrimiento**: ¿Te das cuenta? ¡Ya entiendes qué son las funciones antes de escribir una sola línea de código!
#
# ---
#
# ## ¿Cómo "programamos" nuestra primera jugada maestra?

# %% [markdown]
# ## ¿Cómo diseñamos una "jugada maestra" en código?
#
# **Pregunta guía**: Si fueras a crear el manual táctico del Barcelona, ¿qué información incluirías para cada jugada?
#
# ### Piénsalo paso a paso:
#
# 1. **¿Qué nombre le darías a la jugada?** (Debe ser claro y descriptivo)
# 2. **¿Qué información necesita el equipo antes de ejecutarla?** (Posiciones, timing, etc.)
# 3. **¿Cuáles son los pasos específicos a seguir?** (La ejecución)
# 4. **¿Qué resultado esperas obtener?** (Gol, posesión, ventaja posicional)
#
# **Revelación**: La estructura de una función sigue exactamente este mismo patrón.
#
# ---
#
# ### Estructura de una "jugada programada":
#
# ```python
# def nombre_de_la_jugada(informacion_necesaria):
#     """¿Para qué sirve esta jugada y cuándo usarla?"""
#     # Pasos específicos de ejecución
#     # Cálculos y operaciones necesarias
#     return resultado_obtenido
# ```
#
# **Desglose de cada elemento**:
#
# #### 1. `def nombre_de_la_jugada`:
# **Analogía**: Como nombrar "Tiki-taka", "Contra-ataque rápido", "Presión alta"
# - Debe ser descriptivo y claro
# - En español para nuestro proyecto
# - Sin espacios (usa guiones bajos: `calcular_promedio_goles`)
#
# #### 2. `(informacion_necesaria)`:
# **Analogía**: Los datos que necesita el entrenador antes de dar la orden
# - ¿Cuántos jugadores? ¿En qué posición? ¿Qué minuto es?
# - En programación: ¿qué datos necesitamos para hacer el cálculo?
#
# #### 3. `"""Documentación"""`:
# **Analogía**: Las instrucciones en el manual táctico
# - Explica cuándo y cómo usar la jugada
# - Fundamental para que otros entiendan tu estrategia
#
# #### 4. `# Código de ejecución`:
# **Analogía**: Los movimientos específicos que hacen los jugadores
# - Las operaciones matemáticas y lógicas
# - El "trabajo interno" de la jugada
#
# #### 5. `return resultado_obtenido`:
# **Analogía**: Lo que logra la jugada (gol, posesión, ventaja)
# - El valor útil que devuelve la función
# - Lo que podremos usar después en otras partes del análisis
#
# **Pregunta de reflexión**: ¿Ya visualizas cómo una función es realmente una "jugada maestra" que puedes usar una y otra vez?

# %%
# NUESTRA PRIMERA JUGADA MAESTRA: Análisis de efectividad goleadora

# ¿Cómo sabemos si un delantero está rindiendo bien?
# Pregunta reflexiva: ¿Es mejor un jugador que mete 20 goles en 20 partidos
# o uno que mete 25 goles en 40 partidos?

# ¡Necesitamos una "jugada programada" que calcule esto automáticamente!


def calcular_promedio_goles(goles_totales, partidos_jugados):
    """
    JUGADA MAESTRA: Evaluación de efectividad goleadora

    ¿Cuándo usar esta jugada?
    - Para comparar el rendimiento de diferentes delanteros
    - Para evaluar la evolución de un jugador a lo largo de la temporada
    - Para tomar decisiones de fichajes basadas en datos

    Información necesaria:
    goles_totales: número total de goles anotados por el jugador
    partidos_jugados: número total de partidos disputados

    Resultado que obtenemos:
    promedio de goles por partido (float)
    """
    # ¿Qué pasa si un jugador no ha jugado ningún partido?
    # ¡Hay que prevenir la división por cero como un buen entrenador prevé lesiones!
    if partidos_jugados == 0:
        return 0  # Sin partidos = sin promedio calculable

    # El cálculo fundamental: ¡la esencia de la jugada!
    promedio = goles_totales / partidos_jugados
    return promedio


# ¡MOMENTO DE PRUEBA! Usemos nuestra jugada con datos reales

print("=== LABORATORIO DE ANÁLISIS GOLEADOR ===")
print("¿Cómo se comparan los grandes delanteros actuales?")
print()

# Datos reales de la temporada 2023-24
# ¿Puedes predecir quién tendrá mejor promedio antes de ejecutar el código?

# Erling Haaland (Manchester City)
haaland_goles = 36
haaland_partidos = 35

# Kylian Mbappé (PSG)
mbappe_goles = 29
mbappe_partidos = 29

# Harry Kane (Bayern Munich)
kane_goles = 32
kane_partidos = 31

# ¡Ejecutamos nuestra jugada maestra con cada delantero!
promedio_haaland = calcular_promedio_goles(haaland_goles, haaland_partidos)
promedio_mbappe = calcular_promedio_goles(mbappe_goles, mbappe_partidos)
promedio_kane = calcular_promedio_goles(kane_goles, kane_partidos)

# Presentamos los resultados como un analista profesional
print(f"Haaland: {haaland_goles} goles en {haaland_partidos} partidos")
print(f"Promedio: {promedio_haaland:.3f} goles por partido")
print()

print(f"Mbappé: {mbappe_goles} goles en {mbappe_partidos} partidos")
print(f"Promedio: {promedio_mbappe:.3f} goles por partido")
print()

print(f"Kane: {kane_goles} goles en {kane_partidos} partidos")
print(f"Promedio: {promedio_kane:.3f} goles por partido")
print()

# ¿Cuál es el resultado más sorprendente?
print("=== REFLEXIÓN ANALÍTICA ===")
print("¿Qué patrones observas en estos datos?")
print("¿Qué nos dice esto sobre la consistencia vs. el volumen total?")

# %% [markdown]
# ### ¡Tu turno de crear una jugada maestra!
#
# **Momento de aplicación práctica**: Acabas de ver cómo analizamos delanteros, pero ¿qué pasa con los porteros?
#
# **Escenario desafío**: Eres el nuevo director deportivo del Real Madrid y necesitas decidir entre tres porteros para la próxima temporada. Los delanteros se evalúan por goles, pero **¿cómo evaluamos objetivamente a un portero?**
#
# #### Pregunta de reflexión crítica:
# ¿Qué es más importante: un portero que recibe pocos tiros pero falla algunos, o uno que recibe muchos tiros pero para la mayoría?
#
# ### Desafío de diseño estratégico:
#
# **Tu misión**: Crear una "jugada maestra" que calcule la efectividad de cualquier portero.
#
# **Antes de programar, piensa como un estratega**:
#
# 1. **¿Qué información necesitas para evaluar a un portero?**
#    - Pista: ¿Cuántos tiros enfrentó? ¿Cuántos goles recibió?
#
# 2. **¿Cuál sería la fórmula matemática ideal?**
#    - Reflexiona: ¿El porcentaje de tiros detenidos o el de goles recibidos?
#
# 3. **¿Qué casos especiales debes considerar?**
#    - ¿Qué pasa si un portero no enfrentó ningún tiro? (¡División por cero!)
#
# 4. **¿Cómo presentarías el resultado?**
#    - ¿Como decimal, porcentaje, o clasificación?
#
# **Tiempo de reflexión**: 3-5 minutos antes de ver el código
#
# **Pregunta guía**: ¿Ya tienes clara tu estrategia? ¡Hora de programar tu jugada maestra!

# %%
# DESAFÍO: Tu primera jugada maestra personalizada

# ¿Ya reflexionaste sobre la estrategia? ¡Hora de construir!


def calcular_efectividad_portero(tiros_recibidos, goles_recibidos):
    """
    TU JUGADA MAESTRA: Evaluación de efectividad de porteros

    Estrategia de análisis:
    - Calcula qué porcentaje de tiros fue capaz de detener el portero
    - Resultado: porcentaje de paradas exitosas (0-100)

    Información necesaria:
    tiros_recibidos: número total de disparos al arco que enfrentó
    goles_recibidos: número de goles que le anotaron

    Resultado:
    porcentaje de efectividad (las paradas exitosas sobre el total)
    """

    # PASO 1: ¿Qué pasa si no enfrentó ningún tiro?
    # Reflexiona: ¿Cómo evaluarías a un portero que no jugó?
    if tiros_recibidos == 0:
        return 0  # Sin tiros = no hay datos para evaluar

    # PASO 2: Calcula las paradas exitosas
    # Pregunta clave: Si recibió 10 tiros y le hicieron 3 goles, ¿cuántos paró?
    tiros_parados = tiros_recibidos - goles_recibidos

    # PASO 3: Convierte a porcentaje
    # ¿Qué proporción de tiros logró detener?
    efectividad = (tiros_parados / tiros_recibidos) * 100

    return efectividad


# ¡LABORATORIO DE EVALUACIÓN DE PORTEROS!
print("=== ANÁLISIS COMPARATIVO DE PORTEROS DE ÉLITE ===")
print("¿Quién crees que tendrá mejor efectividad?")
print()

# Datos reales aproximados temporada 2023-24
# ¿Puedes predecir el ranking antes de ejecutar?

# Ter Stegen (FC Barcelona)
ter_stegen_tiros = 125
ter_stegen_goles = 35

# Courtois (Real Madrid) - antes de la lesión
courtois_tiros = 89
courtois_goles = 22

# Oblak (Atlético Madrid)
oblak_tiros = 108
oblak_goles = 29

# ¡Ejecutamos nuestra jugada con cada portero!
efectividad_ter_stegen = calcular_efectividad_portero(
    ter_stegen_tiros, ter_stegen_goles
)
efectividad_courtois = calcular_efectividad_portero(courtois_tiros, courtois_goles)
efectividad_oblak = calcular_efectividad_portero(oblak_tiros, oblak_goles)

# Resultados del análisis
print(f"Ter Stegen: {ter_stegen_goles} goles en {ter_stegen_tiros} tiros")
print(f"Efectividad: {efectividad_ter_stegen:.1f}% de paradas exitosas")
print()

print(f"Courtois: {courtois_goles} goles en {courtois_tiros} tiros")
print(f"Efectividad: {efectividad_courtois:.1f}% de paradas exitosas")
print()

print(f"Oblak: {oblak_goles} goles en {oblak_tiros} tiros")
print(f"Efectividad: {efectividad_oblak:.1f}% de paradas exitosas")
print()

# Momento de reflexión analítica
print("=== REFLEXIÓN ESTRATÉGICA ===")
print("¿Qué revela este análisis sobre cada portero?")
print("¿El portero con menos goles es necesariamente el mejor?")
print("¿Cómo influye el estilo de juego del equipo en estos números?")

# Pregunta de conexión
print()
print("¿Te das cuenta de cómo una función hace que el análisis sea:")
print("- Reutilizable: funciona con cualquier portero")
print("- Preciso: evita errores de cálculo manual")
print("- Escalable: puedes analizar 50 porteros en segundos")
print("- Profesional: resultados consistentes y comparables")

# %% [markdown]
# ---
#
# ## ¿Qué pasa cuando las situaciones se vuelven más complejas?
#
# **Momento de reflexión estratégica**: Hasta ahora hemos creado jugadas simples con pocos datos. Pero en el fútbol real, ¿las decisiones importantes se toman con solo una o dos variables?
#
# ### Escenario de complejidad real:
#
# Imagínate que eres Pep Guardiola y debes evaluar si Kevin De Bruyne tuvo una buena temporada. **¿Con qué criterios lo evaluarías?**
#
# **Pregunta de reflexión**: ¿Sería suficiente mirar solo los goles? ¿O necesitarías considerar...?
# - Goles anotados
# - Asistencias realizadas  
# - Partidos jugados
# - Posición en la que juega
# - Edad del jugador
# - Minutos totales
# - ¿Qué otros factores?
#
# **Descubrimiento clave**: Las evaluaciones reales requieren **múltiples variables** trabajando juntas.
#
# ---
#
# ## Funciones con "información compleja": El análisis multidimensional
#
# **Analogía futbolística**: Cuando Ancelotti evalúa a un jugador, no mira una sola estadística. Combina datos de:
# - Rendimiento ofensivo (goles + asistencias)
# - Consistencia (partidos jugados)
# - Contexto posicional (delantero vs. mediocampista)
# - Evolución temporal (edad y proyección)
#
# **En programación**: Las funciones pueden recibir **múltiples parámetros** para hacer análisis tan sofisticados como los de los cuerpos técnicos profesionales.
#
# ### Estructura de una "evaluación integral":
#
# ```python
# def analizar_jugador_completo(parametro1, parametro2, parametro3, parametro4):
#     # Combinamos múltiples variables para obtener una conclusión integral
#     # Como un director técnico que considera todos los aspectos
#     return evaluacion_completa
# ```
#
# **Pregunta de anticipación**: ¿Puedes imaginar cómo sería una función que evalúe a un jugador considerando goles, asistencias, partidos jugados Y su posición específica?
#
# **Descubrimiento**: ¡Estás a punto de crear análisis tan sofisticados como los que usan los grandes clubes europeos!

# %%
# ¡JUGADA MAESTRA AVANZADA! Análisis multidimensional como los grandes clubes

# ¿Estás listo para crear un sistema de análisis tan sofisticado como el del PSG o Bayern Munich?


def analizar_rendimiento_jugador(nombre, goles, asistencias, partidos, posicion):
    """
    SISTEMA DE EVALUACIÓN PROFESIONAL: Análisis integral de jugadores

    Esta función replica cómo los departamentos de análisis de los grandes clubes
    evalúan a sus jugadores combinando múltiples métricas y contexto posicional.

    Información requerida:
    nombre: nombre completo del jugador
    goles: goles anotados en la temporada
    asistencias: asistencias realizadas
    partidos: número de partidos disputados
    posicion: posición principal (delantero, mediocampo, defensa)

    Resultado:
    evaluación integral con métricas, contexto y clasificación final
    """

    # VALIDACIÓN INICIAL: ¿Tenemos datos suficientes?
    # Como un analista profesional, siempre verificamos la calidad de los datos
    if partidos == 0:
        return (
            f"{nombre}: Datos insuficientes - No ha disputado partidos esta temporada"
        )

    # MÉTRICAS FUNDAMENTALES: Los números que todo director técnico necesita
    goles_por_partido = goles / partidos
    asistencias_por_partido = asistencias / partidos
    participaciones_gol = goles + asistencias  # Contribución total al ataque
    participaciones_por_partido = participaciones_gol / partidos

    # EVALUACIÓN CONTEXTUAL: Diferentes estándares según la posición
    # ¿Por qué? Porque no puedes evaluar a Busquets con los mismos criterios que a Haaland

    if posicion.lower() in ["delantero", "extremo", "9", "falso 9"]:
        # Para atacantes: priorizamos la efectividad goleadora
        if goles_por_partido >= 0.8:  # Más de 0.8 goles por partido
            nivel = "ÉLITE MUNDIAL"
            comentario = "Rendimiento de delantero estrella internacional"
        elif goles_por_partido >= 0.5:  # Entre 0.5 y 0.8 goles por partido
            nivel = "MUY BUENO"
            comentario = "Delantero confiable de nivel profesional"
        elif goles_por_partido >= 0.3:  # Entre 0.3 y 0.5 goles por partido
            nivel = "PROMEDIO"
            comentario = "Rendimiento aceptable, con margen de mejora"
        else:
            nivel = "NECESITA MEJORAR"
            comentario = "Efectividad goleadora por debajo del estándar profesional"

    elif posicion.lower() in ["mediocampo", "mediocentro", "8", "10", "volante"]:
        # Para mediocampistas: equilibrio entre goles y asistencias
        if participaciones_por_partido >= 0.6:  # Más de 0.6 participaciones por partido
            nivel = "ÉLITE MUNDIAL"
            comentario = "Mediocampista decisivo de nivel internacional"
        elif participaciones_por_partido >= 0.4:  # Entre 0.4 y 0.6 participaciones
            nivel = "MUY BUENO"
            comentario = "Mediocampista productivo y confiable"
        elif participaciones_por_partido >= 0.2:  # Entre 0.2 y 0.4 participaciones
            nivel = "PROMEDIO"
            comentario = "Contribución ofensiva aceptable para su posición"
        else:
            nivel = "NECESITA MEJORAR"
            comentario = "Poco impacto ofensivo para su posición"

    else:  # Defensas y porteros
        # Para defensas: cualquier contribución ofensiva es valiosa
        if participaciones_por_partido >= 0.3:  # Más de 0.3 participaciones por partido
            nivel = "EXCEPCIONAL"
            comentario = "Defensa con contribución ofensiva extraordinaria"
        elif participaciones_por_partido >= 0.15:  # Entre 0.15 y 0.3 participaciones
            nivel = "MUY BUENO"
            comentario = "Defensa con buena proyección ofensiva"
        elif participaciones_por_partido >= 0.05:  # Entre 0.05 y 0.15 participaciones
            nivel = "BUENO"
            comentario = "Contribución ofensiva ocasional pero valiosa"
        else:
            nivel = "DEFENSIVO"
            comentario = "Enfocado en tareas defensivas (normal para su posición)"

    # CONSTRUCCIÓN DEL REPORTE PROFESIONAL
    # Como los informes que reciben los entrenadores antes de cada partido

    reporte = f"""
╔═══════════════════════════════════════════════════════════════╗
║                    ANÁLISIS DE RENDIMIENTO                    ║
╠═══════════════════════════════════════════════════════════════╣
║ JUGADOR: {nombre.upper()}
║ POSICIÓN: {posicion.title()}
║ 
║ MÉTRICAS DE TEMPORADA:
║ • Goles: {goles} en {partidos} partidos ({goles_por_partido:.2f} por partido)
║ • Asistencias: {asistencias} ({asistencias_por_partido:.2f} por partido)
║ • Participaciones: {participaciones_gol} ({participaciones_por_partido:.2f} por partido)
║ 
║ EVALUACIÓN: {nivel}
║ ANÁLISIS: {comentario}
╚═══════════════════════════════════════════════════════════════╝
    """

    return reporte


# ¡LABORATORIO DE ANÁLISIS PROFESIONAL!
print("=== DEPARTAMENTO DE ANÁLISIS: EVALUACIÓN DE PLANTILLA ===")
print("Simulando el trabajo de un analista de datos de un gran club europeo")
print()

# Datos reales de jugadores estrella temporada 2023-24
# ¿Puedes predecir qué evaluaciones obtendrán?

# Análisis de diferentes posiciones para mostrar la contextualización

# Delantero estrella
haaland_reporte = analizar_rendimiento_jugador("Erling Haaland", 36, 8, 35, "delantero")

# Mediocampista creativo
de_bruyne_reporte = analizar_rendimiento_jugador(
    "Kevin De Bruyne", 12, 18, 32, "mediocampo"
)

# Defensa con proyección
rudiger_reporte = analizar_rendimiento_jugador("Antonio Rüdiger", 2, 1, 31, "defensa")

# Presentamos los análisis
print(haaland_reporte)
print(de_bruyne_reporte)
print(rudiger_reporte)

# Reflexión analítica
print("=== REFLEXIÓN SOBRE EL ANÁLISIS MULTIDIMENSIONAL ===")
print("¿Observas cómo cada posición tiene criterios de evaluación diferentes?")
print("¿Por qué es importante contextualizar los números según el rol del jugador?")
print("¿Cómo usarías esta información si fueras director deportivo?")

# %% [markdown]
# ---
#
# ## SÍNTESIS DE SESIÓN 1: ¿Qué hemos descubierto sobre crear "jugadas maestras"?
#
# ### Momento de reflexión estratégica (5 minutos)
#
# **Pregunta de autoevaluación**: Antes de avanzar, ¿podrías explicar a un compañero qué es una función usando solo analogías futbolísticas?
#
# #### ¿Qué dominamos ahora?
# - **Funciones básicas**: Crear "jugadas programadas" reutilizables como calcular_promedio_goles()
# - **Múltiples parámetros**: Análisis complejos que consideran varios factores simultáneamente  
# - **Análisis contextual**: Evaluar jugadores según su posición específica (delanteros vs. mediocampistas)
# - **Sistemas profesionales**: Crear evaluaciones tan sofisticadas como las de clubes de élite
#
# #### ¿Qué patrones descubrimos?
# 1. **Reutilización inteligente**: Una función bien diseñada funciona con cualquier jugador
# 2. **Prevención de errores**: Validar datos como prevenir división por cero  
# 3. **Contextualización**: Diferentes criterios según la posición y rol
# 4. **Automatización de calidad**: Evitar errores humanos en cálculos repetitivos
#
# **Pregunta de conexión**: ¿Te das cuenta de que ya programas con la mentalidad de un analista deportivo profesional?
#
# ### Vista previa de Sesión 2:
# **¿Sabías que existe todo un universo de "jugadas maestras" creadas por otros programadores que puedes usar directamente?**
#
# **Pregunta motivadora**: ¿Por qué crear desde cero un sistema de análisis estadístico cuando expertos mundiales ya han resuelto esos problemas?
#
# ¿Estás listo para acceder a las herramientas que usan los departamentos de análisis del Barcelona, Real Madrid y Manchester City?

# %% [markdown]
# # SESIÓN 2: ¿Cómo acceden los técnicos de élite a la sabiduría colectiva? (50 minutos)
#
# ## ¿Te has preguntado por qué algunos entrenadores siempre parecen tener la estrategia perfecta?
#
# **Escenario revelador**: Jurgen Klopp llega al Liverpool y en pocos años los convierte en campeones de todo. Pep Guardiola revoluciona el Manchester City. Ancelotti domina en el Real Madrid...
#
# **Pregunta clave**: ¿Estos entrenadores geniales inventan todo desde cero, o tienen un "secreto" diferente?
#
# ### ¿Cuál es realmente el secreto de los grandes estrategas?
#
# **Momento de reflexión**: Piensa en los entrenadores más exitosos que conoces. ¿Qué tienen en común?
#
# **Descubrimiento sorprendente**: Los mejores entrenadores no reinventan todo. Son maestros en **aprovechar la sabiduría acumulada** de toda la comunidad futbolística mundial.
#
# #### ¿Cómo lo hacen?
# - **Estudian tácticas** de entrenadores históricos y contemporáneos
# - **Adaptan métodos** de entrenamiento probados en diferentes culturas
# - **Combinan estrategias** que han funcionado en otros contextos
# - **Usan herramientas especializadas** desarrolladas por expertos en análisis deportivo
# - **Colaboran con especialistas** en diferentes áreas (psicología, medicina, datos)
#
# **Conexión reveladora**: En programación, funciona exactamente igual. Los mejores programadores no reinventan todo... ¡acceden a la sabiduría colectiva mundial!
#
# ---
#
# ## Módulos y librerías: Tu acceso al conocimiento mundial
#
# **Analogía futbolística perfecta**: 
#
# | En el fútbol profesional | En programación |
# |-------------------------|------------------|
# | Manual de tácticas de Cruyff | Módulo de matemáticas |
# | Métodos de entrenamiento alemanes | Librería de estadísticas |
# | Análisis de datos del Barcelona | Módulo de visualización |
# | Sistema médico del Real Madrid | Librería de análisis de datos |
#
# **Pregunta de descubrimiento**: ¿Qué pasaría si pudieras usar directamente las herramientas matemáticas que usan los analistas del PSG o Bayern Munich?
#
# ### ¿Qué son realmente los módulos?
#
# **Reflexión estratégica**: Si tuvieras que organizar el manual táctico del Real Madrid, ¿cómo lo estructurarías?
#
# **Tu respuesta mental probablemente incluye**:
# - Capítulo 1: Tácticas defensivas
# - Capítulo 2: Estrategias ofensivas  
# - Capítulo 3: Jugadas de pelota parada
# - Capítulo 4: Análisis de rivales
# - Capítulo 5: Condición física
#
# **¡Exacto!** En Python, los módulos organizan funciones relacionadas como capítulos especializados de un manual profesional.
#
# **Momento revelador**: ¿Ya entiendes qué son los módulos antes de ver una línea de código?

# %%
# ¡ACCEDIENDO A LAS HERRAMIENTAS DE LOS PROFESIONALES!

# ¿Alguna vez te preguntaste cómo calculan las distancias exactas en el campo?
# ¿O cómo simulan miles de partidos para crear predicciones?

# ¡Python ya tiene todas estas herramientas listas para usar!

print("=== DESCUBRIENDO LAS HERRAMIENTAS PROFESIONALES ===")
print("¿Cómo usan los analistas del Real Madrid las matemáticas avanzadas?")
print()

# MÓDULO MATH: Las matemáticas de los expertos
import math

# ¿Sabías que puedes calcular distancias exactas en el campo como los sistemas de tracking?
print("1. CÁLCULOS GEOMÉTRICOS PROFESIONALES:")


# Distancia entre dos jugadores en el campo (coordenadas x, y)
def calcular_distancia_jugadores(x1, y1, x2, y2):
    """Calcula la distancia exacta entre dos jugadores usando teorema de Pitágoras"""
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia


# Ejemplo: Distancia entre portero y delantero
portero_x, portero_y = 5, 50  # Portero en el área
delantero_x, delantero_y = 95, 55  # Delantero cerca del arco

distancia = calcular_distancia_jugadores(portero_x, portero_y, delantero_x, delantero_y)
print(f"Distancia entre portero y delantero: {distancia:.1f} metros")
print(f"¿Está en posición de fuera de juego? (análisis geométrico)")
print()


# Ángulo de tiro - ¿desde qué posición es más fácil anotar?
def calcular_angulo_tiro(x_jugador, y_jugador):
    """Calcula el ángulo de tiro al arco (usamos trigonometría como los expertos)"""
    # Arco está en x=100, desde y=45 hasta y=55 (10m de ancho)
    angulo_superior = math.atan2(55 - y_jugador, 100 - x_jugador)
    angulo_inferior = math.atan2(45 - y_jugador, 100 - x_jugador)
    angulo_tiro = abs(angulo_superior - angulo_inferior)

    # Convertir a grados (más fácil de entender)
    angulo_grados = math.degrees(angulo_tiro)
    return angulo_grados


# Comparando diferentes posiciones de tiro
posiciones_tiro = [
    (90, 50, "Centro del área"),
    (85, 40, "Lateral izquierdo"),
    (85, 60, "Lateral derecho"),
    (75, 50, "Borde del área"),
]

print("2. ANÁLISIS DE POSICIONES DE TIRO:")
for x, y, descripcion in posiciones_tiro:
    angulo = calcular_angulo_tiro(x, y)
    print(f"{descripcion}: Ángulo de {angulo:.1f}° (mayor ángulo = mejor oportunidad)")

print()

# MÓDULO RANDOM: Simulaciones como los departamentos de análisis
import random

print("3. SIMULACIONES PROFESIONALES:")
print("¿Cómo predicen los analistas los resultados de la temporada?")


def simular_partido(equipo_local_fuerza, equipo_visitante_fuerza):
    """
    Simula un partido basado en la 'fuerza' relativa de los equipos
    (como los modelos probabilísticos que usan los clubes)
    """
    # Ajustamos probabilidades según la fuerza relativa
    total_fuerza = equipo_local_fuerza + equipo_visitante_fuerza
    prob_local = equipo_local_fuerza / total_fuerza

    # Factor casa (ventaja de jugar en casa)
    prob_local += 0.1  # 10% de ventaja por jugar en casa

    # Simulamos múltiples "momentos de peligro" en el partido
    goles_local = 0
    goles_visitante = 0

    # Simulamos 20 oportunidades de gol en el partido
    for oportunidad in range(20):
        if random.random() < prob_local * 0.15:  # 15% de chance de gol por oportunidad
            goles_local += 1
        elif random.random() < 0.12:  # 12% para el visitante
            goles_visitante += 1

    return goles_local, goles_visitante


# Simulando El Clásico: Real Madrid vs Barcelona
print("SIMULANDO EL CLÁSICO (Real Madrid vs Barcelona):")
print("Usando modelo probabilístico basado en fuerza relativa...")

# Fuerza del equipo (escala 1-100, basada en plantilla y forma)
madrid_fuerza = 92
barcelona_fuerza = 88

# Simulamos 5 versiones del mismo partido
for simulacion in range(1, 6):
    goles_madrid, goles_barcelona = simular_partido(madrid_fuerza, barcelona_fuerza)
    resultado = "Empate"
    if goles_madrid > goles_barcelona:
        resultado = "Victoria Real Madrid"
    elif goles_barcelona > goles_madrid:
        resultado = "Victoria Barcelona"

    print(
        f"Simulación {simulacion}: Real Madrid {goles_madrid} - {goles_barcelona} Barcelona ({resultado})"
    )

print()
print("¿Observas cómo cada simulación da un resultado diferente?")
print("¡Así es como los analistas calculan probabilidades de múltiples escenarios!")

# REFLEXIÓN FINAL
print()
print("=== REFLEXIÓN: EL PODER DE LAS HERRAMIENTAS PROFESIONALES ===")
print("¿Te das cuenta de que acabas de usar las mismas herramientas matemáticas")
print("que emplean los departamentos de análisis de los grandes clubes?")
print()
print("Con módulos tienes acceso instantáneo a:")
print("- Matemáticas avanzadas (geometría, trigonometría, estadística)")
print("- Simulaciones complejas (modelos probabilísticos)")
print("- Herramientas especializadas creadas por expertos mundiales")
print("- ¡Y mucho más que descubriremos en próximas sesiones!")

# %% [markdown]
# ---
#
# ## ¿Cómo "invocamos" a los especialistas según la situación?
#
# **Pregunta de reflexión futbolística**: En tu equipo, ¿cómo te refieres a los jugadores según el contexto?
#
# **Piénsalo**:
# - En formal: "Lionel Andrés Messi Cuccittini"
# - En confianza: "Leo" 
# - En táctica: "El 10"
# - En urgencia: "¡Pásala al argentino!"
#
# **Descubrimiento**: En programación también tenemos diferentes formas de "llamar" a las herramientas según nuestras necesidades.
#
# ### ¿Por qué necesitamos diferentes formas de importar?
#
# **Situaciones reales**:
# 1. **Análisis completo**: Necesitas muchas funciones matemáticas → Importas todo el módulo
# 2. **Código frecuente**: Usas las mismas funciones muchas veces → Les das alias cortos  
# 3. **Función específica**: Solo necesitas una herramienta → Importas únicamente esa
# 4. **Múltiples módulos**: Evitas confusiones → Mantienes nombres claros
#
# **Analogía táctica**: Como un entrenador que adapta su comunicación según el momento del partido.

# %%
# ¡EXPLORANDO LAS DIFERENTES FORMAS DE "CONVOCAR" ESPECIALISTAS!

# Como un entrenador que adapta su comunicación según la situación

print("=== LABORATORIO: FORMAS DE IMPORTAR HERRAMIENTAS ===")
print("¿Cómo un analista del Real Madrid accede a diferentes herramientas?")
print()

# SITUACIÓN 1: "Necesito acceso completo al departamento de matemáticas"
import math

print("1. IMPORTACIÓN COMPLETA (como tener todo el departamento disponible):")
angulo_tiro = 45  # grados - ángulo típico de tiro libre
angulo_radianes = math.radians(angulo_tiro)  # Convertir a radianes
altura_balon = math.sin(angulo_radianes) * 25  # Altura que alcanza el balón

print(f"   Tiro libre a {angulo_tiro}°:")
print(f"   - Ángulo en radianes: {angulo_radianes:.3f}")
print(f"   - Altura máxima del balón: {altura_balon:.2f} metros")
print("   ✓ Ventaja: Acceso a todas las funciones matemáticas")
print("   ✗ Desventaja: Código más largo (math.función)")
print()

# SITUACIÓN 2: "Voy a usar mucho las matemáticas, necesito un nombre más corto"
import math as mat

print("2. IMPORTACIÓN CON ALIAS (como dar un apodo al especialista):")
velocidad_inicial = 25  # m/s
tiempo_vuelo = 2 * (velocidad_inicial * mat.sin(angulo_radianes)) / 9.81  # Gravedad
distancia_tiro = velocidad_inicial * mat.cos(angulo_radianes) * tiempo_vuelo

print(f"   Análisis de trayectoria del balón:")
print(f"   - Tiempo en el aire: {tiempo_vuelo:.2f} segundos")
print(f"   - Distancia recorrida: {distancia_tiro:.1f} metros")
print("   ✓ Ventaja: Código más corto y claro")
print("   ✓ Ideal cuando usas muchas funciones del mismo módulo")
print()

# SITUACIÓN 3: "Solo necesito herramientas específicas para mi análisis"
from math import cos, sin, sqrt, pi

print("3. IMPORTACIÓN ESPECÍFICA (como convocar solo los expertos que necesitas):")
# Ahora puedo usar las funciones directamente, sin prefijo
velocidad_horizontal = cos(angulo_radianes) * 25  # Componente horizontal
velocidad_vertical = sin(angulo_radianes) * 25  # Componente vertical
velocidad_total = sqrt(velocidad_horizontal**2 + velocidad_vertical**2)
area_semicirculo = (pi * 16.5**2) / 2  # Área semicircular del área grande

print(f"   Análisis vectorial del tiro:")
print(f"   - Velocidad horizontal: {velocidad_horizontal:.1f} m/s")
print(f"   - Velocidad vertical: {velocidad_vertical:.1f} m/s")
print(f"   - Velocidad total: {velocidad_total:.1f} m/s")
print(f"   - Área del área grande: {area_semicirculo:.1f} m²")
print("   ✓ Ventaja: Código más limpio, funciones directas")
print("   ✓ Ideal para funciones que usas frecuentemente")
print()

# SITUACIÓN 4: La opción "peligrosa" (existe pero NO la recomendamos)
print("4. IMPORTAR TODO CON * (como traer todo el departamento sin organización):")
print("   from math import *  # ¡NO recomendado!")
print("   Problemas:")
print("   ✗ Puede causar conflictos de nombres")
print("   ✗ No sabes qué funciones están disponibles")
print("   ✗ Código difícil de mantener y debuggear")
print()

# COMPARACIÓN PRÁCTICA: El mismo cálculo con diferentes estilos
print("=== COMPARACIÓN DE ESTILOS ===")
print("El mismo cálculo (distancia entre dos jugadores) con diferentes importaciones:")
print()

# Estilo 1: import completo
import math as m1

x1, y1 = 10, 20  # Posición jugador 1
x2, y2 = 30, 50  # Posición jugador 2
distancia1 = m1.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(
    f"Estilo completo: distancia = m1.sqrt((x2-x1)**2 + (y2-y1)**2) = {distancia1:.1f}m"
)

# Estilo 2: import específico
from math import sqrt as raiz

distancia2 = raiz((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(
    f"Estilo específico: distancia = raiz((x2-x1)**2 + (y2-y1)**2) = {distancia2:.1f}m"
)

print()
print("¿Cuál prefieres y por qué?")
print("¿En qué situaciones usarías cada estilo?")

# RECOMENDACIÓN PROFESIONAL
print()
print("=== RECOMENDACIÓN DE EXPERTOS ===")
print("Para código profesional como el de los clubes de élite:")
print("Usa 'import módulo' para módulos que usas poco")
print("Usa 'import módulo as alias' para módulos frecuentes")
print("Usa 'from módulo import función' para funciones específicas")
print("Evita 'from módulo import *' en código profesional")
print()
print("¡Como un buen entrenador: claridad y organización siempre!")

# %% [markdown]
# ---
#
# ## ¡Tu turno de ser el arquitecto del conocimiento!
#
# **Momento de aplicación práctica**: Acabas de aprender a usar herramientas creadas por otros expertos. Pero **¿qué pasa cuando necesitas crear tu propia especialización?**
#
# ### Escenario desafío: El manual de análisis del Club
#
# **Situación real**: Eres el nuevo analista del Athletic Bilbao y necesitas crear un sistema de evaluación específico para el estilo de juego del club.
#
# **Pregunta estratégica**: Si tuvieras que crear tu propio "manual de análisis futbolístico", ¿qué herramientas especializadas incluirías?
#
# #### Reflexión previa (3 minutos):
#
# **Piensa como un experto en análisis deportivo**:
# 1. **¿Qué cálculos haces repetidamente?** (puntos, forma, comparaciones...)
# 2. **¿Qué análisis son únicos de tu metodología?** (criterios específicos del club)
# 3. **¿Cómo organizarías las herramientas por especialidad?** (ofensiva, defensiva, física...)
# 4. **¿Qué información necesita cada función para funcionar?** (datos de entrada)
#
# ### Descubrimiento: Creando tu primer módulo especializado
#
# **Analogía perfecta**: Vamos a crear nuestro "departamento de análisis personalizado" con funciones específicas para diferentes aspectos del análisis futbolístico.
#
# **¿Estás listo para construir herramientas tan especializadas como las que usan en La Liga?**

# %%
# ¡CREANDO NUESTRO DEPARTAMENTO DE ANÁLISIS PERSONALIZADO!

# Como si fuéramos los diseñadores del sistema de análisis del FC Barcelona

print("=== CONSTRUYENDO NUESTRO MÓDULO ESPECIALIZADO ===")
print("Departamento de Análisis Futbolístico - Versión Profesional")
print()


# ESPECIALIZACIÓN 1: ANÁLISIS DE PUNTUACIÓN Y CLASIFICACIÓN
def calcular_puntos_equipo(victorias, empates, derrotas):
    """
    HERRAMIENTA BÁSICA: Cálculo de puntos en liga

    Como los sistemas automáticos que actualizan las tablas de posiciones
    en tiempo real durante los partidos.

    Entrada: victorias, empates, derrotas (números enteros)
    Salida: puntos totales según el sistema de La Liga
    """
    puntos = (victorias * 3) + (empates * 1) + (derrotas * 0)
    return puntos


# ESPECIALIZACIÓN 2: ANÁLISIS DE FORMA RECIENTE
def analizar_forma_equipo(ultimos_resultados):
    """
    HERRAMIENTA AVANZADA: Evaluación de momento deportivo

    Replica el análisis que hacen los medios deportivos cuando dicen
    "el Real Madrid viene en racha" o "el Barcelona está en crisis"

    Entrada: lista con últimos 5 resultados ['V', 'E', 'D']
    Salida: evaluación cualitativa y cuantitativa de la forma
    """
    # Validación como un analista profesional
    if len(ultimos_resultados) != 5:
        return "Error: Se necesitan exactamente los últimos 5 resultados"

    # Conversión de resultados a puntos (sistema FIFA)
    puntos_forma = 0
    for resultado in ultimos_resultados:
        if resultado.upper() == "V":  # Victoria
            puntos_forma += 3
        elif resultado.upper() == "E":  # Empate
            puntos_forma += 1
        # Derrota = 0 puntos (no sumamos nada)

    # Clasificación según criterios profesionales
    if puntos_forma >= 12:  # 4+ victorias en últimos 5
        forma = "EXCELENTE - Racha ganadora"
        analisis = "Equipo en estado de gracia, alta confianza"
    elif puntos_forma >= 8:  # 2-3 victorias, resto no derrotas
        forma = "BUENA - Tendencia positiva"
        analisis = "Momento sólido, sin derrotas críticas"
    elif puntos_forma >= 4:  # 1-2 victorias o varios empates
        forma = "REGULAR - Inconsistente"
        analisis = "Rendimiento irregular, necesita estabilidad"
    else:  # 3+ derrotas en últimos 5
        forma = "MALA - Crisis de resultados"
        analisis = "Momento crítico, cambios necesarios"

    return f"{forma} ({puntos_forma}/15 puntos) - {analisis}"


# ESPECIALIZACIÓN 3: ANÁLISIS COMPARATIVO
def comparar_equipos(equipo1_puntos, equipo2_puntos, nombres_equipos=None):
    """
    HERRAMIENTA ESTRATÉGICA: Evaluación de distancias competitivas

    Como el análisis que hacen antes de El Clásico: "¿Qué tan cerca están
    los equipos?" "¿Es una diferencia recuperable?"

    Entrada: puntos de cada equipo, nombres opcionales
    Salida: análisis de la diferencia competitiva
    """
    diferencia = abs(equipo1_puntos - equipo2_puntos)

    # Análisis contextual según la fase de la temporada
    if diferencia == 0:
        evaluacion = "EMPATE TÉCNICO"
        contexto = "Máxima igualdad competitiva"
    elif diferencia <= 3:  # 1 partido de diferencia
        evaluacion = "DIFERENCIA MÍNIMA"
        contexto = "Un partido puede cambiar todo"
    elif diferencia <= 6:  # 2 partidos de diferencia
        evaluacion = "VENTAJA MODERADA"
        contexto = "Diferencia recuperable con buena racha"
    elif diferencia <= 12:  # 4 partidos de diferencia
        evaluacion = "DIFERENCIA CONSIDERABLE"
        contexto = "Requiere cambio de tendencia sostenido"
    else:  # 5+ partidos de diferencia
        evaluacion = "DIFERENCIA DECISIVA"
        contexto = "Brecha muy difícil de cerrar"

    # Construcción del reporte profesional
    if nombres_equipos:
        reporte = f"{nombres_equipos[0]} vs {nombres_equipos[1]}: "
    else:
        reporte = "Análisis comparativo: "

    reporte += f"{evaluacion} ({diferencia} puntos) - {contexto}"
    return reporte


# ¡LABORATORIO DE PRUEBAS CON DATOS REALES!
print("Probando nuestro departamento con datos de La Liga 2023-24:")
print()

# CASOS DE ESTUDIO: Los equipos más analizados de España
print("ANÁLISIS DE PUNTUACIÓN:")

# Real Madrid - Temporada dominante
madrid_v, madrid_e, madrid_d = 29, 8, 1  # Temporada casi perfecta
madrid_puntos = calcular_puntos_equipo(madrid_v, madrid_e, madrid_d)
print(f"Real Madrid: {madrid_v}V-{madrid_e}E-{madrid_d}D = {madrid_puntos} puntos")

# FC Barcelona - Temporada sólida
barcelona_v, barcelona_e, barcelona_d = 27, 7, 4
barcelona_puntos = calcular_puntos_equipo(barcelona_v, barcelona_e, barcelona_d)
print(
    f"FC Barcelona: {barcelona_v}V-{barcelona_e}E-{barcelona_d}D = {barcelona_puntos} puntos"
)

# Atlético Madrid - Temporada irregular
atletico_v, atletico_e, atletico_d = 24, 8, 6
atletico_puntos = calcular_puntos_equipo(atletico_v, atletico_e, atletico_d)
print(
    f"Atlético Madrid: {atletico_v}V-{atletico_e}E-{atletico_d}D = {atletico_puntos} puntos"
)
print()

print("ANÁLISIS DE FORMA RECIENTE:")
# Simulando los últimos 5 partidos de cada equipo
madrid_forma = ["V", "V", "V", "E", "V"]  # Racha excelente
barcelona_forma = ["V", "V", "D", "V", "E"]  # Forma buena pero irregular
atletico_forma = ["E", "D", "V", "D", "V"]  # Muy inconsistente

print(f"Real Madrid: {analizar_forma_equipo(madrid_forma)}")
print(f"FC Barcelona: {analizar_forma_equipo(barcelona_forma)}")
print(f"Atlético Madrid: {analizar_forma_equipo(atletico_forma)}")
print()

print("ANÁLISIS COMPARATIVO:")
equipos_clasico = ["Real Madrid", "FC Barcelona"]
equipos_derbi = ["Real Madrid", "Atlético Madrid"]

print(
    f"El Clásico: {comparar_equipos(madrid_puntos, barcelona_puntos, equipos_clasico)}"
)
print(
    f"Derbi madrileño: {comparar_equipos(madrid_puntos, atletico_puntos, equipos_derbi)}"
)
print(
    f"Rivalidad catalana: {comparar_equipos(barcelona_puntos, atletico_puntos, ['FC Barcelona', 'Atlético Madrid'])}"
)

print()
print("=== REFLEXIÓN SOBRE TU MÓDULO PERSONALIZADO ===")
print("¿Observas cómo cada función tiene una especialización específica?")
print("¿Cómo podrías expandir este módulo con más herramientas?")
print("¿Qué otras funciones añadirías para un análisis más completo?")
print()
print("¡Acabas de crear herramientas tan profesionales como las de La Liga!")

# %% [markdown]
# ---
#
# ## SÍNTESIS DE SESIÓN 2: ¿Qué hemos descubierto sobre acceder a la sabiduría colectiva?
#
# ### Momento de metacognición (5 minutos)
#
# **Pregunta de autoevaluación**: ¿Podrías explicar a un entrenador profesional cómo los módulos son como tener acceso a todos los departamentos especializados del mundo?
#
# #### ¿Qué dominamos ahora?
# - **Módulos básicos**: Acceso a herramientas matemáticas profesionales (math, random)
# - **Importaciones estratégicas**: Diferentes formas de convocar especialistas según la necesidad
# - **Simulaciones avanzadas**: Modelos probabilísticos como los que usan en análisis deportivo
# - **Módulos propios**: Crear departamentos especializados con nuestras herramientas
#
# #### ¿Qué patrones descubrimos?
# 1. **Reutilización de conocimiento experto**: No reinventar lo que ya está perfeccionado
# 2. **Organización por especialidades**: Funciones agrupadas por área de conocimiento
# 3. **Flexibilidad en la convocatoria**: Adaptar el acceso según las necesidades específicas
# 4. **Escalabilidad profesional**: Herramientas que crecen con la complejidad del análisis
#
# **Descubrimiento clave**: Ya programas con acceso a las mismas herramientas que usan los departamentos de análisis de los grandes clubes europeos.
#
# ### Conexión reveladora:
# **¿Te das cuenta de que puedes crear análisis tan sofisticados como los de:**
# - Departamento de datos del Manchester City
# - Sistema de scouting del Real Madrid  
# - Análisis táctico del FC Barcelona
# - Modelos predictivos del Bayern Munich
#
# ### Vista previa de Sesión 3:
# **¿Estás listo para el desafío final?** Vamos a integrar funciones + módulos + toda tu creatividad para crear un **Sistema Completo de Análisis Futbolístico**.
#
# **Pregunta motivadora**: ¿Podrías crear una herramienta tan completa que un entrenador real la usaría para tomar decisiones importantes?
#
# **Adelanto del proyecto**: Sistema integrado que evalúa jugadores individuales, analiza equipos completos, compara rivales y hasta predice resultados.
#
# ¿Estás listo para tu examen final como analista deportivo profesional?

# %% [markdown]
# # SESIÓN 3: ¿Podrías crear un sistema como los que usan los técnicos de élite? (50 minutos)
#
# ## Tu desafío final: El examen del analista profesional
#
# **Escenario del desafío**: Es tu primer día como analista principal del Real Madrid. Florentino Pérez y Carlo Ancelotti te esperan en la sala de juntas con una petición específica:
#
# *"Necesitamos un sistema que evalúe automáticamente a toda nuestra plantilla, compare nuestro rendimiento con rivales, y nos ayude a tomar decisiones estratégicas. ¿Puedes tenerlo listo para la junta directiva de esta tarde?"*
#
# **Pregunta de reflexión crítica**: ¿Te sientes preparado para este reto? ¿Qué herramientas ya tienes en tu arsenal?
#
# ### ¿Qué necesita realmente un sistema de análisis profesional?
#
# **Momento de diseño estratégico**: Antes de programar, piensa como un arquitecto de sistemas...
#
# **¿Qué módulos especializados necesitarías?**
#
# 1. **Módulo de análisis individual**: ¿Cómo evaluar a cada jugador según su posición?
# 2. **Módulo de análisis colectivo**: ¿Cómo evaluar el rendimiento del equipo completo?
# 3. **Módulo comparativo**: ¿Cómo posicionar al equipo frente a rivales?
# 4. **Módulo predictivo**: ¿Cómo proyectar tendencias futuras?
#
# **Descubrimiento emocionante**: ¡Ya tienes todas las herramientas necesarias! Solo necesitas integrarlas de manera elegante.
#
# ---
#
# ## Tu misión: Sistema Integrado de Análisis Futbolístico
#
# **Objetivo del proyecto**: Combinar funciones, módulos y lógica para crear una herramienta que simule los sistemas profesionales de análisis deportivo.
#
# ### Especificaciones del sistema:
#
# **El sistema debe poder**:
# - Evaluar automáticamente a cualquier jugador según criterios posicionales
# - Generar reportes completos de rendimiento de equipos
# - Comparar múltiples equipos con análisis contextual
# - Proporcionar recomendaciones estratégicas basadas en datos
# - Presentar resultados de manera profesional y comprensible
#
# **Pregunta motivadora**: ¿Estás listo para demostrar que puedes crear análisis tan sofisticados como los de los grandes clubes?
#
# ### Estructura del desarrollo:
#
# **Fase 1** (15 min): Construcción del módulo de análisis individual avanzado
# **Fase 2** (20 min): Desarrollo del sistema de análisis colectivo 
# **Fase 3** (10 min): Integración y pruebas con datos reales
# **Fase 4** (5 min): Reflexión y proyección profesional
#
# ¡Empezamos!

# %%
# PROYECTO INTEGRADOR: SISTEMA COMPLETO DE ANÁLISIS FUTBOLÍSTICO
# El desafío final - Crear una herramienta profesional como analista del Real Madrid

print("=== SISTEMA INTEGRADO DE ANÁLISIS DEPORTIVO ===")
print("Desarrollado por: [Tu nombre] - Analista Principal")
print("Club: Real Madrid CF")
print("Versión: 1.0 - Sistema Profesional")
print()

# Importamos las herramientas de expertos que ya dominamos
import random
import math

# ===============================
# FASE 1: MÓDULO DE ANÁLISIS INDIVIDUAL AVANZADO (15 minutos)
# ===============================


def evaluar_jugador_elite(nombre, posicion, estadisticas):
    """
    SISTEMA DE EVALUACIÓN ÉLITE: Análisis individual completo

    ¿Cómo evalúan los grandes clubes a sus estrellas?
    Combinando múltiples métricas con contexto posicional y criterios de élite.

    Entrada:
    - nombre: nombre completo del jugador
    - posicion: posición específica (delantero, mediocampo, defensa, portero)
    - estadisticas: diccionario con métricas completas

    Salida:
    - evaluación integral con calificación profesional
    """
    # VALIDACIÓN COMO ANALISTA PROFESIONAL
    partidos = estadisticas.get("partidos", 0)
    if partidos == 0:
        return {"error": f"{nombre} - Sin datos suficientes para análisis profesional"}

    # MÉTRICAS FUNDAMENTALES
    goles = estadisticas.get("goles", 0)
    asistencias = estadisticas.get("asistencias", 0)
    pases_exitosos = estadisticas.get("pases_exitosos", 0)
    total_pases = estadisticas.get("total_pases", 1)  # Evitar división por cero

    # CÁLCULOS AVANZADOS (como los sistemas del City Football Group)
    goles_por_partido = goles / partidos
    asistencias_por_partido = asistencias / partidos
    precision_pases = (pases_exitosos / total_pases) * 100 if total_pases > 0 else 0
    participaciones_gol = goles + asistencias
    participaciones_por_partido = participaciones_gol / partidos

    # EVALUACIÓN CONTEXTUAL POR POSICIÓN (criterios de élite mundial)
    posicion_lower = posicion.lower()

    if any(pos in posicion_lower for pos in ["delantero", "extremo", "9", "falso 9"]):
        # DELANTEROS: Criterios de goleadores de élite
        if goles_por_partido >= 1.0:  # +1 gol por partido (Haaland, Mbappé)
            calificacion = "ÉLITE MUNDIAL"
            puntuacion = 95
            analisis = "Goleador de clase mundial - Nivel Balón de Oro"
        elif goles_por_partido >= 0.7:  # 0.7+ goles por partido
            calificacion = "CLASE A+"
            puntuacion = 88
            analisis = "Delantero de élite europea - Nivel Champions League"
        elif goles_por_partido >= 0.5:  # 0.5+ goles por partido
            calificacion = "PROFESIONAL SÓLIDO"
            puntuacion = 78
            analisis = "Delantero confiable de primera división"
        elif goles_por_partido >= 0.3:  # 0.3+ goles por partido
            calificacion = "EN DESARROLLO"
            puntuacion = 68
            analisis = "Potencial con margen de crecimiento"
        else:
            calificacion = "CRÍTICO"
            puntuacion = 55
            analisis = "Rendimiento muy por debajo del estándar profesional"

    elif any(
        pos in posicion_lower
        for pos in ["mediocampo", "mediocentro", "8", "10", "volante"]
    ):
        # MEDIOCAMPISTAS: Equilibrio entre creatividad y eficiencia
        metric_principal = (
            participaciones_por_partido * 0.7 + (precision_pases / 100) * 0.3
        )

        if metric_principal >= 0.8 and precision_pases >= 88:  # De Bruyne, Modric level
            calificacion = "ÉLITE MUNDIAL"
            puntuacion = 94
            analisis = "Mediocampista maestro - Nivel legendario"
        elif metric_principal >= 0.6 and precision_pases >= 85:  # Top European level
            calificacion = "CLASE A+"
            puntuacion = 87
            analisis = "Mediocampista de élite - Pilar del equipo"
        elif metric_principal >= 0.4 and precision_pases >= 80:  # Solid professional
            calificacion = "PROFESIONAL SÓLIDO"
            puntuacion = 77
            analisis = "Mediocampista confiable y consistente"
        elif metric_principal >= 0.25 and precision_pases >= 75:  # Developing
            calificacion = "EN DESARROLLO"
            puntuacion = 67
            analisis = "Potencial con aspectos técnicos que mejorar"
        else:
            calificacion = "CRÍTICO"
            puntuacion = 58
            analisis = "Impacto limitado en ambas fases del juego"

    else:  # DEFENSAS Y PORTEROS
        # Para defensas: cualquier contribución ofensiva es excepcional
        if participaciones_por_partido >= 0.4:  # Ramos, Alaba level
            calificacion = "ÉLITE MUNDIAL"
            puntuacion = 92
            analisis = "Defensa completo con proyección ofensiva extraordinaria"
        elif participaciones_por_partido >= 0.2 and precision_pases >= 85:
            calificacion = "CLASE A+"
            puntuacion = 85
            analisis = "Defensa moderno con buena salida de balón"
        elif participaciones_por_partido >= 0.1 and precision_pases >= 80:
            calificacion = "PROFESIONAL SÓLIDO"
            puntuacion = 76
            analisis = "Defensa sólido con contribución ocasional"
        elif precision_pases >= 75:
            calificacion = "ESPECIALISTA DEFENSIVO"
            puntuacion = 72
            analisis = "Especialista en tareas defensivas"
        else:
            calificacion = "EN DESARROLLO"
            puntuacion = 65
            analisis = "Enfocado principalmente en aspectos defensivos"

    # CONSTRUCCIÓN DEL REPORTE PROFESIONAL
    return {
        "jugador": nombre,
        "posicion": posicion.title(),
        "metricas": {
            "goles_por_partido": round(goles_por_partido, 3),
            "asistencias_por_partido": round(asistencias_por_partido, 3),
            "participaciones_por_partido": round(participaciones_por_partido, 3),
            "precision_pases": round(precision_pases, 1),
        },
        "evaluacion": {
            "calificacion": calificacion,
            "puntuacion": puntuacion,
            "analisis": analisis,
        },
        "estadisticas_base": {
            "partidos": partidos,
            "goles": goles,
            "asistencias": asistencias,
            "precision": f"{pases_exitosos}/{total_pases} pases",
        },
    }


# ===============================
# FASE 2: SISTEMA DE ANÁLISIS COLECTIVO (20 minutos)
# ===============================


def analizar_plantilla_completa(nombre_equipo, jugadores_datos, resultados_recientes):
    """
    ANÁLISIS DE PLANTILLA ÉLITE: Evaluación integral del equipo

    ¿Cómo evalúan los departamentos técnicos la calidad global de sus plantillas?
    Combinando análisis individual, dinámicas colectivas y tendencias de forma.

    Entrada:
    - nombre_equipo: nombre oficial del club
    - jugadores_datos: lista con datos completos de cada jugador
    - resultados_recientes: últimos 5 resultados para análisis de forma

    Salida:
    - reporte ejecutivo completo para la junta directiva
    """
    print(f"Analizando plantilla de {nombre_equipo}...")
    print("Procesando evaluaciones individuales...")

    # EVALUACIONES INDIVIDUALES
    evaluaciones_jugadores = []
    total_goles_plantilla = 0
    total_asistencias_plantilla = 0
    puntuaciones = []

    for jugador_data in jugadores_datos:
        evaluacion = evaluar_jugador_elite(
            jugador_data["nombre"],
            jugador_data["posicion"],
            jugador_data["estadisticas"],
        )

        if "error" not in evaluacion:
            evaluaciones_jugadores.append(evaluacion)
            puntuaciones.append(evaluacion["evaluacion"]["puntuacion"])
            total_goles_plantilla += jugador_data["estadisticas"].get("goles", 0)
            total_asistencias_plantilla += jugador_data["estadisticas"].get(
                "asistencias", 0
            )

    # ANÁLISIS DE FORMA RECIENTE (momentum del equipo)
    puntos_forma = sum(
        3 if resultado == "V" else 1 if resultado == "E" else 0
        for resultado in resultados_recientes
    )

    # Clasificación de momento deportivo
    if puntos_forma >= 13:  # 4+ victorias
        momento_deportivo = "MOMENTUM EXCEPCIONAL"
        analisis_forma = "El equipo está en estado de gracia competitiva"
    elif puntos_forma >= 10:  # 3+ victorias
        momento_deportivo = "EXCELENTE FORMA"
        analisis_forma = "Tendencia muy positiva y confianza alta"
    elif puntos_forma >= 7:  # 2+ victorias
        momento_deportivo = "BUENA FORMA"
        analisis_forma = "Momento sólido con resultados consistentes"
    elif puntos_forma >= 4:  # 1+ victoria
        momento_deportivo = "FORMA IRREGULAR"
        analisis_forma = "Rendimiento inconsistente, necesita estabilidad"
    else:  # Muy pocos puntos
        momento_deportivo = "CRISIS DE RESULTADOS"
        analisis_forma = "Momento crítico que requiere intervención inmediata"

    # MÉTRICAS GLOBALES DE PLANTILLA
    promedio_calidad = sum(puntuaciones) / len(puntuaciones) if puntuaciones else 0

    # Clasificación de calidad de plantilla
    if promedio_calidad >= 90:
        nivel_plantilla = "ÉLITE MUNDIAL"
        competencia_objetivo = "Champions League - Candidato al título"
    elif promedio_calidad >= 85:
        nivel_plantilla = "ALTA COMPETENCIA"
        competencia_objetivo = "Champions League - Fase eliminatoria"
    elif promedio_calidad >= 78:
        nivel_plantilla = "COMPETITIVO"
        competencia_objetivo = "Liga doméstica - Puestos europeos"
    elif promedio_calidad >= 70:
        nivel_plantilla = "EN DESARROLLO"
        competencia_objetivo = "Liga doméstica - Mitad de tabla"
    else:
        nivel_plantilla = "RECONSTRUCCIÓN"
        competencia_objetivo = "Liga doméstica - Permanencia"

    # CONSTRUCCIÓN DEL REPORTE EJECUTIVO
    return {
        "club": nombre_equipo,
        "resumen_ejecutivo": {
            "nivel_plantilla": nivel_plantilla,
            "promedio_calidad": round(promedio_calidad, 1),
            "momento_deportivo": momento_deportivo,
            "puntos_forma": f"{puntos_forma}/15",
            "objetivo_realista": competencia_objetivo,
        },
        "metricas_globales": {
            "jugadores_analizados": len(evaluaciones_jugadores),
            "goles_totales_plantilla": total_goles_plantilla,
            "asistencias_totales_plantilla": total_asistencias_plantilla,
            "productividad_ofensiva": total_goles_plantilla
            + total_asistencias_plantilla,
        },
        "analisis_forma": {
            "ultimos_resultados": resultados_recientes,
            "tendencia": analisis_forma,
            "puntos_obtenidos": puntos_forma,
        },
        "evaluaciones_individuales": evaluaciones_jugadores,
    }


print("Módulos de análisis individual y colectivo desarrollados")
print("Sistema listo para procesar datos de élite")
print()

# %%
# ===============================
# FASE 3: MÓDULO DE SIMULACIÓN Y ANÁLISIS COMPARATIVO (10 minutos)
# ===============================


def simular_enfrentamiento_elite(equipo1_data, equipo2_data):
    """
    SIMULADOR DE ENFRENTAMIENTOS ÉLITE: Predicción avanzada de partidos

    ¿Cómo predicen los departamentos de análisis los resultados de partidos importantes?
    Usando modelos probabilísticos basados en múltiples variables.

    Entrada:
    - equipo1_data: diccionario con análisis completo del primer equipo
    - equipo2_data: diccionario con análisis completo del segundo equipo

    Salida:
    - predicción detallada del enfrentamiento con probabilidades y análisis
    """
    # EXTRACCIÓN DE MÉTRICAS CLAVE
    calidad_equipo1 = equipo1_data["resumen_ejecutivo"]["promedio_calidad"]
    calidad_equipo2 = equipo2_data["resumen_ejecutivo"]["promedio_calidad"]
    forma_equipo1 = equipo1_data["analisis_forma"]["puntos_obtenidos"]
    forma_equipo2 = equipo2_data["analisis_forma"]["puntos_obtenidos"]

    # CÁLCULO DE FUERZA RELATIVA (como los modelos Elo de FIFA)
    # Peso: 70% calidad plantilla, 30% forma reciente
    fuerza_equipo1 = (calidad_equipo1 * 0.7) + (
        forma_equipo1 * 0.3 * 6
    )  # Escalar forma a escala 0-90
    fuerza_equipo2 = (calidad_equipo2 * 0.7) + (forma_equipo2 * 0.3 * 6)

    # FACTOR ALEATORIO (impredecibilidad del fútbol)
    factor_impredecible = random.uniform(0.85, 1.15)

    # PROBABILIDADES BÁSICAS
    diferencia_fuerza = (fuerza_equipo1 - fuerza_equipo2) * factor_impredecible
    probabilidad_equipo1 = 50 + (diferencia_fuerza * 0.4)

    # LIMITAR PROBABILIDADES (máximo realismo: entre 15% y 85%)
    probabilidad_equipo1 = max(15, min(85, probabilidad_equipo1))
    probabilidad_empate = (
        25 - abs(diferencia_fuerza) * 0.2
    )  # Menos empates si hay gran diferencia
    probabilidad_empate = max(10, min(30, probabilidad_empate))
    probabilidad_equipo2 = 100 - probabilidad_equipo1 - probabilidad_empate

    # SIMULACIÓN DEL RESULTADO
    resultado_aleatorio = random.uniform(0, 100)

    if resultado_aleatorio < probabilidad_equipo1:
        # Victoria equipo 1
        goles_e1 = random.randint(1, 4)
        goles_e2 = random.randint(0, min(goles_e1 - 1, 2))
        resultado_texto = f"Victoria {equipo1_data['club']}"
        ganador = equipo1_data["club"]
    elif resultado_aleatorio < probabilidad_equipo1 + probabilidad_empate:
        # Empate
        goles_empate = random.randint(0, 3)
        goles_e1 = goles_e2 = goles_empate
        resultado_texto = "Empate"
        ganador = "Empate"
    else:
        # Victoria equipo 2
        goles_e2 = random.randint(1, 4)
        goles_e1 = random.randint(0, min(goles_e2 - 1, 2))
        resultado_texto = f"Victoria {equipo2_data['club']}"
        ganador = equipo2_data["club"]

    # ANÁLISIS TÁCTICO AUTOMÁTICO
    if abs(calidad_equipo1 - calidad_equipo2) < 3:
        analisis_tactico = "Partido muy igualado - Los detalles marcarán la diferencia"
    elif calidad_equipo1 > calidad_equipo2 + 5:
        analisis_tactico = f"{equipo1_data['club']} parte como favorito claro por su superior plantilla"
    elif calidad_equipo2 > calidad_equipo1 + 5:
        analisis_tactico = (
            f"{equipo2_data['club']} tiene ventaja significativa en calidad individual"
        )
    else:
        analisis_tactico = (
            "Duelo equilibrado donde la forma del momento puede ser decisiva"
        )

    # FACTORES CLAVE PARA EL ANÁLISIS
    factores_clave = []
    if forma_equipo1 > forma_equipo2 + 3:
        factores_clave.append(f"Momentum de {equipo1_data['club']} puede ser decisivo")
    elif forma_equipo2 > forma_equipo1 + 3:
        factores_clave.append(f"Racha de {equipo2_data['club']} genera confianza extra")

    if (
        equipo1_data["metricas_globales"]["productividad_ofensiva"]
        > equipo2_data["metricas_globales"]["productividad_ofensiva"] + 10
    ):
        factores_clave.append(f"Superioridad ofensiva de {equipo1_data['club']}")
    elif (
        equipo2_data["metricas_globales"]["productividad_ofensiva"]
        > equipo1_data["metricas_globales"]["productividad_ofensiva"] + 10
    ):
        factores_clave.append(f"Mayor potencial goleador de {equipo2_data['club']}")

    return {
        "enfrentamiento": f"{equipo1_data['club']} vs {equipo2_data['club']}",
        "prediccion": {
            "marcador_simulado": f"{goles_e1} - {goles_e2}",
            "resultado": resultado_texto,
            "ganador_predicho": ganador,
        },
        "probabilidades": {
            f"victoria_{equipo1_data['club'].lower().replace(' ', '_')}": round(
                probabilidad_equipo1, 1
            ),
            "empate": round(probabilidad_empate, 1),
            f"victoria_{equipo2_data['club'].lower().replace(' ', '_')}": round(
                probabilidad_equipo2, 1
            ),
        },
        "analisis_previo": {
            "fuerza_relativa": {
                equipo1_data["club"]: round(fuerza_equipo1, 1),
                equipo2_data["club"]: round(fuerza_equipo2, 1),
            },
            "analisis_tactico": analisis_tactico,
            "factores_clave": (
                factores_clave
                if factores_clave
                else ["Partido equilibrado sin factores decisivos claros"]
            ),
        },
    }


def generar_reporte_comparativo(equipos_data):
    """
    GENERADOR DE REPORTES COMPARATIVOS: Análisis multi-equipo

    Para comparar múltiples equipos como hacen en las presentaciones
    de jefes de scouting antes de mercados de fichajes.

    Entrada:
    - equipos_data: lista con análisis completos de múltiples equipos

    Salida:
    - ranking y análisis comparativo professional
    """
    print("=" * 80)
    print("                    REPORTE COMPARATIVO DE ÉLITE")
    print("=" * 80)

    # ORDENAR POR CALIDAD DE PLANTILLA
    equipos_ordenados = sorted(
        equipos_data,
        key=lambda x: x["resumen_ejecutivo"]["promedio_calidad"],
        reverse=True,
    )

    print("RANKING DE CALIDAD DE PLANTILLA:")
    for i, equipo in enumerate(equipos_ordenados, 1):
        calidad = equipo["resumen_ejecutivo"]["promedio_calidad"]
        nivel = equipo["resumen_ejecutivo"]["nivel_plantilla"]
        momento = equipo["resumen_ejecutivo"]["momento_deportivo"]
        print(f"{i}. {equipo['club']}: {calidad}/100 ({nivel}) - {momento}")

    print("\n" + "=" * 80)
    print("MÉTRICAS COMPARATIVAS:")

    # Equipo más goleador
    mas_goleador = max(
        equipos_data, key=lambda x: x["metricas_globales"]["goles_totales_plantilla"]
    )
    print(
        f"Mayor potencia ofensiva: {mas_goleador['club']} ({mas_goleador['metricas_globales']['goles_totales_plantilla']} goles)"
    )

    # Equipo en mejor forma
    mejor_forma = max(
        equipos_data, key=lambda x: x["analisis_forma"]["puntos_obtenidos"]
    )
    print(
        f"Mejor momento: {mejor_forma['club']} ({mejor_forma['analisis_forma']['puntos_obtenidos']}/15 puntos)"
    )

    # Equipo más equilibrado (mayor número de jugadores con buena evaluación)
    for equipo in equipos_data:
        jugadores_elite = sum(
            1
            for jugador in equipo["evaluaciones_individuales"]
            if jugador["evaluacion"]["puntuacion"] >= 85
        )
        equipo["jugadores_elite"] = jugadores_elite

    mas_equilibrado = max(equipos_data, key=lambda x: x["jugadores_elite"])
    print(
        f"Plantilla más equilibrada: {mas_equilibrado['club']} ({mas_equilibrado['jugadores_elite']} jugadores de élite)"
    )

    print("\n" + "=" * 80)
    return equipos_ordenados


print("Módulo de simulación y análisis comparativo completado")
print("Sistema integrado listo para análisis profesional")
print()

# %%
# ===============================
# FASE 4: DEMOSTRACIÓN PROFESIONAL CON DATOS REALES (5 minutos)
# ===============================

print("=" * 80)
print("              DEMOSTRACIÓN: ANÁLISIS DE EL CLÁSICO")
print("                    Sistema Integrado Profesional")
print("=" * 80)
print()

# ¿Estás listo para poner a prueba tu sistema con el partido más importante del mundo?

print("INICIALIZANDO SISTEMA DE ANÁLISIS...")
print("Procesando datos de las dos superpotencias del fútbol mundial...")
print()

# DATOS REALES SIMPLIFICADOS TEMPORADA 2023-24
# (En un sistema real, estos datos vendrían de bases de datos especializadas)

real_madrid_plantilla = [
    {
        "nombre": "Vinícius Jr",
        "posicion": "Extremo",
        "estadisticas": {
            "goles": 24,
            "asistencias": 11,
            "partidos": 39,
            "pases_exitosos": 892,
            "total_pases": 1180,
        },
    },
    {
        "nombre": "Jude Bellingham",
        "posicion": "Mediocampista",
        "estadisticas": {
            "goles": 23,
            "asistencias": 13,
            "partidos": 42,
            "pases_exitosos": 1456,
            "total_pases": 1680,
        },
    },
    {
        "nombre": "Luka Modrić",
        "posicion": "Mediocampista",
        "estadisticas": {
            "goles": 3,
            "asistencias": 8,
            "partidos": 46,
            "pases_exitosos": 1998,
            "total_pases": 2234,
        },
    },
    {
        "nombre": "Antonio Rüdiger",
        "posicion": "Defensa",
        "estadisticas": {
            "goles": 2,
            "asistencias": 2,
            "partidos": 48,
            "pases_exitosos": 2156,
            "total_pases": 2398,
        },
    },
]

barcelona_plantilla = [
    {
        "nombre": "Robert Lewandowski",
        "posicion": "Delantero",
        "estadisticas": {
            "goles": 26,
            "asistencias": 8,
            "partidos": 49,
            "pases_exitosos": 756,
            "total_pases": 943,
        },
    },
    {
        "nombre": "Pedri",
        "posicion": "Mediocampista",
        "estadisticas": {
            "goles": 7,
            "asistencias": 8,
            "partidos": 37,
            "pases_exitosos": 1834,
            "total_pases": 2089,
        },
    },
    {
        "nombre": "Gavi",
        "posicion": "Mediocampista",
        "estadisticas": {
            "goles": 2,
            "asistencias": 13,
            "partidos": 51,
            "pases_exitosos": 2145,
            "total_pases": 2456,
        },
    },
    {
        "nombre": "Ronald Araújo",
        "posicion": "Defensa",
        "estadisticas": {
            "goles": 6,
            "asistencias": 1,
            "partidos": 37,
            "pases_exitosos": 1567,
            "total_pases": 1789,
        },
    },
]

# FORMA RECIENTE DE AMBOS EQUIPOS (últimos 5 partidos antes de El Clásico)
madrid_forma_reciente = ["V", "V", "E", "V", "V"]  # Excelente: 13/15 puntos
barcelona_forma_reciente = ["V", "D", "V", "V", "E"]  # Buena: 10/15 puntos

print("ANALIZANDO REAL MADRID...")
# Ejecutamos nuestro sistema profesional
madrid_analisis = analizar_plantilla_completa(
    "Real Madrid", real_madrid_plantilla, madrid_forma_reciente
)

print("ANALIZANDO FC BARCELONA...")
barcelona_analisis = analizar_plantilla_completa(
    "FC Barcelona", barcelona_plantilla, barcelona_forma_reciente
)

print("\n" + "=" * 80)
print("                    REPORTE EJECUTIVO")
print("=" * 80)

# PRESENTACIÓN ESTILO JUNTA DIRECTIVA
print(
    f"""
REAL MADRID CF
▫️ Nivel de plantilla: {madrid_analisis['resumen_ejecutivo']['nivel_plantilla']}
▫️ Calidad promedio: {madrid_analisis['resumen_ejecutivo']['promedio_calidad']}/100
▫️ Momento deportivo: {madrid_analisis['resumen_ejecutivo']['momento_deportivo']}
▫️ Forma reciente: {madrid_analisis['resumen_ejecutivo']['puntos_forma']} puntos
▫️ Potencial ofensivo: {madrid_analisis['metricas_globales']['productividad_ofensiva']} participaciones en gol
▫️ Objetivo realista: {madrid_analisis['resumen_ejecutivo']['objetivo_realista']}

FC BARCELONA  
▫️ Nivel de plantilla: {barcelona_analisis['resumen_ejecutivo']['nivel_plantilla']}
▫️ Calidad promedio: {barcelona_analisis['resumen_ejecutivo']['promedio_calidad']}/100
▫️ Momento deportivo: {barcelona_analisis['resumen_ejecutivo']['momento_deportivo']}
▫️ Forma reciente: {barcelona_analisis['resumen_ejecutivo']['puntos_forma']} puntos
▫️ Potencial ofensivo: {barcelona_analisis['metricas_globales']['productividad_ofensiva']} participaciones en gol
▫️ Objetivo realista: {barcelona_analisis['resumen_ejecutivo']['objetivo_realista']}
"""
)

print("=" * 80)
print("                PREDICCIÓN DEL ENFRENTAMIENTO")
print("=" * 80)

# SIMULACIÓN AVANZADA DEL CLÁSICO
prediccion_clasico = simular_enfrentamiento_elite(madrid_analisis, barcelona_analisis)

print(
    f"""
{prediccion_clasico['enfrentamiento']}

PREDICCIÓN DEL SISTEMA:
   • Marcador simulado: {prediccion_clasico['prediccion']['marcador_simulado']}
   • Resultado predicho: {prediccion_clasico['prediccion']['resultado']}

PROBABILIDADES:
   • Victoria Real Madrid: {prediccion_clasico['probabilidades']['victoria_real_madrid']}%
   • Empate: {prediccion_clasico['probabilidades']['empate']}%  
   • Victoria Barcelona: {prediccion_clasico['probabilidades']['victoria_fc_barcelona']}%

ANÁLISIS TÁCTICO:
   {prediccion_clasico['analisis_previo']['analisis_tactico']}

FACTORES CLAVE:"""
)

for factor in prediccion_clasico["analisis_previo"]["factores_clave"]:
    print(f"   • {factor}")

print(
    f"""
FUERZA RELATIVA:
   • Real Madrid: {prediccion_clasico['analisis_previo']['fuerza_relativa']['Real Madrid']}/100
   • FC Barcelona: {prediccion_clasico['analisis_previo']['fuerza_relativa']['FC Barcelona']}/100
"""
)

print("=" * 80)
print("           ¡ANÁLISIS COMPLETADO EXITOSAMENTE!")
print("=" * 80)

print(
    """
LOGROS DESBLOQUEADOS:
- Sistema de evaluación individual de élite mundial
- Análisis de plantilla completa como clubes profesionales  
- Simulador de enfrentamientos con múltiples variables
- Reportes ejecutivos dignos de juntas directivas
- Herramientas comparativas de nivel Champions League

¡Has creado un sistema tan sofisticado como los que usan 
   los departamentos de análisis del Real Madrid y Barcelona!
"""
)

print("\nREFLEXIÓN FINAL:")
print("¿Te das cuenta de que acabas de integrar funciones, módulos,")
print("lógica compleja y presentación profesional en una sola herramienta?")
print()
print("¡Esto es exactamente lo que hacen los analistas de datos")
print("en los mejores clubes del mundo!")

# %% [markdown]
# ---
#
# ## ¡Tu turno de brillar como analista profesional!
#
# **Momento de maestría personal**: Has visto el sistema funcionando con el Real Madrid y Barcelona. Ahora **¿podrías aplicar estas herramientas a tu equipo favorito?**
#
# ### Desafío de personalización (10 minutos):
#
# **Tu misión**: Adaptar el sistema integrado para analizar tu equipo favorito o crear una comparación entre equipos que te interesen.
#
# #### Opciones de proyecto personal:
#
# 1. **Analizar tu equipo local**: ¿Cómo evaluarías a los jugadores de tu equipo de la ciudad?
#
# 2. **Comparar ligas diferentes**: ¿Real Madrid vs. Manchester City vs. PSG?
#
# 3. **Análisis histórico**: ¿Cómo sería el Barcelona de Messi vs. el Real Madrid actual?
#
# 4. **Crear tu equipo ideal**: ¿Combinar jugadores de diferentes equipos para tu "Dream Team"?
#
# #### Reflexión estratégica:
#
# **Pregunta de diseño**: ¿Qué modificaciones harías al sistema para que se adapte mejor a tu análisis específico?
#
# - ¿Añadirías nuevas métricas?
# - ¿Cambiarías los criterios de evaluación?
# - ¿Incluirías factores como la edad o el valor de mercado?
# - ¿Cómo personalizarías el reporte final?
#
# #### Código base para tu personalización:
#
# ```python
# # Plantilla para tu análisis personalizado
# mi_equipo_datos = [
#     {
#         "nombre": "[Nombre del jugador]",
#         "posicion": "[Posición]", 
#         "estadisticas": {
#             "goles": 0, "asistencias": 0, "partidos": 0,
#             "pases_exitosos": 0, "total_pases": 0
#         }
#     },
#     # Añade más jugadores...
# ]
#
# mi_equipo_forma = ['V', 'E', 'D', 'V', 'E']  # Últimos 5 resultados
#
# # Ejecuta tu análisis
# mi_analisis = analizar_plantilla_completa("Mi Equipo", mi_equipo_datos, mi_equipo_forma)
# ```
#
# **Pregunta de reflexión**: ¿Qué insights descubrirías sobre tu equipo que no conocías antes?

# %% [markdown]
# ## 2. Experimentando con nuestras primeras "jugadas": ¿Cómo creamos funciones útiles?
#
# ### ¿Listos para crear tus primeras herramientas personalizadas?
#
# **Pregunta de transición**: Ahora que entendemos el concepto, ¿qué tal si creamos nuestras primeras funciones simples?
#
# ### 2.1 Funciones Simples - ¿Cómo empezamos?
#
# **Desafío conceptual**: ¿Cuál sería la función más simple que podrías imaginar? ¿Una que simplemente salude o dé un mensaje?

# %%
# ¿Cómo crearías una función que simplemente haga algo útil?
# Empecemos con lo más básico


def saludar_equipo():
    """¿Qué hace esta función? ¿Por qué incluimos esta documentación?"""
    print("¡Hola equipo! ¡Listos para el análisis!")
    print("Vamos a analizar datos deportivos con Python")


# ¿Cómo "ejecutamos" o "llamamos" a nuestra función?
saludar_equipo()  # ¿Qué crees que pasa cuando ejecutas esto?

print("\n" + "=" * 50)


# ¿Qué diferencia hay entre una función que hace algo y una que devuelve algo?
def obtener_mensaje_motivacional():
    """¿Notas la diferencia? Esta función retorna un valor"""
    return "¡El análisis de datos es como el fútbol: requiere práctica y estrategia!"


# ¿Cómo capturarías el resultado de una función?
mensaje = obtener_mensaje_motivacional()  # ¿Qué guarda la variable mensaje?
print(mensaje)

# ¿O podrías usar el resultado directamente?
print(obtener_mensaje_motivacional())

# Pregunta de reflexión: ¿Cuál es la ventaja de que una función retorne un valor vs. que solo imprima?

# %% [markdown]
# ### 2.2 Funciones con Parámetros - ¿Cómo hacemos nuestras funciones más flexibles?
#
# **Pregunta de limitación**: Las funciones anteriores siempre hacen exactamente lo mismo. ¿Qué pasaría si quisieras saludar a diferentes jugadores por nombre?
#
# **Analogía práctica**: Una jugada de corner siempre tiene los mismos principios, pero ¿se adapta según qué jugadores están en el campo? ¿Cómo harías que tus funciones se adapten a diferentes situaciones?

# %%
# ¿Cómo harías una función que se adapte a diferentes situaciones?
# Los parámetros son como "variables de entrada"


def saludar_jugador(nombre):
    """¿Cómo esta función es más flexible que la anterior?"""
    print(f"¡Hola {nombre}! Bienvenido al análisis")


# ¿Qué pasaría si necesitas más información?
def presentar_jugador(nombre, posicion, edad):
    """¿Por qué es útil tener múltiples parámetros?"""
    return f"{nombre} es {posicion} y tiene {edad} años"


# ¿Y si algunos parámetros son opcionales?
def calcular_puntos(victorias, empates, derrotas=0):
    """¿Qué hace el =0 en derrotas? ¿Por qué sería útil?"""
    return victorias * 3 + empates * 1 + derrotas * 0


# ¿Cómo usarías estas funciones más flexibles?
saludar_jugador("Messi")  # ¿Qué valor toma el parámetro nombre?
saludar_jugador("Ronaldo")  # ¿Y ahora?

print("\nPresentaciones:")
print(
    presentar_jugador("Lionel Messi", "Delantero", 36)
)  # ¿En qué orden van los parámetros?
print(presentar_jugador("Sergio Ramos", "Defensa", 37))

print("\nCálculo de puntos:")
print(
    f"Equipo A: {calcular_puntos(10, 5, 3)} puntos"
)  # ¿Qué valor tiene cada parámetro?
print(f"Equipo B: {calcular_puntos(12, 4)} puntos")  # ¿Qué valor toma derrotas aquí?

# Pregunta de diseño: ¿Cuándo sería útil tener parámetros con valores por defecto?

# %% [markdown]
# ### 2.3 Funciones para Análisis Deportivo - ¿Cómo creamos herramientas especializadas?
#
# **Pregunta de aplicación**: Ahora que sabes crear funciones básicas, ¿cómo crearías herramientas específicas para analizar datos deportivos?
#
# **Desafío conceptual**: ¿Qué funciones serían más valiosas para un analista deportivo? ¿Cuáles usarías una y otra vez en diferentes análisis?

# %%
# ¿Qué herramientas de análisis serían útiles para cualquier analista deportivo?
# Creemos funciones especializadas que puedas reutilizar


def calcular_promedio_goles(lista_goles):
    """¿Por qué sería importante validar que la lista no esté vacía?"""
    if len(lista_goles) == 0:  # ¿Qué pasaría sin esta validación?
        return 0
    return sum(lista_goles) / len(lista_goles)


def determinar_resultado(goles_local, goles_visitante):
    """¿Cómo automatizarías la determinación de resultados?"""
    if goles_local > goles_visitante:
        return "Victoria Local"
    elif goles_visitante > goles_local:
        return "Victoria Visitante"
    else:
        return "Empate"


def calcular_eficiencia(goles, tiros):
    """¿Por qué necesitas validar que tiros no sea cero?"""
    if tiros == 0:  # ¿Qué error matemático evitas?
        return 0
    return (goles / tiros) * 100


# ¿Podrías crear una función más compleja que combine múltiples análisis?
def analizar_jugador(nombre, goles, partidos, posicion):
    """¿Cómo evalúas el rendimiento según la posición del jugador?"""
    promedio_goles = goles / partidos if partidos > 0 else 0

    # ¿Por qué diferentes estándares para diferentes posiciones?
    if posicion.lower() == "delantero":
        if promedio_goles >= 0.8:
            rendimiento = "Excelente"
        elif promedio_goles >= 0.5:
            rendimiento = "Bueno"
        else:
            rendimiento = "Necesita mejorar"
    else:  # Para centrocampistas, defensas, etc.
        if promedio_goles >= 0.3:
            rendimiento = "Excelente"
        elif promedio_goles >= 0.1:
            rendimiento = "Bueno"
        else:
            rendimiento = "Aceptable"

    # ¿Por qué retornar un diccionario en lugar de solo texto?
    return {
        "nombre": nombre,
        "promedio_goles": round(promedio_goles, 2),
        "rendimiento": rendimiento,
        "total_goles": goles,
        "partidos_jugados": partidos,
    }


# ¿Cómo pondrías a prueba estas herramientas?
goles_equipo = [2, 1, 3, 0, 2, 1, 4]
print(f"Promedio de goles: {calcular_promedio_goles(goles_equipo):.2f}")

print(f"\nResultado del partido: {determinar_resultado(2, 1)}")
print(f"Eficiencia de gol: {calcular_eficiencia(8, 25):.1f}%")

print("\nAnálisis de jugadores:")
messi = analizar_jugador("Messi", 25, 30, "Delantero")
busquets = analizar_jugador("Busquets", 3, 28, "Centrocampista")

print(
    f"{messi['nombre']}: {messi['promedio_goles']} goles/partido - {messi['rendimiento']}"
)
print(
    f"{busquets['nombre']}: {busquets['promedio_goles']} goles/partido - {busquets['rendimiento']}"
)

# Pregunta de reflexión: ¿Qué ventajas tiene crear estas funciones especializadas vs. calcular todo manualmente cada vez?

# %% [markdown]
# ### 2.4 Funciones con Múltiples Valores de Retorno - ¿Cómo obtenemos varios resultados a la vez?
#
# **Pregunta de eficiencia**: ¿Qué pasa si quieres calcular varias estadísticas de una lista al mismo tiempo? ¿Crearías una función para cada una o encontrarías una forma más elegante?
#
# **Situación práctica**: Imagina que analizas el rendimiento de un jugador y quieres saber simultáneamente: máximo, mínimo, promedio y total. ¿Cómo lo harías?

# %%
# ¿Cómo harías que una función calcule múltiples estadísticas de una vez?
# Python permite retornar múltiples valores simultáneamente


def estadisticas_basicas(lista_numeros):
    """¿Por qué es más eficiente calcular todo junto?"""
    if not lista_numeros:  # ¿Qué evita esta validación?
        return 0, 0, 0, 0

    total = sum(lista_numeros)
    promedio = total / len(lista_numeros)
    maximo = max(lista_numeros)
    minimo = min(lista_numeros)

    # ¿Cómo retornamos múltiples valores? ¿Qué estructura crea Python?
    return total, promedio, maximo, minimo


# ¿Podrías crear una función que analice un partido completo?
def analizar_partido(equipo_local, goles_local, equipo_visitante, goles_visitante):
    """¿Qué información completa podrías extraer de un solo partido?"""
    total_goles = goles_local + goles_visitante
    diferencia = abs(goles_local - goles_visitante)
    resultado = determinar_resultado(
        goles_local, goles_visitante
    )  # ¿Reutilizando función anterior?

    # ¿Cómo determinarías el ganador específico?
    if goles_local > goles_visitante:
        ganador = equipo_local
    elif goles_visitante > goles_local:
        ganador = equipo_visitante
    else:
        ganador = "Empate"

    # ¿Podrías clasificar qué tan emocionante fue el partido?
    if total_goles >= 4:
        emocion = "Muy emocionante"
    elif total_goles >= 2:
        emocion = "Emocionante"
    else:
        emocion = "Poco emocionante"

    # ¿Qué ventaja tiene retornar toda esta información junta?
    return resultado, ganador, total_goles, diferencia, emocion


# ¿Cómo "desempaquetas" múltiples valores?
goles_temporada = [2, 1, 0, 3, 1, 2, 4, 0, 1, 2]

# ¿Notas cómo cada variable recibe un valor específico?
total, promedio, maximo, minimo = estadisticas_basicas(goles_temporada)

print("=== ESTADÍSTICAS DE LA TEMPORADA ===")
print(f"Total de goles: {total}")
print(f"Promedio por partido: {promedio:.2f}")
print(f"Máximo de goles en un partido: {maximo}")
print(f"Mínimo de goles en un partido: {minimo}")

print("\n=== ANÁLISIS DE PARTIDO ===")
# ¿Cómo recibes múltiples resultados de una función?
resultado, ganador, total_goles, diferencia, emocion = analizar_partido(
    "Barcelona", 3, "Real Madrid", 2
)

print(f"Resultado: {resultado}")
print(f"Ganador: {ganador}")
print(f"Total de goles: {total_goles}")
print(f"Diferencia: {diferencia}")
print(f"Nivel de emoción: {emocion}")

# Pregunta de diseño: ¿Cuándo prefieres una función que retorna múltiples valores vs. varias funciones separadas?

# %% [markdown]
# ## 3. Módulos: ¿Cómo usamos herramientas que otros ya crearon?
#
# ### Pregunta de eficiencia: ¿Deberías reinventar la rueda?
#
# **Reflexión práctica**: Imagina que necesitas calcular la raíz cuadrada de un número para una fórmula estadística. ¿Crearías tu propia función desde cero o usarías una que ya existe y está probada?
#
# **Analogía deportiva**: Los equipos de fútbol no fabrican sus propios balones, ¿verdad? Usan equipment especializado creado por expertos. ¿Cómo funciona esto en programación?
#
# ### 3.1 Descubriendo módulos: ¿Qué son estas "cajas de herramientas"?
#
# **Pregunta conceptual**: ¿Qué pasaría si Python viniera con miles de funciones pre-construidas para matemáticas, fechas, números aleatorios, etc., pero todas estuvieran mezcladas?
#
# **Descubrimiento**: Los **módulos** son como cajas de herramientas organizadas: cada una contiene funciones relacionadas que puedes "importar" cuando las necesites.
#
# ### 3.2 Módulos Integrados - ¿Qué herramientas vienen incluidas?
#
# **Pregunta de exploración**: ¿Qué tipo de herramientas matemáticas, de fechas o de aleatoriedad podrían ser útiles en análisis deportivo?

# %%
# ¿Cómo "importas" cajas de herramientas especializadas?
# Cada import trae un conjunto de funciones relacionadas

import math  # ¿Qué tipo de herramientas matemáticas esperarías?
import random  # ¿Para qué usarías números aleatorios en deportes?
import datetime  # ¿Cómo manejarías fechas y horarios de partidos?

# ¿Cómo usas funciones de un módulo específico?
print("=== MÓDULO MATH ===")
promedio_goles = 2.7
print(f"Promedio: {promedio_goles}")
print(
    f"Redondeado hacia arriba: {math.ceil(promedio_goles)}"
)  # ¿Para qué sirve ceil()?
print(f"Redondeado hacia abajo: {math.floor(promedio_goles)}")  # ¿Y floor()?
print(f"Raíz cuadrada: {math.sqrt(16)}")  # ¿En qué estadísticas usarías sqrt()?

print("\n=== MÓDULO RANDOM ===")
equipos = ["Barcelona", "Real Madrid", "Atletico", "Valencia"]
print(f"Equipo aleatorio: {random.choice(equipos)}")  # ¿Cómo simularías sorteos?
print(
    f"Resultado aleatorio: {random.randint(0, 5)} - {random.randint(0, 5)}"
)  # ¿Para simular partidos?

# ¿Cómo simularías una decisión de campo en un partido?
lado = random.choice(["Águila", "Sello"])
print(f"Tirada de moneda: {lado}")

print("\n=== MÓDULO DATETIME ===")
ahora = datetime.datetime.now()  # ¿Cómo obtienes la fecha/hora actual?
print(f"Fecha y hora actual: {ahora}")
print(f"Solo fecha: {ahora.date()}")  # ¿Y si solo necesitas la fecha?
print(f"Solo hora: {ahora.time()}")  # ¿O solo la hora?

# ¿Cómo crearías la fecha de un partido específico?
fecha_partido = datetime.date(2024, 12, 25)
print(f"Próximo partido: {fecha_partido}")

# Pregunta de aplicación: ¿En qué otros análisis deportivos serían útiles estos módulos?

# %% [markdown]
# ### 3.3 Diferentes Formas de Importar - ¿Cómo optimizas tu caja de herramientas?
#
# **Pregunta de eficiencia**: ¿Qué pasaría si solo necesitas un destornillador de una caja completa de herramientas? ¿Cargarías toda la caja o solo tomarías lo que necesitas?
#
# **Situación práctica**: ¿Cómo harías tu código más limpio y eficiente al importar solo lo que realmente usas?

# %%
# ¿Hay formas más eficientes de importar solo lo que necesitas?
# Exploremos diferentes estrategias de importación

# 1. ¿Cómo importas funciones específicas en lugar del módulo completo?
from math import sqrt, ceil, floor  # ¿Solo las funciones que usarás?
from random import choice, randint  # ¿Más directo, no?

# ¿Notas la diferencia? Ahora puedes usar directamente sin prefijos
print(f"Raíz cuadrada de 25: {sqrt(25)}")  # En lugar de math.sqrt(25)
print(f"Número aleatorio: {randint(1, 10)}")  # En lugar de random.randint(1, 10)

# 2. ¿Qué pasa si los nombres de los módulos son muy largos?
import datetime as dt  # ¿Cómo acortas nombres largos?
import random as rnd  # ¿Alias más convenientes?

print(f"\nFecha actual: {dt.date.today()}")  # ¿Más fácil que datetime.date.today()?
print(f"Número aleatorio: {rnd.random()}")  # ¿Qué hace random()?

# 3. ¿Existe una forma de importar TODO? (Ten cuidado con esta)
# from math import *  # ¿Por qué esto podría ser problemático?


# ¿Cómo aplicarías estos conceptos en funciones deportivas?
def simular_partido(equipo1, equipo2):
    """¿Cómo simularías un partido realista?"""
    goles1 = randint(0, 4)  # ¿Rango realista de goles?
    goles2 = randint(0, 4)

    fecha = dt.date.today()  # ¿Fecha del partido simulado?
    resultado = determinar_resultado(goles1, goles2)  # ¿Reutilizando función propia?

    # ¿Qué información sería útil retornar?
    return {
        "fecha": fecha,
        "equipo1": equipo1,
        "equipo2": equipo2,
        "goles1": goles1,
        "goles2": goles2,
        "resultado": resultado,
    }


# ¿Cómo simularías múltiples partidos automáticamente?
print("\n=== SIMULACIÓN DE PARTIDOS ===")
for i in range(3):  # ¿Cuántos partidos simular?
    equipos = ["Barcelona", "Real Madrid", "Atletico", "Valencia"]
    equipo1 = choice(equipos)
    equipos.remove(equipo1)  # ¿Por qué quitar el equipo seleccionado?
    equipo2 = choice(equipos)

    partido = simular_partido(equipo1, equipo2)
    print(
        f"{partido['equipo1']} {partido['goles1']} - {partido['goles2']} {partido['equipo2']} ({partido['resultado']})"
    )

# Pregunta de decisión: ¿Cuándo usarías cada tipo de importación? ¿Qué ventajas y desventajas ves?

# %% [markdown]
# ### 3.4 Creando Funciones Avanzadas con Módulos - ¿Cómo combinamos herramientas especializadas?
#
# **Pregunta de síntesis**: ¿Qué pasaría si combinaras tus propias funciones con módulos especializados para crear análisis realmente poderosos?
#
# **Desafío de escalabilidad**: ¿Cómo analizarías una temporada completa de 30+ partidos de forma automática y profesional?

# %%
# ¿Cómo crearías funciones verdaderamente profesionales usando módulos especializados?
# Vamos a combinar nuestras habilidades con herramientas estadísticas avanzadas

import statistics  # ¿Qué análisis estadísticos profesionales podrías hacer?
from collections import Counter  # ¿Cómo contarías frecuencias automáticamente?


def analizar_temporada_completa(resultados):
    """¿Cómo analizarías una temporada completa automáticamente?

    Args:
        resultados: Lista de tuplas (goles_local, goles_visitante)

    Returns:
        Diccionario con estadísticas completas de la temporada
    """
    if not resultados:  # ¿Siempre validar datos de entrada?
        return {"error": "No hay resultados para analizar"}

    # ¿Cómo extraerías datos específicos de tuplas?
    todos_goles_local = [goles[0] for goles in resultados]  # List comprehension
    todos_goles_visitante = [goles[1] for goles in resultados]
    todos_goles = todos_goles_local + todos_goles_visitante

    # ¿Cómo calcularías goles totales por partido?
    goles_por_partido = [local + visitante for local, visitante in resultados]

    # ¿Cómo clasificarías automáticamente todos los resultados?
    tipos_resultado = []
    for local, visitante in resultados:
        if local > visitante:
            tipos_resultado.append("Victoria Local")
        elif visitante > local:
            tipos_resultado.append("Victoria Visitante")
        else:
            tipos_resultado.append("Empate")

    # ¿Cómo contarías automáticamente cada tipo de resultado?
    conteo_resultados = Counter(tipos_resultado)  # ¡Módulo especializado!

    # ¿Qué estadísticas profesionales podrías calcular?
    estadisticas_temporada = {
        "total_partidos": len(resultados),
        "promedio_goles_partido": statistics.mean(
            goles_por_partido
        ),  # ¿Módulo statistics?
        "mediana_goles_partido": statistics.median(
            goles_por_partido
        ),  # ¿Diferencia con promedio?
        "max_goles_partido": max(goles_por_partido),
        "min_goles_partido": min(goles_por_partido),
        "desviacion_estandar": (
            statistics.stdev(goles_por_partido) if len(goles_por_partido) > 1 else 0
        ),
        "ventaja_local": sum(todos_goles_local)
        > sum(todos_goles_visitante),  # ¿Hay ventaja de campo?
        "porcentaje_victorias_local": (
            conteo_resultados["Victoria Local"] / len(resultados)
        )
        * 100,
        "porcentaje_empates": (conteo_resultados["Empate"] / len(resultados)) * 100,
        "porcentaje_victorias_visitante": (
            conteo_resultados["Victoria Visitante"] / len(resultados)
        )
        * 100,
        "distribucion_resultados": dict(conteo_resultados),
    }

    return estadisticas_temporada


def generar_reporte_temporada(estadisticas):
    """¿Cómo convertirías datos en un reporte profesional legible?"""
    if "error" in estadisticas:
        return estadisticas["error"]

    # ¿Cómo formatearías un reporte profesional?
    reporte = f"""
=== REPORTE DE TEMPORADA ===

ESTADÍSTICAS GENERALES:
• Total de partidos: {estadisticas['total_partidos']}
• Promedio de goles por partido: {estadisticas['promedio_goles_partido']:.2f}
• Mediana de goles por partido: {estadisticas['mediana_goles_partido']}
• Partido con más goles: {estadisticas['max_goles_partido']}
• Partido con menos goles: {estadisticas['min_goles_partido']}
• Desviación estándar: {estadisticas['desviacion_estandar']:.2f}

VENTAJA LOCAL:
• ¿Hay ventaja local?: {'Sí' if estadisticas['ventaja_local'] else 'No'}
• Victorias locales: {estadisticas['porcentaje_victorias_local']:.1f}%
• Empates: {estadisticas['porcentaje_empates']:.1f}%
• Victorias visitantes: {estadisticas['porcentaje_victorias_visitante']:.1f}%

DISTRIBUCIÓN DE RESULTADOS:
"""

    for tipo, cantidad in estadisticas["distribucion_resultados"].items():
        reporte += f"• {tipo}: {cantidad} partidos\n"

    return reporte


# ¿Cómo probarías estas funciones avanzadas?
resultados_liga = [
    (2, 1),
    (0, 0),
    (3, 2),
    (1, 1),
    (4, 0),
    (2, 3),
    (1, 0),
    (2, 2),
    (0, 1),
    (3, 1),
    (1, 2),
    (2, 0),
    (1, 1),
    (3, 3),
    (0, 2),
]

# ¿Cómo usarías tus herramientas profesionales?
stats = analizar_temporada_completa(resultados_liga)
reporte = generar_reporte_temporada(stats)
print(reporte)

# Pregunta de síntesis: ¿Cómo estas funciones cambiarían tu capacidad de análisis deportivo?

# %% [markdown]
# ---
#
# # SÍNTESIS FINAL: ¿Qué has descubierto sobre crear sistemas elegantes y reutilizables?
#
# ## Reflexión sobre las 3 sesiones (150 minutos totales)
#
# ### SESIÓN 1: ¿Cómo crear "jugadas programadas" reutilizables?
# **Lo que dominamos ahora**:
# - Diseñar funciones como "jugadas maestras" que se ejecutan perfectamente cada vez
# - Crear análisis multidimensionales que consideran posición, forma y contexto
# - Construir evaluaciones automáticas tan sofisticadas como las de clubes profesionales
# - Aplicar la mentalidad de "elegancia reutilizable" en lugar de código repetitivo
#
# ### SESIÓN 2: ¿Cómo acceder a la sabiduría colectiva mundial?
# **Lo que revelamos**:
# - Aprovechar herramientas matemáticas y estadísticas de nivel profesional
# - Importar conocimiento especializado creado por expertos mundiales
# - Combinar módulos externos con nuestras funciones personalizadas
# - Crear nuestros propios "departamentos especializados" organizados por función
#
# ### SESIÓN 3: ¿Cómo integrar todo en sistemas de élite mundial?
# **Lo que construimos**:
# - Sistema completo de análisis individual, colectivo y comparativo
# - Simulador avanzado de enfrentamientos con múltiples variables
# - Reportes ejecutivos dignos de juntas directivas profesionales
# - Herramientas integradas que rivalizan con departamentos de análisis reales
#
# ---
#
# ## Transformación de identidad: ¿Quién eres ahora como programador?
#
# **Pregunta de transformación personal**: ¿Recuerdas cuando solo podías ejecutar código línea por línea? **¿Cómo te sientes ahora que puedes crear sistemas completos que otros analistas profesionales usarían?**
#
# ### ¿Qué ha cambiado en tu forma de abordar problemas complejos?
#
# **Antes**: "¿Cómo resuelvo este problema específico?"
# **Ahora**: "¿Cómo creo una herramienta que resuelva esta categoría de problemas para siempre?"
#
# **Antes**: "Voy a calcular esto manualmente para este caso"
# **Ahora**: "Voy a diseñar un sistema que automatice esto para cualquier caso"
#
# **Antes**: "Necesito escribir código desde cero cada vez"
# **Ahora**: "¿Qué herramientas existentes puedo combinar con mis creaciones?"
#
# ### Habilidades de élite que ahora posees:
#
# #### **Arquitecto de Sistemas**
# - Diseñas funciones especializadas para cada aspecto del análisis
# - Organizas código en módulos coherentes y mantenibles
# - Integras múltiples componentes en sistemas unificados
#
# #### **Estratega de Reutilización**
# - Creas herramientas que funcionan con cualquier conjunto de datos
# - Evitas repetir trabajo mediante funciones elegantes
# - Construyes sobre el conocimiento de expertos mundiales
#
# #### **Analista de Datos Profesional**  
# - Produces reportes ejecutivos con métricas sofisticadas
# - Simulas escenarios complejos con modelos probabilísticos
# - Presentas insights de manera clara y accionable
#
# #### **Integrador de Conocimiento**
# - Combinas herramientas especializadas con creatividad personal
# - Adaptas soluciones existentes a problemas específicos
# - Colaboras efectivamente con sistemas creados por otros
#
# ---
#
# ## ¿Qué puedes crear ahora que era imposible antes?
#
# **Reflexión de capacidades**:
#
# ### Análisis que antes tomaban horas, ahora toman segundos:
# - Evaluación completa de plantillas de 25+ jugadores
# - Comparación automática entre múltiples equipos
# - Simulación de temporadas completas con miles de partidos
# - Generación de reportes ejecutivos profesionales
#
# ### Sistemas que antes requerían equipos especializados:
# - Departamento de scouting automatizado
# - Centro de análisis táctico personalizado  
# - Simulador de mercado de fichajes
# - Plataforma de inteligencia competitiva
#
# **Pregunta reveladora**: ¿Te das cuenta de que ahora piensas como los arquitectos de sistemas que trabajan en el Manchester City, Real Madrid o FC Barcelona?
#
# ---
#
# ## Vista previa del próximo nivel: ¿Estás listo para manejar Big Data?
#
# **Pregunta de escalabilidad**: Tu sistema actual funciona perfectamente con datos que puedes escribir manualmente. **¿Pero qué pasaría si quisieras analizar:**
# - 50,000 partidos de los últimos 5 años
# - Estadísticas en tiempo real de 500 jugadores
# - Datos de transferencias de toda Europa
# - Métricas avanzadas como xG, heatmaps, distancias recorridas?
#
# ### Lo que descubriremos en Semana 4:
# **Pandas y NumPy**: Las herramientas que usan los departamentos de Big Data de los clubes más grandes del mundo.
#
# - **DataFrames**: Manejar millones de datos como hojas de cálculo superinteligentes
# - **Operaciones vectorizadas**: Cálculos instantáneos en datasets masivos
# - **Filtrado avanzado**: Encontrar patrones en océanos de información
# - **Agregaciones complejas**: Estadísticas que revelan insights ocultos
# - **Integración de fuentes**: Combinar datos de múltiples orígenes
#
# **Pregunta motivadora**: ¿Podrías crear análisis tan profundos que cambien la forma en que se entiende el fútbol moderno?
#
# ---
#
# ## Reflexión final: ¿Qué herramienta te gustaría crear?
#
# **Momento de visión personal**: Si tuvieras acceso a todos los datos del fútbol mundial, **¿qué sistema crearías que nadie más ha construido?**
#
# **Tu evolución**: 
# - **Semana 1**: Aprendiste el lenguaje básico
# - **Semana 2**: Dominaste la lógica y automatización
# - **Semana 3**: Te convertiste en arquitecto de sistemas
#
# **Próximo desafío**: Manejar la escala y complejidad del análisis deportivo moderno.
#
# **¿Estás listo para trabajar con datasets reales tan grandes como los que usan en la Champions League?**

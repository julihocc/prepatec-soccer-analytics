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

# Semana 8: ¿Cómo los números cuentan historias deportivas?

## ¿Alguna vez te has preguntado cómo los analistas transforman montañas de datos en insights precisos?

**Reflexión inicial**: Cuando ves las estadísticas de la Liga MX, observas miles de números. ¿Pero cómo distinguir lo importante de lo irrelevante? ¿Cómo saber si un promedio de 2.1 goles es excepcional o normal?

### Pregunta motivadora para la semana:
Si fueras analista del Toluca y tuvieras datos de 500 jugadores para reforzar el equipo, ¿cómo resumirías toda esa información para tomar la decisión correcta?

---

## ESTRUCTURA SEMANAL: 3 Sesiones de Descubrimiento

### SESIÓN 1: ¿Qué secretos revelan los resúmenes estadísticos? (50 min)
**Pregunta guía**: ¿Cómo condensar miles de números en insights útiles?
- ¿Qué diferencia hay entre datos crudos y conocimiento deportivo?
- ¿Por qué algunos promedios engañan y otros iluminan?
- ¿Cómo detectar patrones ocultos en el rendimiento?

### SESIÓN 2: ¿Cómo visualizar la esencia de los datos? (50 min)  
**Pregunta guía**: ¿Qué revelan los gráficos que los números solos no pueden?
- ¿Cómo las distribuciones muestran la "personalidad" de un equipo?
- ¿Qué patrones emergen cuando comparas grupos visualmente?
- ¿Por qué la variabilidad es tan importante como el promedio?

### SESIÓN 3: ¿Cómo aplicar estadística descriptiva profesionalmente? (50 min)
**Pregunta guía**: ¿Cómo tomar decisiones deportivas basadas en evidencia?
- ¿Qué métricas son más confiables para evaluar rendimiento?
- ¿Cómo detectar sesgos y limitaciones en tus análisis?
- ¿Qué insights estadísticos buscan los equipos profesionales?

---

## ¿Por qué dominar la estadística descriptiva en el fútbol?

**Pregunta reflexiva**: ¿Has notado que los mejores analistas deportivos no solo presentan números, sino que cuentan historias convincentes? ¿Será porque dominan el arte de hacer "hablar" a los datos?

### La revolución del análisis estadístico en el deporte:
- **¿Sabías que...?** Los equipos top invierten millones en departamentos de análisis estadístico
- **¿Te imaginas que...?** Una sola métrica mal interpretada puede costar transferencias de 50 millones de euros
- **¿Has considerado que...?** Los entrenadores modernos toman decisiones tácticas basadas en patrones estadísticos en tiempo real

**Tu misión esta semana**: Convertirte en un "traductor" experto que convierte números fríos en insights estratégicos.

¿Estás listo para descubrir cómo hacer que los datos deportivos cuenten sus historias más reveladoras?


# SESIÓN 1: ¿Qué secretos revelan los resúmenes estadísticos? (50 minutos)

## Pregunta de apertura: ¿Qué tienen en común un chef y un analista deportivo?

**Reflexiona antes de continuar**: Ambos toman ingredientes crudos (números o alimentos) y los transforman en algo mucho más valioso y comprensible. ¿Pero qué habilidades necesitan para esta alquimia?

---

## Momento de curiosidad: ¿Por qué nuestro cerebro necesita "resúmenes" de información?

Imagina que tienes que evaluar 100 jugadores para el equipo de tu escuela. Cada uno tiene 20 estadísticas diferentes. Eso son 2,000 números. ¿Crees que tu cerebro puede procesar toda esa información de manera efectiva?

**Pregunta reflexiva**: ¿Qué estrategia usarías para no perderte en esa montaña de datos y aún así tomar la mejor decisión?

### ¿Qué diferencia hay entre "ver números" y "entender patrones"?

Antes de analizar datos deportivos, necesitamos entender que existe una diferencia fundamental entre tener información y tener conocimiento. ¿Has notado que los comentaristas deportivos siempre mencionan promedios, máximos y mínimos? ¿Por qué será?

<VSCode.Cell id="#VSC-fa0e8320" language="markdown">
## ¿Cómo exploramos el arte de "resumir" grandes cantidades de información?

**Momento de reflexión**: En el mundo real, los equipos manejan datos de cientos de jugadores, miles de partidos, y millones de estadísticas. ¿Pero cómo extraen lo esencial sin perderse en el ruido?

**Pregunta clave**: Si fueras director técnico y tuvieras 30 segundos para evaluar a un jugador, ¿qué 3 números te dirían todo lo que necesitas saber?

### ¡Vamos a ser "destiladores" de información deportiva!

Antes de generar estadísticas complejas, necesitamos entender qué tipos de "resúmenes" son más útiles para tomar decisiones. ¿Has notado que algunos promedios son más informativos que otros?

### ¿Qué herramientas necesitamos para nuestro laboratorio estadístico?

**Pregunta instrumental**: Para descubrir patrones ocultos en datos deportivos, ¿qué capacidades computacionales serían esenciales?

```python
# ¿Te has preguntado qué herramientas necesita un analista deportivo profesional?
# Vamos a configurar nuestro "laboratorio" de estadística descriptiva paso a paso

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# ¿Por qué necesitamos cada una de estas herramientas?
# pandas -> ¿Para qué crees que sirve cuando tenemos datos de miles de jugadores?
# numpy -> ¿Qué ventajas tiene para cálculos estadísticos precisos?
# seaborn -> ¿Cómo puede transformar números en visualizaciones que cuenten historias?
# matplotlib -> ¿Por qué necesitamos control total sobre nuestros gráficos?

# ¿Qué diferencia esperas ver con esta configuración profesional?
sns.set_theme(style="whitegrid", palette="Set2")
plt.rcParams["figure.figsize"] = (10, 6)

print("¡Laboratorio de estadística descriptiva deportiva activado!")
print(
    "¿Te has preguntado alguna vez cómo los analistas del Real Madrid procesan miles de estadísticas?"
)
print("¡Exactamente con las mismas herramientas que acabamos de cargar!")
print()
print("pandas: Tu interrogador de grandes volúmenes de datos deportivos")
print("seaborn: Tu intérprete visual de patrones estadísticos")
print("numpy: Tu motor de cálculos matemáticos precisos")
print("matplotlib: Tu arquitecto de revelaciones visuales")
print()
print(
    "Pregunta de reflexión: ¿Cómo crees que estas herramientas cambiarán tu capacidad de descubrir insights?"
)
```

## ¿Cómo creamos nuestro "universo futbolístico" de práctica?

**Momento de reflexión**: Para aprender estadística descriptiva, necesitamos datos que representen la diversidad real del fútbol. ¿Pero qué características debe tener un dataset ideal para practicar?

**Pregunta clave**: Si tuvieras que crear datos sintéticos que capturen la esencia del rendimiento futbolístico, ¿qué variables incluirías y por qué?

### ¡Vamos a ser "arquitectos" de datos deportivos realistas!

Antes de calcular estadísticas, necesitamos generar un conjunto de datos que refleje la variabilidad real del fútbol profesional. ¿Has notado que no todos los jugadores rinden igual, ni todas las posiciones tienen las mismas expectativas?

### ¿Qué dimensiones del rendimiento debemos capturar?

**Pregunta de diseño**: Para que nuestras estadísticas sean significativas, ¿qué aspectos del fútbol profesional deberíamos modelar?

**Dimensiones esenciales**:
- **Rendimiento ofensivo**: ¿Los goles como medida de efectividad?
- **Experiencia competitiva**: ¿Los partidos jugados como indicador de madurez?
- **Especialización táctica**: ¿La posición como determinante de función?
- **Desarrollo profesional**: ¿La edad como factor de potencial vs experiencia?

**Pregunta metodológica**: ¿Prefieres datos perfectamente balanceados o datos que reflejen la irregularidad natural del deporte?

```python
# ¿Te has preguntado cómo crear datos que representen la diversidad del fútbol real?
# Vamos a construir nuestro "plantel" de análisis estadístico paso a paso

# ¿Por qué es crucial fijar una semilla aleatoria en análisis estadístico?
np.random.seed(42)  # Reproducibilidad: todos obtendremos los mismos resultados

print("CREANDO NUESTRO DATASET FUTBOLÍSTICO")
print("=" * 50)

# ¿Qué tamaño de muestra es representativo para aprender estadística?
n_jugadores = 30

# ¿Cómo generamos datos que reflejen la realidad del fútbol profesional?
datos = {
    "Jugador": [f"Jugador_{i+1}" for i in range(n_jugadores)],
    # ¿Por qué estas tres posiciones representan bien la diversidad táctica?
    "Posicion": np.random.choice(
        ["Delantero", "Mediocampista", "Defensor"], n_jugadores
    ),
    # ¿El rango 18-35 años captura las diferentes etapas de una carrera?
    "Edad": np.random.randint(18, 35, n_jugadores),
    # ¿Por qué 10-38 partidos refleja realidades de temporada diversas?
    "Partidos": np.random.randint(10, 38, n_jugadores),
    # ¿El rango 0-25 goles incluye desde defensores hasta goleadores estrella?
    "Goles": np.random.randint(0, 25, n_jugadores),
}

# ¿Qué ventajas tiene organizar estos datos en un DataFrame?
df_jugadores = pd.DataFrame(datos)

print(f"Dataset creado: {len(df_jugadores)} jugadores")
print("\nPrimeros 5 jugadores de nuestro análisis:")
print(df_jugadores.head())

print(f"\nDistribución por posición:")
print(df_jugadores["Posicion"].value_counts())

print(
    "\nPregunta de reflexión: ¿Estos datos capturan la variabilidad que esperarías en el fútbol real?"
)
print("¿Qué patrones estadísticos crees que emergerán de este dataset?")
```

# ¿Qué secretos revelan los "resúmenes" estadísticos?

## Pregunta fundamental: ¿Cómo convertir 30 números individuales en conocimiento útil?

**Reflexiona**: Tienes los goles de 30 jugadores diferentes. ¿Pero cómo extraes insights que un director técnico pueda usar para tomar decisiones estratégicas?

**Momento de descubrimiento**: Vamos a explorar cómo tres números simples pueden capturar la "esencia" de todo un plantel.

### ¿Qué diferencia hay entre "tener datos" y "entender patrones"?

**Pregunta clave**: Si un periodista deportivo te preguntara "¿cómo rinde ofensivamente este equipo?" en 10 segundos, ¿qué números le dirías y por qué?

#### Las tres dimensiones fundamentales del rendimiento:
- **¿Qué es típico?** → El centro de gravedad del rendimiento
- **¿Cuáles son los límites?** → Los extremos de lo posible  
- **¿Qué tan variable es?** → La consistencia vs impredecibilidad

**Pregunta analítica**: ¿Crees que estos tres elementos pueden resumir la complejidad de 30 carreras deportivas diferentes?

```python
# ¿Te has preguntado cómo extraer la "esencia" estadística de un grupo de jugadores?
# Vamos a descubrir qué revelan los números cuando se "comprimen" inteligentemente

print("EXPLORANDO LAS MEDIDAS DE TENDENCIA CENTRAL")
print("=" * 50)

# ¿Qué nos dice el "centro de gravedad" de nuestros datos?
goles = df_jugadores["Goles"]

# Las tres perspectivas fundamentales del rendimiento:
promedio = goles.mean()  # ¿Qué es "típico"?
maximo = goles.max()  # ¿Cuál es el límite superior?
minimo = goles.min()  # ¿Cuál es la línea base?

print(f"Rendimiento típico (promedio): {promedio:.1f} goles")
print(f"Estrella del plantel (máximo): {maximo} goles")
print(f"Línea base (mínimo): {minimo} goles")

# ¿Qué revela la amplitud del rendimiento?
rango = maximo - minimo
print(f"Amplitud de talento: {rango} goles de diferencia")

print("\n" + "=" * 50)
print("ANÁLISIS POR POSICIÓN: ¿Cada especialización tiene su propia historia?")
print("=" * 50)

# ¿Las diferentes posiciones revelan patrones de rendimiento distintivos?
for posicion in df_jugadores["Posicion"].unique():
    goles_pos = df_jugadores[df_jugadores["Posicion"] == posicion]["Goles"]
    promedio_pos = goles_pos.mean()
    print(f"{posicion}: {promedio_pos:.1f} goles promedio")

print(
    "\nPregunta de reflexión: ¿Los promedios por posición confirman tus expectativas?"
)
print("¿Qué posición muestra el rendimiento más consistente?")

# ¿Cómo visualizamos estas diferencias para que sean más claras?
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_jugadores, x="Posicion", y="Goles", palette="Set2")
plt.title(
    "¿Cómo varía el rendimiento ofensivo por especialización táctica?", size=16, pad=20
)
plt.ylabel("Goles por Temporada")
plt.xlabel("Posición Táctica")
plt.show()

print("\nPreguntas de análisis:")
print("¿Qué posición tiene mayor variabilidad en el rendimiento?")
print("¿El promedio general representa bien a todas las posiciones?")
print("¿Estos datos cambian tu percepción del valor por posición?")
plt.title("Distribución de Goles por Especialización Táctica", size=16, pad=20)
plt.ylabel("Número de Goles por Temporada")
plt.xlabel("Posición Táctica")
plt.show()

print("\nReflexión de insights:")
print("¿Confirman los datos tus expectativas sobre rendimiento por posición?")
print("¿Qué posición muestra mayor variabilidad en el rendimiento?")
print("¿El promedio general representa bien a todas las posiciones?")

# Tu análisis: ¿Estos números cambian tu percepción del valor por posición?
```

---

## SÍNTESIS DE LA SESIÓN 1: ¿Qué hemos descubierto sobre resúmenes estadísticos?

**Reflexión de 50 minutos**:
- ¿Cómo tres números simples (promedio, máximo, mínimo) pueden capturar la esencia de un grupo?
- ¿Por qué el análisis por subgrupos (posiciones) revela patrones ocultos?
- ¿Cuándo los resúmenes numéricos son más útiles que ver todos los datos individuales?

**Pregunta preparatoria**: ¿Estás listo para descubrir cómo las visualizaciones pueden revelar patrones que los números solos no pueden mostrar?

---

# SESIÓN 2: ¿Cómo visualizar la esencia de los datos? (50 minutos)

## Pregunta de apertura: ¿Qué pueden "ver" tus ojos que tu mente calculadora no puede capturar?

**Reflexiona**: Has calculado promedios y extremos, pero ¿qué pasa cuando conviertes esos números en gráficos? ¿Crees que emergerán patrones que los cálculos no revelaron?

**Desafío visual**: Si tuvieras que explicar el rendimiento de tu plantel a alguien en 5 segundos, ¿usarías números o gráficos?

---

## ¿Qué secretos revelan las distribuciones visuales?

**Momento de curiosidad**: Una cosa es saber que el promedio de edad es 26 años, pero ¿qué forma tiene esa distribución? ¿Hay muchos jóvenes y pocos veteranos, o está todo balanceado?

```python
# ¿Te has preguntado qué forma tiene la "demografía" de tu plantel?
# Vamos a explorar cómo las visualizaciones revelan patrones ocultos en los números

print("EXPLORANDO LA DISTRIBUCIÓN VISUAL DE EDADES")
print("=" * 50)

# ¿Qué ventajas tiene combinar histograma con curva de densidad?
plt.figure(figsize=(12, 6))
sns.histplot(data=df_jugadores, x="Edad", bins=8, kde=True, color="lightblue")
plt.title("¿Cómo se distribuye la experiencia en nuestro plantel?", size=16, pad=20)
plt.xlabel("Edad (años)")
plt.ylabel("Número de Jugadores")
plt.show()

# ¿Qué revelan los números demográficos?
edades = df_jugadores["Edad"]
promedio_edad = edades.mean()
edad_min = edades.min()
edad_max = edades.max()

print(f"Edad promedio del plantel: {promedio_edad:.1f} años")
print(f"Veterano del grupo: {edad_max} años")
print(f"Promesa más joven: {edad_min} años")
print(f"Amplitud generacional: {edad_max - edad_min} años")

# ¿Cómo interpretamos la estructura demográfica?
print("\nAnálisis de la estructura etaria:")
if promedio_edad < 25:
    interpretacion = "Plantel joven con potencial de desarrollo"
elif promedio_edad > 30:
    interpretacion = "Plantel experimentado con madurez deportiva"
else:
    interpretacion = "Plantel balanceado entre experiencia y potencial"

print(f"→ {interpretacion}")

print(
    "\nPregunta de reflexión: ¿La forma del histograma te sugiere algo sobre la estrategia del equipo?"
)
print("¿Hay concentraciones etarias que revelen patrones de fichaje?")
print("¿Cómo podría esta demografía influir en el rendimiento colectivo?")

# ¿Qué revela la comparación visual entre variables?
plt.figure(figsize=(12, 5))

# Gráfico 1: Edad vs Goles - ¿Hay relación entre experiencia y rendimiento?
plt.subplot(1, 2, 1)
plt.scatter(df_jugadores["Edad"], df_jugadores["Goles"], alpha=0.6, color="green", s=60)
plt.title("¿La experiencia se traduce en goles?")
plt.xlabel("Edad (años)")
plt.ylabel("Goles por Temporada")

# Gráfico 2: Partidos vs Goles - ¿Más minutos = más goles?
plt.subplot(1, 2, 2)
plt.scatter(
    df_jugadores["Partidos"], df_jugadores["Goles"], alpha=0.6, color="orange", s=60
)
plt.title("¿Más oportunidades generan más goles?")
plt.xlabel("Partidos Jugados")
plt.ylabel("Goles por Temporada")

plt.tight_layout()
plt.show()

print("\nPreguntas de análisis visual:")
print("¿Observas alguna tendencia entre edad y rendimiento?")
print("¿Los jugadores con más partidos tienden a anotar más?")
print("¿Qué patrones visuales no capturaste con las estadísticas numéricas?")
```

---

## SÍNTESIS DE LA SESIÓN 2: ¿Qué hemos revelado con visualizaciones?

**Reflexión de 50 minutos**:
- ¿Cómo las distribuciones visuales muestran patrones que los promedios ocultan?
- ¿Qué ventajas tienen los gráficos de dispersión para detectar relaciones?
- ¿Por qué combinar diferentes tipos de visualización enriquece el análisis?

**Pregunta preparatoria**: ¿Estás listo para aplicar todo lo aprendido en un análisis profesional completo?

---

# SESIÓN 3: ¿Cómo aplicar estadística descriptiva profesionalmente? (50 minutos)

## Pregunta de apertura: ¿Qué diferencia hay entre hacer cálculos y generar insights estratégicos?

**Reflexiona**: Has aprendido a calcular promedios y crear gráficos, pero ¿cómo usarían esta información los analistas del Real Madrid para tomar decisiones de millones de euros?

**Desafío integrador**: Si fueras el director deportivo de un equipo profesional, ¿cómo combinarías todas estas técnicas para evaluar fichajes potenciales?

---

## ¿Qué análisis sofisticados emergen cuando combinas múltiples técnicas?

**Momento de síntesis**: Los analistas profesionales no usan una sola métrica. La magia sucede cuando combinas estadísticas descriptivas + visualizaciones + pensamiento crítico.

```python
# ¿Te has preguntado cómo crear un análisis integrador que use todas las técnicas aprendidas?
# Vamos a construir un dashboard estadístico profesional

print("ANÁLISIS INTEGRADOR: PERFIL COMPLETO DEL PLANTEL")
print("=" * 60)

# ¿Cómo creamos un resumen ejecutivo para directivos?
print("RESUMEN EJECUTIVO DEL PLANTEL")
print("-" * 40)

# Estadísticas clave por posición
for posicion in df_jugadores["Posicion"].unique():
    datos_pos = df_jugadores[df_jugadores["Posicion"] == posicion]

    print(f"\n{posicion.upper()}:")
    print(f"  Jugadores: {len(datos_pos)}")
    print(f"  Goles promedio: {datos_pos['Goles'].mean():.1f}")
    print(f"  Edad promedio: {datos_pos['Edad'].mean():.1f} años")
    print(f"  Partidos promedio: {datos_pos['Partidos'].mean():.1f}")

# ¿Qué métricas de rendimiento son más reveladoras?
print("\n" + "=" * 60)
print("MÉTRICAS DE EFICIENCIA")
print("=" * 60)

# Creamos una métrica compuesta: Goles por Partido
df_jugadores["Eficiencia"] = df_jugadores["Goles"] / df_jugadores["Partidos"]

# ¿Quiénes son los jugadores más eficientes?
top_eficientes = df_jugadores.nlargest(5, "Eficiencia")[
    ["Jugador", "Posicion", "Eficiencia", "Goles", "Partidos"]
]
print("Top 5 jugadores más eficientes (goles por partido):")
print(top_eficientes)

# Visualización integrada: Dashboard profesional
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle("DASHBOARD ESTADÍSTICO PROFESIONAL", fontsize=16, fontweight="bold")

# Gráfico 1: Distribución de rendimiento por posición
sns.violinplot(
    data=df_jugadores, x="Posicion", y="Goles", ax=axes[0, 0], palette="Set2"
)
axes[0, 0].set_title("Distribución de Goles por Posición")
axes[0, 0].tick_params(axis="x", rotation=45)

# Gráfico 2: Relación Edad-Rendimiento
sns.scatterplot(
    data=df_jugadores, x="Edad", y="Goles", hue="Posicion", ax=axes[0, 1], s=80
)
axes[0, 1].set_title("Rendimiento vs Experiencia")

# Gráfico 3: Eficiencia por posición
sns.boxplot(
    data=df_jugadores, x="Posicion", y="Eficiencia", ax=axes[1, 0], palette="Set3"
)
axes[1, 0].set_title("Eficiencia por Posición")
axes[1, 0].tick_params(axis="x", rotation=45)

# Gráfico 4: Matriz de correlaciones
correlaciones = df_jugadores[["Edad", "Partidos", "Goles", "Eficiencia"]].corr()
sns.heatmap(correlaciones, annot=True, cmap="coolwarm", center=0, ax=axes[1, 1])
axes[1, 1].set_title("Correlaciones entre Variables")

plt.tight_layout()
plt.show()

print(
    "\nPregunta de reflexión: ¿Qué insights estratégicos emergen de este análisis integrado?"
)
print("¿Qué decisiones tomarías basándote en esta evidencia estadística?")
```

## ¿Cómo aplicar pensamiento crítico a las estadísticas?

**Momento de aplicación**: Ahora que dominas las técnicas, vamos a explorar las limitaciones y sesgos que todo analista profesional debe considerar.

**Pregunta crítica**: ¿Cuándo las estadísticas pueden engañarnos y cómo evitar esas trampas?

### Actividad Práctica: Evaluación de un fichaje

**Escenario**: Eres analista del Cruz Azul y tienes que evaluar a dos jugadores para reforzar el ataque:

- **Jugador X**: 15 goles en 30 partidos, 28 años
- **Jugador Y**: 12 goles en 20 partidos, 23 años

**Pregunta estratégica**: ¿A quién ficharías y por qué? ¿Qué análisis estadísticos adicionales necesitarías?

### ¿Qué limitaciones tienen nuestros análisis?

**Reflexión crítica**:
- ¿Los datos sintéticos capturan toda la complejidad del fútbol real?
- ¿Qué factores importantes no estamos considerando?
- ¿Cómo podrían cambiar nuestras conclusiones con más variables?

### Conexión con el análisis profesional moderno

**¿Sabías que...?**
- Los equipos top usan más de 200 métricas diferentes
- Las decisiones de fichaje involucran análisis predictivo, no solo descriptivo
- Los contextos (liga, sistema táctico, adversarios) influyen enormemente en las estadísticas

```python
# ¿Te has preguntado cómo identificar sesgos y limitaciones en análisis estadísticos?
# Vamos a explorar el pensamiento crítico aplicado a nuestros datos

print("ANÁLISIS CRÍTICO: DETECTANDO LIMITACIONES")
print("=" * 50)

# ¿Qué sesgos podríamos tener en nuestro dataset?
print("Evaluando posibles sesgos en nuestros datos:")
print()

# Sesgo 1: ¿Tamaño de muestra por posición?
distribucion_posiciones = df_jugadores["Posicion"].value_counts()
print("Distribución por posición:")
for pos, count in distribucion_posiciones.items():
    porcentaje = (count / len(df_jugadores)) * 100
    print(f"  {pos}: {count} jugadores ({porcentaje:.1f}%)")

# ¿Esta distribución es realista?
if max(distribucion_posiciones) / min(distribucion_posiciones) > 2:
    print("⚠️  ALERTA: Distribución muy desbalanceada entre posiciones")
else:
    print("✓ Distribución relativamente balanceada")

print("\n" + "=" * 50)
print("SIMULANDO DECISIÓN DE FICHAJE")
print("=" * 50)

# Creamos dos candidatos para evaluación
candidato_x = {"Nombre": "Jugador X", "Goles": 15, "Partidos": 30, "Edad": 28}
candidato_y = {"Nombre": "Jugador Y", "Goles": 12, "Partidos": 20, "Edad": 23}

for candidato in [candidato_x, candidato_y]:
    eficiencia = candidato["Goles"] / candidato["Partidos"]
    print(f"\n{candidato['Nombre']}:")
    print(f"  Goles totales: {candidato['Goles']}")
    print(f"  Eficiencia: {eficiencia:.3f} goles/partido")
    print(f"  Edad: {candidato['Edad']} años")

    # ¿Cómo se compara con nuestro plantel actual?
    eficiencia_promedio = df_jugadores["Eficiencia"].mean()
    if eficiencia > eficiencia_promedio:
        print(
            f"  ✓ Eficiencia superior al promedio del plantel ({eficiencia_promedio:.3f})"
        )
    else:
        print(
            f"  ⚠️ Eficiencia inferior al promedio del plantel ({eficiencia_promedio:.3f})"
        )

print("\n" + "=" * 50)
print("PREGUNTAS CRÍTICAS PARA EL ANÁLISIS")
print("=" * 50)

print("1. ¿Qué información adicional necesitarías para decidir?")
print("   - ¿Liga de procedencia? ¿Nivel de competencia?")
print("   - ¿Historial de lesiones?")
print("   - ¿Adaptabilidad al sistema táctico?")
print()
print("2. ¿Qué limitaciones tienen nuestras métricas?")
print("   - ¿Los goles reflejan toda la contribución de un jugador?")
print("   - ¿El contexto del equipo influye en las estadísticas individuales?")
print()
print("3. ¿Qué sesgos podrían afectar la decisión?")
print("   - ¿Preferencia por juventud vs experiencia?")
print("   - ¿Sobrevaloración de eficiencia en muestras pequeñas?")

print(
    "\nReflexión final: ¿Cómo balanceas evidencia estadística con intuición futbolística?"
)
```

---

# SÍNTESIS FINAL: ¿Qué hemos descubierto sobre el arte de interpretar datos?

## Reflexión de las 3 sesiones (150 minutos totales)

### SESIÓN 1: ¿Qué secretos revelan los resúmenes estadísticos?
**Lo que dominamos ahora**:
- Extraer la "esencia" de grupos de datos usando medidas de tendencia central
- Interpretar promedios, máximos y mínimos en contexto deportivo
- Analizar diferencias entre subgrupos (posiciones, edades, etc.)
- Distinguir entre "tener números" y "generar conocimiento"

### SESIÓN 2: ¿Cómo visualizar la esencia de los datos?
**Lo que revelamos**:
- Cómo las distribuciones visuales muestran patrones ocultos en los promedios
- Ventajas de histogramas, gráficos de dispersión y visualizaciones comparativas
- Por qué los ojos pueden detectar patrones que escapan a los cálculos
- Cuándo usar cada tipo de visualización para máximo impacto

### SESIÓN 3: ¿Cómo aplicar estadística descriptiva profesionalmente?
**Lo que integramos**:
- Análisis multidimensionales que combinan múltiples métricas
- Pensamiento crítico sobre limitaciones y sesgos en los datos
- Aplicación práctica en decisiones deportivas reales
- Metodologías de análisis profesional para equipos deportivos

---

## Pregunta de preparación para la próxima semana:

**¿Te has dado cuenta de que ahora puedes "leer" historias completas en conjuntos de datos deportivos?**

### ¿Qué nuevos insights quieres descubrir?

**Reflexión personal**: 
- ¿Cuál técnica te resultó más reveladora?
- ¿Qué análisis te gustaría hacer con datos reales de la Liga MX?
- ¿Cómo cambió tu comprensión sobre la toma de decisiones basada en datos?

### Vista previa de la próxima semana:
**¿Sabías que las visualizaciones pueden transformar completamente cómo entendemos el fútbol?**

La próxima semana exploraremos:
- Técnicas avanzadas de visualización deportiva
- Cómo crear gráficos que cuenten historias convincentes
- Visualizaciones interactivas y dashboards profesionales
- Estrategias para comunicar insights a diferentes audiencias

**Pregunta motivadora**: ¿Crees que podrías crear una visualización que cambie la percepción de un entrenador sobre su equipo?

---
marp: true
theme: default
paginate: true
class: lead
---

# Semana 9: ¿Cómo se visualizan los datos para tomar mejores decisiones en fútbol?

**Ciencia de Datos aplicada al Fútbol – Prepa Tec**

---

# SESIÓN 1: ¿Por qué la visualización es clave en el análisis deportivo? (50 min)

---

## Pregunta guía

¿Alguna vez una gráfica te ayudó a entender mejor el rendimiento de un equipo?

---

### Teoría: El valor de la visualización

- Las gráficas permiten ver patrones y tendencias
- Facilitan la comunicación de hallazgos
- Son esenciales para la toma de decisiones

---

### Analogía deportiva

Una gráfica es como el pizarrón del entrenador: resume la estrategia de manera visual y clara.

---

## Práctica: Gráfica de barras para comparar equipos

```python
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid", palette="viridis")

equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']
goles = [85, 80, 92, 78]

plt.bar(equipos, goles)
plt.title('Goles por equipo en la temporada')
plt.xlabel('Equipo')
plt.ylabel('Goles')
plt.show()
```

---

### Reflexión

¿Qué ventajas tiene ver los datos en una gráfica en vez de una tabla?

---

### Práctica: Gráfica de líneas para evolución de rendimiento

```python
jornadas = [1, 2, 3, 4, 5]
goles_barcelona = [2, 3, 1, 4, 2]
goles_madrid = [1, 2, 2, 3, 1]

plt.plot(jornadas, goles_barcelona, marker='o', label='Barcelona')
plt.plot(jornadas, goles_madrid, marker='s', label='Real Madrid')
plt.title('Evolución de goles por jornada')
plt.xlabel('Jornada')
plt.ylabel('Goles')
plt.legend()
plt.show()
```

---

### Reflexión

¿En qué situaciones deportivas sería útil una gráfica de líneas?

---

### Actividad práctica

Crea una gráfica de barras con los goles de tu equipo favorito en los últimos 5 partidos.

---

## Síntesis de la sesión 1

- Visualización: clave para el análisis y la comunicación
- Gráficas de barras y líneas
- Herramientas: Matplotlib y Seaborn

---

# SESIÓN 2: ¿Cómo elegir y personalizar la mejor gráfica? (50 min)

---

## Pregunta guía

¿Todas las gráficas sirven para cualquier tipo de dato?

---

### Teoría: Tipos de gráficas y personalización

- Barras: comparar cantidades
- Líneas: mostrar evolución
- Dispersión: ver relaciones
- Pastel: mostrar proporciones

---

### Analogía deportiva

Elegir la gráfica correcta es como elegir la mejor táctica para un partido: depende del objetivo.

---

### Práctica: Gráfica de dispersión (scatter)

```python
import numpy as np
edades = np.random.randint(18, 35, size=20)
goles = np.random.randint(0, 20, size=20)

plt.scatter(edades, goles)
plt.title('Relación entre edad y goles')
plt.xlabel('Edad')
plt.ylabel('Goles')
plt.show()
```

---

### Práctica: Gráfica de pastel

```python
posesion = [55, 25, 20]
etiquetas = ['Barcelona', 'Real Madrid', 'Otros']

plt.pie(posesion, labels=etiquetas, autopct='%1.1f%%', startangle=90)
plt.title('Porcentaje de posesión de balón')
plt.show()
```

---

### Reflexión

¿En qué casos sería útil una gráfica de dispersión o de pastel en el fútbol?

---

### Actividad práctica

Elige un tipo de gráfica y justifica por qué es la mejor opción para mostrar los datos de tarjetas amarillas de tu equipo favorito.

---

## Síntesis de la sesión 2

- Tipos de gráficas y cuándo usarlas
- Personalización para mayor claridad
- Importancia de elegir bien según el dato

---

# SESIÓN 3: ¿Cómo crear reportes visuales profesionales? (50 min)

---

## Pregunta guía

¿Cómo presentarías tus hallazgos a un entrenador o directivo?

---

### Teoría: El arte de contar historias con datos

- Un buen reporte combina datos, gráficas y explicaciones
- La visualización debe responder preguntas clave
- El diseño importa: claridad y orden

---

### Práctica: Mini-reporte visual

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].bar(equipos, goles)
axs[0].set_title('Goles por equipo')
axs[0].set_xlabel('Equipo')
axs[0].set_ylabel('Goles')

axs[1].pie(posesion, labels=etiquetas, autopct='%1.1f%%', startangle=90)
axs[1].set_title('Posesión de balón')

plt.suptitle('Reporte visual de desempeño')
plt.tight_layout()
plt.show()
```

---

### Reflexión

¿Qué elementos hacen que un reporte visual sea profesional y fácil de entender?

---

### Actividad práctica

Crea un mini-reporte visual con al menos dos tipos de gráficas usando datos de tu equipo favorito.

---

## Síntesis de la sesión 3

- Reportes visuales: combinación de gráficas y análisis
- Importancia de la narrativa visual
- Herramientas para presentaciones profesionales

---

# Preguntas para tu autoevaluación

- ¿Qué tipo de gráfica te resultó más útil y por qué?
- ¿Cómo elegirías la mejor visualización para un dato nuevo?
- ¿Qué aprendiste sobre comunicar hallazgos?

---

# Próxima semana

- Análisis e interpretación de datos
- Conclusiones y recomendaciones
- Preparación para el siguiente bloque

**¿Listo para presentar tus hallazgos como un analista profesional?**

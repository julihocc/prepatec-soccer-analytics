---
marp: true
theme: default
paginate: true
class: lead
---

# Semana 10: ¿Cómo se interpretan los datos para tomar decisiones en fútbol?

**Ciencia de Datos aplicada al Fútbol – Prepa Tec**

---

# SESIÓN 1: ¿Por qué no basta con ver los datos, sino que hay que interpretarlos? (50 min)

---

## Pregunta guía

¿Alguna vez los datos te han llevado a una conclusión equivocada?

---

### Teoría: De la observación a la interpretación

- Observar datos es solo el primer paso
- Interpretar implica buscar causas, consecuencias y contexto
- La interpretación correcta guía mejores decisiones

---

### Analogía deportiva

Ver la posesión de balón no siempre significa que un equipo dominó el partido. ¿Por qué?

---

## Práctica: Analizando un caso real

```python
import pandas as pd
partidos = pd.DataFrame({
    'equipo': ['Barcelona', 'Real Madrid', 'Barcelona', 'Real Madrid', 'Barcelona'],
    'goles': [2, 1, 3, 0, 2],
    'posesion': [65, 55, 60, 52, 70],
    'remates': [15, 10, 18, 8, 20]
})
print(partidos)

# ¿El equipo con más posesión siempre gana?
print(partidos[['goles', 'posesion']])
```

---

### Reflexión

¿Puedes encontrar un partido donde la posesión no se relaciona con el resultado?

---

### Práctica: Buscando patrones y excepciones

```python
# ¿Hay alguna excepción?
excepciones = partidos[partidos['goles'] < partidos['posesion']/2]
print(excepciones)
```

---

### Actividad práctica

Busca en tus propios datos un caso donde la estadística principal no explique el resultado.

---

## Síntesis de la sesión 1

- Interpretar datos: ir más allá de la observación
- Buscar causas y contexto
- Identificar excepciones y patrones

---

# SESIÓN 2: ¿Cómo generar conclusiones y recomendaciones a partir de los datos? (50 min)

---

## Pregunta guía

¿Cómo pasar de los datos a una recomendación concreta para un entrenador?

---

### Teoría: De los datos a la acción

- Conclusiones: resumen de hallazgos clave
- Recomendaciones: sugerencias basadas en el análisis

---

### Analogía deportiva

Un analista no solo reporta datos, propone cambios tácticos basados en la evidencia.

---

### Práctica: Redactando conclusiones y recomendaciones

```python
print("Conclusión: El equipo con mayor posesión no siempre gana, pero suele generar más remates.")
print("Recomendación: Mejorar la efectividad de los remates podría ser más importante que solo aumentar la posesión.")
```

---

### Actividad práctica

Redacta una conclusión y una recomendación usando los datos de tu equipo favorito.

---

## Síntesis de la sesión 2

- Conclusiones y recomendaciones: puente entre análisis y acción
- Importancia de justificar cada sugerencia

---

# SESIÓN 3: ¿Cómo presentar tus hallazgos de manera profesional? (50 min)

---

## Pregunta guía

¿Cómo convencerías a un directivo de que tus recomendaciones son válidas?

---

### Teoría: Presentación profesional de resultados

- Claridad, orden y evidencia visual
- Uso de gráficas y tablas para respaldar argumentos

---

### Práctica: Mini-presentación de resultados

```python
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid", palette="viridis")

plt.bar(partidos['equipo'], partidos['goles'])
plt.title('Goles por equipo')
plt.xlabel('Equipo')
plt.ylabel('Goles')
plt.show()
```

---

### Reflexión

¿Qué elementos hacen que una presentación sea convincente y profesional?

---

### Actividad práctica

Prepara una mini-presentación con datos, gráfica y recomendación para tu equipo favorito.

---

## Síntesis de la sesión 3

- Presentación profesional: claridad y evidencia
- Importancia de comunicar para la toma de decisiones

---

# Preguntas para tu autoevaluación

- ¿Qué aprendiste sobre la diferencia entre observar e interpretar?
- ¿Cómo justificarías una recomendación basada en datos?
- ¿Qué hace que una presentación sea profesional?

---

# Próxima semana

- Introducción al modelado predictivo
- Primeros pasos en Machine Learning
- Preparación para el siguiente bloque

**¿Listo para predecir el futuro del fútbol con datos?**

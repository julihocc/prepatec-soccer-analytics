---
marp: true
theme: default
paginate: true
class: lead
---

# Semana 12: ¿Cómo predecir si un equipo ganará, empatará o perderá?

**Ciencia de Datos aplicada al Fútbol – Prepa Tec**

---

# SESIÓN 1: ¿Por qué no basta con predecir un número, sino una categoría? (50 min)

---

## Pregunta guía

¿Te has preguntado cómo los analistas predicen si un equipo ganará, empatará o perderá?

---

### Teoría: Modelos de clasificación

- Clasificación: predecir categorías (ganar, empatar, perder)
- Diferencia con regresión: no es un número, es una clase
- Aplicaciones: predicción de resultados, lesiones, posiciones

---

### Analogía deportiva

Un modelo de clasificación es como un árbitro: decide entre varias opciones posibles según las reglas y los datos.

---

## Práctica: Simulación de clasificación básica

```python
import random
equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']
resultados = []
for i in range(5):
    local = random.choice(equipos)
    visitante = random.choice([e for e in equipos if e != local])
    prediccion = random.choice(['Gana local', 'Empate', 'Gana visitante'])
    resultados.append({'Local': local, 'Visitante': visitante, 'Predicción': prediccion})
for partido in resultados:
    print(partido)
```

---

### Reflexión

¿En qué se parece y en qué se diferencia esta simulación de una predicción real?

---

### Práctica: Variables para clasificación

```python
variables = ['Goles previos', 'Localía', 'Racha', 'Lesiones', 'Posición en tabla']
print("Variables posibles:", variables)
```

---

### Actividad práctica

Haz una lista de variables que tú considerarías para predecir si un equipo ganará, empatará o perderá.

---

## Síntesis de la sesión 1

- Clasificación: predecir categorías
- Diferencia con regresión
- Variables relevantes para clasificación

---

# SESIÓN 2: ¿Cómo funciona un modelo de clasificación básico? (50 min)

---

## Pregunta guía

¿Puede una fórmula sencilla predecir si un equipo ganará, empatará o perderá?

---

### Teoría: Regresión logística básica

- Predice la probabilidad de pertenecer a una clase
- Ejemplo: probabilidad de ganar según goles previos

---

### Analogía deportiva

Entrenar un modelo de clasificación es como practicar penales: cada intento ayuda a mejorar la decisión final.

---

## Práctica: Regresión logística con datos simulados

```python
import numpy as np
from sklearn.linear_model import LogisticRegression

# Datos simulados: goles previos y resultado (1=gana, 0=no gana)
goles_previos = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
resultado = np.array([0, 0, 1, 1, 1])

modelo = LogisticRegression()
modelo.fit(goles_previos, resultado)

print("Coeficiente:", modelo.coef_[0][0])
print("Intersección:", modelo.intercept_[0])
print("Probabilidad de ganar con 6 goles previos:", modelo.predict_proba([[6]])[0][1])
```

---

### Reflexión

¿Crees que una sola variable es suficiente para predecir el resultado? ¿Por qué sí o por qué no?

---

### Actividad práctica

Simula una regresión logística con datos de tu equipo favorito (goles previos vs ganar/no ganar).

---

## Síntesis de la sesión 2

- Regresión logística: modelo de clasificación básico
- Entrenamiento = aprender de datos
- Limitaciones de modelos simples

---

# SESIÓN 3: ¿Cómo evaluar la calidad de un modelo de clasificación? (50 min)

---

## Pregunta guía

¿Cómo saber si tu modelo de clasificación es bueno?

---

### Teoría: Precisión y matriz de confusión

- Precisión: porcentaje de aciertos
- Matriz de confusión: muestra aciertos y errores

---

### Analogía deportiva

Evaluar un modelo es como revisar el porcentaje de penales anotados vs fallados: mide el desempeño real.

---

## Práctica: Evaluación básica de un modelo

```python
from sklearn.metrics import accuracy_score, confusion_matrix

# Supón que tienes predicciones y resultados reales
reales = [1, 0, 1, 1, 0]
predichos = [1, 0, 0, 1, 1]

print("Precisión:", accuracy_score(reales, predichos))
print("Matriz de confusión:\n", confusion_matrix(reales, predichos))
```

---

### Reflexión

¿Qué significa tener alta precisión pero muchos errores en una clase específica?

---

### Actividad práctica

Calcula la precisión y la matriz de confusión para un modelo simulado con tus propios datos.

---

## Síntesis de la sesión 3

- Precisión y matriz de confusión: evaluación básica
- Importancia de analizar errores y aciertos
- Preparación para modelos más avanzados

---

# Preguntas para tu autoevaluación

- ¿Qué variable te parece más importante para clasificar?
- ¿Por qué es útil la matriz de confusión?
- ¿Qué aprendiste sobre la evaluación de modelos?

---

# Próxima semana

- Métricas avanzadas de evaluación
- Comparación de modelos
- Profundización en Machine Learning

**¿Listo para comparar y mejorar tus modelos de predicción?**

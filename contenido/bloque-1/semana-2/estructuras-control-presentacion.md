---
marp: true
theme: default
paginate: true
class: lead
---

# Semana 2: Automatización de Decisiones en Fútbol con Python

**Curso de Ciencia de Datos aplicada al Fútbol (Preparatoria)**

---

# ¿Cómo automatizamos decisiones como un entrenador profesional?

- ¿Qué patrones de decisión observas en el fútbol moderno?
- ¿Cómo podrías programar un asistente técnico que tome decisiones automáticas?

---

# Ruta de la sesión (120 minutos)

1. Repetición sistemática: bucles for y while
2. Decisiones complejas: condicionales y operadores lógicos
3. Organización elegante: funciones, listas, diccionarios, tuplas y conjuntos
4. Síntesis y reflexión

---

# 1. Repetición sistemática: ¿Por qué la repetición genera maestría?

- ¿Cómo automatizan los clubes profesionales las repeticiones en entrenamiento?
- ¿Qué tienen en común un ejercicio de pases y un bucle en programación?

---

# Ejemplo: Procesamiento automático de plantilla

```python
plantilla_barcelona = [
    "Ter Stegen", "Pedri", "Gavi", "Lewandowski",
    "Raphinha", "Frenkie de Jong", "Ronald Araújo", "Jules Koundé"
]
for numero_jugador, nombre_jugador in enumerate(plantilla_barcelona, 1):
    print(f"{numero_jugador:2d}. {nombre_jugador}")
```

- ¿Qué pasaría si tuvieras 25 jugadores en vez de 8?

---

# ¿Cuándo usamos while en vez de for?

- ¿Cómo simularías una práctica de penales hasta lograr 5 goles consecutivos?

```python
penales_consecutivos = 0
intentos_totales = 0
objetivo = 5
while penales_consecutivos < objetivo:
    # Simulación de penal
    # ...
    pass
```

- ¿Por qué while es útil cuando no sabemos cuántas repeticiones necesitaremos?

---

# 2. Decisiones complejas: ¿Cómo piensa un entrenador?

- ¿Qué variables considera un DT antes de hacer un cambio?
- ¿Cómo combinamos condiciones múltiples en Python?

---

# Condicionales: if, elif, else

```python
if energia_equipo >= 6 and minuto_actual >= 70:
    print("CAMBIO OFENSIVO")
elif jugadores_con_tarjeta >= 3:
    print("Jugar conservador")
else:
    print("Mantener esquema actual")
```

- ¿Por qué es importante el orden de las condiciones?

---

# Operadores lógicos: and, or, not

- ¿Cuándo necesitas que se cumplan varias condiciones a la vez?
- ¿En qué situaciones deportivas usarías or o not?

---

# Decisiones jerárquicas: condicionales anidados

```python
if lesion_previa:
    decision = "SUBSTITUCIÓN INMEDIATA"
else:
    if goles_anotados >= 1:
        if nivel_cansancio >= 8:
            decision = "Substitución al minuto 85"
        else:
            decision = "Mantener en campo"
```

- ¿Por qué evaluamos primero el riesgo de lesión?

---

# 3. Organización elegante: funciones y estructuras

- ¿Cómo reutilizarías una evaluación para todos los jugadores?
- ¿Qué ventajas tiene dividir problemas grandes en partes pequeñas?

---

# Funciones: jugadas tácticas reutilizables

```python
def evaluar_jugador(nombre, goles, asistencias, edad, lesionado):
    if lesionado:
        return "NO CONVOCADO"
    puntuacion = (goles * 3) + (asistencias * 2)
    if puntuacion >= 15:
        return "CONVOCADO - Excelente"
    elif puntuacion >= 8:
        return "CONVOCADO - Bueno"
    else:
        return "NO CONVOCADO"
```

- ¿En qué se parece una función a una jugada ensayada?

---

# Listas y diccionarios: organización eficiente

- Listas: para secuencias (alineaciones)
- Diccionarios: para fichas completas de jugadores

```python
ficha_messi = {
    "nombre": "Lionel Messi",
    "posicion": "Delantero",
    "edad": 36,
    "equipo": "Inter Miami"
}
```

---

# Tuplas y conjuntos: datos inmutables y únicos

- Tuplas: resultados históricos, posiciones en campo
- Conjuntos: equipos únicos en una liga

```python
resultado_final = ("Barcelona", 3, "Real Madrid", 1)
equipos = {"Barcelona", "Real Madrid", "Atletico Madrid"}
```

---

# Síntesis y reflexión

- ¿Cómo automatizamos el procesamiento de listas completas de jugadores?
- ¿Cuándo usar for vs while?
- ¿Por qué la lógica de programación imita el pensamiento de un entrenador?
- ¿Qué ventajas tiene organizar el código en funciones y estructuras?

---

# Preguntas para tu autoevaluación

- ¿Qué fue lo más claro y lo más desafiante?
- ¿Cómo aplicarías estos patrones fuera del fútbol?
- ¿Qué te gustaría automatizar en tu vida diaria usando lógica similar?

---

# Próxima semana

- Funciones avanzadas para análisis estadístico
- Módulos para organizar sistemas complejos
- Manejo de errores y bibliotecas de funciones

**¿Listo para el siguiente nivel?**

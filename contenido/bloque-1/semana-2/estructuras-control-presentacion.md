---
marp: true
theme: default
paginate: true
class: lead
---


# Semana 2: Automatización de Decisiones en Fútbol con Python

**Programación Básica 1 – Prepa Tec**

---

# SESIÓN 1: ¿Cómo repetimos tareas como un entrenamiento sistemático? (50 min)

---

## Pregunta guía

¿Qué hace un equipo cuando practica jugadas una y otra vez?

---

- ¿Cómo automatizamos acciones repetitivas en Python?
- ¿Por qué la repetición controlada mejora el rendimiento?
- ¿Cuándo sabemos que hemos practicado lo suficiente?

---

## Teoría: Bucles y repetición en fútbol y código

Imagina que eres el preparador físico del Real Madrid. Necesitas que cada jugador complete exactamente 20 sprints de 30 metros.

---

¿Cómo te asegurarías de que TODOS cumplan sin excepción?

---

## Pregunta reflexiva

¿Preferirías decirle a cada jugador individualmente "corre 30 metros" 20 veces, o crear un sistema que automáticamente supervise las 20 repeticiones?

---

## Práctica: Procesamiento automático de plantilla

```python
plantilla_barcelona = [
    "Ter Stegen", "Pedri", "Gavi", "Lewandowski",
    "Raphinha", "Frenkie de Jong", "Ronald Araújo", "Jules Koundé"
]
for numero_jugador, nombre_jugador in enumerate(plantilla_barcelona, 1):
    print(f"{numero_jugador:2d}. {nombre_jugador}")
```

---

¿Qué pasaría si tuvieras 25 jugadores en vez de 8?

---

## Práctica: ¿Cuándo usamos while en vez de for?

Imagina que eres Xavi y quieres que tus jugadores practiquen penales HASTA que cada uno anote 5 consecutivos.

---

¿Sabes de antemano cuántos intentos necesitará cada jugador?

---

```python
penales_consecutivos = 0
intentos_totales = 0
objetivo = 5
while penales_consecutivos < objetivo:
    # Simulación de penal
    # ...
    pass
```

---

¿Por qué while es útil cuando no sabemos cuántas repeticiones necesitaremos?

---

## Síntesis de la sesión 1

- ¿Cómo automatizamos el procesamiento de listas completas de jugadores?
- ¿Cuándo usamos 'for' (repeticiones conocidas) vs 'while' (hasta lograr objetivo)?
- ¿Por qué la automatización es crucial en análisis deportivo masivo?

---

# SESIÓN 2: ¿Cómo tomamos decisiones complejas bajo presión? (50 min)

---

## Pregunta guía

¿Qué proceso mental sigue un capitán antes de cada jugada?

---

- ¿Cómo combinamos múltiples condiciones como un estratega?
- ¿Por qué algunos equipos son más predecibles que otros?
- ¿Cómo optimizamos la toma de decisiones rápida?

---

## Teoría: Condicionales y operadores lógicos

¿Qué variables considera un DT antes de hacer un cambio?

---

```python
if energia_equipo >= 6 and minuto_actual >= 70:
    print("CAMBIO OFENSIVO")
elif jugadores_con_tarjeta >= 3:
    print("Jugar conservador")
else:
    print("Mantener esquema actual")
```

---

¿Por qué es importante el orden de las condiciones?

---

## Práctica: Decisiones jerárquicas y condicionales anidados

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

---

¿Por qué evaluamos primero el riesgo de lesión?

---

## Síntesis de la sesión 2

- ¿Cómo combinamos múltiples condiciones con operadores lógicos (and, or, not)?
- ¿Por qué las decisiones jerárquicas (condicionales anidados) reflejan el pensamiento real?
- ¿Cómo la lógica de programación imita los procesos mentales de un entrenador?

---

# SESIÓN 3: ¿Cómo organizamos estrategias complejas de manera elegante? (50 min)

---

## Pregunta guía

¿Cómo simplifica Messi las jugadas más complicadas?

---

- ¿Qué ventajas tiene dividir problemas grandes en partes pequeñas?
- ¿Cómo reutilizamos tácticas exitosas en diferentes situaciones?
- ¿Por qué la organización determina la efectividad del análisis?

---

## Teoría: Funciones, listas, diccionarios, tuplas y conjuntos

¿Cómo reutilizarías una evaluación para todos los jugadores?

---

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

---

Listas: para secuencias (alineaciones)

---

Diccionarios: para fichas completas de jugadores

---

```python
ficha_messi = {
    "nombre": "Lionel Messi",
    "posicion": "Delantero",
    "edad": 36,
    "equipo": "Inter Miami"
}
```

---

Tuplas: resultados históricos, posiciones en campo

---

Conjuntos: equipos únicos en una liga

---

```python
resultado_final = ("Barcelona", 3, "Real Madrid", 1)
equipos = {"Barcelona", "Real Madrid", "Atletico Madrid"}
```

---

## Síntesis de la sesión 3

- ¿Qué ventajas tiene organizar el código en funciones y estructuras?
- ¿Cómo reutilizarías tus análisis para diferentes equipos?
- ¿En qué otras áreas podrías usar esta lógica sistemática?

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

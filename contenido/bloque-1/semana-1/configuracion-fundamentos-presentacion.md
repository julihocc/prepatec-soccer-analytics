---
marp: true
theme: default
paginate: true
class: lead
---

# Semana 1: Primer paso en el análisis de datos de fútbol

**Curso de Ciencia de Datos aplicada al Fútbol (Preparatoria)**

---

# ¿Por qué analizar fútbol con datos?

- ¿Qué decisiones futbolísticas te gustaría respaldar con datos?
- ¿Dónde ves hoy que se usan números en el fútbol?
- ¿Qué te gustaría poder responder con datos al terminar el curso?

---

# Ruta del curso

1. **Describir datos** (Bloque 1)
2. **Analizar y visualizar** (Bloque 2)
3. **Predecir resultados** (Bloque 3)

---

# Semana 1: Objetivo central

Aprender a guardar y manipular datos simples (nombres, edades, goles) para que la computadora pueda "razonar" sobre ellos.

---

# Preguntas guía de la semana

1. ¿Cómo le digo a la computadora que un jugador se llama X y tiene Y goles?
2. ¿Qué diferencia hay entre un número, un texto y un dato Verdadero/Falso?
3. ¿Cómo realizar operaciones simples (sumar goles, calcular promedios)?
4. ¿Por qué organizar bien la información desde el inicio facilita el análisis?

---

# SESIÓN 1: ¿Qué es realmente programar?

- ¿En qué se parecen un entrenador y un programador?
- Ambos dan instrucciones paso a paso para lograr un objetivo.

---

# ¿Por qué Python?

- Es el idioma favorito de los analistas deportivos.
- Sencillo, claro y poderoso para datos.

---

# ¿Cómo "recordamos" información sobre jugadores?

- Ejemplo: Messi tiene 37 años, juega en Inter Miami, 10 goles.
- ¿Cómo organizarías esa información para que la computadora la entienda?

---

# Primer código en Python

```python
jugador = "Lionel Messi"
edad = 37
goles = 10
altura = 1.70
es_activo = True
print(f"Nombre: {jugador}, Edad: {edad}, Goles: {goles}, Altura: {altura}, ¿Activo?: {es_activo}")
```

---

# Tipos de datos en fútbol

- **Texto**: nombres, equipos ("Barcelona")
- **Números enteros**: goles, edad (10, 37)
- **Números decimales**: altura (1.70)
- **Booleanos**: ¿Está activo? (True/False)

---

# Operaciones básicas

- Sumar goles
- Calcular promedios
- Convertir unidades (metros a centímetros)

```python
goles_objetivo = 15
goles_faltantes = goles_objetivo - goles
altura_cm = altura * 100
```

---

# Reflexión

- ¿Por qué es importante distinguir entre tipos de datos?
- ¿Qué errores podrías cometer si mezclas texto y números?

---

# SESIÓN 2: ¿Cómo calculamos como un entrenador?

- Los entrenadores comparan estadísticas para tomar decisiones.
- ¿Podemos enseñar a la computadora a comparar y decidir?

---

# Comparaciones en Python

```python
es_veterano = edad > 30
en_forma = goles > 8
es_titular = partidos_jugados > 20
```

- ¿Qué significa que el resultado sea True o False?

---

# Decisiones automáticas: if/elif/else

```python
if edad < 35:
    print("Edad apropiada para alto rendimiento")
else:
    print("Jugador veterano - requiere evaluación especial")
```

- ¿Cómo ayuda la indentación a Python?

---

# Ejemplo: Asistente técnico automático

- ¿Debería este jugador ser convocado?
- Evaluar edad, goles, altura.

---

# SESIÓN 3: ¿Cómo organizamos datos como un club profesional?

- ¿Cómo organiza el Barcelona la información de sus 25 jugadores?
- ¿Prefieres 25 variables separadas o una forma más inteligente?

---

# Listas en Python

```python
jugadores_convocados = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Kylian Mbappé",
    "Erling Haaland",
    "Vinicius Jr"
]
```

- ¿Por qué los índices empiezan en 0?

---

# Diccionarios en Python

```python
estadisticas_messi = {
    "nombre": "Lionel Messi",
    "edad": 37,
    "goles_temporada": 10,
    "asistencias": 8
}
```

- ¿Cuándo usarías una lista y cuándo un diccionario?

---

# Mini sistema de gestión deportiva

- Combina listas, diccionarios y decisiones automáticas.
- Clasifica jugadores según goles y edad.

---

# Ejemplo: Análisis de plantilla

```python
plantilla_completa = [
    {"nombre": "Lionel Messi", "goles": 10, "edad": 37},
    {"nombre": "Cristiano Ronaldo", "goles": 12, "edad": 39},
    {"nombre": "Kylian Mbappé", "goles": 15, "edad": 25},
    {"nombre": "Erling Haaland", "goles": 18, "edad": 24}
]
for jugador in plantilla_completa:
    if jugador["goles"] >= 15:
        print(f"{jugador['nombre']}: ESTRELLA GOLEADORA")
```

---

# Resumen de la semana

- Guardar información con variables
- Operaciones y comparaciones
- Decisiones automáticas
- Listas y diccionarios
- Primer análisis real de datos de fútbol

---

# Reflexión final

- ¿Qué fue lo más interesante?
- ¿Qué aplicación le darías a lo aprendido?
- ¿En qué otras áreas podrías usar este pensamiento lógico?

---

# Próxima semana

- Estructuras de control más avanzadas
- Bucles para analizar temporadas completas
- Funciones para automatizar análisis

**¿Listo para el siguiente nivel?**

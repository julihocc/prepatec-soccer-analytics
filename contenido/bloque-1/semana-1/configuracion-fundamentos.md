---
marp: true
theme: default
size: 16:9
paginate: true
backgroundColor: #ffffff
color: #2c3e50
footer: 'Ciencia de Datos aplicada al Fútbol | Preparatoria'
style: |
  h1 { color: #3498db; }
  h2 { color: #e74c3c; }
  .highlight { background-color: #fff3cd; padding: 10px; border-radius: 5px; }
  .question { background-color: #d1ecf1; padding: 15px; border-radius: 5px; border-left: 4px solid #3498db; }
  .code-small { font-size: 0.8em; }
  .center { text-align: center; }
---

# Semana 1: Primer paso en el análisis de datos de fútbol

<div class="center">

**Ciencia de Datos aplicada al Fútbol**

*Preparatoria / Bachillerato*

</div>

---

# SESIÓN 1: ¿Qué es realmente programar? (50 minutos)
#
## Pregunta de apertura: ¿En qué se parecen un entrenador de fútbol y un programador?
#
<span class="highlight">**Reflexiona antes de continuar**</span>: Ambos dan instrucciones específicas, paso a paso, para lograr un objetivo. El entrenador a sus jugadores, el programador a la computadora.
#
---
#
## Momento de curiosidad: ¿Cómo le enseñamos a pensar a una máquina?
#
Imagina que eres Pep Guardiola y quieres explicarle a un jugador nuevo exactamente cómo ejecutar un pase perfecto. Tendrías que ser muy específico, ¿verdad?
#
<div class="question">

<span class="highlight">**Pregunta reflexiva**</span>: ¿Qué pasaría si le dijeras a un jugador simplemente "juega bien" versus darle instrucciones precisas?
#
### ¿Por qué elegimos Python como nuestro "idioma" con la computadora?
#

</div>
<span class="highlight">**Piensa en esto**</span>: De todos los lenguajes de programación que existen (más de 100), ¿por qué Python es el favorito de los analistas deportivos del mundo?

---

## ¿Cómo "recordamos" información sobre jugadores y equipos?
#
<div class="question">

<span class="highlight">**Pregunta crucial**</span>: Si quisieras que la computadora recuerde que Messi tiene 37 años, que juega para el Inter Miami, y que ha anotado 10 goles esta temporada, ¿cómo se lo dirías?
#

</div>
<span class="highlight">**Analogía deportiva**</span>: Es como cuando un comentarista deportivo tiene fichas con información de cada jugador. ¿Cómo organizarías esas fichas?
#
### ¡Vamos a crear nuestro primer "archivo" de jugador!

## Prueba de Verificación: ¿Funciona Python?
#
### ¡Nuestro primer código! 
Ejecuta esta celda para verificar que Python funciona correctamente:

---

## ¿Qué puede hacer la computadora con esta información?
#
<span class="highlight">**Momento de descubrimiento**</span>: Ahora que la computadora "conoce" a nuestro jugador, ¿qué tipo de cálculos crees que podríamos pedirle que haga?
#
<div class="question">

<span class="highlight">**Pregunta de conexión**</span>: Cuando ves las estadísticas en ESPN o FIFA, ¿qué operaciones matemáticas crees que hay detrás de esos números?
#
### ¡Vamos a pedirle a Python que "piense" como un analista deportivo!

</div>

---

## ¿Qué son las Variables?
#
<span class="highlight">**Una variable es como una caja donde guardamos información.**</span>
#
### Ejemplo de la vida real:
- En tu cuarto, tienes cajas con etiquetas: "videojuegos", "ropa", "libros"
- En Python, las variables son cajas con nombres: `jugador`, `goles`, `equipo`
#
### Ejemplo futbolístico:
- Jugador: "Lionel Messi"
- Goles: 15
- Equipo: "Inter Miami"
#
<span class="highlight">**¡Vamos a crear nuestras primeras variables con datos de fútbol!**</span>
#
---
#
## Creando Variables de Fútbol

---
#
## SÍNTESIS DE LA SESIÓN 1: ¿Qué hemos descubierto?
#
<span class="highlight">**Reflexión de 50 minutos**</span>:
- ¿Cómo "guardamos" información en la memoria de la computadora?
- ¿Qué tipos de datos deportivos requieren diferentes formatos?
- ¿Cómo realiza Python operaciones matemáticas básicas?
#
<div class="question">

<span class="highlight">**Pregunta preparatoria**</span>: ¿Estás listo para que Python tome decisiones automáticas basadas en datos deportivos?
#
---
#
# SESIÓN 2: ¿Cómo calculamos como lo haría un entrenador? (50 minutos)
#
## Pregunta de apertura: ¿Qué decisiones toma un DT basándose en números?
#

</div>
<span class="highlight">**Reflexiona**</span>: Cuando Xavi decide si un jugador debe entrar al campo, ¿crees que solo usa intuición o también analiza estadísticas?
#
<span class="highlight">**Desafío mental**</span>: Si fueras entrenador y tuvieras que decidir entre dos jugadores para el próximo partido, ¿qué números compararías?
#
---
#
## ¿Cómo enseñamos a Python a comparar y decidir?
#
<span class="highlight">**Momento de curiosidad**</span>: Al igual que un entrenador compara estadísticas para tomar decisiones, ¿podemos enseñar a la computadora a hacer comparaciones automáticas?

### Variables de Números
#
<span class="highlight">**Los números en Python NO van entre comillas**</span>
#
#### Hay dos tipos:
1. <span class="highlight">**Enteros**</span> (sin decimal): 10, 25, 100
2. <span class="highlight">**Decimales**</span> (con punto): 1.85, 24.5, 89.7
#
### Estadísticas numéricas:

---

## ¿Cómo enseñamos a Python a tomar decisiones automáticas?
#
<div class="question">

<span class="highlight">**Pregunta clave**</span>: ¿Has notado que los entrenadores siguen patrones? "SI el jugador tiene más de X goles, ENTONCES entra en la lista de convocados"
#

</div>
<span class="highlight">**Analogía práctica**</span>: Es como un semáforo - SI está en verde, ENTONCES avanza. ¿Cómo le dirías a Python que siga reglas similares?
#
### ¡Vamos a crear nuestro primer "asistente técnico" automático!

### Variables de Verdadero o Falso (Booleanos)
#
<span class="highlight">**A veces solo queremos responder SÍ o NO**</span>
#
- ¿El equipo ganó? True (Verdadero)
- ¿El jugador está lesionado? False (Falso)
#
En Python usamos: `True` y `False` (con mayúscula)

---
#
## SÍNTESIS DE LA SESIÓN 2: ¿Qué decisiones puede tomar Python?
#
<span class="highlight">**Reflexión de 50 minutos**</span>:
- ¿Cómo Python compara valores usando operadores matemáticos?
- ¿Por qué las comparaciones devuelven True o False?
- ¿Cómo las estructuras if/elif/else imitan el pensamiento de un entrenador?
#
<div class="question">

<span class="highlight">**Pregunta preparatoria**</span>: ¿Te imaginas manejar las estadísticas de 25 jugadores usando solo variables individuales?
#
---
#
# SESIÓN 3: ¿Cómo organizamos datos como un club profesional? (50 minutos)
#
## Pregunta de apertura: ¿Cómo organiza el Barcelona la información de sus 25 jugadores?
#

</div>
<span class="highlight">**Reflexiona**</span>: Si fueras el director deportivo y necesitaras consultar rápidamente las estadísticas de cualquier jugador, ¿cómo organizarías esa información?
#
<span class="highlight">**Desafío organizacional**</span>: ¿Prefieres 25 variables separadas (jugador1, jugador2, ...) o una forma más inteligente de agrupar información?
#
---
#
## ¿Qué estructuras de datos usan los clubes de élite?
#
<span class="highlight">**Momento de escalabilidad**</span>: Los mejores equipos manejan información de cientos de jugadores. ¿Cómo crees que lo hacen de manera eficiente?

## Resumen de la Sesión 2
#
### Lo que aprendimos hoy:
1. <span class="highlight">**Variables de texto**</span>: guardamos nombres (entre comillas)
2. <span class="highlight">**Variables de números**</span>: enteros y decimales (sin comillas)
3. <span class="highlight">**Variables booleanas**</span>: True o False para respuestas sí/no
4. <span class="highlight">**Operaciones matemáticas**</span>: +, -, *, / para calcular estadísticas
#
### Ahora puedes:
- Crear variables para datos de fútbol
- Hacer cálculos básicos con estadísticas
- Entender diferentes tipos de información
#
---
#
# SESIÓN 3: Mi Primer Análisis de Datos de Fútbol
<span class="highlight">**Tiempo:**</span> 50 minutos | <span class="highlight">**Nivel:**</span> Preparatoria
#
---
#
## ¡Hora de analizar datos reales!
#
Ahora que conoces variables y operaciones, vamos a trabajar con <span class="highlight">**datos reales de fútbol**</span> como un analista deportivo profesional.

### Actividad: Comparando Dos Equipos
#
<span class="highlight">**¡Ahora tú eres el analista!**</span> Vamos a comparar el rendimiento de dos equipos populares:

---
#
# SÍNTESIS FINAL: ¿Qué hemos descubierto juntos esta semana?
#
## Reflexión de las 3 sesiones (150 minutos totales)
#
### SESIÓN 1: ¿Qué es realmente programar?
<span class="highlight">**Lo que dominamos ahora**</span>:
- Entender cómo las computadoras "recuerdan" información deportiva
- Distinguir entre diferentes tipos de datos (texto, números, verdadero/falso)
- Realizar operaciones matemáticas básicas como lo haría un analista
- Comprender por qué Python es el lenguaje del análisis deportivo moderno
#
### SESIÓN 2: ¿Cómo calculamos como lo haría un entrenador?
<span class="highlight">**Lo que revelamos**</span>:
- Comparar valores usando operadores matemáticos
- Crear sistemas automáticos de evaluación de jugadores
- Implementar lógica condicional (if/elif/else) para decisiones
- Imitar el proceso de pensamiento de un entrenador profesional
#
### SESIÓN 3: ¿Cómo organizamos datos como un club profesional?
<span class="highlight">**Lo que construimos**</span>:
- Organizar múltiples jugadores usando listas eficientemente
- Estructurar información compleja con diccionarios
- Procesar datos masivamente usando bucles
- Integrar todas las herramientas en un sistema de gestión básico
#
---
#
## Pregunta de transformación personal:
#
<span class="highlight">**¿Te has dado cuenta de que ya piensas como un analista de datos deportivos?**</span>
#
### ¿Qué cambió en tu forma de ver la tecnología?
#
<span class="highlight">**Reflexión personal**</span>: 
- ¿Cuál fue tu momento "¡ahá!" más importante de la semana?
- ¿Qué aspecto de la programación te resultó más natural?
- ¿Cómo cambió tu perspectiva sobre el uso de datos en deportes?
- ¿En qué otras áreas de tu vida podrías aplicar este pensamiento lógico?
#
### Vista previa de la próxima semana:
<span class="highlight">**¿Sabías que las decisiones técnicas más complejas requieren estructuras de control más sofisticadas?**</span>
#
La próxima semana exploraremos:
- Bucles para procesar estadísticas de temporadas completas
- Funciones para automatizar análisis repetitivos
- Algoritmos para encontrar patrones ocultos en datos
- Sistemas de ranking automático de jugadores
#
<div class="question">

<span class="highlight">**Pregunta motivadora**</span>: ¿Crees que podrías programar un sistema que encuentre automáticamente al próximo Messi analizando datos de juveniles?
#

</div>
<span class="highlight">**Tu misión**</span>: Esta semana has aprendido el "alfabeto" de la programación. La próxima semana aprenderás a escribir "novelas" completas de análisis deportivo.
#
¿Estás listo para el siguiente nivel de sofisticación analítica?

## ¡Felicidades! Completaste tu Primera Semana
#
### Resumen de la Sesión 3:
- Analizaste datos reales de equipos de fútbol
- Calculaste estadísticas como porcentajes y diferencias
- Comparaste el rendimiento de dos equipos
- ¡Usaste Python como un analista deportivo profesional!
#
---
#
## Lo que Lograste Esta Semana
#
### <span class="highlight">**Sesión 1**</span>: Instalación y Primer Contacto
- Instalaste Python y Jupyter Notebook
- Ejecutaste tu primer código
- Entendiste qué es la programación
#
### <span class="highlight">**Sesión 2**</span>: Variables y Operaciones
- Creaste variables de texto, números y booleanos
- Aprendiste operaciones matemáticas básicas
- Trabajaste con datos deportivos
#
### <span class="highlight">**Sesión 3**</span>: Primer Análisis Real
- Analizaste estadísticas de equipos reales
- Calculaste porcentajes y comparaciones
- Creaste tu primer "reporte" de análisis
#
---
#
## Próxima Semana: Estructuras de Control
#
### Te esperan nuevos desafíos:
- <span class="highlight">**Decisiones**</span>: ¿Cómo hacer que Python tome decisiones?
- <span class="highlight">**Repeticiones**</span>: ¿Cómo analizar muchos partidos automáticamente?
- <span class="highlight">**Listas**</span>: ¿Cómo manejar información de múltiples jugadores?
#
### Tarea para Pensar:
¿Qué otros datos de fútbol te gustaría analizar? Piensa en:
- Estadísticas de jugadores individuales
- Comparaciones entre ligas
- Análisis de rendimiento por temporada
#
---
#
## ¡Reflexión Final!
#
<span class="highlight">**¿Qué te pareció más interesante de esta semana?**</span>
<span class="highlight">**¿Qué aplicación le darías a lo que aprendiste?**</span>
#
¡Estás en el camino correcto para convertirte en un analista de datos deportivos!

```python
# ¿Cómo le decimos a Python que "recuerde" información sobre un jugador?

# Pregúntate: ¿Qué información básica necesitas de cualquier futbolista?
jugador = "Lionel Messi"  # ¿Por qué usamos comillas para el nombre?
edad = 37  # ¿Por qué NO usamos comillas para la edad?
goles = 10  # ¿Qué tipo de número representa mejor los goles?
altura = 1.70  # ¿Por qué necesitamos decimales para la altura?
es_activo = True  # ¿Qué significa True y False en programación?

# ¡Veamos qué "recordó" la computadora!
print("FICHA DEL JUGADOR")
print("=" * 25)
print(f"Nombre: {jugador}")
print(f"Edad: {edad} años")
print(f"Goles esta temporada: {goles}")
print(f"Altura: {altura} metros")
print(f"¿Está activo?: {es_activo}")

print("\nPregunta de reflexión:")
print("¿Notas cómo cada tipo de información se guarda de manera diferente?")
print("- Texto (nombres) va entre comillas")
print("- Números enteros (edad, goles) van sin comillas")
print("- Números decimales (altura) usan punto")
print("- Verdadero/Falso (estado) son True/False")

print("\n¿Por qué crees que es importante esta diferencia?")
```

```python
# ¿QUÉ CÁLCULOS DEPORTIVOS PUEDE HACER PYTHON?

print("OPERACIONES BÁSICAS CON DATOS DEPORTIVOS")
print("=" * 45)

# ¿Cuántos goles más necesita para llegar a 15 esta temporada?
goles_objetivo = 15
goles_faltantes = goles_objetivo - goles
print(f"Goles para llegar al objetivo: {goles_faltantes}")

# ¿Cuántos años tendrá cuando termine su contrato en 3 años?
anos_contrato = 3
edad_al_terminar = edad + anos_contrato
print(f"Edad al terminar contrato: {edad_al_terminar} años")

# ¿Cuál sería su altura en centímetros?
altura_cm = altura * 100
print(f"Altura en centímetros: {altura_cm} cm")

# ¿Cuántos goles lleva en promedio por cada año de edad?
# (Pregunta: ¿Por qué usamos // en lugar de / ?)
promedio_goles_por_edad = goles // edad
print(f"Goles promedio por año de vida: {promedio_goles_por_edad}")

print("\nEXPLORANDO OPERADORES:")
print("=" * 30)
print("+ (suma): para agregar valores")
print("- (resta): para encontrar diferencias")
print("* (multiplicación): para convertir unidades")
print("// (división entera): para promedios sin decimales")
print("/ (división decimal): para cálculos precisos")

print("\nPreguntas de reflexión:")
print("1. ¿Cuál es la diferencia entre // y / ?")
print("2. ¿En qué casos deportivos usarías cada operador?")
print("3. ¿Qué otros cálculos te gustaría hacer con estos datos?")
```

```python
# ¿CÓMO COMPARA PYTHON COMO LO HARÍA UN ENTRENADOR?

print("ANÁLISIS COMPARATIVO DE RENDIMIENTO")
print("=" * 40)

# Datos de comparación deportiva
partidos_jugados = 25
minutos_jugados = 2250

# ¿Es un jugador experimentado? (más de 30 años)
es_veterano = edad > 30
print(f"¿Es un veterano (>30 años)?: {es_veterano}")

# ¿Está en forma goleadora? (más de 8 goles)
en_forma = goles > 8
print(f"¿Está en buena forma goleadora?: {en_forma}")

# ¿Es un jugador clave? (más de 20 partidos)
es_titular = partidos_jugados > 20
print(f"¿Es jugador titular habitual?: {es_titular}")

# ¿Cuál es su promedio de goles por partido?
promedio_goles_por_partido = goles / partidos_jugados
print(f"Promedio de goles por partido: {promedio_goles_por_partido:.2f}")

# ¿Es un goleador eficiente? (más de 0.3 goles por partido)
es_goleador = promedio_goles_por_partido > 0.3
print(f"¿Es considerado goleador?: {es_goleador}")

print("\nOPERADORES DE COMPARACIÓN:")
print("=" * 30)
print("> (mayor que): para superar límites")
print("< (menor que): para estar por debajo")
print(">= (mayor o igual): para alcanzar mínimos")
print("<= (menor o igual): para no exceder máximos")
print("== (igual a): para coincidencias exactas")
print("!= (diferente de): para exclusiones")

print("\nPreguntas de análisis:")
print("1. ¿Por qué las comparaciones devuelven True o False?")
print("2. ¿Qué otros límites deportivos podrías evaluar?")
print("3. ¿Cómo ayudan estas comparaciones en decisiones técnicas?")

# ¿Qué significa cada resultado?
print(f"\nINTERPRETACIÓN:")
print(
    f"Veterano: {es_veterano} - {'Experiencia valiosa' if es_veterano else 'Jugador joven'}"
)
print(f"En forma: {en_forma} - {'Buen momento' if en_forma else 'Puede mejorar'}")
print(
    f"Titular: {es_titular} - {'Jugador clave' if es_titular else 'Necesita más minutos'}"
)
```

```python
# ¿CÓMO TOMA DECISIONES AUTOMÁTICAS NUESTRO "ASISTENTE TÉCNICO"?

print("SISTEMA AUTOMÁTICO DE EVALUACIÓN DE JUGADORES")
print("=" * 50)

# ¿Debería este jugador ser convocado? Veamos qué decide Python...

print("ANÁLISIS PARA CONVOCATORIA:")
print("-" * 30)

# Regla 1: ¿Cumple criterios de edad?
if edad < 35:
    print("Edad apropiada para alto rendimiento")
    convocable_por_edad = True
else:
    print("Jugador veterano - requiere evaluación especial")
    convocable_por_edad = False

# Regla 2: ¿Está en forma goleadora?
if goles >= 8:
    print("Excelente forma goleadora")
    convocable_por_goles = True
elif goles >= 5:
    print("Forma aceptable")
    convocable_por_goles = True
else:
    print("Necesita mejorar efectividad")
    convocable_por_goles = False

# Regla 3: ¿Cuál es su estado físico estimado?
if altura > 1.80:
    ventaja_fisica = "Buena presencia aérea"
elif altura > 1.70:
    ventaja_fisica = "Altura promedio equilibrada"
else:
    ventaja_fisica = "Ventaja en velocidad y agilidad"

print(f"Análisis físico: {ventaja_fisica}")

# Decisión final del sistema
if convocable_por_edad and convocable_por_goles:
    decision_final = "CONVOCADO"
    estado_decision = "APROBADO"
else:
    decision_final = "EVALUACIÓN PENDIENTE"
    estado_decision = "PENDIENTE"

print(f"\n{estado_decision} - DECISIÓN FINAL: {decision_final}")

print("\nESTRUCTURA DE DECISIONES:")
print("=" * 35)
print("if (condición): - SI se cumple la condición")
print("    # hacer algo - ENTONCES ejecutar esta acción")
print("elif (otra_condición): - SINO SI se cumple otra condición")
print("    # hacer otra cosa - ENTONCES ejecutar esta otra acción")
print("else: - SINO")
print("    # alternativa final - ENTONCES ejecutar acción por defecto")

print("\nPreguntas de reflexión:")
print("1. ¿Cómo ayuda la indentación (espacios) a Python?")
print("2. ¿Qué otros criterios usarías para convocar jugadores?")
print("3. ¿Por qué es útil que la computadora tome decisiones automáticas?")
print("4. ¿En qué se parece esto a como piensa un entrenador real?")
```

```python
# ¿CÓMO ORGANIZAMOS MÚLTIPLES JUGADORES DE MANERA INTELIGENTE?

print("CREANDO NUESTRO PRIMER 'PLANTEL DIGITAL'")
print("=" * 45)

# ¿Cómo almacenaríamos una lista de convocados?
# Pregunta: ¿Qué es más eficiente: 11 variables separadas o una lista?

jugadores_convocados = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Kylian Mbappé",
    "Erling Haaland",
    "Vinicius Jr",
]

print("LISTA DE CONVOCADOS:")
print("-" * 20)
for i, nombre in enumerate(jugadores_convocados, 1):
    print(f"{i}. {nombre}")

# ¿Cuántos jugadores tenemos convocados?
total_convocados = len(jugadores_convocados)
print(f"\nTotal de jugadores convocados: {total_convocados}")

# ¿Cómo accedemos a un jugador específico?
primer_jugador = jugadores_convocados[0]  # ¿Por qué empezamos en 0?
ultimo_jugador = jugadores_convocados[-1]  # ¿Qué significa el -1?

print(f"Primer convocado: {primer_jugador}")
print(f"Último convocado: {ultimo_jugador}")

print("\nPreguntas sobre listas:")
print("=" * 25)
print("1. ¿Por qué los índices empiezan en 0 y no en 1?")
print("2. ¿Qué ventajas tiene usar listas vs variables separadas?")
print("3. ¿Cómo agregarías un jugador más a la lista?")
print("4. ¿Qué pasa si intentas acceder a la posición 10?")

# ¿Podemos organizar información más compleja?
print("\n" + "=" * 45)
print("ORGANIZANDO ESTADÍSTICAS COMPLETAS DE UN JUGADOR")
print("=" * 45)

# ¿Cómo relacionamos diferentes tipos de datos de un mismo jugador?
estadisticas_messi = {
    "nombre": "Lionel Messi",
    "edad": 37,
    "goles_temporada": 10,
    "asistencias": 8,
    "partidos_jugados": 25,
    "posicion": "Extremo Derecho",
    "es_capitan": True,
}

print("FICHA COMPLETA DEL JUGADOR:")
print("-" * 30)
for clave, valor in estadisticas_messi.items():
    print(f"{clave.replace('_', ' ').title()}: {valor}")

# ¿Cómo accedemos a información específica?
print(f"\nGoles esta temporada: {estadisticas_messi['goles_temporada']}")
print(f"Asistencias: {estadisticas_messi['asistencias']}")

# ¿Es el capitán del equipo?
if estadisticas_messi["es_capitan"]:
    print("Es el capitán del equipo")
else:
    print("No es capitán")

print("\nDIFERENCIAS CLAVE:")
print("=" * 20)
print("LISTAS [] - Para elementos del mismo tipo")
print("   Ejemplo: lista de nombres, lista de goles")
print("DICCIONARIOS {} - Para información relacionada")
print("   Ejemplo: todos los datos de un jugador")

print("\nPreguntas de organización:")
print("1. ¿Cuándo usarías una lista y cuándo un diccionario?")
print("2. ¿Cómo organizarías las estadísticas de todo un equipo?")
print("3. ¿Qué información adicional incluirías en la ficha del jugador?")
```

```python
# Análisis del Rendimiento del FC Barcelona
# Datos de la temporada (ejemplo)

print("=== ANÁLISIS FC BARCELONA ===")
print()

# Datos del equipo
nombre_equipo = "FC Barcelona"
partidos_jugados = 10
victorias = 7
empates = 2
derrotas = 1

# Calculamos estadísticas
puntos_totales = (victorias * 3) + (empates * 1) + (derrotas * 0)
porcentaje_victorias = (victorias / partidos_jugados) * 100

print("Equipo:", nombre_equipo)
print("Partidos jugados:", partidos_jugados)
print("Victorias:", victorias)
print("Empates:", empates)
print("Derrotas:", derrotas)
print()
print("ESTADÍSTICAS CALCULADAS:")
print("Puntos totales:", puntos_totales)
print("Porcentaje de victorias:", porcentaje_victorias, "%")
```

```python
# PROYECTO FINAL: ¿CÓMO CREARÍAMOS UN SISTEMA COMPLETO DE GESTIÓN?

print("INTEGRANDO TODO LO APRENDIDO")
print("=" * 40)

# ¿Podemos combinar listas, diccionarios y decisiones automáticas?
# ¡Vamos a crear un mini-sistema de gestión deportiva!

# Base de datos de jugadores
plantilla_completa = [
    {"nombre": "Lionel Messi", "goles": 10, "edad": 37, "posicion": "Extremo"},
    {"nombre": "Cristiano Ronaldo", "goles": 12, "edad": 39, "posicion": "Delantero"},
    {"nombre": "Kylian Mbappé", "goles": 15, "edad": 25, "posicion": "Extremo"},
    {"nombre": "Erling Haaland", "goles": 18, "edad": 24, "posicion": "Delantero"},
]

print("ANÁLISIS AUTOMÁTICO DE LA PLANTILLA")
print("-" * 35)

# ¿Quiénes son los máximos goleadores?
for jugador in plantilla_completa:
    nombre = jugador["nombre"]
    goles = jugador["goles"]
    edad = jugador["edad"]

    # Sistema automático de clasificación
    if goles >= 15:
        categoria = "ESTRELLA GOLEADORA"
    elif goles >= 10:
        categoria = "GOLEADOR REGULAR"
    else:
        categoria = "EN DESARROLLO"

    # ¿Es un jugador joven con potencial?
    if edad < 26:
        potencial = " (GRAN POTENCIAL)"
    else:
        potencial = " (VETERANO EXPERTO)"

    print(f"{nombre}: {goles} goles - {categoria}{potencial}")

# ¿Cuál es el promedio de goles del equipo?
total_goles_equipo = 0
for jugador in plantilla_completa:
    total_goles_equipo += jugador["goles"]

promedio_equipo = total_goles_equipo / len(plantilla_completa)
print(f"\nPromedio de goles del equipo: {promedio_equipo:.1f}")

# ¿Quién está por encima del promedio?
print(f"\nJUGADORES SOBRE EL PROMEDIO ({promedio_equipo:.1f}):")
for jugador in plantilla_completa:
    if jugador["goles"] > promedio_equipo:
        print(f"- {jugador['nombre']}: {jugador['goles']} goles")

print("\nRESUMEN DE CAPACIDADES DESARROLLADAS:")
print("=" * 45)
print("- Variables: Guardar información individual")
print("- Operaciones: Realizar cálculos deportivos")
print("- Comparaciones: Evaluar rendimientos")
print("- Condicionales: Tomar decisiones automáticas")
print("- Listas: Organizar múltiples elementos")
print("- Diccionarios: Estructura datos relacionados")
print("- Bucles: Procesar información masivamente")

print("\nREFLEXIÓN FINAL:")
print("¿Te das cuenta de que acabas de crear un sistema básico")
print("similar a los que usan clubes profesionales para gestionar")
print("sus plantillas y tomar decisiones basadas en datos?")

print("\nPRÓXIMO NIVEL:")
print("¿Estás listo para aprender cómo los clubes de élite")
print("procesan estadísticas de cientos de jugadores automáticamente?")
```

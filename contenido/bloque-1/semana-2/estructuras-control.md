---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.2
  kernelspec:
    display_name: .venv (3.10.12)
    language: python
    name: python3
---

# Semana 2: ¿Cómo automatizamos decisiones repetitivas como un entrenador profesional?

## ¿Alguna vez has observado los patrones de decisión en el fútbol moderno?

**Reflexión inicial**: Cuando ves a Pep Guardiola dirigir un partido, ¿has notado que toma ciertos tipos de decisiones de manera sistemática? "SI el rival presiona alto, ENTONCES jugamos por las bandas", "MIENTRAS tengamos posesión, CONTINUAR con pases cortos".

### Pregunta motivadora para la semana

Si tuvieras que programar un asistente técnico que tome decisiones automáticas durante 90 minutos de partido, ¿qué instrucciones le darías?

---

## ESTRUCTURA SEMANAL: 3 Sesiones de Descubrimiento

### SESIÓN 1: ¿Cómo repetimos tareas como un entrenamiento sistemático? (50 min)

**Pregunta guía**: ¿Qué hace un equipo cuando practica jugadas una y otra vez?

- ¿Cómo automatizamos acciones repetitivas en Python?
- ¿Por qué la repetición controlada mejora el rendimiento?
- ¿Cuándo sabemos que hemos practicado lo suficiente?

### SESIÓN 2: ¿Cómo tomamos decisiones complejas bajo presión? (50 min)  

**Pregunta guía**: ¿Qué proceso mental sigue un capitán antes de cada jugada?

- ¿Cómo combinamos múltiples condiciones como un estratega?
- ¿Por qué algunos equipos son más predecibles que otros?
- ¿Cómo optimizamos la toma de decisiones rápida?

### SESIÓN 3: ¿Cómo organizamos estrategias complejas de manera elegante? (50 min)

**Pregunta guía**: ¿Cómo simplifica Messi las jugadas más complicadas?

- ¿Qué ventajas tiene dividir problemas grandes en partes pequeñas?
- ¿Cómo reutilizamos tácticas exitosas en diferentes situaciones?
- ¿Por qué la organización determina la efectividad del análisis?

---

## ¿Por qué automatizar decisiones deportivas?

**Pregunta reflexiva**: ¿Sabías que los equipos de élite procesan más de 200 decisiones tácticas diferentes durante un partido promedio?

### La evolución del pensamiento táctico

- **¿Te imaginas que...?** Cada sustitución sigue algoritmos de decisión complejos
- **¿Sabías que...?** Los análisis post-partido procesan miles de datos automáticamente
- **¿Has considerado que...?** Las estrategias ganadoras se basan en patrones repetibles

**Tu misión esta semana**: Aprender a crear sistemas de decisión automática que piensen como un entrenador profesional.

¿Estás listo para descubrir cómo la repetición inteligente genera excelencia deportiva?

# SESIÓN 1: ¿Cómo repetimos tareas como un entrenamiento sistemático? (50 minutos)

## Pregunta de apertura: ¿Qué tienen en común un ejercicio de pases y un bucle en programación?

**Reflexiona antes de continuar**: Ambos repiten una acción específica hasta alcanzar un objetivo. En fútbol: "repite 100 pases hasta automatizar la técnica". En programación: "repite este cálculo hasta procesar todos los jugadores".

---

## Momento de curiosidad: ¿Por qué la repetición genera maestría?

Imagina que eres el preparador físico del Real Madrid. Necesitas que cada jugador complete exactamente 20 sprints de 30 metros. ¿Cómo te asegurarías de que TODOS cumplan sin excepción?

**Pregunta reflexiva**: ¿Preferirías decirle a cada jugador individualmente "corre 30 metros" 20 veces, o crear un sistema que automáticamente supervise las 20 repeticiones?

### ¿Cómo enseñamos a Python a ser tan sistemático como un entrenador?

**Piensa en esto**: Los mejores entrenadores nunca dejan nada al azar. Cada ejercicio tiene un número específico de repeticiones, cada práctica sigue un patrón. ¿Cómo podríamos darle esa misma precisión a nuestro código?

## ¿Cómo procesamos listas de jugadores de manera automática?

**Pregunta crucial**: Si tuvieras que calcular las estadísticas de 25 jugadores de un equipo, ¿escribirías 25 líneas de código iguales o buscarías una forma más inteligente?

**Analogía táctica**: Es como un corner ensayado. En lugar de explicar la jugada 11 veces (una a cada jugador), el entrenador da una instrucción que TODOS ejecutan automáticamente.

### ¡Vamos a ver cómo Python maneja las repeticiones automáticas

### Creando tu primera alineación

**¿Cómo crearías la alineación titular del Barcelona?**

Una lista se crea usando corchetes [ ] y separando elementos con comas:

```python
# ¿CÓMO PROCESAN LOS CLUBES PROFESIONALES LAS LISTAS DE JUGADORES?

print("PROCESAMIENTO AUTOMÁTICO DE PLANTILLA")
print("="*40)

# ¿Cómo analizaríamos rápidamente toda una plantilla?
# Pregunta: ¿Qué es más eficiente: 11 variables separadas o una lista automatizada?

plantilla_barcelona = [
    "Ter Stegen",
    "Pedri", 
    "Gavi",
    "Lewandowski",
    "Raphinha",
    "Frenkie de Jong",
    "Ronald Araújo",
    "Jules Koundé"
]

print("LISTA OFICIAL DE CONVOCADOS:")
print("-" * 25)

# ¿Cómo presenta la lista un entrenador profesional?
for numero_jugador, nombre_jugador in enumerate(plantilla_barcelona, 1):
    print(f"{numero_jugador:2d}. {nombre_jugador}")

# ¿Cuántos jugadores tenemos convocados automáticamente?
total_convocados = len(plantilla_barcelona)
print(f"\nTotal de jugadores procesados: {total_convocados}")

print("\nReflexión importante:")
print("¿Notas cómo una sola instrucción 'for' procesó TODA la lista?")
print("¿Qué pasaría si tuviéramos 25 jugadores en lugar de 8?")
print("¿El código cambiaría en algo? ¡Exactamente! Esa es la magia de la automatización.")

print("\nPregunta de análisis:")
print("¿En qué se parece este bucle 'for' a cuando un entrenador")
print("pasa lista antes del entrenamiento?")
```

## ¿Qué pasa cuando no sabemos cuántas repeticiones necesitamos?

**Pregunta estratégica**: Imagina que eres Xavi y quieres que tus jugadores practiquen penales HASTA que cada uno anote 5 consecutivos. ¿Sabes de antemano cuántos intentos necesitará cada jugador?

**Situación real**: Algunos podrían necesitar 6 intentos, otros 15, otros 25. El criterio no es "repite X veces", sino "repite HASTA que logres el objetivo".

### ¿Cómo programamos esta lógica de "continuar hasta lograr el objetivo"?

**Analogía deportiva**: Es como la diferencia entre "corre 10 vueltas" (sabemos el número) y "corre hasta que tu ritmo cardíaco baje a 120" (depende de una condición).

### Actividad Práctica: Tu Equipo Ideal

Pregunta clave: **¿Cómo organizarías tu equipo ideal?**

**Tiempo estimado: 8 minutos**

Reflexiona mientras creamos tu lista:

- ¿Qué jugadores incluirías en tu equipo favorito?
- ¿En qué orden los colocarías según su importancia?
- ¿Cómo accederías rápidamente a información específica de cada jugador?

```python
# ¿CÓMO SIMULAMOS UNA PRÁCTICA DE PENALES "HASTA LOGRAR EL OBJETIVO"?

print("SIMULACIÓN: PRÁCTICA DE PENALES DE MESSI")
print("="*45)

# Objetivo: Anotar 5 penales consecutivos
# Pregunta: ¿Cuántos intentos necesitará? ¡No lo sabemos!

import random

penales_consecutivos = 0
intentos_totales = 0
objetivo = 5

print(f"Objetivo: {objetivo} penales consecutivos")
print("Simulando práctica...")
print("-" * 25)

# ¿Cómo funciona la lógica "MIENTRAS no logre el objetivo"?
while penales_consecutivos < objetivo:
    intentos_totales += 1
    
    # ¿Anota el penal? (85% de efectividad de Messi)
    penal_anotado = random.random() < 0.85  # 85% de probabilidad
    
    if penal_anotado:
        penales_consecutivos += 1
        print(f"Intento {intentos_totales}: GOOOOL - Consecutivos: {penales_consecutivos}")
    else:
        penales_consecutivos = 0  # Se reinicia la racha
        print(f"Intento {intentos_totales}: FALLO - Racha reiniciada")
    
    # Protección: evitar bucle infinito en simulación
    if intentos_totales > 50:
        print("Práctica suspendida (límite de intentos alcanzado)")
        break

if penales_consecutivos >= objetivo:
    print(f"\nOBJETIVO LOGRADO!")
    print(f"Messi necesitó {intentos_totales} intentos totales")
    print(f"para anotar {objetivo} penales consecutivos")

print("\nAnálisis de la lógica 'while':")
print("="*30)
print("- MIENTRAS (condición sea verdadera):")
print("  - Ejecuta las acciones")
print("  - Verifica la condición nuevamente") 
print("- CUANDO la condición se vuelve falsa: PARA")

print("\nPreguntas de reflexión:")
print("1. ¿Por qué usamos 'while' en lugar de 'for' aquí?")
print("2. ¿Qué hubiera pasado sin la protección de 50 intentos?")
print("3. ¿En qué otros entrenamientos deportivos aplicarías esta lógica?")
print("4. ¿Cuál es la diferencia clave entre 'for' y 'while'?")
```

---

## SÍNTESIS DE LA SESIÓN 1: ¿Qué patrones de repetición dominamos?

**Reflexión de 50 minutos**:

- ¿Cómo automatizamos el procesamiento de listas completas de jugadores?
- ¿Cuándo usamos 'for' (repeticiones conocidas) vs 'while' (hasta lograr objetivo)?
- ¿Por qué la automatización es crucial en análisis deportivo masivo?

**Pregunta preparatoria**: ¿Estás listo para que Python tome decisiones complejas combinando múltiples condiciones como un estratega?

---

# SESIÓN 2: ¿Cómo tomamos decisiones complejas bajo presión? (50 minutos)

## Pregunta de apertura: ¿Qué diferencia a Guardiola de otros entrenadores en situaciones críticas?

**Reflexiona**: En los últimos 10 minutos de un partido importante, ¿has notado cómo los grandes entrenadores evalúan múltiples factores simultáneamente? "SI vamos perdiendo Y tenemos posesión Y quedan menos de 15 minutos, ENTONCES cambio la formación a 3-4-3".

**Desafío mental**: Si tuvieras que programar las decisiones de Ancelotti durante un Real Madrid vs Barcelona, ¿qué variables considerarías y cómo las combinarías?

---

## ¿Cómo combinamos condiciones múltiples como un director técnico?

**Momento de complejidad estratégica**: Los entrenadores de élite nunca toman decisiones basándose en un solo factor. ¿Cómo enseñamos a Python a pensar con esa misma sofisticación?

## Diccionarios: Fichas Completas de Jugadores

Las listas nos permiten organizar nombres, pero **¿qué pasa cuando necesitamos más información de cada jugador?**

En el fútbol, cada jugador tiene múltiples características:

- Nombre
- Posición
- Edad
- Equipo
- Goles anotados

Los **diccionarios** nos permiten organizar esta información compleja de manera eficiente.

```python
# Creando una ficha completa de jugador con diccionario
ficha_messi = {
    "nombre": "Lionel Messi",
    "posicion": "Delantero",
    "edad": 36,
    "equipo": "Inter Miami",
    "goles_temporada": 11,
    "pais": "Argentina"
}

print("=== FICHA DE JUGADOR ===")
print("Nombre:", ficha_messi["nombre"])
print("Posición:", ficha_messi["posicion"])
print("Edad:", ficha_messi["edad"])
print("Equipo actual:", ficha_messi["equipo"])
print("Goles esta temporada:", ficha_messi["goles_temporada"])
```

---

## Resumen de la Sesión 1 (50 minutos)

**¿Qué hemos aprendido sobre organización de datos futbolísticos?**

### Conceptos Clave

- **Listas**: Para organizar secuencias de elementos (alineaciones, equipos)
- **Diccionarios**: Para almacenar información completa y estructurada
- **Acceso a datos**: Usando índices y claves para obtener información específica

### Aplicación Futbolística

- Creación de alineaciones usando listas
- Fichas completas de jugadores con diccionarios
- Organización eficiente de datos deportivos

**Pregunta para reflexionar**: ¿Cómo podrías usar estas estructuras para organizar toda la información de tu equipo favorito?

---

**Próxima sesión**: Aprenderemos a tomar decisiones automáticas basadas en estos datos usando estructuras de control.

# Sesión 2: Estructuras de Control y Decisiones Futbolísticas

**(50 minutos)**

## Objetivo de la Sesión

Aprender a crear programas que tomen decisiones automáticas basadas en datos futbolísticos.

### Pregunta Central

**¿Cómo puede un programa tomar decisiones como un entrenador?**

En el fútbol, los entrenadores constantemente toman decisiones:

- ¿Este jugador está en forma para jugar?
- ¿Debemos cambiar la formación según el marcador?
- ¿Qué jugador debería tomar el penalty?

Hoy aprenderemos a programar estas decisiones usando **estructuras de control**.

---

## Estructuras Condicionales: If, Elif, Else

**Pregunta reflexiva**: ¿Cómo decides si un jugador debe ser titular o suplente?

Los entrenadores evalúan múltiples condiciones:

- Si el jugador está lesionado → No juega
- Si tiene tarjetas amarillas → Evaluar riesgo  
- Si está en buena forma → Es titular
- En caso contrario → Va al banquillo

En programación usamos **if, elif, else** para estas decisiones.

```python
# ¿CÓMO EVALÚAN LOS ENTRENADORES MÚLTIPLES CONDICIONES SIMULTÁNEAMENTE?

print("SISTEMA DE DECISIÓN TÁCTICA AVANZADA")
print("="*40)

# Datos del partido: Real Madrid vs Barcelona (minuto 75)
marcador_local = 1
marcador_visitante = 1  
minuto_actual = 75
jugadores_con_tarjeta = 2
lesionados = 1
energia_equipo = 7  # Escala del 1 al 10

print("SITUACIÓN DEL PARTIDO:")
print("-" * 20)
print(f"Marcador: {marcador_local} - {marcador_visitante}")
print(f"Minuto: {minuto_actual}")
print(f"Jugadores con tarjeta amarilla: {jugadores_con_tarjeta}")  
print(f"Lesionados: {lesionados}")
print(f"Nivel de energía del equipo: {energia_equipo}/10")

print("\nANÁLISIS DE DECISIÓN ESTRATÉGICA:")
print("="*35)

# ¿Necesitamos cambio ofensivo urgente?
# Un entrenador evalúa: ¿Vamos empate Y queda poco tiempo Y tenemos energía?
cambio_ofensivo_urgente = (marcador_local == marcador_visitante and 
                          minuto_actual >= 70 and 
                          energia_equipo >= 6)

print(f"¿Cambio ofensivo urgente?: {cambio_ofensivo_urgente}")

# ¿Debemos ser conservadores?
# Evalúa: ¿Vamos ganando O tenemos muchos amonestados O bajo nivel físico?
jugar_conservador = (marcador_local > marcador_visitante or 
                    jugadores_con_tarjeta >= 3 or 
                    energia_equipo <= 4)

print(f"¿Jugar conservador?: {jugar_conservador}")

# ¿Es momento de cambios por lesión?
# Solo si: NO vamos perdiendo Y tenemos lesionados Y aún queda tiempo
cambios_por_lesion = (not (marcador_local < marcador_visitante) and 
                     lesionados > 0 and 
                     minuto_actual <= 80)

print(f"¿Cambios por lesión?: {cambios_por_lesion}")

print("\nDECISIÓN FINAL DEL ENTRENADOR:")
print("-" * 30)

if cambio_ofensivo_urgente and not jugar_conservador:
    decision = "CAMBIO ULTRA-OFENSIVO: 3 delanteros"
elif jugar_conservador:
    decision = "MANTENER SOLIDEZ DEFENSIVA"
elif cambios_por_lesion:
    decision = "CAMBIO TÁCTICO POR LESIONES"
else:
    decision = "MANTENER ESQUEMA ACTUAL"

print(f"Decisión: {decision}")

print("\nOPERADORES LÓGICOS EXPLICADOS:")
print("="*30)
print("and - TODAS las condiciones deben ser verdaderas")
print("or  - AL MENOS UNA condición debe ser verdadera")  
print("not - INVIERTE el valor (True se vuelve False)")

print("\nPreguntas de reflexión:")
print("1. ¿Cómo se parece esto al proceso mental de un entrenador real?")
print("2. ¿Qué otras variables incluirías en las decisiones?")
print("3. ¿Por qué es importante combinar condiciones con 'and' y 'or'?")
print("4. ¿En qué situaciones deportivas usarías 'not'?")
```

```python
# ¿CÓMO ESTRUCTURAN LOS TÉCNICOS SUS DECISIONES EN CASCADA?

print("SISTEMA DE SUSTITUCIONES INTELIGENTE")
print("="*40)

# Datos de un jugador específico  
nombre_jugador = "Pedri"
minutos_jugados = 78
goles_anotados = 1
asistencias = 2
tarjetas_amarillas = 1
nivel_cansancio = 8  # Escala del 1 al 10 (10 = muy cansado)
lesion_previa = False

print(f"EVALUACIÓN DE: {nombre_jugador}")
print("-" * 25)
print(f"Minutos jugados: {minutos_jugados}")
print(f"Goles: {goles_anotados}")
print(f"Asistencias: {asistencias}")
print(f"Tarjetas amarillas: {tarjetas_amarillas}")
print(f"Nivel de cansancio: {nivel_cansancio}/10")
print(f"Lesión previa: {lesion_previa}")

print("\nANÁLISIS JERÁRQUICO DE SUSTITUCIÓN:")
print("="*35)

# ¿Cómo piensa un entrenador? Jerarquía de decisiones
if lesion_previa:
    decision = "SUBSTITUCIÓN INMEDIATA por seguridad"
    prioridad = "CRÍTICA"
else:
    # Si no hay lesión, evaluamos rendimiento y cansancio
    if goles_anotados >= 1 or asistencias >= 2:
        # Jugador destacado
        if nivel_cansancio >= 8:
            decision = "Substitución al minuto 85 (preservar estrella)"
            prioridad = "MODERADA"
        else:
            decision = "MANTENER en campo (está brillando)"
            prioridad = "BAJA"
    else:
        # Jugador sin grandes aportes
        if nivel_cansancio >= 7 or tarjetas_amarillas >= 1:
            decision = "Substitución ahora (liberar espacio)"
            prioridad = "ALTA"
        else:
            if minutos_jugados >= 75:
                decision = "Substitución próximos 5 minutos"
                prioridad = "MODERADA"
            else:
                decision = "Continuar evaluando"
                prioridad = "BAJA"

print(f"Decisión: {decision}")
print(f"Prioridad: {prioridad}")

print("\nLÓGICA DE DECISIÓN JERÁRQUICA:")
print("="*30)
print("1. PRIMERO: ¿Hay riesgo de lesión? (máxima prioridad)")
print("2. SEGUNDO: ¿El jugador está rindiendo bien?")
print("3. TERCERO: ¿Está muy cansado o en riesgo de tarjeta?") 
print("4. ÚLTIMO: ¿Cuántos minutos lleva jugando?")

print("\nPATRÓN DE CONDICIONALES ANIDADOS:")
print("if (condición_crítica):")
print("    # acción inmediata")
print("else:")
print("    if (condición_importante):")
print("        if (subcondición):")
print("            # acción específica")
print("        else:")
print("            # alternativa")

print("\nPreguntas de reflexión:")
print("1. ¿Por qué evaluamos la lesión ANTES que el rendimiento?")
print("2. ¿Cómo se parece esta estructura a las decisiones reales?")
print("3. ¿Qué ventaja tienen las decisiones 'anidadas'?")
print("4. ¿Qué otros criterios agregarías a esta evaluación?")
```

---

## SÍNTESIS DE LA SESIÓN 2: ¿Qué decisiones complejas dominamos?

**Reflexión de 50 minutos**:

- ¿Cómo combinamos múltiples condiciones con operadores lógicos (and, or, not)?
- ¿Por qué las decisiones jerárquicas (condicionales anidados) reflejan el pensamiento real?
- ¿Cómo la lógica de programación imita los procesos mentales de un entrenador?

**Pregunta preparatoria**: ¿Estás listo para organizar toda esta complejidad en sistemas elegantes y reutilizables?

---

# SESIÓN 3: ¿Cómo organizamos estrategias complejas de manera elegante? (50 minutos)

## Pregunta de apertura: ¿Por qué Messi hace ver fácil lo que es extremadamente complejo?

**Reflexiona**: Cuando ves a Messi resolver una jugada que requiere 15 movimientos coordinados en 3 segundos, ¿crees que está pensando en cada paso individual o tiene "patrones" automatizados?

**Desafío organizacional**: Si tuvieras que enseñar las tácticas del Barcelona a un equipo juvenil, ¿las explicarías como 1000 instrucciones separadas o las dividirías en "jugadas" reutilizables?

---

## ¿Cómo creamos "jugadas tácticas" reutilizables en código?

**Momento de elegancia**: Los mejores entrenadores convierten estrategias complejas en sistemas simples. ¿Cómo aplicamos esa misma filosofía a nuestro código?

### 2.2 Diccionarios - ¿Cómo organizamos información con etiquetas?

**Pregunta de conexión**: Si las listas son como una fila de jugadores numerados, ¿cómo sería tener una "ficha" de cada jugador con etiquetas claras?

**Desafío conceptual**: ¿Qué es más fácil: recordar que la edad de Messi está en la posición 2 de una lista, o simplemente preguntar por "edad"?

```python
# ¿CÓMO CREAMOS "JUGADAS TÁCTICAS" REUTILIZABLES EN CÓDIGO?

print("CREANDO NUESTRO PRIMER SISTEMA TÁCTICO")
print("="*40)

# ¿Qué pasaría si necesitáramos evaluar 25 jugadores?
# ¿Escribiríamos el mismo código 25 veces?

def evaluar_jugador_para_convocatoria(nombre, goles, asistencias, edad, lesionado):
    """
    Función que simula el proceso mental de un entrenador
    para decidir si convoca a un jugador.
    
    Es como tener un 'patrón de evaluación' que aplicamos
    consistentemente a todos los candidatos.
    """
    print(f"\nEVALUANDO A: {nombre}")
    print("-" * 20)
    
    # ¿Cumple criterios básicos?
    if lesionado:
        decision = "NO CONVOCADO - Lesionado"
        puntuacion = 0
    elif edad > 35:
        decision = "EVALUACIÓN ESPECIAL - Veterano"
        puntuacion = 5
    else:
        # Sistema de puntuación deportiva
        puntuacion = (goles * 3) + (asistencias * 2)
        
        if puntuacion >= 15:
            decision = "CONVOCADO - Rendimiento excelente"
        elif puntuacion >= 8:
            decision = "CONVOCADO - Rendimiento bueno"
        else:
            decision = "NO CONVOCADO - Necesita mejorar"
    
    print(f"Goles: {goles}, Asistencias: {asistencias}, Edad: {edad}")
    print(f"Puntuación: {puntuacion}")
    print(f"Decisión: {decision}")
    
    return decision, puntuacion

# ¡Probemos nuestro sistema con varios jugadores!
print("PROCESO DE CONVOCATORIA AUTOMÁTICA")
print("="*35)

# ¿Cómo evaluaría el técnico a estos candidatos?
evaluar_jugador_para_convocatoria("Lewandowski", 5, 3, 35, False)
evaluar_jugador_para_convocatoria("Pedri", 2, 8, 21, False)  
evaluar_jugador_para_convocatoria("Ansu Fati", 1, 1, 21, True)
evaluar_jugador_para_convocatoria("Busquets", 0, 5, 35, False)

print("\n" + "="*40)
print("VENTAJAS DE LAS FUNCIONES:")
print("="*25)
print("1. REUTILIZACIÓN: Una sola definición, múltiples usos")
print("2. CONSISTENCIA: Mismos criterios para todos")
print("3. MANTENIMIENTO: Cambiar lógica en un solo lugar")
print("4. CLARIDAD: Código más fácil de entender")

print("\nPreguntas de reflexión:")
print("1. ¿En qué se parece una función a una 'jugada ensayada'?")
print("2. ¿Qué ventaja tiene definir criterios una sola vez?")
print("3. ¿Cómo mejorarías los criterios de evaluación?")
print("4. ¿Qué otras 'funciones tácticas' crearías para un club?")
```

```python
# ¿CÓMO CREAMOS SISTEMAS TÁCTICOS QUE "DEVUELVAN" RESULTADOS ÚTILES?

print("SISTEMA AVANZADO DE ANÁLISIS TÁCTICO")
print("="*40)

def analizar_rendimiento_equipo(goles_favor, goles_contra, partidos_jugados):
    """
    Función que analiza el rendimiento general del equipo
    y devuelve múltiples métricas, como lo haría un analista profesional.
    """
    # ¿Cuáles son las métricas clave que evalúa un técnico?
    promedio_goles_favor = goles_favor / partidos_jugados
    promedio_goles_contra = goles_contra / partidos_jugados
    diferencia_goles = goles_favor - goles_contra
    
    # ¿Cómo clasificaríamos el rendimiento?
    if promedio_goles_favor >= 2.0 and promedio_goles_contra <= 1.0:
        categoria = "EQUIPO DE ÉLITE"
    elif promedio_goles_favor >= 1.5 and promedio_goles_contra <= 1.5:
        categoria = "EQUIPO SÓLIDO"
    elif diferencia_goles > 0:
        categoria = "EQUIPO EN DESARROLLO"
    else:
        categoria = "EQUIPO NECESITA REFUERZOS"
    
    # Retornamos MÚLTIPLES valores (¡muy útil!)
    return promedio_goles_favor, promedio_goles_contra, categoria

def calcular_efectividad_jugador(goles, tiros_totales, minutos_jugados):
    """
    Calcula la efectividad de un jugador específico.
    ¿Qué métricas usa un entrenador para evaluar delanteros?
    """
    if tiros_totales == 0:
        efectividad_tiro = 0
    else:
        efectividad_tiro = (goles / tiros_totales) * 100
    
    goles_por_90_min = (goles / minutos_jugados) * 90
    
    # ¿Es un delantero eficiente?
    if efectividad_tiro >= 25 and goles_por_90_min >= 0.5:
        calificacion = "DELANTERO LETAL"
    elif efectividad_tiro >= 15:
        calificacion = "DELANTERO EFICIENTE"
    else:
        calificacion = "NECESITA TRABAJAR DEFINICIÓN"
    
    return efectividad_tiro, goles_por_90_min, calificacion

# ¡Probemos nuestros sistemas de análisis!
print("ANÁLISIS DEL FC BARCELONA")
print("-" * 25)

# ¿Cómo rinde el equipo esta temporada?
prom_goles_f, prom_goles_c, categoria_equipo = analizar_rendimiento_equipo(45, 20, 25)

print(f"Goles por partido: {prom_goles_f:.2f}")
print(f"Goles recibidos por partido: {prom_goles_c:.2f}")
print(f"Categoría del equipo: {categoria_equipo}")

print("\nANÁLISIS DE LEWANDOWSKI")
print("-" * 22)

# ¿Qué tan efectivo es como delantero?
efectividad, goles_90min, calificacion = calcular_efectividad_jugador(15, 45, 1800)

print(f"Efectividad de tiro: {efectividad:.1f}%")
print(f"Goles cada 90 minutos: {goles_90min:.2f}")
print(f"Calificación: {calificacion}")

print("\nCONCEPTOS CLAVE DE FUNCIONES:")
print("="*30)
print("def nombre_funcion(parámetros): - Define la 'jugada'")
print("    # código de la función - Pasos de la jugada")
print("    return resultado - Devuelve el resultado")
print("")
print("# Para usar la función:")
print("resultado = nombre_funcion(valores)")

print("\nPreguntas de reflexión:")
print("1. ¿Por qué es útil que las funciones 'devuelvan' valores?")
print("2. ¿Cómo se parece esto a delegarle tareas a tu asistente técnico?")
print("3. ¿Qué otras funciones de análisis crearías?")
print("4. ¿Por qué es mejor tener funciones especializadas vs una función gigante?")
```

---

# SÍNTESIS FINAL: ¿Qué hemos descubierto sobre la automatización inteligente?

## Reflexión de las 3 sesiones (150 minutos totales)

### SESIÓN 1: ¿Cómo repetimos tareas como un entrenamiento sistemático?

**Lo que dominamos ahora**:

- Procesar automáticamente listas completas de jugadores con bucles for
- Implementar lógica de "repetir hasta lograr objetivo" con bucles while
- Distinguir cuándo usar cada tipo de repetición según la situación
- Aplicar la mentalidad de "automatización de entrenamientos" al código

### SESIÓN 2: ¿Cómo tomamos decisiones complejas bajo presión?

**Lo que revelamos**:

- Combinar múltiples condiciones usando operadores lógicos (and, or, not)
- Crear jerarquías de decisión con condicionales anidados
- Imitar el proceso mental de un entrenador profesional en situaciones críticas
- Estructurar evaluaciones complejas de manera lógica y sistemática

### SESIÓN 3: ¿Cómo organizamos estrategias complejas de manera elegante?

**Lo que construimos**:

- Crear "jugadas tácticas" reutilizables mediante funciones
- Diseñar sistemas de análisis que devuelven resultados útiles
- Organizar código complejo en componentes especializados y mantenibles
- Aplicar principios de elegancia y eficiencia como los grandes estrategas

---

## Pregunta de transformación estratégica

**¿Te has dado cuenta de que ya programas con la mentalidad de un director técnico profesional?**

### ¿Qué cambió en tu forma de abordar problemas complejos?

**Reflexión personal**:

- ¿Cuál fue tu momento de mayor comprensión sobre la automatización?
- ¿Qué aspecto de las estructuras de control te resultó más natural?
- ¿Cómo aplicarías estos patrones de pensamiento fuera de la programación?
- ¿En qué otras áreas de tu vida podrías usar esta lógica sistemática?

### Vista previa de la próxima semana

**¿Sabías que los sistemas de análisis deportivo procesan millones de datos usando exactamente los mismos principios que acabas de aprender?**

La próxima semana exploraremos:

- Funciones avanzadas para análisis estadístico automático
- Módulos para organizar sistemas complejos de análisis deportivo
- Manejo de errores como un entrenador que anticipa problemas
- Creación de bibliotecas de funciones reutilizables para ciencia de datos

**Pregunta motivadora**: ¿Crees que podrías crear un sistema completo que analice automáticamente el rendimiento de todos los jugadores de La Liga?

**Tu evolución**: Esta semana aprendiste a estructurar el pensamiento lógico como un estratega. La próxima semana aprenderás a escalar esos sistemas para manejar la complejidad del análisis deportivo profesional.

¿Estás listo para pensar a la escala de los grandes clubes europeos?

## 3. Control de Flujo: ¿Cómo automatizamos decisiones y repeticiones?

### Pregunta fundamental: ¿Cómo procesarías información de múltiples jugadores eficientemente?

**Situación de reflexión**: Imagina que tienes una lista de 100 jugadores y necesitas calcular estadísticas para cada uno. ¿Los procesarías uno por uno manualmente?

**Analogía práctica**: ¿Cómo haría un entrenador para revisar el rendimiento de todos sus jugadores? ¿Los evaluaría al azar o seguiría un proceso sistemático?

### 3.1 Bucles FOR - ¿Cómo procesamos cada elemento de una colección?

**Pregunta guía**: Si quisieras hacer algo con cada jugador de tu lista, ¿cómo le dirías a Python que repita la misma operación para todos?

```python
# ¿Cómo crearías una tabla de goleadores automáticamente?
# Observa diferentes formas de iterar sobre nuestros datos

jugadores_goles = ["Messi", "Ronaldo", "Neymar", "Mbappé"]
goles = [15, 12, 8, 20]

# Método 1: ¿Qué hace range() y len()?
print("=== TABLA DE GOLEADORES ===")
for i in range(len(jugadores_goles)):  # ¿Por qué usamos range(len())?
    print(f"{i+1}. {jugadores_goles[i]}: {goles[i]} goles")

# Método 2: ¿Qué ventaja tiene enumerate()?
print("\n=== USANDO ENUMERATE ===")
for posicion, jugador in enumerate(jugadores_goles, 1):  # ¿Qué hace el 1 aquí?
    print(f"{posicion}. {jugador}: {goles[posicion-1]} goles")

# Método 3: ¿Cómo zip() combina dos listas?
print("\n=== USANDO ZIP ===")
for jugador, gol in zip(jugadores_goles, goles):  # ¿Qué está "uniendo" zip?
    print(f"{jugador}: {gol} goles")

# ¿Podrías calcular estadísticas mientras iteras?
total_goles = 0
mejor_goleador = ""
max_goles = 0

# ¿Qué lógica usarías para encontrar el mejor goleador?
for jugador, gol in zip(jugadores_goles, goles):
    total_goles += gol  # ¿Qué hace += ?
    if gol > max_goles:  # ¿Cómo identifica al mejor?
        max_goles = gol
        mejor_goleador = jugador

print(f"\nTotal de goles: {total_goles}")
print(f"Mejor goleador: {mejor_goleador} con {max_goles} goles")
print(f"Promedio: {total_goles/len(goles):.2f} goles por jugador")

# Pregunta de análisis: ¿Cuál método de iteración te parece más claro y por qué?
```

```python
# Bucle FOR con diccionarios
liga_equipos = {
    "Real Madrid": {"puntos": 65, "goles_favor": 45, "goles_contra": 20},
    "Barcelona": {"puntos": 58, "goles_favor": 42, "goles_contra": 25},
    "Atletico Madrid": {"puntos": 55, "goles_favor": 35, "goles_contra": 18},
    "Valencia": {"puntos": 48, "goles_favor": 30, "goles_contra": 28}
}

print("=== TABLA DE POSICIONES ===")
print(f"{'Equipo':<15} {'Puntos':<8} {'GF':<4} {'GC':<4} {'Dif':<5}")
print("-" * 45)

for equipo, stats in liga_equipos.items():
    diferencia = stats["goles_favor"] - stats["goles_contra"]
    print(f"{equipo:<15} {stats['puntos']:<8} {stats['goles_favor']:<4} {stats['goles_contra']:<4} {diferencia:<5}")

# Análisis de la liga
print("\n=== ANÁLISIS DE LA LIGA ===")
total_puntos = sum(stats["puntos"] for stats in liga_equipos.values())
total_goles = sum(stats["goles_favor"] for stats in liga_equipos.values())
promedio_puntos = total_puntos / len(liga_equipos)

print(f"Promedio de puntos: {promedio_puntos:.1f}")
print(f"Total de goles en la liga: {total_goles}")
print(f"Promedio de goles por equipo: {total_goles/len(liga_equipos):.1f}")

# Encontrar líder
lider = max(liga_equipos.items(), key=lambda x: x[1]["puntos"])
print(f"Líder de la liga: {lider[0]} con {lider[1]['puntos']} puntos")
```

### 3.2 Bucles WHILE - ¿Cómo repetimos algo hasta que se cumpla una condición?

**Pregunta de diferenciación**: ¿Cuál es la diferencia entre "hacer algo con cada jugador de la lista" y "seguir jugando hasta que termine el partido"?

**Situación práctica**: Un partido dura 90 minutos, pero no sabes exactamente cuándo ocurrirán los eventos. ¿Cómo simularías esto?

```python
# Simulación de un partido con bucle WHILE
print("=== SIMULACIÓN DE PARTIDO ===")
minuto = 0
goles_local = 0
goles_visitante = 0
eventos = []

# Simulación simple (algunos minutos con eventos)
eventos_programados = [
    (15, "gol", "local"),
    (23, "gol", "visitante"),
    (67, "gol", "local"),
    (89, "gol", "visitante")
]

evento_actual = 0
while minuto <= 90:
    # Verificar si hay evento en este minuto
    if evento_actual < len(eventos_programados):
        min_evento, tipo, equipo = eventos_programados[evento_actual]
        if minuto == min_evento:
            if tipo == "gol":
                if equipo == "local":
                    goles_local += 1
                    eventos.append(f"Minuto {minuto}: ¡GOL del equipo local! {goles_local}-{goles_visitante}")
                else:
                    goles_visitante += 1
                    eventos.append(f"Minuto {minuto}: ¡GOL del equipo visitante! {goles_local}-{goles_visitante}")
            evento_actual += 1
    
    minuto += 1

print("\nEventos del partido:")
for evento in eventos:
    print(evento)

print(f"\nResultado final: {goles_local} - {goles_visitante}")
if goles_local > goles_visitante:
    print("¡Victoria del equipo local!")
elif goles_visitante > goles_local:
    print("¡Victoria del equipo visitante!")
else:
    print("¡Empate!")
```

### 3.3 Condicionales Avanzados - ¿Cómo tomamos decisiones complejas?

**Pregunta de reflexión**: ¿Cómo clasificarías automáticamente equipos según su rendimiento? ¿Qué criterios usarías?

**Desafío de lógica**: ¿Cómo combinarías múltiples condiciones? Por ejemplo: ¿un equipo con muchos puntos pero mala diferencia de goles es realmente excelente?

```python
# Sistema de clasificación de equipos
def clasificar_equipo(puntos, partidos_jugados, goles_favor, goles_contra):
    """Clasifica un equipo según sus estadísticas"""
    promedio_puntos = puntos / partidos_jugados if partidos_jugados > 0 else 0
    diferencia_goles = goles_favor - goles_contra
    
    # Clasificación compleja
    if promedio_puntos >= 2.5 and diferencia_goles > 15:
        categoria = "Excelente"
        descripcion = "Candidato al título"
    elif promedio_puntos >= 2.0 and diferencia_goles > 5:
        categoria = "Muy Bueno"
        descripcion = "Clasificación a competencias europeas"
    elif promedio_puntos >= 1.5 and diferencia_goles >= 0:
        categoria = "Bueno"
        descripcion = "Posición media-alta"
    elif promedio_puntos >= 1.0:
        categoria = "Regular"
        descripcion = "Posición media-baja"
    else:
        categoria = "Malo"
        descripcion = "Zona de descenso"
    
    return categoria, descripcion, promedio_puntos

# Evaluar varios equipos
equipos_evaluacion = [
    ("Manchester City", 72, 28, 68, 22),
    ("Arsenal", 65, 28, 58, 35),
    ("Chelsea", 45, 28, 42, 38),
    ("Everton", 28, 28, 25, 55)
]

print("=== EVALUACIÓN DE EQUIPOS ===")
print(f"{'Equipo':<15} {'Puntos':<8} {'Prom':<6} {'Categoría':<12} {'Descripción'}")
print("-" * 70)

for nombre, puntos, partidos, gf, gc in equipos_evaluacion:
    categoria, descripcion, promedio = clasificar_equipo(puntos, partidos, gf, gc)
    print(f"{nombre:<15} {puntos:<8} {promedio:<6.2f} {categoria:<12} {descripcion}")

# Análisis condicional con múltiples criterios
print("\n=== ANÁLISIS DETALLADO ===")
for nombre, puntos, partidos, gf, gc in equipos_evaluacion:
    diferencia = gf - gc
    eficiencia = (puntos / (partidos * 3)) * 100
    
    print(f"\n{nombre}:")
    print(f"  Eficiencia: {eficiencia:.1f}%")
    print(f"  Diferencia de goles: {diferencia:+d}")
    
    # Análisis específico
    if eficiencia > 80:
        print(f"  Excelente rendimiento")
    elif eficiencia > 60:
        print(f"  Buen rendimiento")
    elif eficiencia > 40:
        print(f"  Rendimiento regular")
    else:
        print(f"  Rendimiento deficiente")
    
    if diferencia > 10:
        print(f"  Ataque muy efectivo")
    elif diferencia > 0:
        print(f"  Ataque balanceado")
    elif diferencia > -10:
        print(f"  Defensa necesita mejoras")
    else:
        print(f"  Serios problemas defensivos")
```

## 4. Tuplas y Conjuntos: ¿Cuándo necesitamos estructuras especializadas?

### Pregunta de aplicación: ¿Cuándo NO quieres que algo cambie?

**Reflexión práctica**: Una vez que un partido termina, ¿debería ser posible cambiar accidentalmente el resultado? ¿Qué tipo de datos deportivos son "permanentes"?

### 4.1 Tuplas - ¿Cómo protegemos datos importantes?

**Situación**: Imagina que almacenas resultados históricos. ¿Qué pasaría si alguien pudiera modificarlos por error?

```python
# ¿Qué información deportiva nunca debería cambiar una vez registrada?
# Las tuplas protegen datos importantes de modificaciones accidentales

resultado_final = ("Barcelona", 3, "Real Madrid", 1)  # ¿Debería poder cambiarse este resultado?
fecha_partido = (2024, 10, 26, 20, 30)  # ¿Y la fecha/hora del partido?
posicion_campo = (25.5, 40.2)  # ¿Las coordenadas de un gol específico?
temporada = (2023, 2024)  # ¿El período de una temporada?

print("Resultado del partido:")
print(f"{resultado_final[0]} {resultado_final[1]} - {resultado_final[3]} {resultado_final[2]}")

print(f"\nFecha: {fecha_partido[2]}/{fecha_partido[1]}/{fecha_partido[0]}")
print(f"Hora: {fecha_partido[3]}:{fecha_partido[4]:02d}")

print(f"\nPosición en el campo: ({posicion_campo[0]}, {posicion_campo[1]})")
print(f"Temporada: {temporada[0]}-{temporada[1]}")

# ¿Sabías que puedes "desempaquetar" tuplas? ¿Qué ventajas tiene esto?
equipo_local, goles_local, equipo_visitante, goles_visitante = resultado_final
print(f"\nDesempaquetado:")
print(f"Local: {equipo_local} ({goles_local} goles)")
print(f"Visitante: {equipo_visitante} ({goles_visitante} goles)")

# ¿Cómo manejarías múltiples resultados? ¿Una lista de tuplas?
resultados_jornada = [
    ("Barcelona", 3, "Real Madrid", 1),
    ("Atletico Madrid", 2, "Valencia", 0),
    ("Sevilla", 1, "Villarreal", 1),
    ("Real Sociedad", 0, "Athletic Bilbao", 2)
]

print("\n=== RESULTADOS DE LA JORNADA ===")
for local, g_local, visitante, g_visitante in resultados_jornada:
    print(f"{local} {g_local} - {g_visitante} {visitante}")

# Pregunta de seguridad: ¿Qué pasaría si intentaras hacer resultado_final[0] = "Arsenal"?
```

### 4.2 Conjuntos - ¿Cómo manejamos elementos únicos?

**Pregunta conceptual**: En una liga de fútbol, ¿puede haber dos equipos con el mismo nombre? ¿Y dos jugadores que hayan marcado el mismo gol?

**Desafío de análisis**: Si quisieras saber qué jugadores han marcado para ambos equipos rivales, ¿cómo lo calcularías?

```python
# ¿Qué pasa si accidentalmente incluyes un jugador dos veces?
# Los conjuntos automáticamente eliminan duplicados

goleadores_barcelona = {"Messi", "Suarez", "Neymar", "Griezmann", "Messi"}  # ¿Notas el Messi duplicado?
goleadores_real_madrid = {"Ronaldo", "Benzema", "Bale", "Modric"}
goleadores_champions = {"Messi", "Ronaldo", "Lewandowski", "Benzema"}

print("Goleadores Barcelona:", goleadores_barcelona)  # ¿Cuántos Messi ves?
print("Goleadores Real Madrid:", goleadores_real_madrid)
print("Goleadores Champions:", goleadores_champions)

# ¿Qué operaciones podrías hacer para comparar estos grupos?
print("\n=== OPERACIONES CON CONJUNTOS ===")

# ¿Cómo obtendrías TODOS los goleadores únicos?
todos_goleadores = goleadores_barcelona | goleadores_real_madrid  # ¿Qué hace el símbolo |?
print(f"Todos los goleadores: {todos_goleadores}")

# ¿Cómo encontrarías jugadores que han marcado para AMBOS equipos?
goleadores_ambos = goleadores_barcelona & goleadores_real_madrid  # ¿Y el símbolo &?
print(f"Goleadores en ambos equipos: {goleadores_ambos}")

# ¿Cómo identificarías goleadores SOLO del Barcelona?
solo_barcelona = goleadores_barcelona - goleadores_real_madrid  # ¿Y el -?
print(f"Solo goleadores del Barcelona: {solo_barcelona}")

# ¿Cómo encontrarías goleadores que NO están en ambos equipos?
no_comunes = goleadores_barcelona ^ goleadores_real_madrid  # ¿Y el ^?
print(f"Goleadores no comunes: {no_comunes}")

# ¿Cómo verificarías si un jugador específico ha marcado?
print("\n=== VERIFICACIONES ===")
print(f"¿Messi ha marcado para el Barcelona? {'Messi' in goleadores_barcelona}")
print(f"¿Ronaldo ha marcado para el Barcelona? {'Ronaldo' in goleadores_barcelona}")
print(f"¿Hay goleadores comunes? {len(goleadores_barcelona & goleadores_real_madrid) > 0}")

# Análisis avanzado: ¿Qué jugadores de cada equipo también han brillado en Champions?
barcelonistas_champions = goleadores_barcelona & goleadores_champions
madridistas_champions = goleadores_real_madrid & goleadores_champions

print(f"\nBarcelonistas en Champions: {barcelonistas_champions}")
print(f"Madridistas en Champions: {madridistas_champions}")
print(f"Total jugadores únicos en Champions: {len(goleadores_champions)}")

# Pregunta de aplicación: ¿En qué otros análisis deportivos serían útiles estas operaciones de conjuntos?
```

## 5. Reflexión y Síntesis: ¿Qué hemos descubierto sobre la organización de datos?

### ¿Cómo ha evolucionado tu comprensión?

**Pregunta de autoevaluación**: ¿Recuerdas cuando solo podías manejar una variable a la vez? ¿Cómo te sientes ahora que puedes organizar información compleja?

### ¿Qué herramientas hemos añadido a nuestro kit de análisis?

**Estructuras de datos que ahora dominas**:

- **Listas**: ¿Cuándo las usarías? ¿Qué las hace especiales?
- **Diccionarios**: ¿En qué situaciones son superiores a las listas?
- **Tuplas**: ¿Por qué es importante tener datos inmutables?
- **Conjuntos**: ¿Qué problemas resuelven que otras estructuras no pueden?

**Control de flujo que ahora entiendes**:

- **Bucles FOR**: ¿Cómo han cambiado tu capacidad de procesar datos?
- **Bucles WHILE**: ¿En qué escenarios son más apropiados que FOR?
- **Condicionales complejos**: ¿Cómo automatizas decisiones sofisticadas?

### ¿Qué conexiones ves entre estas herramientas?

**Pregunta de síntesis**: ¿Podrías combinar diferentes estructuras? Por ejemplo, ¿una lista de diccionarios o un diccionario de conjuntos?

**Aplicaciones que podrías crear**:

- ¿Cómo gestionarías una liga completa con equipos, jugadores y resultados?
- ¿Qué análisis estadísticos podrías automatizar?
- ¿Cómo crearías reportes dinámicos?

### Mirando hacia el futuro: ¿Qué limitaciones aún tenemos?

**Pregunta motivadora**: Con lo que sabes ahora, ¿qué te gustaría poder hacer pero aún no puedes?

En la Semana 3 descubriremos:

- **Funciones**: ¿Cómo crear tus propias herramientas reutilizables?
- **Módulos**: ¿Cómo organizar código complejo?
- **Bibliotecas especializadas**: ¿Qué herramientas han creado otros para análisis deportivo?
- **Arquitectura de programas**: ¿Cómo estructurar proyectos grandes?

### Reflexión final

**Pregunta de perspectiva**: ¿Cómo ha cambiado tu visión sobre lo que es posible analizar en el deporte?

**Desafío de aplicación**: ¿Qué análisis real te gustaría crear con tu equipo favorito usando estas herramientas?

---

**¡Excelente progreso en tu journey de análisis deportivo!**

*Recuerda: Ahora puedes pensar en términos de colecciones y patrones, no solo elementos individuales. ¿Qué descubrirás cuando puedas crear tus propias herramientas?*

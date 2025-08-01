# Ejercicio Semana 1: Configuración y Fundamentos

## Información General

**Bloque:** 1 - Prerrequisitos de Programación  
**Semana:** 1  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 1

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:
- Verificar la configuración correcta del entorno Python
- Crear y manipular variables con tipos de datos básicos
- Aplicar operadores aritméticos y de comparación
- Presentar resultados de manera clara y profesional

## Conocimientos Previos Requeridos

- Conceptos básicos de programación (variables, tipos de datos)
- Operadores aritméticos y de comparación
- Uso básico de Python

## Ejercicio: Análisis de un Partido de Fútbol

### Contexto
Eres un analista deportivo junior y tu primera tarea es crear un programa que analice los datos básicos de un partido de fútbol. Utilizarás Python para procesar la información y generar un reporte básico.

### Parte 1: Configuración del Entorno (25 puntos)

**Instrucciones:**
1. Crea un nuevo notebook de Jupyter o archivo Python
2. Ejecuta el siguiente código para verificar tu entorno:

```python
# Verificación del entorno de trabajo
import sys
print("=== VERIFICACIÓN DEL ENTORNO ===")
print(f"Versión de Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

# Verificar librerías principales
librerias_requeridas = ['pandas', 'numpy', 'matplotlib']
librerias_instaladas = []

for libreria in librerias_requeridas:
    try:
        __import__(libreria)
        librerias_instaladas.append(libreria)
        print(f" {libreria}: Instalada")
    except ImportError:
        print(f" {libreria}: NO instalada")

print(f"\nLibrerías instaladas: {len(librerias_instaladas)}/{len(librerias_requeridas)}")
if len(librerias_instaladas) == len(librerias_requeridas):
    print(" ¡Entorno listo para trabajar!")
else:
    print("⚠️ Algunas librerías faltan por instalar")
```

**Entrega requerida:**
- Captura de pantalla de la salida del código
- Confirmación de que todas las librerías están instaladas

### Parte 2: Datos del Partido (25 puntos)

**Instrucciones:**
Crea variables para almacenar la información de un partido entre Barcelona y Real Madrid:

```python
# Información básica del partido
equipo_local = "FC Barcelona"
equipo_visitante = "Real Madrid"
estadio = "Camp Nou"
fecha_partido = "2024-10-26"

# Resultados del partido
goles_local = 2
goles_visitante = 1
minutos_jugados = 90
tiempo_extra = 3  # minutos de tiempo añadido

# Información adicional
asistencia = 85_000
capacidad_estadio = 99_354
temperatura = 18  # grados Celsius

# Tu código aquí - Agrega 3 variables más relevantes para el análisis
# Ejemplos: árbitro, tarjetas_amarillas, tarjetas_rojas, etc.

# Tu código aquí - Muestra toda la información usando print()
print("=== INFORMACIÓN DEL PARTIDO ===")
# Completa con f-strings para mostrar todos los datos
```

**Requisitos específicos:**
1. Copia el código anterior
2. Agrega 3 variables más que consideres relevantes para el análisis del partido
3. Muestra toda la información usando `print()` con formato claro
4. Usa f-strings para una presentación profesional

### Parte 3: Cálculos Estadísticos (25 puntos)

**Instrucciones:**
Realiza los siguientes cálculos usando las variables de la Parte 2:

```python
# Tu código aquí - calcula:

# 1. Total de goles en el partido
total_goles = goles_local + goles_visitante

# 2. Diferencia de goles
diferencia_goles = # Tu código aquí

# 3. Promedio de goles por minuto (considera tiempo extra)
tiempo_total = # Tu código aquí
promedio_goles_minuto = # Tu código aquí

# 4. Porcentaje de ocupación del estadio
porcentaje_ocupacion = # Tu código aquí

# 5. Goles por cada 10,000 espectadores
goles_por_espectadores = # Tu código aquí

# Mostrar todos los resultados con formato claro
print("=== ESTADÍSTICAS DEL PARTIDO ===")
print(f"Total de goles: {total_goles}")
# Completa con el resto de estadísticas usando f-strings
```

**Requisitos específicos:**
- Usa operadores aritméticos para todos los cálculos
- Redondea los decimales a 2 posiciones usando `round()`
- Presenta los resultados con descripciones claras
- Incluye las unidades correspondientes (%, minutos, etc.)

### Parte 4: Análisis del Resultado (25 puntos)

**Instrucciones:**
Crea un programa que analice el resultado del partido y proporcione insights:

```python
# Tu código aquí - implementa:

# 1. Determinar el ganador del partido
if goles_local > goles_visitante:
    ganador = # Tu código
elif goles_visitante > goles_local:
    ganador = # Tu código
else:
    ganador = # Tu código

# 2. Clasificar el tipo de victoria
if diferencia_goles >= 3:
    tipo_partido = "Goleada"
elif diferencia_goles == 2:
    tipo_partido = "Victoria clara"
elif diferencia_goles == 1:
    tipo_partido = "Victoria ajustada"
else:
    tipo_partido = "Empate"

# 3. Evaluar la asistencia al estadio
if porcentaje_ocupacion >= 90:
    evaluacion_asistencia = "Lleno total"
elif porcentaje_ocupacion >= 75:
    evaluacion_asistencia = "Excelente asistencia"
elif porcentaje_ocupacion >= 50:
    evaluacion_asistencia = "Buena asistencia"
else:
    evaluacion_asistencia = "Asistencia regular"

# 4. Generar reporte final
print("=== ANÁLISIS FINAL DEL PARTIDO ===")
# Tu código para mostrar el análisis completo
```

**Entrega requerida:**
Un reporte final que incluya:
- Ganador del partido
- Tipo de partido según la diferencia de goles
- Evaluación de la asistencia
- Una conclusión de 2-3 líneas sobre el partido

## Instrucciones de Entrega

1. **Formato:** Archivo `.py` o notebook `.ipynb`
2. **Nombre del archivo:** `[matricula]-ejercicio-semana-1.ipynb`
3. **Contenido mínimo:**
   - Código completo de las 4 partes
   - Comentarios explicando cada sección
   - Salida de todos los `print()` statements
4. **Documentación adicional:**
   - Captura de pantalla de la verificación del entorno
   - Breve reflexión (2-3 líneas) sobre lo aprendido

## Criterios de Evaluación (100 puntos)

### Correctitud Técnica (40 puntos)

- **Excelente (36-40):** Código ejecuta sin errores, sintaxis correcta, cálculos precisos
- **Competente (28-35):** Errores menores, sintaxis mayormente correcta
- **En desarrollo (20-27):** Errores significativos, implementación parcial
- **Insuficiente (0-19):** Código no ejecuta o errores graves

### Aplicación Práctica (30 puntos)

- **Excelente (27-30):** Resolución completa, uso creativo del contexto deportivo
- **Competente (21-26):** Resolución adecuada de todos los problemas
- **En desarrollo (15-20):** Resolución básica, uso limitado del contexto
- **Insuficiente (0-14):** Problemas no resueltos correctamente

### Claridad y Documentación (30 puntos)

- **Excelente (27-30):** Código bien comentado, presentación profesional, explicaciones claras
- **Competente (21-26):** Comentarios adecuados, presentación clara
- **En desarrollo (15-20):** Comentarios básicos, presentación simple
- **Insuficiente (0-14):** Sin comentarios, presentación deficiente

## Consejos para el Éxito

1. **Planifica antes de programar:** Lee todo el ejercicio antes de empezar
2. **Prueba tu código:** Ejecuta cada parte por separado para verificar errores
3. **Usa nombres descriptivos:** Las variables deben explicar qué contienen
4. **Comenta tu código:** Explica qué hace cada sección importante
5. **Revisa los cálculos:** Verifica que las operaciones matemáticas sean correctas

##  Recursos Adicionales

- [Documentación oficial de Python](https://docs.python.org/3/)
- [Tutorial de variables en Python](https://www.w3schools.com/python/python_variables.asp)
- [Operadores en Python](https://www.w3schools.com/python/python_operators.asp)

---

*¿Preguntas? Contacta a tu instructor durante las horas de oficina o en el foro del curso.*

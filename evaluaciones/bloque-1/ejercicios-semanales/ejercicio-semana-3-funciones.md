# Información General

**Tema:** Funciones y Módulos en Python  
**Semana:** 3  
**Bloque:** 1 - Prerrequisitos de Programación  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 3  
**Archivo entrega:** `[matricula]-ejercicio-semana-3.ipynb`

## Objetivos de Aprendizaje

Al finalizar este ejercicio, el estudiante será capaz de:

1. **Crear funciones modulares** para análisis deportivo reutilizable
2. **Implementar parámetros y valores de retorno** de manera eficiente
3. **Documentar funciones** con docstrings claros y precisos
4. **Organizar código** en módulos para proyectos escalables
5. **Validar datos** usando funciones de control de calidad

## Prerrequisitos

- Ejercicios de las Semanas 1 y 2 completados exitosamente
- Dominio de estructuras de control (if, for, while)
- Conocimiento de listas y diccionarios en Python
- Comprensión de operaciones matemáticas básicas

## Contexto del Ejercicio

Eres el **desarrollador principal** del sistema de análisis del FC Barcelona. El director técnico necesita herramientas reutilizables para:

- Calcular estadísticas avanzadas de manera consistente
- Generar reportes automáticos para diferentes equipos
- Analizar patrones de rendimiento usando funciones especializadas
- Crear un módulo completo de análisis deportivo

---

# Ejercicio Integrador: Sistema Modular de Análisis FC Barcelona

## Parte 1: Biblioteca de Funciones Estadísticas (25 puntos)

### Objetivo
Desarrollar una biblioteca completa de funciones para cálculos estadísticos deportivos.

### Instrucciones Detalladas

**Paso 1:** Crea funciones especializadas para análisis estadístico:

```python
# Datos de prueba del FC Barcelona temporada 2023-24
goles_por_partido = [3, 1, 2, 4, 0, 2, 1, 3, 2, 1, 4, 2, 1, 3, 0]
asistencias_messi = [2, 1, 3, 2, 0, 1, 2, 1, 1, 2, 3, 1, 0, 2, 1]
minutos_jugados = [90, 85, 90, 78, 90, 88, 90, 82, 90, 75, 90, 90, 65, 90, 80]

# TU CÓDIGO AQUÍ:
# Implementa estas 5 funciones con docstrings completos:

def calcular_promedio_deportivo(lista_valores, nombre_estadistica):
    """
    Calcula el promedio de cualquier estadística deportiva
    
    Parámetros:
    lista_valores (list): Lista con valores numéricos
    nombre_estadistica (str): Nombre de la estadística para el reporte
    
    Retorna:
    dict: {"promedio": float, "estadistica": str, "total_partidos": int}
    """
    # Tu implementación aquí

def encontrar_mejor_actuacion(lista_valores, lista_rivales):
    """
    Encuentra la mejor actuación y contra qué rival fue
    
    Parámetros:
    lista_valores (list): Valores de rendimiento
    lista_rivales (list): Nombres de equipos rivales
    
    Retorna:
    dict: {"valor_maximo": int, "rival": str, "partido_numero": int}
    """
    # Tu implementación aquí

def calcular_consistencia(lista_valores):
    """
    Calcula la consistencia del rendimiento (desviación estándar simple)
    
    Parámetros:
    lista_valores (list): Lista de valores numéricos
    
    Retorna:
    dict: {"consistencia": str, "variabilidad": float}
    # Categorías: "Muy Consistente" < 1.0, "Consistente" < 1.5, "Variable" >= 1.5
    """
    # Tu implementación aquí

def generar_reporte_rendimiento(goles, asistencias, minutos, nombre_jugador):
    """
    Genera un reporte completo de rendimiento de un jugador
    
    Parámetros:
    goles (list): Goles por partido
    asistencias (list): Asistencias por partido  
    minutos (list): Minutos jugados por partido
    nombre_jugador (str): Nombre del jugador
    
    Retorna:
    dict: Reporte completo con todas las estadísticas
    """
    # Tu implementación aquí

def validar_datos_partido(goles_local, goles_visitante, minutos_partido):
    """
    Valida que los datos de un partido sean coherentes
    
    Parámetros:
    goles_local (int): Goles del equipo local
    goles_visitante (int): Goles del equipo visitante
    minutos_partido (int): Duración del partido
    
    Retorna:
    dict: {"valido": bool, "errores": list, "advertencias": list}
    """
    # Tu implementación aquí

# PRUEBA TUS FUNCIONES:
rivales = ["Real Madrid", "Sevilla", "Valencia", "Atletico", "Betis", 
          "Sociedad", "Villarreal", "Celta", "Getafe", "Osasuna",
          "Granada", "Cadiz", "Mallorca", "Girona", "Almeria"]

# Ejecuta todas las funciones y muestra los resultados
```

### Criterios de Evaluación
- **Funciones implementadas correctamente** (15 puntos)
- **Docstrings completos y claros** (5 puntos)
- **Validación y manejo de errores** (5 puntos)

---

## Parte 2: Sistema de Análisis de Plantilla (25 puntos)

### Objetivo
Crear funciones para analizar el rendimiento de toda la plantilla del FC Barcelona.

### Instrucciones Detalladas

**Paso 2:** Desarrolla un sistema completo de análisis de plantilla:

```python
# Base de datos de la plantilla del FC Barcelona
plantilla_barcelona = [
    {"nombre": "Ter Stegen", "posicion": "Portero", "edad": 31, "partidos": 25, "goles": 0, "asistencias": 0},
    {"nombre": "Pedri", "posicion": "Centrocampista", "edad": 21, "partidos": 28, "goles": 4, "asistencias": 6},
    {"nombre": "Gavi", "posicion": "Centrocampista", "edad": 19, "partidos": 32, "goles": 2, "asistencias": 8},
    {"nombre": "Lewandowski", "posicion": "Delantero", "edad": 35, "partidos": 30, "goles": 22, "asistencias": 3},
    {"nombre": "Raphinha", "posicion": "Extremo", "edad": 27, "partidos": 29, "goles": 8, "asistencias": 12},
    {"nombre": "Frenkie de Jong", "posicion": "Centrocampista", "edad": 27, "partidos": 24, "goles": 3, "asistencias": 4},
    {"nombre": "Ronald Araujo", "posicion": "Defensa", "edad": 25, "partidos": 26, "goles": 2, "asistencias": 1}
]

# TU CÓDIGO AQUÍ:
# Implementa estas funciones especializadas:

def filtrar_por_posicion(plantilla, posicion_buscada):
    """
    Filtra jugadores por posición específica
    
    Parámetros:
    plantilla (list): Lista de diccionarios con datos de jugadores
    posicion_buscada (str): Posición a filtrar
    
    Retorna:
    list: Lista de jugadores de esa posición
    """
    # Tu implementación aquí

def calcular_promedio_edad_posicion(plantilla, posicion):
    """
    Calcula la edad promedio de jugadores por posición
    
    Parámetros:
    plantilla (list): Lista de jugadores
    posicion (str): Posición a analizar
    
    Retorna:
    float: Edad promedio de la posición
    """
    # Tu implementación aquí

def encontrar_goleador_equipo(plantilla):
    """
    Encuentra al máximo goleador del equipo
    
    Parámetros:
    plantilla (list): Lista de jugadores
    
    Retorna:
    dict: Información completa del máximo goleador
    """
    # Tu implementación aquí

def analizar_efectividad_por_minuto(plantilla):
    """
    Calcula goles + asistencias por partido para cada jugador
    
    Parámetros:
    plantilla (list): Lista de jugadores
    
    Retorna:
    list: Lista ordenada por efectividad (mayor a menor)
    """
    # Tu implementación aquí

def generar_reporte_plantilla_completo(plantilla):
    """
    Genera un análisis completo de toda la plantilla
    
    Parámetros:
    plantilla (list): Lista de jugadores
    
    Retorna:
    dict: Reporte completo con estadísticas generales
    """
    # Tu implementación aquí

# EJECUTA EL ANÁLISIS COMPLETO:
# 1. Filtra por cada posición y muestra estadísticas
# 2. Encuentra los 3 jugadores más efectivos
# 3. Calcula la edad promedio del equipo
# 4. Genera el reporte completo de la plantilla
```

### Criterios de Evaluación
- **Análisis por posición correcto** (10 puntos)
- **Cálculos de efectividad precisos** (10 puntos)
- **Reporte integral coherente** (5 puntos)

---

## Parte 3: Simulador de Partidos con Funciones (25 puntos)

### Objetivo
Desarrollar un simulador de partidos usando funciones modulares y reutilizables.

### Instrucciones Detalladas

**Paso 3:** Crea un simulador completo de enfrentamientos:

```python
import random

# TU CÓDIGO AQUÍ:
# Implementa este simulador modular:

def calcular_fuerza_ataque(plantilla):
    """
    Calcula la fuerza ofensiva total del equipo
    
    Parámetros:
    plantilla (list): Lista de jugadores
    
    Retorna:
    float: Índice de fuerza ofensiva (0-100)
    """
    # Fórmula: (total_goles + total_asistencias) / total_partidos * 10
    # Tu implementación aquí

def calcular_fuerza_defensa(plantilla):
    """
    Calcula la solidez defensiva del equipo
    
    Parámetros:
    plantilla (list): Lista de jugadores
    
    Retorna:
    float: Índice defensivo (0-100)
    """
    # Fórmula basada en minutos jugados de defensas y portero
    # Tu implementación aquí

def simular_partido_individual(equipo_local, equipo_visitante, nombre_local, nombre_visitante):
    """
    Simula un partido entre dos equipos
    
    Parámetros:
    equipo_local (list): Plantilla del equipo local
    equipo_visitante (list): Plantilla del equipo visitante
    nombre_local (str): Nombre del equipo local
    nombre_visitante (str): Nombre del equipo visitante
    
    Retorna:
    dict: Resultado completo del partido simulado
    """
    # Tu implementación aquí
    # Incluye: goles, goleadores, tiempo de goles, estadísticas

def simular_temporada_completa(equipos_liga):
    """
    Simula una temporada completa entre múltiples equipos
    
    Parámetros:
    equipos_liga (dict): Diccionario con equipos y sus plantillas
    
    Retorna:
    dict: Tabla de clasificación y estadísticas de temporada
    """
    # Tu implementación aquí

def generar_reporte_simulacion(resultados_temporada):
    """
    Genera un reporte detallado de la temporada simulada
    
    Parámetros:
    resultados_temporada (dict): Resultados de la simulación
    
    Retorna:
    str: Reporte formateado para presentación
    """
    # Tu implementación aquí

# EJECUTA LA SIMULACIÓN:
# Crea datos de al menos 3 equipos diferentes
# Simula una mini-liga entre ellos
# Muestra el reporte final con estadísticas completas
```

### Criterios de Evaluación
- **Simulación matemáticamente coherente** (15 puntos)
- **Modularidad y reutilización** (5 puntos)
- **Presentación de resultados** (5 puntos)

---

## Parte 4: Módulo de Validación y Testing (25 puntos)

### Objetivo
Crear un sistema de validación y testing para asegurar la calidad del código.

### Instrucciones Detalladas

**Paso 4:** Desarrolla funciones de testing y validación:

```python
# TU CÓDIGO AQUÍ:
# Crea un módulo completo de testing:

def test_funcion_promedio():
    """
    Prueba la función calcular_promedio_deportivo con casos conocidos
    
    Retorna:
    bool: True si todas las pruebas pasan, False en caso contrario
    """
    # Casos de prueba:
    # Lista [1, 2, 3, 4, 5] debe dar promedio 3.0
    # Lista vacía debe manejar el error apropiadamente
    # Lista [10] debe dar promedio 10.0
    # Tu implementación aquí

def test_validacion_datos():
    """
    Prueba la función validar_datos_partido
    
    Retorna:
    bool: True si todas las validaciones funcionan correctamente
    """
    # Casos de prueba:
    # Goles negativos deben ser inválidos
    # Minutos > 120 deben generar advertencia
    # Datos normales deben ser válidos
    # Tu implementación aquí

def test_analisis_plantilla():
    """
    Prueba las funciones de análisis de plantilla
    
    Retorna:
    bool: True si el análisis es correcto
    """
    # Crear datos de prueba conocidos
    # Verificar cálculos matemáticos
    # Tu implementación aquí

def ejecutar_bateria_completa_tests():
    """
    Ejecuta todas las pruebas del sistema
    
    Retorna:
    dict: Reporte completo de testing con resultados
    """
    # Tu implementación aquí

def validar_integridad_datos_liga(datos_liga):
    """
    Valida que los datos de una liga sean coherentes y completos
    
    Parámetros:
    datos_liga (dict): Datos completos de equipos y jugadores
    
    Retorna:
    dict: Reporte de integridad con errores y advertencias
    """
    # Verificar:
    # - Todos los equipos tienen jugadores
    # - No hay datos faltantes críticos
    # - Rangos de valores son realistas
    # Tu implementación aquí

# EJECUTA EL TESTING COMPLETO:
# 1. Ejecuta todos los tests individuales
# 2. Muestra un reporte de cobertura
# 3. Valida la integridad de todos los datos usados
# 4. Genera recomendaciones de mejora
```

### Criterios de Evaluación
- **Tests comprensivos y correctos** (15 puntos)
- **Validación robusta de datos** (5 puntos)
- **Reporte de calidad detallado** (5 puntos)

---

# Criterios de Evaluación Total

## Distribución de Puntos (100 total)

### 1. Correctitud Técnica (40 puntos)
- **Sintaxis y ejecución:** Código funciona sin errores
- **Implementación de funciones:** Lógica correcta y eficiente
- **Uso de parámetros:** Manejo apropiado de entradas y salidas
- **Validación de datos:** Control de errores y casos extremos

### 2. Aplicación Práctica (30 puntos)
- **Modularidad:** Funciones reutilizables y bien organizadas
- **Análisis deportivo:** Cálculos estadísticos correctos y relevantes
- **Simulaciones:** Resultados coherentes y realistas
- **Integración:** Combinación efectiva de múltiples funciones

### 3. Claridad y Documentación (30 puntos)
- **Docstrings completos:** Documentación clara de todas las funciones
- **Comentarios explicativos:** Código bien documentado
- **Nombres descriptivos:** Variables y funciones con nombres claros
- **Presentación:** Outputs formateados profesionalmente

---

# Instrucciones de Entrega

## Lista de Verificación

Antes de entregar, asegúrate de:

1. **✅ Implementar todas las funciones** solicitadas en las 4 partes
2. **✅ Incluir docstrings completos** en cada función
3. **✅ Ejecutar testing completo** sin errores
4. **✅ Usar nombres en español** para variables y comentarios
5. **✅ Mostrar ejemplos de uso** de cada función importante

## Formato de Entrega

- **Nombre del archivo:** `[matricula]-ejercicio-semana-3.ipynb`
- **Formato:** Jupyter Notebook ejecutado completamente
- **Fecha límite:** Final de la Semana 3
- **Método:** Subir a la plataforma del curso

## Recursos de Apoyo

- **Notebook principal:** `bloque-1/semana-3/funciones-modulos.ipynb`
- **Documentación Python:** [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- **Rúbrica detallada:** `evaluaciones/bloque-1/rubrica-unificada-bloque1.md`

---

**¡Domina la programación modular y construye herramientas de análisis deportivo profesionales!**
    
    Retorna:
    int: Máximo de goles en un partido
    """
    # Tu código aquí
    pass

def partidos_sin_goles(lista_goles):
    """
    Cuenta cuántos partidos sin goles tuvo el equipo
    
    Parámetros:
    lista_goles (list): Lista con goles por partido
    
    Retorna:
    int: Número de partidos sin goles
    """
    # Tu código aquí
    pass

def reporte_equipo(nombre_equipo, lista_goles):
    """
    Genera un reporte completo del equipo
    
    Parámetros:
    nombre_equipo (str): Nombre del equipo
    lista_goles (list): Lista con goles por partido
    
    Retorna:
    str: Reporte formateado del equipo
    """
    # Tu código aquí usando las funciones anteriores
    pass

# Probar todas las funciones con los datos de Barcelona y Real Madrid
```

### Tu Respuesta

*Completa todas las funciones y pruébalas con los datos proporcionados.*

## Ejercicio 2: Funciones de Análisis de Partidos (20 puntos)

### Instrucciones

Desarrolla funciones para analizar resultados de partidos:

```python
# Datos de partidos: [equipo_local, goles_local, equipo_visitante, goles_visitante]
partidos_liga = [
    ["Barcelona", 3, "Real Madrid", 1],
    ["Valencia", 2, "Atletico Madrid", 2],
    ["Sevilla", 1, "Barcelona", 2],
    ["Real Madrid", 4, "Valencia", 0],
    ["Atletico Madrid", 1, "Sevilla", 0]
]

def quien_gano(goles_local, goles_visitante):
    """
    Determina el resultado del partido
    
    Parámetros:
    goles_local (int): Goles del equipo local
    goles_visitante (int): Goles del equipo visitante
    
    Retorna:
    str: 'Local', 'Visitante' o 'Empate'
    """
    # Tu código aquí
    pass

def diferencia_goles(goles_local, goles_visitante):
    """
    Calcula la diferencia de goles en el partido
    
    Parámetros:
    goles_local (int): Goles del equipo local
    goles_visitante (int): Goles del equipo visitante
    
    Retorna:
    int: Diferencia de goles (valor absoluto)
    """
    # Tu código aquí
    pass

def partido_emocionante(goles_local, goles_visitante, umbral=3):
    """
    Determina si un partido fue emocionante (muchos goles)
    
    Parámetros:
    goles_local (int): Goles del equipo local
    goles_visitante (int): Goles del equipo visitante
    umbral (int): Número mínimo de goles para ser emocionante
    
    Retorna:
    bool: True si fue emocionante, False si no
    """
    # Tu código aquí
    pass

def analizar_partido(partido):
    """
    Análisis completo de un partido
    
    Parámetros:
    partido (list): [equipo_local, goles_local, equipo_visitante, goles_visitante]
    
    Retorna:
    dict: Análisis completo del partido
    """
    # Tu código aquí usando las funciones anteriores
    # Debe retornar un diccionario con: resultado, diferencia, emocionante, descripcion
    pass

# Analizar todos los partidos de la liga
```

### Tu Respuesta

*Completa todas las funciones de análisis de partidos y analiza toda la liga.*

## Ejercicio 3: Funciones Avanzadas con Parámetros Opcionales (20 puntos)

### Instrucciones

Crea funciones más sofisticadas con parámetros opcionales:

```python
def calcular_puntos(victorias, empates, derrotas, puntos_victoria=3, puntos_empate=1):
    """
    Calcula los puntos de un equipo en la liga
    
    Parámetros:
    victorias (int): Número de victorias
    empates (int): Número de empates
    derrotas (int): Número de derrotas
    puntos_victoria (int): Puntos por victoria (default: 3)
    puntos_empate (int): Puntos por empate (default: 1)
    
    Retorna:
    int: Total de puntos
    """
    # Tu código aquí
    pass

def estadisticas_goleador(goles_partidos, nombre="Jugador", mostrar_detalles=True):
    """
    Analiza las estadísticas de un goleador
    
    Parámetros:
    goles_partidos (list): Lista con goles por partido
    nombre (str): Nombre del jugador (default: "Jugador")
    mostrar_detalles (bool): Si mostrar detalles completos (default: True)
    
    Retorna:
    dict: Estadísticas del goleador
    """
    # Tu código aquí
    # Calcular: total_goles, promedio, mejor_partido, partidos_sin_gol
    # Si mostrar_detalles es True, incluir más información
    pass

def comparar_equipos(equipo1_stats, equipo2_stats, criterio="puntos"):
    """
    Compara dos equipos según diferentes criterios
    
    Parámetros:
    equipo1_stats (dict): Estadísticas del equipo 1
    equipo2_stats (dict): Estadísticas del equipo 2
    criterio (str): Criterio de comparación (default: "puntos")
    
    Retorna:
    str: Resultado de la comparación
    """
    # Criterios disponibles: "puntos", "goles", "diferencia"
    # Tu código aquí
    pass

# Datos para probar
barcelona_stats = {"nombre": "Barcelona", "puntos": 45, "goles_favor": 68, "goles_contra": 35}
real_madrid_stats = {"nombre": "Real Madrid", "puntos": 43, "goles_favor": 65, "goles_contra": 32}

messi_goles = [2, 0, 1, 3, 1, 0, 2, 1, 1, 0]
ronaldo_goles = [1, 1, 2, 0, 1, 3, 0, 1, 2, 1]

# Probar todas las funciones con diferentes parámetros
```

### Tu Respuesta

*Completa las funciones avanzadas y pruébalas con diferentes combinaciones de parámetros.*

## Ejercicio 4: Organizando Código en Módulos (20 puntos)

### Instrucciones

Organiza tu código en un módulo reutilizable:

```python
# Crear un "módulo" estadisticas_futbol.py (simular como clase o diccionario)

class EstadisticasFutbol:
    """
    Módulo para análisis estadístico de fútbol
    """
    
    @staticmethod
    def eficiencia_goleadora(goles, tiros):
        """
        Calcula la eficiencia goleadora de un jugador/equipo
        
        Parámetros:
        goles (int): Número de goles
        tiros (int): Número de tiros
        
        Retorna:
        float: Porcentaje de eficiencia
        """
        # Tu código aquí
        pass
    
    @staticmethod
    def indice_defensivo(goles_contra, partidos):
        """
        Calcula el índice defensivo
        
        Parámetros:
        goles_contra (int): Goles recibidos
        partidos (int): Partidos jugados
        
        Retorna:
        float: Goles contra por partido
        """
        # Tu código aquí
        pass
    
    @staticmethod
    def clasificar_equipo(puntos, partidos):
        """
        Clasifica el rendimiento del equipo
        
        Parámetros:
        puntos (int): Puntos obtenidos
        partidos (int): Partidos jugados
        
        Retorna:
        str: Clasificación del equipo
        """
        # Clasificaciones:
        # "Excelente": >= 2.0 puntos por partido
        # "Bueno": >= 1.5 puntos por partido
        # "Regular": >= 1.0 puntos por partido
        # "Malo": < 1.0 puntos por partido
        # Tu código aquí
        pass
    
    @staticmethod
    def reporte_completo(datos_equipo):
        """
        Genera un reporte completo usando todas las funciones del módulo
        
        Parámetros:
        datos_equipo (dict): Todos los datos del equipo
        
        Retorna:
        dict: Reporte completo
        """
        # Usar todas las funciones anteriores
        # Tu código aquí
        pass

# Datos para probar el módulo
equipo_test = {
    "nombre": "Barcelona",
    "goles": 68,
    "tiros": 450,
    "goles_contra": 35,
    "puntos": 45,
    "partidos": 30
}

# Usar el módulo para generar análisis completo
```

### Tu Respuesta

*Completa la clase EstadisticasFutbol y genera un análisis completo del equipo.*

## Ejercicio 5: Proyecto Mini - Sistema de Análisis (20 puntos)

### Instrucciones

Combina todas las funciones en un sistema integrado:

```python
def sistema_analisis_liga():
    """
    Sistema completo de análisis de liga
    
    Este sistema debe incluir:
    1. Funciones de carga de datos
    2. Funciones de análisis individual
    3. Funciones de comparación
    4. Funciones de reportes
    5. Menú interactivo (opcional)
    """
    
    # Datos de ejemplo
    equipos = {
        "Barcelona": {"puntos": 45, "goles_favor": 68, "goles_contra": 35, "partidos": 30},
        "Real Madrid": {"puntos": 43, "goles_favor": 65, "goles_contra": 32, "partidos": 30},
        "Atletico Madrid": {"puntos": 38, "goles_favor": 52, "goles_contra": 28, "partidos": 30}
    }
    
    # Implementar funciones del sistema:
    
    def cargar_equipo(nombre):
        """Carga datos de un equipo específico"""
        # Tu código aquí
        pass
    
    def top_equipos(criterio="puntos", n=3):
        """Obtiene los mejores equipos según criterio"""
        # Tu código aquí
        pass
    
    def analisis_comparativo(equipo1, equipo2):
        """Compara dos equipos en múltiples aspectos"""
        # Tu código aquí
        pass
    
    def reporte_liga():
        """Genera reporte completo de la liga"""
        # Tu código aquí
        pass
    
    def buscar_estadistica(equipo, estadistica):
        """Busca una estadística específica"""
        # Tu código aquí
        pass
    
    # Demostrar el uso del sistema
    print("=== SISTEMA DE ANÁLISIS DE LIGA ===")
    # Mostrar ejemplos de uso de todas las funciones
    
    return equipos

# Ejecutar el sistema
sistema_analisis_liga()
```

### Tu Respuesta

*Completa el sistema integrado de análisis y demuestra su funcionamiento.*

## Ejercicio Bonus: Funciones Lambda y Programación Funcional (10 puntos extra)

### Instrucciones

**Ejercicio opcional para puntos adicionales:**

```python
# Datos de jugadores
jugadores = [
    {"nombre": "Messi", "goles": 30, "asistencias": 12, "partidos": 25},
    {"nombre": "Ronaldo", "goles": 28, "asistencias": 8, "partidos": 24},
    {"nombre": "Mbappé", "goles": 25, "asistencias": 10, "partidos": 22},
    {"nombre": "Haaland", "goles": 35, "asistencias": 5, "partidos": 20}
]

# Usar funciones lambda para:
# 1. Ordenar jugadores por goles
# 2. Filtrar jugadores con más de 1 gol por partido
# 3. Crear lista de nombres con más de 10 asistencias
# 4. Calcular promedio de goles por partido para cada jugador
# 5. Crear función que combine múltiples criterios

# Ejemplo:
# goles_por_partido = list(map(lambda j: j["goles"] / j["partidos"], jugadores))
```

### Tu Respuesta

*Ejercicio opcional: Implementa análisis usando programación funcional.*

## Criterios de Evaluación

### Funcionalidad (40%)

- [ ] Funciones básicas implementadas correctamente (10%)
- [ ] Funciones con parámetros opcionales funcionando (10%)
- [ ] Módulo/clase organizada apropiadamente (10%)
- [ ] Sistema integrado funcionando (10%)

### Aplicación Práctica (30%)

- [ ] Análisis deportivo relevante y útil (15%)
- [ ] Reutilización efectiva de código (15%)

### Calidad de Código (30%)

- [ ] Documentación clara en todas las funciones (15%)
- [ ] Código bien estructurado y legible (15%)

## Instrucciones de Entrega

1. **Completa todos los ejercicios** en este notebook
2. **Prueba todas las funciones** con diferentes datos
3. **Documenta tu código** con comentarios claros
4. **Guarda como:** `[matricula]-ejercicio-semana-3.ipynb`
5. **Entrega antes del final de Semana 3**

## Recursos de Apoyo

- Notebook de la Semana 3: `funciones-modulos.ipynb`
- Documentación Python sobre funciones: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Guía de mejores prácticas para funciones

---

**¡Crea código reutilizable y organizado para análisis deportivos profesionales!** ⚽🔧

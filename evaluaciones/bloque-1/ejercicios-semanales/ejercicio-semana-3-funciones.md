# Ejercicio Semana 3: Funciones y Módulos en Análisis Deportivo

## Información del Ejercicio

**Bloque:** 1 - Prerrequisitos de Programación  
**Peso:** 12% de la calificación del bloque (60% ÷ 5 ejercicios)  
**Tiempo estimado:** 1.5-2 horas  
**Entrega:** Final de Semana 3

## Objetivos

Al completar este ejercicio, serás capaz de:

- Crear funciones reutilizables para análisis deportivo
- Implementar funciones con parámetros y valores de retorno
- Organizar código en módulos para mayor eficiencia
- Aplicar principios de programación modular a datos de fútbol

## Ejercicio 1: Funciones Básicas de Estadísticas (20 puntos)

### Instrucciones

Crea funciones para calcular estadísticas básicas de equipos:

```python
# Datos de ejemplo para probar tus funciones
goles_barcelona = [3, 1, 2, 4, 0, 2, 1, 3, 2, 1]
goles_real_madrid = [2, 3, 1, 2, 1, 3, 0, 2, 4, 1]

# Crear las siguientes funciones:

def promedio_goles(lista_goles):
    """
    Calcula el promedio de goles por partido
    
    Parámetros:
    lista_goles (list): Lista con goles por partido
    
    Retorna:
    float: Promedio de goles
    """
    # Tu código aquí
    pass

def maximo_goles(lista_goles):
    """
    Encuentra la mayor cantidad de goles en un partido
    
    Parámetros:
    lista_goles (list): Lista con goles por partido
    
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
4. **Guarda como:** `ejercicio-semana-3-[tu-apellido].ipynb`
5. **Entrega antes del final de Semana 3**

## Recursos de Apoyo

- Notebook de la Semana 3: `funciones-modulos.ipynb`
- Documentación Python sobre funciones: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Guía de mejores prácticas para funciones

---

**¡Crea código reutilizable y organizado para análisis deportivos profesionales!** ⚽🔧

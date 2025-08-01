# Ejercicio Semana 2: Estructuras de Control

## 📋 Información General

**Bloque:** 1 - Prerrequisitos de Programación  
**Semana:** 2  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 2

## 🎯 Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

- Implementar estructuras condicionales para análisis deportivo
- Utilizar bucles para procesar múltiples datos de partidos
- Aplicar estructuras de control anidadas
- Crear reportes automatizados de análisis deportivo

## 📚 Conocimientos Previos Requeridos

- Variables y tipos de datos básicos
- Operadores de comparación y lógicos
- Condicionales (if, elif, else)
- Bucles (for, while)

## 🚀 Ejercicio: Sistema de Análisis de Temporada

### Contexto

Como analista deportivo, necesitas crear un sistema que analice los resultados de varios partidos de una temporada. El sistema debe clasificar partidos, calcular estadísticas y generar reportes automáticos.

### Parte 1: Clasificador de Partidos (25 puntos)

**Instrucciones:**
Crea una función que clasifique partidos según diferentes criterios:

```python
def clasificar_partido(goles_local, goles_visitante, asistencia, capacidad):
    """
    Clasifica un partido según el resultado y la asistencia
    
    Parámetros:
    - goles_local: goles del equipo local
    - goles_visitante: goles del equipo visitante  
    - asistencia: número de espectadores
    - capacidad: capacidad máxima del estadio
    
    Retorna: diccionario con clasificaciones
    """
    
    # Tu código aquí
    resultado = {}
    
    # 1. Clasificar por resultado
    diferencia = # Tu código
    
    if # Tu condición para goleada (diferencia >= 3):
        resultado['tipo_partido'] = "Goleada"
    elif # Tu condición para victoria clara:
        resultado['tipo_partido'] = "Victoria clara"
    elif # Tu condición para victoria ajustada:
        resultado['tipo_partido'] = "Victoria ajustada"
    else:
        resultado['tipo_partido'] = "Empate"
    
    # 2. Determinar ganador
    if # Tu condición:
        resultado['ganador'] = "Local"
    elif # Tu condición:
        resultado['ganador'] = "Visitante"
    else:
        resultado['ganador'] = "Empate"
    
    # 3. Clasificar asistencia
    porcentaje_asistencia = # Tu código
    
    if porcentaje_asistencia >= 95:
        resultado['asistencia'] = "Lleno total"
    elif porcentaje_asistencia >= 80:
        resultado['asistencia'] = "Excelente"
    elif porcentaje_asistencia >= 60:
        resultado['asistencia'] = "Buena"
    else:
        resultado['asistencia'] = "Regular"
    
    return resultado

# Prueba tu función con estos partidos:
partidos_prueba = [
    (3, 1, 45000, 50000),  # Partido 1
    (0, 0, 30000, 60000),  # Partido 2
    (4, 0, 55000, 55000),  # Partido 3
]

print("=== PRUEBAS DEL CLASIFICADOR ===")
for i, (gl, gv, ast, cap) in enumerate(partidos_prueba, 1):
    print(f"Partido {i}: {gl}-{gv}")
    clasificacion = clasificar_partido(gl, gv, ast, cap)
    # Tu código para mostrar la clasificación
```

### Parte 2: Análisis de Múltiples Partidos (30 puntos)

**Instrucciones:**
Analiza una lista de partidos usando bucles:

```python
# Datos de partidos de la temporada
partidos_temporada = [
    {"local": "Barcelona", "visitante": "Real Madrid", "goles_l": 2, "goles_v": 1, "asistencia": 85000},
    {"local": "Liverpool", "visitante": "Manchester City", "goles_l": 3, "goles_v": 2, "asistencia": 54000},
    {"local": "Bayern Munich", "visitante": "Borussia Dortmund", "goles_l": 1, "goles_v": 1, "asistencia": 75000},
    {"local": "Juventus", "visitante": "AC Milan", "goles_l": 0, "goles_v": 2, "asistencia": 65000},
    {"local": "PSG", "visitante": "Olympique Lyon", "goles_l": 4, "goles_v": 0, "asistencia": 47000},
]

# Capacidades de los estadios
capacidades = {
    "Barcelona": 99354,
    "Liverpool": 54074,
    "Bayern Munich": 75000,
    "Juventus": 80000,
    "PSG": 47929
}

# Tu código aquí
# 1. Inicializar contadores
total_goles = 0
partidos_empate = 0
partidos_goleada = 0
mejor_asistencia = 0
partido_mas_goles = 0

# 2. Procesar cada partido con un bucle for
for i, partido in enumerate(partidos_temporada):
    print(f"\n--- PARTIDO {i+1} ---")
    print(f"{partido['local']} vs {partido['visitante']}")
    print(f"Resultado: {partido['goles_l']}-{partido['goles_v']}")
    
    # Tu código para:
    # - Calcular total de goles del partido
    # - Clasificar el partido usando tu función anterior
    # - Actualizar contadores
    # - Mostrar información del partido
    
    goles_partido = # Tu código
    total_goles += goles_partido
    
    # Obtener capacidad del estadio local
    capacidad_estadio = capacidades[partido['local']]
    
    # Clasificar el partido
    clasificacion = # Tu código usando tu función
    
    # Mostrar clasificación
    print(f"Tipo: {clasificacion['tipo_partido']}")
    print(f"Ganador: {clasificacion['ganador']}")
    print(f"Asistencia: {clasificacion['asistencia']}")
    
    # Actualizar estadísticas
    if # condición para empate:
        partidos_empate += 1
    
    if # condición para goleada:
        partidos_goleada += 1
    
    if # condición para mejor asistencia:
        mejor_asistencia = partido['asistencia']
    
    if # condición para partido con más goles:
        partido_mas_goles = goles_partido

# 3. Mostrar estadísticas finales
print("\n=== ESTADÍSTICAS DE LA TEMPORADA ===")
# Tu código para mostrar:
# - Total de partidos analizados
# - Total de goles en todos los partidos
# - Promedio de goles por partido
# - Número de empates
# - Número de goleadas
# - Mejor asistencia registrada
# - Partido con más goles
```

### Parte 3: Búsqueda y Filtrado (25 puntos)

**Instrucciones:**
Implementa funciones de búsqueda usando bucles y condicionales:

```python
def buscar_partidos_por_criterio(partidos, criterio, valor):
    """
    Busca partidos que cumplan un criterio específico
    
    Criterios disponibles:
    - 'equipo': busca partidos donde participe un equipo
    - 'goles_minimos': partidos con al menos X goles totales
    - 'resultado': partidos con resultado específico ('empate', 'goleada')
    """
    
    partidos_encontrados = []
    
    # Tu código aquí usando bucles y condicionales
    
    for partido in partidos:
        cumple_criterio = False
        
        if criterio == "equipo":
            # Tu código: verificar si el equipo participa (local o visitante)
            pass
        
        elif criterio == "goles_minimos":
            # Tu código: verificar si el total de goles >= valor
            pass
        
        elif criterio == "resultado":
            # Tu código: clasificar y verificar el tipo de resultado
            pass
        
        if cumple_criterio:
            partidos_encontrados.append(partido)
    
    return partidos_encontrados

# Pruebas de la función de búsqueda
print("=== PRUEBAS DE BÚSQUEDA ===")

# 1. Buscar partidos del Barcelona
print("Partidos del Barcelona:")
partidos_barca = buscar_partidos_por_criterio(partidos_temporada, "equipo", "Barcelona")
# Tu código para mostrar los resultados

# 2. Buscar partidos con al menos 4 goles
print("\nPartidos con 4+ goles:")
partidos_goles = buscar_partidos_por_criterio(partidos_temporada, "goles_minimos", 4)
# Tu código para mostrar los resultados

# 3. Buscar empates
print("\nPartidos empatados:")
empates = buscar_partidos_por_criterio(partidos_temporada, "resultado", "empate")
# Tu código para mostrar los resultados
```

### Parte 4: Generador de Reportes (20 puntos)

**Instrucciones:**
Crea un generador de reportes automático:

```python
def generar_reporte_completo(partidos, capacidades):
    """
    Genera un reporte completo de análisis de partidos
    """
    
    print("=" * 50)
    print("REPORTE COMPLETO DE ANÁLISIS DEPORTIVO")
    print("=" * 50)
    
    # 1. Estadísticas generales
    total_partidos = len(partidos)
    print(f"\n📊 ESTADÍSTICAS GENERALES")
    print(f"Total de partidos analizados: {total_partidos}")
    
    # Tu código para calcular y mostrar:
    total_goles_reporte = 0
    equipos_participantes = set()  # usar set para equipos únicos
    
    # Usar bucles para calcular estadísticas
    for partido in partidos:
        # Tu código aquí
        pass
    
    print(f"Total de goles: {total_goles_reporte}")
    print(f"Promedio de goles por partido: {total_goles_reporte/total_partidos:.2f}")
    print(f"Equipos participantes: {len(equipos_participantes)}")
    
    # 2. Análisis por categorías
    print(f"\n🏆 ANÁLISIS POR CATEGORÍAS")
    
    # Contadores por categoría
    categorias = {
        "Empate": 0,
        "Victoria ajustada": 0,
        "Victoria clara": 0,
        "Goleada": 0
    }
    
    # Tu código: usar bucle para categorizar todos los partidos
    
    for categoria, cantidad in categorias.items():
        porcentaje = (cantidad / total_partidos) * 100
        print(f"{categoria}: {cantidad} partidos ({porcentaje:.1f}%)")
    
    # 3. Ranking de asistencias
    print(f"\n👥 RANKING DE ASISTENCIAS")
    
    # Tu código: crear y mostrar ranking de asistencias
    # Pista: puedes usar una lista de tuplas y ordenarla
    
    print("\n" + "=" * 50)
    print("FIN DEL REPORTE")
    print("=" * 50)

# Generar el reporte completo
generar_reporte_completo(partidos_temporada, capacidades)
```

## 📤 Instrucciones de Entrega

1. **Formato:** Archivo `.py` o notebook `.ipynb`
2. **Nombre del archivo:** `apellido_nombre_ejercicio_semana02.py`
3. **Contenido mínimo:**
   - Todas las funciones implementadas y probadas
   - Comentarios explicando la lógica de cada parte
   - Salida completa de todas las pruebas
   - Reporte final generado

4. **Documentación adicional:**
   - Explicación de al menos 2 decisiones de programación que tomaste
   - Reflexión sobre qué parte fue más desafiante y por qué

## 🏆 Criterios de Evaluación

### Correctitud Técnica (40 puntos)

- **Excelente (36-40):** Todas las funciones ejecutan correctamente, lógica de control perfecta
- **Competente (28-35):** Funciones ejecutan con errores menores, lógica mayormente correcta
- **En desarrollo (20-27):** Algunas funciones fallan, errores en estructuras de control
- **Insuficiente (0-19):** Múltiples errores, estructuras de control mal implementadas

### Aplicación Práctica (30 puntos)

- **Excelente (27-30):** Uso avanzado de estructuras de control, búsquedas eficientes
- **Competente (21-26):** Uso apropiado de condicionales y bucles
- **En desarrollo (15-20):** Uso básico de estructuras de control
- **Insuficiente (0-14):** Uso incorrecto o limitado de estructuras de control

### Claridad y Documentación (30 puntos)

- **Excelente (27-30):** Código muy bien documentado, funciones claras, reporte profesional
- **Competente (21-26):** Buena documentación, código legible
- **En desarrollo (15-20):** Documentación básica, código parcialmente claro
- **Insuficiente (0-14):** Poca o nula documentación, código confuso

## 💡 Consejos para el Éxito

1. **Planifica la lógica:** Antes de programar, escribe en papel qué condiciones necesitas
2. **Prueba paso a paso:** Ejecuta cada función por separado antes de integrar
3. **Usa nombres descriptivos:** `goles_totales` es mejor que `gt`
4. **Comenta las condiciones:** Explica qué verifica cada `if`
5. **Maneja casos especiales:** ¿Qué pasa si hay 0 goles? ¿Y si la lista está vacía?

## 🔗 Recursos Adicionales

- [Estructuras de control en Python](https://docs.python.org/3/tutorial/controlflow.html)
- [Bucles for y while](https://www.w3schools.com/python/python_for_loops.asp)
- [Condicionales if/elif/else](https://www.w3schools.com/python/python_conditions.asp)

---

*¿Preguntas? Contacta a tu instructor durante las horas de oficina o en el foro del curso.*

# Ejercicio Semana 3: Funciones y Módulos

## 📋 Información General

**Bloque:** 1 - Prerrequisitos de Programación  
**Semana:** 3  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 3

## 🎯 Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

- Crear funciones modulares para análisis deportivo
- Implementar funciones con parámetros y valores de retorno
- Organizar código en módulos reutilizables
- Aplicar principios de programación modular

## 📚 Conocimientos Previos Requeridos

- Definición y llamada de funciones
- Parámetros y argumentos
- Valores de retorno
- Alcance de variables (scope)
- Importación de módulos

## 🚀 Ejercicio: Biblioteca de Análisis Deportivo

### Contexto

Como analista deportivo senior, necesitas crear una biblioteca de funciones reutilizables que otros analistas puedan usar. Esta biblioteca debe incluir funciones para calcular estadísticas, generar reportes y analizar rendimiento de equipos.

### Parte 1: Funciones de Cálculo Básico (25 puntos)

**Instrucciones:**
Crea un conjunto de funciones básicas para cálculos deportivos:

```python
def calcular_puntos_liga(victorias, empates, derrotas):
    """
    Calcula los puntos de un equipo en la liga
    
    Parámetros:
    - victorias: número de partidos ganados (3 puntos cada uno)
    - empates: número de partidos empatados (1 punto cada uno)  
    - derrotas: número de partidos perdidos (0 puntos cada uno)
    
    Retorna: total de puntos
    """
    # Tu código aquí
    pass

def calcular_diferencia_goles(goles_favor, goles_contra):
    """
    Calcula la diferencia de goles de un equipo
    
    Parámetros:
    - goles_favor: goles anotados por el equipo
    - goles_contra: goles recibidos por el equipo
    
    Retorna: diferencia de goles
    """
    # Tu código aquí
    pass

def calcular_promedio_goles(goles_totales, partidos_jugados):
    """
    Calcula el promedio de goles por partido
    
    Parámetros:
    - goles_totales: total de goles en todos los partidos
    - partidos_jugados: número de partidos jugados
    
    Retorna: promedio de goles por partido (float, 2 decimales)
    """
    # Tu código aquí
    # Maneja el caso donde partidos_jugados sea 0
    pass

def calcular_porcentaje_victorias(victorias, total_partidos):
    """
    Calcula el porcentaje de victorias de un equipo
    
    Parámetros:
    - victorias: número de partidos ganados
    - total_partidos: total de partidos jugados
    
    Retorna: porcentaje de victorias (float, 1 decimal)
    """
    # Tu código aquí
    # Maneja el caso donde total_partidos sea 0
    pass

# Pruebas de las funciones básicas
print("=== PRUEBAS DE FUNCIONES BÁSICAS ===")

# Datos de prueba del FC Barcelona
victorias_barca = 18
empates_barca = 3
derrotas_barca = 2
goles_favor_barca = 65
goles_contra_barca = 20

# Tu código para probar todas las funciones
print("Estadísticas del FC Barcelona:")
puntos = # Tu código
diferencia_goles = # Tu código
promedio_goles = # Tu código
porcentaje_victorias = # Tu código

print(f"Puntos en la liga: {puntos}")
print(f"Diferencia de goles: {diferencia_goles:+d}")  # El +:d muestra el signo
print(f"Promedio de goles por partido: {promedio_goles:.2f}")
print(f"Porcentaje de victorias: {porcentaje_victorias:.1f}%")
```

### Parte 2: Funciones de Análisis Avanzado (30 puntos)

**Instrucciones:**
Implementa funciones más complejas para análisis deportivo:

```python
def analizar_rendimiento_equipo(nombre_equipo, estadisticas):
    """
    Analiza el rendimiento completo de un equipo
    
    Parámetros:
    - nombre_equipo: nombre del equipo
    - estadisticas: diccionario con las estadísticas del equipo
      {'victorias': int, 'empates': int, 'derrotas': int, 
       'goles_favor': int, 'goles_contra': int}
    
    Retorna: diccionario con análisis completo
    """
    
    # Tu código aquí
    analisis = {}
    
    # Usar las funciones básicas que ya creaste
    total_partidos = # Tu código
    analisis['partidos_jugados'] = total_partidos
    analisis['puntos'] = # Tu código usando calcular_puntos_liga()
    analisis['diferencia_goles'] = # Tu código usando calcular_diferencia_goles()
    analisis['promedio_goles'] = # Tu código usando calcular_promedio_goles()
    analisis['porcentaje_victorias'] = # Tu código usando calcular_porcentaje_victorias()
    
    # Clasificación del rendimiento
    if analisis['porcentaje_victorias'] >= 70:
        analisis['clasificacion'] = "Excelente"
    elif analisis['porcentaje_victorias'] >= 50:
        analisis['clasificacion'] = "Bueno"
    elif analisis['porcentaje_victorias'] >= 30:
        analisis['clasificacion'] = "Regular"
    else:
        analisis['clasificacion'] = "Necesita mejorar"
    
    return analisis

def comparar_equipos(equipo1, stats1, equipo2, stats2):
    """
    Compara el rendimiento de dos equipos
    
    Parámetros:
    - equipo1, equipo2: nombres de los equipos
    - stats1, stats2: diccionarios con estadísticas de cada equipo
    
    Retorna: diccionario con la comparación
    """
    
    # Tu código aquí
    # Analizar ambos equipos usando la función anterior
    analisis1 = # Tu código
    analisis2 = # Tu código
    
    comparacion = {
        'equipo_mejor_puntos': '',
        'equipo_mejor_diferencia': '',
        'equipo_mejor_promedio': '',
        'ventaja_puntos': 0,
        'ventaja_diferencia': 0
    }
    
    # Tu código para determinar qué equipo es mejor en cada categoría
    
    return comparacion

def generar_reporte_equipo(nombre_equipo, estadisticas, incluir_comparacion=False, otro_equipo=None, otras_stats=None):
    """
    Genera un reporte completo de un equipo
    
    Parámetros:
    - nombre_equipo: nombre del equipo
    - estadisticas: diccionario con estadísticas
    - incluir_comparacion: si incluir comparación con otro equipo
    - otro_equipo: nombre del otro equipo (opcional)
    - otras_stats: estadísticas del otro equipo (opcional)
    
    No retorna nada, imprime el reporte
    """
    
    print(f"\n{'='*50}")
    print(f"REPORTE DE RENDIMIENTO: {nombre_equipo.upper()}")
    print(f"{'='*50}")
    
    # Tu código aquí
    # Usar analizar_rendimiento_equipo() para obtener el análisis
    analisis = # Tu código
    
    # Mostrar estadísticas básicas
    print(f"\n📊 ESTADÍSTICAS BÁSICAS:")
    print(f"Partidos jugados: {analisis['partidos_jugados']}")
    print(f"Puntos: {analisis['puntos']}")
    print(f"Diferencia de goles: {analisis['diferencia_goles']:+d}")
    print(f"Promedio de goles: {analisis['promedio_goles']:.2f}")
    print(f"Porcentaje de victorias: {analisis['porcentaje_victorias']:.1f}%")
    print(f"Clasificación: {analisis['clasificacion']}")
    
    # Si se solicita comparación
    if incluir_comparacion and otro_equipo and otras_stats:
        print(f"\n🆚 COMPARACIÓN CON {otro_equipo.upper()}:")
        comparacion = # Tu código usando comparar_equipos()
        
        # Tu código para mostrar la comparación
    
    print(f"\n{'='*50}")

# Datos de prueba para equipos
equipos_datos = {
    "Barcelona": {
        "victorias": 18, "empates": 3, "derrotas": 2,
        "goles_favor": 65, "goles_contra": 20
    },
    "Real Madrid": {
        "victorias": 16, "empates": 5, "derrotas": 2,
        "goles_favor": 58, "goles_contra": 25
    },
    "Atletico Madrid": {
        "victorias": 12, "empates": 8, "derrotas": 3,
        "goles_favor": 45, "goles_contra": 30
    }
}

# Pruebas de las funciones avanzadas
print("=== PRUEBAS DE FUNCIONES AVANZADAS ===")

# Generar reportes individuales
for equipo, stats in equipos_datos.items():
    generar_reporte_equipo(equipo, stats)

# Generar reporte con comparación
print("\n=== REPORTE CON COMPARACIÓN ===")
generar_reporte_equipo(
    "Barcelona", 
    equipos_datos["Barcelona"],
    incluir_comparacion=True,
    otro_equipo="Real Madrid",
    otras_stats=equipos_datos["Real Madrid"]
)
```

### Parte 3: Módulo de Utilidades (25 puntos)

**Instrucciones:**
Crea funciones de utilidad que puedan ser reutilizadas:

```python
# === MÓDULO DE UTILIDADES DEPORTIVAS ===

def validar_estadisticas(estadisticas):
    """
    Valida que las estadísticas de un equipo sean correctas
    
    Parámetros:
    - estadisticas: diccionario con estadísticas del equipo
    
    Retorna: tupla (es_valido, lista_errores)
    """
    
    errores = []
    
    # Tu código aquí
    # Verificar que todas las claves necesarias existan
    claves_requeridas = ['victorias', 'empates', 'derrotas', 'goles_favor', 'goles_contra']
    
    for clave in claves_requeridas:
        if # Tu condición:
            errores.append(f"Falta la clave: {clave}")
    
    # Verificar que todos los valores sean números no negativos
    for clave, valor in estadisticas.items():
        if # Tu condición:
            errores.append(f"{clave} debe ser un número no negativo")
    
    # Verificar lógica deportiva (ej: no puede haber más goles contra que partidos * 10)
    total_partidos = estadisticas.get('victorias', 0) + estadisticas.get('empates', 0) + estadisticas.get('derrotas', 0)
    if total_partidos == 0:
        errores.append("El equipo debe haber jugado al menos un partido")
    
    es_valido = len(errores) == 0
    return es_valido, errores

def formatear_numero(numero, tipo='decimal'):
    """
    Formatea números para presentación
    
    Parámetros:
    - numero: número a formatear
    - tipo: 'decimal', 'porcentaje', 'entero'
    
    Retorna: string formateado
    """
    
    # Tu código aquí
    if tipo == 'decimal':
        return # Tu código (2 decimales)
    elif tipo == 'porcentaje':
        return # Tu código (1 decimal con símbolo %)
    elif tipo == 'entero':
        return # Tu código (sin decimales)
    else:
        return str(numero)

def crear_ranking(equipos_dict, criterio='puntos'):
    """
    Crea un ranking de equipos según un criterio
    
    Parámetros:
    - equipos_dict: diccionario con datos de equipos
    - criterio: criterio para ordenar ('puntos', 'diferencia_goles', 'porcentaje_victorias')
    
    Retorna: lista de tuplas (posicion, equipo, valor)
    """
    
    # Tu código aquí
    equipos_con_valores = []
    
    for nombre_equipo, stats in equipos_dict.items():
        # Validar estadísticas primero
        valido, errores = validar_estadisticas(stats)
        if not valido:
            print(f"⚠️ Advertencia: {nombre_equipo} tiene datos inválidos")
            continue
        
        # Calcular el valor según el criterio
        if criterio == 'puntos':
            valor = # Tu código usando calcular_puntos_liga()
        elif criterio == 'diferencia_goles':
            valor = # Tu código usando calcular_diferencia_goles()
        elif criterio == 'porcentaje_victorias':
            total = stats['victorias'] + stats['empates'] + stats['derrotas']
            valor = # Tu código usando calcular_porcentaje_victorias()
        else:
            valor = 0
        
        equipos_con_valores.append((nombre_equipo, valor))
    
    # Ordenar de mayor a menor
    equipos_ordenados = sorted(equipos_con_valores, key=lambda x: x[1], reverse=True)
    
    # Crear ranking con posiciones
    ranking = []
    for i, (equipo, valor) in enumerate(equipos_ordenados, 1):
        ranking.append((i, equipo, valor))
    
    return ranking

def mostrar_ranking(ranking, criterio):
    """
    Muestra un ranking de forma visual
    
    Parámetros:
    - ranking: lista de tuplas del ranking
    - criterio: criterio usado para el ranking
    """
    
    print(f"\n🏆 RANKING POR {criterio.upper().replace('_', ' ')}")
    print("-" * 50)
    
    for posicion, equipo, valor in ranking:
        # Tu código para formatear y mostrar cada línea del ranking
        if criterio == 'porcentaje_victorias':
            valor_fmt = formatear_numero(valor, 'porcentaje')
        elif criterio == 'diferencia_goles':
            valor_fmt = formatear_numero(valor, 'entero')
        else:  # puntos
            valor_fmt = formatear_numero(valor, 'entero')
        
        print(f"{posicion:2d}. {equipo:<20} {valor_fmt}")

# Pruebas del módulo de utilidades
print("=== PRUEBAS DEL MÓDULO DE UTILIDADES ===")

# 1. Validar estadísticas
print("1. Validación de estadísticas:")
for equipo, stats in equipos_datos.items():
    valido, errores = validar_estadisticas(stats)
    print(f"{equipo}: {'✅ Válido' if valido else '❌ Errores: ' + ', '.join(errores)}")

# 2. Probar estadísticas inválidas
print("\n2. Prueba con datos inválidos:")
datos_invalidos = {"victorias": -1, "empates": 2}  # Faltan claves y valor negativo
valido, errores = validar_estadisticas(datos_invalidos)
print(f"Datos inválidos: {'✅ Válido' if valido else '❌ Errores: ' + ', '.join(errores)}")

# 3. Crear y mostrar rankings
criterios = ['puntos', 'diferencia_goles', 'porcentaje_victorias']
for criterio in criterios:
    ranking = crear_ranking(equipos_datos, criterio)
    mostrar_ranking(ranking, criterio)
```

### Parte 4: Integración y Pruebas (20 puntos)

**Instrucciones:**
Crea un programa principal que use todas las funciones:

```python
def programa_principal():
    """
    Programa principal que demuestra el uso de todas las funciones
    """
    
    print("🏈 SISTEMA DE ANÁLISIS DEPORTIVO")
    print("=" * 60)
    
    # Datos adicionales para pruebas más completas
    liga_datos = {
        "Barcelona": {"victorias": 18, "empates": 3, "derrotas": 2, "goles_favor": 65, "goles_contra": 20},
        "Real Madrid": {"victorias": 16, "empates": 5, "derrotas": 2, "goles_favor": 58, "goles_contra": 25},
        "Atletico Madrid": {"victorias": 12, "empates": 8, "derrotas": 3, "goles_favor": 45, "goles_contra": 30},
        "Sevilla": {"victorias": 10, "empates": 7, "derrotas": 6, "goles_favor": 40, "goles_contra": 35},
        "Real Sociedad": {"victorias": 11, "empates": 5, "derrotas": 7, "goles_favor": 38, "goles_contra": 32}
    }
    
    print("\n📋 DATOS DE LA LIGA:")
    for equipo in liga_datos:
        print(f"- {equipo}")
    
    # 1. Validar todos los datos
    print(f"\n🔍 VALIDACIÓN DE DATOS:")
    todos_validos = True
    for equipo, stats in liga_datos.items():
        valido, errores = validar_estadisticas(stats)
        if valido:
            print(f"✅ {equipo}: Datos válidos")
        else:
            print(f"❌ {equipo}: {', '.join(errores)}")
            todos_validos = False
    
    if not todos_validos:
        print("⚠️ Algunos equipos tienen datos inválidos. Revisa antes de continuar.")
        return
    
    # 2. Mostrar análisis individual del líder
    rankings_puntos = crear_ranking(liga_datos, 'puntos')
    lider = rankings_puntos[0][1]  # Equipo en primera posición
    
    print(f"\n👑 ANÁLISIS DEL LÍDER ACTUAL:")
    generar_reporte_equipo(lider, liga_datos[lider])
    
    # 3. Mostrar todos los rankings
    print(f"\n📊 RANKINGS COMPLETOS:")
    for criterio in ['puntos', 'diferencia_goles', 'porcentaje_victorias']:
        ranking = crear_ranking(liga_datos, criterio)
        mostrar_ranking(ranking, criterio)
    
    # 4. Comparación entre los dos primeros
    segundo_lugar = rankings_puntos[1][1]
    print(f"\n🆚 COMPARACIÓN LÍDER vs SEGUNDO LUGAR:")
    generar_reporte_equipo(
        lider, 
        liga_datos[lider],
        incluir_comparacion=True,
        otro_equipo=segundo_lugar,
        otras_stats=liga_datos[segundo_lugar]
    )
    
    # 5. Estadísticas de la liga completa
    print(f"\n🏆 ESTADÍSTICAS GENERALES DE LA LIGA:")
    
    # Tu código para calcular estadísticas generales usando las funciones
    total_partidos = 0
    total_goles = 0
    equipos_excelentes = 0
    
    for equipo, stats in liga_datos.items():
        analisis = analizar_rendimiento_equipo(equipo, stats)
        total_partidos += analisis['partidos_jugados']
        total_goles += stats['goles_favor']
        
        if analisis['clasificacion'] == "Excelente":
            equipos_excelentes += 1
    
    print(f"Total de partidos jugados: {total_partidos}")
    print(f"Total de goles anotados: {total_goles}")
    print(f"Promedio de goles por partido: {formatear_numero(total_goles/total_partidos, 'decimal')}")
    print(f"Equipos con rendimiento excelente: {equipos_excelentes}")
    
    print(f"\n{'='*60}")
    print("🎉 ANÁLISIS COMPLETADO")
    print(f"{'='*60}")

# Ejecutar el programa principal
if __name__ == "__main__":
    programa_principal()
```

## 📤 Instrucciones de Entrega

1. **Formato:** Archivo `.py` 
2. **Nombre del archivo:** `apellido_nombre_ejercicio_semana03.py`
3. **Estructura del código:**
   - Todas las funciones implementadas en el orden presentado
   - Comentarios explicando la lógica de cada función
   - Programa principal que ejecute todas las pruebas
   - Docstrings completos para cada función

4. **Documentación adicional:**
   - Lista de 3 ventajas de usar funciones modulares
   - Ejemplo de cómo reutilizarías una de estas funciones en otro proyecto
   - Reflexión sobre qué función fue más difícil de implementar

## 🏆 Criterios de Evaluación

### Correctitud Técnica (40 puntos)

- **Excelente (36-40):** Todas las funciones implementadas correctamente, manejo de errores
- **Competente (28-35):** Funciones principales correctas, errores menores
- **En desarrollo (20-27):** Algunas funciones fallan, lógica parcialmente correcta
- **Insuficiente (0-19):** Múltiples funciones con errores, lógica incorrecta

### Aplicación Práctica (30 puntos)

- **Excelente (27-30):** Funciones modulares, reutilizables, bien diseñadas
- **Competente (21-26):** Funciones apropiadas, diseño adecuado
- **En desarrollo (15-20):** Funciones básicas, diseño simple
- **Insuficiente (0-14):** Funciones mal diseñadas, no modulares

### Claridad y Documentación (30 puntos)

- **Excelente (27-30):** Docstrings completos, código muy bien comentado, funciones claras
- **Competente (21-26):** Buena documentación, código legible
- **En desarrollo (15-20):** Documentación básica, comentarios simples
- **Insuficiente (0-14):** Poca documentación, código difícil de entender

## 💡 Consejos para el Éxito

1. **Planifica las funciones:** Define qué hace cada función antes de programar
2. **Usa docstrings:** Documenta parámetros, funcionamiento y valor de retorno
3. **Prueba individualmente:** Verifica cada función por separado
4. **Reutiliza código:** Usa funciones básicas dentro de funciones más complejas
5. **Maneja errores:** Considera casos especiales (división por cero, datos faltantes)

## 🔗 Recursos Adicionales

- [Funciones en Python](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Documentación con docstrings](https://www.python.org/dev/peps/pep-257/)
- [Módulos en Python](https://docs.python.org/3/tutorial/modules.html)

---

*¿Preguntas? Contacta a tu instructor durante las horas de oficina o en el foro del curso.*

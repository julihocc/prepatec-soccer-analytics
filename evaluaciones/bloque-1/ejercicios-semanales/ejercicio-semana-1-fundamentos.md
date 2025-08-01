# Ejercicio Semana 1: Configuración y Fundamentos

## Información del Ejercicio

**Bloque:** 1 - Prerrequisitos de Programación  
**Peso:** 12% de la calificación del bloque (60% ÷ 5 ejercicios)  
**Tiempo estimado:** 1-2 horas  
**Entrega:** Final de Semana 1

## Objetivos

Al completar este ejercicio, serás capaz de:
- Verificar la configuración correcta de tu entorno Python
- Trabajar con variables y tipos de datos básicos en contextos deportivos
- Aplicar operadores aritméticos y de comparación
- Formatear y presentar resultados de análisis básicos

## Ejercicio 1: Verificación del Entorno (15 puntos)

### Instrucciones
Ejecuta el siguiente código para verificar que tu entorno está correctamente configurado:

```python
# Verificar versión de Python
import sys
print(f"Versión de Python: {sys.version}")

# Verificar librerías principales
try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    print("✅ Todas las librerías están instaladas correctamente")
    print(f"pandas: {pd.__version__}")
    print(f"numpy: {np.__version__}")
    print(f"matplotlib: {matplotlib.__version__}")
except ImportError as e:
    print(f"❌ Error al importar: {e}")
```

### Tu Respuesta
*Ejecuta el código y pega aquí la salida de tu sistema.*

## Ejercicio 2: Variables Deportivas (20 puntos)

### Instrucciones
Crea variables para representar la información de un partido de fútbol y muestra los resultados:

```python
# Información del partido
equipo_local = "Barcelona"
equipo_visitante = "Real Madrid" 
goles_local = 2
goles_visitante = 1
minutos_jugados = 90
asistencia = 85000

# Tu código aquí - muestra toda la información del partido
# Usa f-strings para una presentación clara
```

### Tu Respuesta
*Completa el código para mostrar toda la información del partido de forma clara y profesional.*

## Ejercicio 3: Cálculos Deportivos (25 puntos)

### Instrucciones
Usando los datos del ejercicio anterior, calcula y muestra:

```python
# Tu código aquí:
# 1. Total de goles en el partido
# 2. Diferencia de goles
# 3. Promedio de goles por minuto
# 4. Promedio de espectadores por gol
# 5. Porcentaje de goles del equipo local

# Muestra todos los resultados con explicaciones claras
```

### Tu Respuesta
*Completa los cálculos y presenta los resultados con explicaciones.*

## Ejercicio 4: Análisis del Resultado (25 puntos)

### Instrucciones
Determina el resultado del partido y proporciona un análisis básico:

```python
# Tu código aquí:
# 1. Determinar quién ganó (usar condicionales)
# 2. Categorizar el tipo de partido:
#    - "Goleada" si la diferencia es >= 3
#    - "Victoria clara" si la diferencia es 2
#    - "Victoria ajustada" si la diferencia es 1
#    - "Empate" si no hay diferencia

# 3. Evaluar la asistencia:
#    - "Lleno total" si >= 80,000
#    - "Buena asistencia" si >= 50,000
#    - "Asistencia regular" si < 50,000

# Presenta un resumen completo del análisis
```

### Tu Respuesta
*Completa el análisis y presenta un resumen del partido.*

## Ejercicio 5: Comparación de Equipos (15 puntos)

### Instrucciones
Compara el rendimiento de dos equipos en la temporada:

```python
# Datos de la temporada
equipo_a = "Manchester City"
goles_a = 95
partidos_a = 38

equipo_b = "Liverpool" 
goles_b = 86
partidos_b = 38

# Tu código aquí:
# 1. Calcular promedio de goles por partido para cada equipo
# 2. Determinar cuál equipo tiene mejor promedio
# 3. Calcular la diferencia en promedio de goles
# 4. Hacer una comparación completa

# Presenta los resultados de forma clara
```

### Tu Respuesta
*Completa la comparación y presenta las conclusiones.*

## Criterios de Evaluación

### Correctitud Técnica (40%)
- [ ] Código ejecuta sin errores (20%)
- [ ] Uso correcto de variables y tipos de datos (10%)
- [ ] Implementación correcta de operadores (10%)

### Aplicación Práctica (30%)
- [ ] Cálculos deportivos son correctos (15%)
- [ ] Análisis lógico y coherente (15%)

### Claridad y Presentación (30%)
- [ ] Código bien comentado (10%)
- [ ] Resultados claramente presentados (10%)
- [ ] Uso efectivo de f-strings (10%)

## Instrucciones de Entrega

1. **Completa todos los ejercicios** en este notebook
2. **Ejecuta todas las celdas** y verifica que muestren resultados
3. **Guarda el archivo** como `ejercicio-semana-1-[tu-apellido].ipynb`
4. **Entrega antes del final de Semana 1**

## Recursos de Apoyo

- Notebook de la Semana 1: `configuracion-fundamentos.ipynb`
- Documentación de Python: https://docs.python.org/3/
- Tutorial de f-strings: https://docs.python.org/3/tutorial/inputoutput.html

---

**¡Buena suerte! Este es tu primer paso hacia el análisis de datos deportivos.** ⚽🐍

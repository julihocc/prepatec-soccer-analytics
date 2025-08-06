# Proyecto Integrador - Bloque 1: Sistema de Análisis de Liga de Fútbol

## 📋 Información General

**Peso en la calificación del bloque:** 40%  
**Tiempo estimado:** 6-8 horas  
**Modalidad:** Proyecto individual  
**Entrega:** Final de Semana 6 (primera semana del Bloque 2)

## 🎯 Descripción del Proyecto

Desarrollarás un **Sistema de Análisis de Liga de Fútbol** que permita gestionar equipos, partidos y estadísticas básicas usando únicamente Python básico y las librerías fundamentales (pandas, numpy, matplotlib).

### Contexto
Eres el analista de datos de una liga de fútbol y necesitas crear un sistema que:
- Gestione información de equipos y partidos
- Calcule estadísticas básicas de rendimiento
- Genere reportes visuales simples
- Proporcione análisis comparativos

## 🛠️ Especificaciones Técnicas

### Herramientas Permitidas
- **Python básico**: Variables, funciones, estructuras de control
- **Estructuras de datos**: Listas, diccionarios, sets
- **pandas**: Para manejo de datos tabulares
- **numpy**: Para cálculos numéricos
- **matplotlib**: Para visualizaciones básicas

### Estructura del Proyecto
```
proyecto-liga-futbol/
├── datos/
│   ├── equipos.csv
│   ├── partidos.csv
│   └── jugadores.csv
├── analisis_liga.ipynb
└── README.md
```

## 📊 Datasets Proporcionados

### equipos.csv
```csv
equipo,ciudad,estadio,capacidad,fundacion
Barcelona,Barcelona,Camp Nou,99354,1899
Real Madrid,Madrid,Santiago Bernabéu,81044,1902
Atletico Madrid,Madrid,Wanda Metropolitano,68456,1903
Valencia,Valencia,Mestalla,55000,1919
Sevilla,Sevilla,Ramón Sánchez-Pizjuán,43883,1890
```

### partidos.csv
```csv
jornada,fecha,equipo_local,equipo_visitante,goles_local,goles_visitante
1,2024-08-15,Barcelona,Valencia,2,1
1,2024-08-15,Real Madrid,Sevilla,3,0
2,2024-08-22,Valencia,Real Madrid,1,2
2,2024-08-22,Sevilla,Barcelona,0,1
3,2024-08-29,Barcelona,Real Madrid,2,1
3,2024-08-29,Atletico Madrid,Valencia,3,1
```

### jugadores.csv
```csv
nombre,equipo,posicion,edad,goles
Lewandowski,Barcelona,Delantero,35,12
Benzema,Real Madrid,Delantero,36,8
Griezmann,Atletico Madrid,Delantero,33,7
Soler,Valencia,Centrocampista,27,4
En-Nesyri,Sevilla,Delantero,27,6
```

## 📝 Requerimientos del Proyecto

### **Módulo 1: Gestión de Datos (25 puntos)**

#### 1.1 Carga y Validación de Datos
- Leer los tres archivos CSV usando pandas
- Verificar integridad de datos (valores faltantes, tipos correctos)
- Mostrar información básica de cada dataset

#### 1.2 Funciones de Utilidad
```python
def cargar_datos():
    \"\"\"Carga todos los datasets y retorna diccionario con DataFrames\"\"\"
    pass

def validar_datos(dataframes):
    \"\"\"Valida integridad de datos y reporta problemas\"\"\"
    pass

def resumen_liga():
    \"\"\"Muestra resumen general de la liga\"\"\"
    pass
```

### **Módulo 2: Análisis de Equipos (25 puntos)**

#### 2.1 Tabla de Posiciones
Crear función que calcule y muestre tabla de posiciones:
- Puntos totales (3 por victoria, 1 por empate, 0 por derrota)
- Partidos jugados, ganados, empatados, perdidos
- Goles a favor, goles en contra, diferencia de goles

#### 2.2 Estadísticas por Equipo
```python
def estadisticas_equipo(nombre_equipo):
    \"\"\"Retorna estadísticas completas de un equipo específico\"\"\"
    pass

def comparar_equipos(equipo1, equipo2):
    \"\"\"Compara rendimiento entre dos equipos\"\"\"
    pass

def mejores_equipos(categoria='puntos'):
    \"\"\"Retorna ranking según categoría especificada\"\"\"
    pass
```

### **Módulo 3: Análisis de Partidos (25 puntos)**

#### 3.1 Análisis de Resultados
- Partidos con más goles
- Victorias locales vs visitantes
- Tendencias por jornada

#### 3.2 Funciones de Análisis
```python
def analizar_partido(equipo_local, equipo_visitante, jornada):
    \"\"\"Analiza un partido específico\"\"\"
    pass

def estadisticas_goles():
    \"\"\"Estadísticas generales de goles en la liga\"\"\"
    pass

def ventaja_local():
    \"\"\"Analiza si existe ventaja de jugar en casa\"\"\"
    pass
```

### **Módulo 4: Visualizaciones (25 puntos)**

#### 4.1 Gráficos Requeridos
1. **Gráfico de barras**: Puntos por equipo
2. **Gráfico de líneas**: Goles por jornada
3. **Histograma**: Distribución de goles por partido
4. **Gráfico comparativo**: Goles locales vs visitantes

#### 4.2 Funciones de Visualización
```python
def grafico_tabla_posiciones():
    \"\"\"Gráfico de barras con puntos por equipo\"\"\"
    pass

def grafico_goles_jornada():
    \"\"\"Evolución de goles por jornada\"\"\"
    pass

def dashboard_liga():
    \"\"\"Dashboard con múltiples gráficos\"\"\"
    pass
```

## 🏆 Entregables

### 1. Notebook Principal (`analisis_liga.ipynb`)
- **Introducción**: Descripción del proyecto y objetivos
- **Carga de datos**: Implementación del Módulo 1
- **Análisis de equipos**: Implementación del Módulo 2
- **Análisis de partidos**: Implementación del Módulo 3
- **Visualizaciones**: Implementación del Módulo 4
- **Conclusiones**: Insights principales del análisis

### 2. README.md
- Descripción del proyecto
- Instrucciones de uso
- Estructura de archivos
- Hallazgos principales

### 3. Presentación de Resultados
- Resumen ejecutivo (1 página)
- 3 insights principales con evidencia
- Recomendaciones para mejoras futuras

## 📊 Criterios de Evaluación

### **Correctitud Técnica (35%)**
- **Código funcional** (15%): Todo el código ejecuta sin errores
- **Uso apropiado de herramientas** (10%): pandas, numpy, matplotlib
- **Implementación de funciones** (10%): Todas las funciones requeridas

### **Calidad del Análisis (30%)**
- **Estadísticas correctas** (15%): Cálculos precisos y validados
- **Insights relevantes** (15%): Descubrimientos significativos

### **Visualización y Comunicación (25%)**
- **Gráficos efectivos** (15%): Visualizaciones claras y apropiadas
- **Presentación clara** (10%): Explicaciones y conclusiones coherentes

### **Aplicación Contextual (10%)**
- **Relevancia deportiva** (5%): Análisis tiene sentido en contexto de fútbol
- **Creatividad** (5%): Análisis adicionales o enfoques innovadores

## 📅 Cronograma Sugerido

### Semana 1-2: Preparación
- Revisión de conceptos básicos
- Familiarización con datasets

### Semana 3-4: Desarrollo
- Implementación de Módulos 1 y 2
- Pruebas y validación

### Semana 5: Finalización
- Implementación de Módulos 3 y 4
- Documentación y presentación

### Semana 6: Entrega
- Revisión final
- Entrega del proyecto completo

## 💡 Consejos para el Éxito

### **Planificación**
- Divide el proyecto en tareas pequeñas
- Trabaja una función a la vez
- Prueba cada módulo antes de continuar

### **Programación**
- Usa nombres descriptivos para variables y funciones
- Comenta tu código claramente
- Maneja errores apropiadamente

### **Análisis**
- Valida tus cálculos manualmente
- Busca patrones interesantes en los datos
- Relaciona hallazgos con el contexto deportivo

## 📞 Recursos de Apoyo

### **Documentación**
- Pandas: https://pandas.pydata.org/docs/
- NumPy: https://numpy.org/doc/
- Matplotlib: https://matplotlib.org/stable/

### **Material del Curso**
- Notebooks Semanas 1-5
- Ejercicios semanales realizados
- Documentación del sistema de evaluaciones

### **Consultas**
- Horarios de oficina del instructor
- Foros de discusión del curso
- Sesiones de ayuda programadas

---

**¡Este proyecto consolidará todos tus conocimientos de Python básico aplicados al análisis deportivo!** ⚽📊

*Recuerda: El objetivo no es solo completar el código, sino demostrar que puedes usar programación para resolver problemas reales del mundo deportivo.*

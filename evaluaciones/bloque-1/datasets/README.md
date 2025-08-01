# Datasets del Bloque 1: Prerrequisitos de Programación

**Enfoque:** Introducción a Python y fundamentos de programación aplicados al análisis deportivo básico.

## Datasets Disponibles

### `futbol-basico.csv`
**Propósito:** Dataset simple para primeros ejercicios de programación y manipulación de datos

**Contenido:**
- **Registros:** 10 equipos con estadísticas básicas de temporada
- **Columnas:** `equipo`, `goles`, `partidos`, `temporada`
- **Nivel:** Introductorio - datos limpios y estructurados
- **Formato:** CSV estándar con headers, encoding UTF-8

**Ejemplo de datos:**
```csv
equipo,goles,partidos,temporada
Barcelona,68,38,2023-24
Real Madrid,87,38,2023-24
Atlético Madrid,70,38,2023-24
```

## Uso en Ejercicios

### Semanas 1-3: Fundamentos de Python
- **Variables y tipos de datos:** Trabajar con nombres de equipos y números
- **Listas y diccionarios:** Organizar datos de equipos
- **Funciones básicas:** Calcular promedios de goles por partido
- **Estructuras de control:** Filtrar equipos por criterios

### Semanas 4-5: Introducción a pandas/numpy
- **Carga de datos:** `pd.read_csv()` con el dataset básico
- **Exploración inicial:** `.head()`, `.info()`, `.describe()`
- **Operaciones básicas:** Filtros simples y agrupaciones
- **Visualización introductoria:** Gráficos básicos con matplotlib

## Proyecto Integrador

**Nota:** El Bloque 1 no usa datasets externos para el proyecto final. Los estudiantes **crean sus propios datasets** como parte del ejercicio:

- `equipos.csv` - Creado por estudiantes
- `partidos.csv` - Generado durante el proyecto  
- `jugadores.csv` - Desarrollado como entregable

Esta metodología enseña:
1. **Creación de datos estructurados**
2. **Validación de consistencia**
3. **Diseño de esquemas de datos**
4. **Documentación de datasets**

## Características Técnicas

### Validaciones Implementadas
- ✅ **Datos limpios:** Sin valores faltantes o inconsistentes
- ✅ **Tipos apropiados:** Números enteros para goles y partidos
- ✅ **Formato estándar:** Nombres consistentes y encoding UTF-8
- ✅ **Realismo:** Valores aproximados a estadísticas reales 2023-24

### Simplicidad Educativa
- **Pocas columnas:** Fácil de entender y manipular
- **Datos familiares:** Equipos conocidos por estudiantes
- **Operaciones claras:** Cálculos matemáticos simples posibles
- **Sin complejidad:** No requiere conocimiento deportivo avanzado

## Progresión Pedagógica

**Bloque 1 → Bloque 2:**
```
Datos simples → Datos complejos
1 archivo → Múltiples datasets
10 registros → 1,500+ registros  
4 columnas → 20+ variables
```

El dataset del Bloque 1 establece **fundamentos sólidos** que se expanden significativamente en bloques posteriores.

---

**Dataset diseñado específicamente para introducir conceptos de programación sin complejidad técnica innecesaria** 🎯📚

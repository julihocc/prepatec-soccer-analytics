# Caso Práctico Individual - Bloque 3
## Predicción Simple con Datos de Champions League

**Modalidad:** Individual  
**Ponderación:** 20% del Bloque Final (30% del curso)  
**Duración:** 1 semana focal (aplica tras semanas de práctica)  
**Entrega:** Notebook de Jupyter (`caso_bloque3.ipynb`)

---

## Contexto del Problema

Eres analista junior y necesitas entregar un informe breve que combine exploración de datos, visualizaciones básicas y una predicción simple sobre resultados de partidos de Champions League.

**Situación:** Cuentas con un dataset de partidos históricos. Debes entender el comportamiento general (goles, distribución de resultados) y luego construir un modelo sencillo que intente predecir si ganará el equipo local o no.

---

## Propósito
Evaluar de forma individual la integración de:
- Exploración de datos (EDA)
- Preparación simple de variables
- Modelo de predicción básico (clasificación) dentro de los límites del curso
- Interpretación y comunicación de resultados con preguntas socráticas

---

## Objetivos de Aprendizaje

Al finalizar el caso práctico podrás:
- Explorar y limpiar un dataset tabular sencillo
- Generar visualizaciones básicas interpretables
- Crear variables derivadas simples (total de goles, indicador binario, etc.)
- Entrenar un modelo de clasificación básico (RandomForestClassifier) sin hiper‑optimización
- Evaluar precisión y reflexionar sobre limitaciones
- Comunicar hallazgos con lenguaje claro

---

## Dataset Proporcionado

**Archivo principal:** `champions_league_matches.csv` (ubicado en `evaluaciones/bloque-3/datasets/`). Copiar al lado del notebook o ajustar la ruta.

Columnas típicas esperadas (pueden variar ligeramente):
```
equipo_local, equipo_visitante, goles_local, goles_visitante, temporada, fase_competicion,
tiros_local, tiros_visitante, tiros_arco_local, tiros_arco_visitante
```

> Preguntas socráticas iniciales: ¿Qué variable te ayuda primero a entender el ritmo ofensivo? ¿Qué diferencia hay entre total de goles y distribución de goles local/visitante?

---

## Tareas Requeridas

### Parte 1: Exploración y Limpieza (40 puntos)
1.1 Carga y vista rápida (`head()`, forma, tipos).  
1.2 Comprobar valores faltantes y describir su impacto.  
1.3 Crear columna `total_goles` (suma local + visitante).  
1.4 Crear variable objetivo binaria `gana_local` (1 si goles_local > goles_visitante, 0 en caso contrario).  
1.5 Pregunta socrática: ¿Qué sesgo introduce usar solo partidos históricos sin variables de contexto (lesiones, clima)?

### Parte 2: Visualización e Interpretación (35 puntos)
2.1 Gráfico de barras: Top 10 equipos con más goles como local.  
2.2 Histograma: Distribución de `total_goles`.  
2.3 Boxplot (opcional si el tiempo lo permite): Goles locales por fase_competicion.  
2.4 Tabla simple: Porcentaje de victorias locales vs empates vs derrotas.  
2.5 Pregunta socrática: ¿La ventaja de jugar en casa es evidente? ¿Qué indicador lo sostiene?

### Parte 3: Predicción Simple (25 puntos)
3.1 Seleccionar variables numéricas básicas (ej. goles_local promedio histórico del equipo, tiros_local si existe, total_goles).  
3.2 Dividir datos train/test (80/20, random_state=42).  
3.3 Entrenar RandomForestClassifier con parámetros por defecto mínimos.  
3.4 Calcular precisión.  
3.5 Pregunta socrática: ¿El modelo está realmente aprendiendo patrones o solo replicando una frecuencia base?

### Parte 4: Conclusiones y Reflexión (Integrado)
4.1 Resumir 2-3 hallazgos clave del EDA.  
4.2 Explicar en lenguaje sencillo qué significa la precisión obtenida.  
4.3 Identificar una limitación clara del modelo.  
4.4 Proponer una mejora simple (nueva variable o filtrado).  
4.5 Pregunta socrática final: ¿Qué información adicional (no disponible) añadirías para mejorar la predicción y por qué?

---

## Guía de Código Inicial
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

sns.set_theme(style="whitegrid", palette="viridis")

datos = pd.read_csv('champions_league_matches.csv')  # Ajustar ruta si es necesario
print(datos.head())
print(datos.info())

datos['total_goles'] = datos['goles_local'] + datos['goles_visitante']
datos['gana_local'] = (datos['goles_local'] > datos['goles_visitante']).astype(int)

caracteristicas = ['goles_local', 'goles_visitante', 'total_goles']
X = datos[caracteristicas]
y = datos['gana_local']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)
preds = modelo.predict(X_test)
print('Precisión:', accuracy_score(y_test, preds))
```

> Pregunta socrática: Si la mayoría de partidos los gana el local, ¿qué precisión tendría un modelo que siempre predice "gana local"? Compáralo.

---

## Rúbrica (Resumen)
Ver rúbrica completa integrada en `evaluaciones/bloque-3/README.md`.
- Ponderación Notebook (20% curso):
  - Exploración y Limpieza (25%)
  - Modelado Básico (35%)
  - Visualización e Interpretación (25%)
  - Documentación y Código (15%)
- Presentación (10% del curso) separada (explica hallazgos y modelo).

---

## Diferencias con el Proyecto de Contenido Semana 15
| Aspecto | Caso Práctico (evaluaciones) | Proyecto Semana 15 (contenido) |
|---------|------------------------------|--------------------------------|
| Rol | Evidencia evaluativa formal | Actividad de aprendizaje aplicada |
| Estructura | Rúbrica oficial (20% curso) | Guía pedagógica de cierre |
| Alcance ML | Modelo simple | Integración narrativa + práctica guiada |
| Enfoque | Cumplimiento de criterios | Exploración formativa |

---

## Lineamientos Técnicos y Pedagógicos
- Limitar complejidad (RandomForestClassifier por defecto o Regresión Logística opcional).
- No hacer tuning exhaustivo (grid search u optimizaciones complejas excluidas).
- Variables derivadas simples y explicables en < 2 oraciones.
- Mantener preguntas socráticas y reflexiones después de cada bloque.
- Código en español, sin emojis.

---

## Integridad Académica
- Código debe ser 100% entendible por el autor.  
- Declarar uso de herramientas de IA si se emplearon para generación de fragmentos.  
- Evitar copiar soluciones completas; justificar decisiones clave (features, métrica).

---

## Autoevaluación (Checklist Rápido)
- [ ] Cargué y exploré la estructura del dataset
- [ ] Creé columnas `total_goles` y `gana_local`
- [ ] Generé al menos 3 visualizaciones interpretadas
- [ ] Entrené un modelo sencillo y reporté precisión
- [ ] Comparé precisión vs baseline ingenua
- [ ] Escribí conclusiones y una mejora futura
- [ ] Revisé la rúbrica antes de entregar

---

## Registro de Cambios
2025-08-10: Creación inicial para renombrar y clarificar el caso práctico del Bloque 3.  
2025-08-10: Migrados dataset y notebook de solución desde antigua carpeta `proyecto-integrador/` (eliminada).  
2025-08-10: Estructura alineada al formato estándar (Bloques 1 y 2).  
2025-08-10: Ajuste de secciones y tareas para claridad y homogeneidad.

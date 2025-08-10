# Bloque 2: Exploración y Análisis Descriptivo de Datos Deportivos
## Evaluación de Exploración, Calidad, Estadística y Visualización

**Duración:** Semanas 6-10  
**Ponderación:** 35% de la calificación final  
**Enfoque:** Exploración estructural, calidad de datos, estadística descriptiva, métricas de eficiencia y visualización interpretativa básica

---

## Componentes de Evaluación

### Examen Canvas (20% del curso)
**Ubicación:** [canvas/banco-preguntas-bloque2.md](canvas/banco-preguntas-bloque2.md)
- **Banco actual:** 75 preguntas (Núcleo). Próxima ampliación: Extended con ítems [S].
- **Formato:** ~70% opción múltiple / ~30% numéricas (tolerancia 5%).
- **Selección fija:** 22 preguntas (muestreo estratificado cognitivo).
- **Distribución cognitiva objetivo:** [R] 7-8, [C] 7-8, [A] 5-6, [S] 1-2 (hasta ampliar banco: 0-1 placeholder [S]).
- **Tiempo:** 50 minutos.
- **Cobertura temática (20% c/u):** Exploración estructural y calidad, estadística descriptiva, métricas derivadas (goles_por_partido, contribucion_ofensiva), agrupaciones + outliers simples, visualización e interpretación básica.
- **Segmentación futura:** Añadir Extended (interpretación y decisiones tácticas) sin renumerar Núcleo.
- **Control de calidad:** Verificar conteo de etiquetas antes de publicar evaluación.

### Caso Práctico Colaborativo (15% del curso)
**Ubicación:** [caso-practico/caso-bloque2.md](caso-practico/caso-bloque2.md)
- **Proyecto:** "Análisis Básico, Calidad y Eficiencia de Jugadores" (Actualizado v2).
- **Equipos:** 2-3 estudiantes.
- **Duración:** 1 semana.
- **Entregables:** Notebook (exploración, calidad, métricas, outliers, visualizaciones, síntesis) + Presentación breve (3-4 diapositivas).
- **Enfoque:** Profundizar en limpieza simple, estadística descriptiva e interpretación de métricas de eficiencia sin herramientas avanzadas.

### Sistema de Evaluación
**Ubicación:** [rubricas/README.md](rubricas/README.md)
- **Rúbrica caso 40/30/30** (Exploración-Calidad / Análisis-Métricas / Visualización-Interpretación).
- **Distribución cognitiva examen** documentada con metas por etiqueta.
- **Competencias transversales** (interpretación y comunicación) integradas.
- **Progresión pedagógica** coherente con Bloque 1 y puente hacia fundamentos de modelado (Bloque 3 Semana 11).

---

## Objetivos de Aprendizaje

### Competencias de Exploración
- **Carga de datos CSV:** Lectura, inspección inicial (`head`, `info`).
- **Calidad básica:** Tipos, valores faltantes, rangos simples.
- **Validación mínima:** Detección de inconsistencias sencillas (edades fuera de rango, valores negativos imposibles).
- **Métricas derivadas básicas:** `goles_por_partido`, `contribucion_ofensiva`.

### Competencias Estadísticas  
- **Descriptiva esencial:** Media, mediana, desviación estándar, conteos.
- **Distribuciones simples:** Histogramas y boxplots básicos.
- **Segmentación:** Agrupaciones por posición (groupby) y comparación de promedios.
- **Variabilidad:** Observación de dispersión sin pruebas formales.

### Competencias de Visualización
- **Seaborn básico:** Barras, caja, dispersión, histograma.
- **Configuración estética uniforme:** Paleta `viridis`, títulos y ejes claros.
- **Comparación visual:** Patrones entre posiciones y métricas derivadas.
- **Interpretación breve:** Texto inmediato tras cada gráfico.

### Competencias Analíticas
- **Interpretación focalizada:** Explicar qué indica una diferencia de promedio.
- **Contexto futbolístico básico:** Relevancia de métricas para roles (delantero vs defensa).
- **Pensamiento crítico inicial:** Evaluar impacto de un outlier.
- **Comunicación clara:** Síntesis en 3-5 conclusiones accionables sencillas.

---

## Cronograma de Evaluación (Propuesto)

### Semana 9: Preparación
- **Canvas:** Habilitar práctica con banco Núcleo (restringir Extended hasta ampliación).
- **Formación de equipos:** Confirmar 2-3 integrantes.
- **Repaso:** Sesión guiada de estadística descriptiva.

### Semana 10: Evaluaciones
- **Examen Canvas:** Ventana Lunes-Martes (22 ítems, 50 min).
- **Lanzamiento caso práctico:** Martes posterior al examen.
- **Checkpoint interno:** Jueves (exploración + métricas derivadas listas).
- **Entrega:** Viernes (notebook y presentación). Presentaciones breves mismo día.

---

## Criterios de Éxito (Alineados a Rúbrica 40/30/30)

### Suficiente (70-79%)
- Exploración estructural y estadísticas básicas correctas.
- Visualizaciones mínimas presentes con títulos simples.
- Interpretaciones breves pero correctas.

### Competente (80-89%)
- Calidad revisada (rangos, NA) y métricas derivadas correctas.
- Visualizaciones claras y ordenadas; respuestas a preguntas socráticas.
- Conclusiones conectan métricas con roles de posición.

### Sobresaliente (90-100%)
- Outliers evaluados con criterio y justificación.
- Métricas derivadas usadas para recomendaciones concretas.
- Síntesis final clara: priorización y recomendación para entrenador.

---

## Alcance de Análisis Requerido (Ajustado al Nivel)

### Rendimiento de Jugadores
- Promedios por posición (goles, asistencias, partidos jugados).
- Métricas derivadas simples (goles_por_partido, contribucion_ofensiva).
- Identificación de top 3 por contribución.

### Calidad y Dispersión
- Revisión de tipos y NA.
- Detección sencilla de outliers (media + 2*std) y reflexión.

### Visualización
- Barras, caja, dispersión, histograma.
- Comparación clara entre posiciones.

---

## Herramientas y Tecnologías (Limitadas al Alcance)

### Stack Necesario
- pandas (agrupaciones, agregaciones básicas).
- seaborn (barras, boxplot, scatter, histograma).
- matplotlib (ajustes menores de etiquetas).

### Datasets
- CSV único con jugadores juveniles (columnas: goles, asistencias, partidos, edad, posición).
- Tamaño pequeño para ejecución rápida en clase.

### Entorno
- Jupyter Notebook estándar.
- Sin dashboards ni interactividad avanzada en este bloque.

---

## Preparación Focalizada

### Para Examen Canvas
1. Practicar exploración: `head`, `info`, dtypes, NA.
2. Repasar fórmulas de media, mediana, desviación (interpretación simple).
3. Ejercitar groupby para promedios por posición.
4. Comprender cuándo usar cada visualización básica.
5. Interpretar un outlier y su efecto en el promedio.

### Para Caso Práctico
1. Dividir tareas: exploración/calidad, métricas/outliers, visualizaciones/síntesis.
2. Preparar plantilla de conclusiones (5 preguntas clave del caso).
3. Ensayar explicación de una métrica derivada en <30 segundos.
4. Verificar ejecución completa antes de preparar presentación.
5. Documentar decisiones (por qué se mantiene o no un outlier).

---

## Conexión Progresiva

Este bloque crea las bases prácticas (limpieza ligera, métricas descriptivas e interpretación) necesarias antes de introducir modelos predictivos simples en Bloque 3. Se evita deliberadamente complejidad (dashboards, métricas avanzadas) para asegurar comprensión sólida.

---

*Este bloque consolida la transición de fundamentos Python (Bloque 1) a análisis estructurado de datos, preparando al estudiante para el modelado introductorio del Bloque 3 sin sobrecargar con herramientas avanzadas prematuras.*
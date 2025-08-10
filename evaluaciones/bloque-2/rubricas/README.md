# Rúbricas de Evaluación - Bloque 2
## Exploración, Calidad, Métricas Derivadas e Interpretación

**Ponderación del Bloque:** 35% de la calificación final  
**Componentes:** Examen Canvas (20%) + Caso Práctico Colaborativo (15%)

---

## Examen Canvas (20% de la calificación total)

### Configuración Automática
- **Preguntas totales actuales:** 75 (Núcleo). Próxima ampliación: Extended (interpretación [S])
- **Preguntas por examen:** 22 (mezcla balanceada de etiquetas)
- **Tiempo límite:** 50 minutos
- **Intentos:** 1 único intento
- **Calificación:** Automática, 100 puntos

### Distribución Cognitiva Objetivo por Examen
- [R] 7-8 (recordar funciones básicas y sintaxis)
- [C] 7-8 (interpretar fragmentos, elegir función correcta)
- [A] 5-6 (aplicar en mini escenarios con datos futbolísticos)
- [S] 1-2 (se activará cuando exista banco Extended; temporalmente 0-1 placeholder)

### Distribución por Temas (alineada a semanas 6–10):
| Tema | % del Examen | Preguntas |
|------|--------------|-----------|
| Exploración estructural y calidad (head, info, dtypes, NA) | 20% | 4-5 |
| Estadística descriptiva (media, mediana, std) | 20% | 4-5 |
| Métricas derivadas (goles_por_partido, contribucion_ofensiva) | 20% | 4-5 |
| Agrupaciones e interpretación (groupby, outliers simples) | 20% | 4-5 |
| Visualización e interpretación básica | 20% | 4-5 |

Nota: Al ampliarse el banco se integrarán preguntas [S] sobre decisiones tácticas basadas en métricas.

---

## Caso Práctico Colaborativo (15% de la calificación total)

### "Análisis Básico, Calidad y Eficiencia de Jugadores" (Actualizado v2)
**Modalidad:** Equipos de 2-3 estudiantes  
**Duración:** 1 semana

Rúbrica actualizada (ver documento del caso) alineada 40/30/30.

### Rúbrica 40 / 30 / 30 (100 puntos)

| Área | Puntos | Subcomponentes | Indicadores clave |
|------|--------|----------------|-------------------|
| Exploración y Calidad | 40 | Carga (5) + Exploración head/info (10) + Calidad (NA, rangos, tipos) (10) + Estadística descriptiva (media/mediana/std) (15) | `.info()`, dtypes revisados, interpretación media vs mediana |
| Análisis y Métricas | 30 | Groupby posiciones (12) + Métricas derivadas (10) + Outliers simples (8) | `goles_por_partido`, `contribucion_ofensiva`, criterio de outliers documentado |
| Visualización e Interpretación | 30 | Gráficos base (10) + Profundización (10) + Síntesis/Presentación (10) | Gráficos limpios, respuestas socráticas, recomendaciones futbolísticas |

Niveles de desempeño:
- Excelente: Completo, decisiones justificadas con métricas.
- Bueno: 1–2 omisiones menores, interpretación razonable.
- Suficiente: Falta una métrica derivada u outliers, interpretación superficial.
- Insuficiente: Errores que impiden análisis o falta de justificación.

Requisitos para nivel Excelente (transversales):
- Variables en español y descriptivas.
- Comentarios en pasos críticos (por qué la métrica, por qué se mantiene un outlier).
- Preguntas socráticas respondidas.
- Notebook ejecuta limpio desde reinicio.

---

## Escala de Calificación del Bloque

### Conversión Final (35% del curso):
- **Examen Canvas:** 20% × (calificación/100)
- **Caso Práctico:** 15% × (calificación/100)
- **Total Bloque 2:** Suma de ambos componentes

### Niveles de Dominio (aplican a ambos componentes):
- Excelente (90-100%): Criterios completos + interpretaciones conectadas a decisiones prácticas.
- Competente (80-89%): 1–2 omisiones menores, lógica general correcta.
- Suficiente (70-79%): Cumple mínimos, interpretación limitada.
- Insuficiente (<70%): Faltan partes clave o errores que impiden comprensión.

---

## Criterios Específicos de Evaluación

### ¿Qué Busco en el Código?
- Ejecución limpia sin errores.
- Funciones vistas: `.head()`, `.info()`, `.describe()`, `.groupby()`, `.value_counts()`, creación de métricas derivadas.
- Validaciones básicas (rangos, NA, tipos).
- Variables en español (`datos_jugadores`, `goles_por_partido`).
- Comentarios que justifican decisiones (no redundantes).

### ¿Qué Busco en los Gráficos?
- Base: barras por posición, caja de goles, dispersión goles vs asistencias.
- Profundización: top 5, eficiencia, distribución edades.
- Títulos informativos, ejes claros, orden lógico.
- Paleta `viridis` configurada globalmente.
- Interpretación breve justo después de cada figura.

### ¿Qué Busco en el Trabajo en Equipo?
- Participación equitativa.
- División clara de roles reflejada en comentarios o presentación.
- Integración de estilos (uniformidad en nombres y formato de celdas).

---

## Entregables Específicos

### Caso Práctico Bloque 2:
1. **analisis_jugadores_equipo[X].ipynb** (incluye calidad, métricas, outliers, interpretación)
2. **presentacion_equipo[X].pdf** (3–4 diapositivas con decisiones justificadas)

### Lo que Debe Funcionar:
- Notebook ejecutable extremo a extremo.
- Análisis incluye exploración estructural, calidad, estadística, métricas derivadas, outliers y síntesis.
- Presentación comunica decisiones (no repite tablas).
- Trabajo colaborativo visible.

---

*Este bloque evalúa la capacidad de explorar y validar datos, calcular estadística descriptiva y métricas de eficiencia, visualizar e interpretar para apoyar decisiones futbolísticas.*
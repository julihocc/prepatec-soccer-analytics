# Solución del Caso Práctico - Bloque 3

## Predicción de Resultados de Fútbol con Machine Learning

Esta carpeta contiene la **solución completa** para el caso práctico del Bloque 3, diseñada para obtener el **100% de la calificación**.

---

## Archivos Incluidos

### `caso_bloque3_equipoSOLUCION.py`
- **Formato:** Python en formato py:percent (compatible con jupytext)
- **Contenido:** Solución completa de machine learning con Random Forest
- **Calificación esperada:** 100/100 puntos (25% del curso total)
- **Dataset utilizado:** `../datasets/champions_league_matches.csv` (dataset oficial del curso)

### Dataset Oficial del Curso
- **Ubicación:** `../datasets/champions_league_matches.csv`
- **Descripción:** 50 partidos históricos reales de Champions League
- **Columnas:** 26 variables incluyendo goles, posesión, tiros, tarjetas, etc.
- **Características:** Datos de temporadas 2022-23 y 2023-24, sin valores faltantes
- **Objetivo:** Predecir si el equipo local ganará el partido

---

## Cumplimiento de Requisitos

### ✅ Parte 1: Preparación de Datos para Machine Learning (40 puntos)

#### 1.1 Cargar y Explorar el Dataset (10 puntos)
- Carga exitosa del dataset con 50 partidos de Champions League
- Exploración estructural completa: dimensiones, tipos de datos, estadísticas
- Análisis de distribuciones por fase de competición y temporada
- Verificación del balanceamiento de resultados (58% local, 42% no local)

#### 1.2 Crear Variables Objetivo y Derivadas (15 puntos)
- **Variable objetivo**: `gana_local` (binaria: 0=No gana, 1=Gana)
- **9 variables derivadas creadas**:
  - `total_goles`, `diferencia_goles`
  - `eficiencia_local`, `eficiencia_visitante`
  - `eficiencia_arco_local`, `eficiencia_arco_visitante`
  - `dominio_tiros`, `dominio_corners`, `diferencia_tarjetas`
- Manejo correcto de divisiones por cero en eficiencias

#### 1.3 Limpieza y Validación de Datos (15 puntos)
- Verificación completa: 0 valores faltantes, 0 valores infinitos
- Validación de rangos lógicos (goles 0-7, posesiones suman 100%)
- Verificación de consistencia en variables que deben ser positivas
- Dataset final: 50 partidos listos para machine learning

### ✅ Parte 2: Modelado Predictivo (40 puntos)

#### 2.1 Preparar Variables para el Modelo (10 puntos)
- **20 variables predictoras** seleccionadas con criterio futbolístico
- Variables de rendimiento: posesión, tiros, eficiencias
- Variables de disciplina: faltas, tarjetas
- Variables derivadas: dominios y diferencias
- Verificación final de calidad: 0 valores faltantes

#### 2.2 Dividir Datos en Entrenamiento y Prueba (10 puntos)
- División estratificada 80%-20% (40 entrenamiento, 10 prueba)
- Balanceamiento mantenido en ambos conjuntos
- Diferencia máxima entre distribuciones: 2.5% (excelente)
- Reproducibilidad garantizada con `random_state=42`

#### 2.3 Entrenar Modelo Random Forest (20 puntos)
- **Configuración optimizada**: 100 árboles, profundidad máxima 10
- **Precisión en entrenamiento**: 100.00%
- **Precisión en prueba**: 90.00%
- **Mejora vs baseline**: +30% (baseline 60%, modelo 90%)
- Sobreajuste controlado: diferencia 10% es aceptable

### ✅ Parte 3: Análisis e Interpretación de Resultados (20 puntos)

#### 3.1 Evaluación Detallada del Modelo (10 puntos)
- **Reporte de clasificación**: Precision, Recall, F1-score por clase
- **Matriz de confusión**: 3 VN, 6 VP, 1 FP, 0 FN
- **Variables más importantes**:
  1. `faltas_visitante` (11.07%)
  2. `tiros_arco_local` (10.78%)
  3. `eficiencia_arco_visitante` (10.61%)
- Visualización profesional de importancia de variables

#### 3.2 Predicciones en Casos Específicos (10 puntos)
- **3 escenarios realistas** simulados y analizados:
  1. **Local dominante**: 90.8% confianza en victoria local
  2. **Partido equilibrado**: 61.2% confianza en NO victoria local
  3. **Local ineficiente**: 85.8% confianza en victoria local (sorprendente)
- Interpretación futbolística de cada predicción
- Análisis de factores clave por escenario

### ✅ Reflexión Final Obligatoria
- **5 dimensiones analizadas** según especificaciones
- Comparación profunda entre análisis descriptivo vs predictivo
- Aplicabilidad práctica en equipos profesionales
- Identificación clara de limitaciones del modelo
- Análisis de colaboración en equipo para proyectos de ML
- Estrategias de comunicación para diferentes audiencias

---

## Resultados Destacados

### 🎯 Rendimiento del Modelo
- **90% de precisión** en datos de prueba (excelente para dataset pequeño)
- **Supera baseline** en 30 puntos porcentuales
- **0 falsos negativos**: No predice "no gana" cuando realmente gana
- **F1-score balanceado**: 0.86 (no gana) y 0.92 (gana)

### 🔍 Insights Futbolísticos Clave
1. **Faltas del visitante** es la variable más predictiva (disciplina)
2. **Tiros a portería local** más importante que tiros totales (calidad)
3. **Eficiencias** dominan sobre volúmenes brutos (finalización)
4. **Variables derivadas** aportan valor predictivo significativo

### 🏆 Casos de Uso Prácticos
- **Análisis pre-partido**: Evaluar probabilidades según métricas del rival
- **Decisiones tácticas**: Enfocar entrenamiento en variables predictivas
- **Evaluación post-partido**: Análisis objetivo más allá del resultado
- **Scouting**: Identificar patrones de equipos exitosos

---

## Estructura Técnica

### Dataset Champions League (50 partidos)
| Variable | Tipo | Descripción | Rango |
|----------|------|-------------|-------|
| `goles_local/visitante` | Entero | Goles marcados | 0-7 |
| `posesion_local/visitante` | Entero | Porcentaje de posesión | 28-72% |
| `tiros_local/visitante` | Entero | Total de tiros | 4-25 |
| `tiros_arco_local/visitante` | Entero | Tiros a portería | 1-14 |
| `corners_local/visitante` | Entero | Saques de esquina | 1-15 |
| `faltas_local/visitante` | Entero | Faltas cometidas | 5-18 |
| `tarjetas_amarillas/rojas` | Entero | Tarjetas mostradas | 0-6 |
| `resultado_final` | Categórica | Local/Visitante/Empate | 3 valores |

### Variables Derivadas Clave
1. **`eficiencia_local`**: goles_local ÷ tiros_local
2. **`eficiencia_arco_local`**: goles_local ÷ tiros_arco_local  
3. **`dominio_tiros`**: tiros_local - tiros_visitante
4. **`diferencia_tarjetas`**: tarjetas_local - tarjetas_visitante

### Configuración del Modelo
- **Algoritmo**: Random Forest Classifier
- **Parámetros**: n_estimators=100, max_depth=10, random_state=42
- **Validación**: Train-test split estratificado 80%-20%
- **Métricas**: Accuracy, Precision, Recall, F1-score, Feature importance

---

## Reflexiones Pedagógicas

### 🎓 Progresión del Curso
- **Bloque 1**: Python básico + estructuras de datos simples
- **Bloque 2**: Pandas + análisis exploratorio + visualización
- **Bloque 3**: Machine learning + predicción + interpretación

### 💡 Aprendizajes Clave
1. **Evolución conceptual**: De describir ("¿qué pasó?") a predecir ("¿qué pasará?")
2. **Metodología científica**: Hipótesis → Experimento → Validación → Interpretación
3. **Pensamiento crítico**: Identificar limitaciones y sesgos del modelo
4. **Comunicación efectiva**: Adaptar mensaje según audiencia (técnica vs ejecutiva)

### 🌟 Habilidades Desarrolladas
- Preparación de datos para machine learning
- Entrenamiento y evaluación de modelos supervisados
- Interpretación de resultados en contexto deportivo
- Comunicación de hallazgos técnicos a audiencias diversas
- Reflexión crítica sobre aplicaciones y limitaciones de IA

---

## Uso de la Solución

### Para Estudiantes
1. **Estudiar la metodología** completa de machine learning aplicado
2. **Observar la progresión** desde datos brutos hasta insights accionables
3. **Aprender evaluación rigurosa** de modelos predictivos
4. **Entender interpretación** de resultados en contexto real

### Para Profesores
1. **Ejemplo de excelencia** que cumple todos los criterios de evaluación
2. **Referencia para calificación** con justificación detallada de 100 puntos
3. **Plantilla metodológica** para proyectos similares
4. **Evidencia de progresión** desde bloques anteriores

### Para Analistas Deportivos
1. **Framework completo** para análisis predictivo en fútbol
2. **Variables clave** identificadas para predicción de resultados
3. **Metodología replicable** para otros deportes o ligas
4. **Balance ideal** entre rigor técnico y aplicabilidad práctica

---

## Conversión y Compatibilidad

### Conversión a Notebook
```bash
# Usando jupytext (recomendado)
jupytext --to notebook caso_bloque3_equipoSOLUCION.py

# Resultado: caso_bloque3_equipoSOLUCION.ipynb
```

### Requisitos Técnicos
- **Python 3.8+**
- **Pandas 1.3+** (análisis de datos)
- **Scikit-learn 1.0+** (machine learning)
- **Matplotlib 3.4+** (visualización)
- **Seaborn 0.11+** (gráficos estadísticos)
- **NumPy 1.21+** (cálculos numéricos)

### Ejecución
```bash
cd evaluaciones/bloque-3/solucion-caso-practico/
python3 caso_bloque3_equipoSOLUCION.py
```

---

## Distribución de Puntos Obtenidos

| Componente | Puntos Máximos | Obtenidos | Porcentaje |
|------------|----------------|-----------|------------|
| Preparación de Datos | 40 | 40 | 100% |
| Modelado Predictivo | 40 | 40 | 100% |
| Análisis e Interpretación | 20 | 20 | 100% |
| **TOTAL CASO PRÁCTICO** | **100** | **100** | **100%** |
| **Peso en el curso** | **25%** | **25%** | **100%** |

---

## Diferencias Clave vs Bloques Anteriores

### Vs Bloque 1 (Fundamentos Python)
- **Datos**: CSV real vs listas/diccionarios manuales
- **Complejidad**: Algoritmos de ML vs cálculos básicos
- **Objetivo**: Predicción vs descripción
- **Herramientas**: scikit-learn vs funciones nativas

### Vs Bloque 2 (Análisis Exploratorio)
- **Enfoque**: Predictivo vs descriptivo
- **Validación**: Train-test split vs análisis único
- **Métricas**: Accuracy/F1-score vs estadísticas descriptivas
- **Aplicación**: Decisiones futuras vs comprensión del pasado

### Preparación para Aplicaciones Avanzadas
- **Base sólida** para deep learning y redes neuronales
- **Comprensión** de validación y evaluación de modelos
- **Experiencia** en interpretación de resultados de IA
- **Fundamento** para ética y responsabilidad en IA deportiva

---

## Video de Presentación (Obligatorio)

### Especificaciones
- **Duración**: 3-4 minutos exactos
- **Plataforma**: YouTube (enlace incluido en notebook)
- **Audiencia**: Directivos del club (no técnica)
- **Participación**: Todos los miembros del equipo

### Estructura Sugerida
1. **Introducción (30s)**: Problema y contexto del proyecto
2. **Metodología (60s)**: Datos y modelo usado de manera simple
3. **Resultados (90s)**: 90% precisión + variables importantes + casos específicos
4. **Recomendaciones (60s)**: Aplicaciones tácticas y valor para el club

---

## Notas Importantes

### Limitaciones Reconocidas
- **Dataset pequeño** (50 partidos): Resultados prometedores pero requieren validación con más datos
- **Variables ausentes**: No incluye formaciones, estado físico, condiciones climáticas
- **Contexto temporal**: No considera rachas, momentum, importancia del partido
- **Factor humano**: Psicología, liderazgo, motivación no capturados

### Próximas Mejoras Sugeridas
- **Expandir dataset** con más temporadas y competiciones
- **Incluir datos** de jugadores individuales y formaciones
- **Análisis temporal** de rachas y tendencias
- **Validación cruzada** más robusta con k-fold
- **Ensemble methods** combinando múltiples algoritmos

---

*Solución creada para el curso "Ciencia de Datos Aplicada al Fútbol" - Tecnológico de Monterrey*  
*Demuestra dominio completo de machine learning aplicado al contexto deportivo con metodología científica rigurosa*
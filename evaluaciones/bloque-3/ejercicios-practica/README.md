# Ejercicios de Práctica - Bloque 3: Mi Primera Predicción con Datos de Fútbol

**Curso:** Introducción a Data Science con Fútbol  
**Bloque:** 3 - Machine Learning y Predicción  
**Peso en calificación:** 25% del Bloque 3  
**Modalidad:** Práctica autónoma con soporte docente

## Información General

Los ejercicios de práctica están diseñados para **reforzar y ampliar** las competencias desarrolladas en los ejercicios semanales, proporcionando oportunidades adicionales de experimentación y aprendizaje autónomo en machine learning aplicado a datos deportivos.

### Objetivos de los Ejercicios de Práctica

1. **Experimentación libre** con técnicas de machine learning avanzadas
2. **Práctica adicional** en áreas donde el estudiante identifique debilidades
3. **Exploración de técnicas** no cubiertas completamente en ejercicios semanales
4. **Desarrollo de portfolio** personal de proyectos de data science
5. **Preparación intensiva** para el proyecto final del bloque

### Estructura y Flexibilidad

- **4 ejercicios prácticos** con diferentes niveles de dificultad
- **Elección libre**: Estudiantes eligen 3 de 4 ejercicios según sus intereses
- **Ritmo personalizado**: Plazos flexibles con entregas escalonadas
- **Soporte continuo**: Mentorías semanales opcionales
- **Evaluación formativa**: Enfoque en aprendizaje más que calificación

---

## Ejercicio de Práctica 1: Experimentación con Algoritmos Avanzados

### Descripción
Implementa y compara algoritmos de machine learning no cubiertos en profundidad en las semanas regulares, explorando su aplicabilidad específica a datos de fútbol.

### Objetivos de Aprendizaje
- Explorar algoritmos avanzados como XGBoost, LightGBM, CatBoost
- Implementar redes neuronales básicas para clasificación
- Comparar rendimiento con métodos tradicionales
- Analizar cuándo usar cada tipo de algoritmo

### Datasets Proporcionados
- `futbol_algoritmos_avanzados.csv`: 1,500 partidos con 40+ variables
- `jugadores_metricas_detalladas.csv`: Estadísticas avanzadas de 150 jugadores
- `equipos_rendimiento_historico.csv`: Datos históricos de 30 equipos

### Tareas Específicas

#### Parte A: Gradient Boosting Avanzado (40%)
1. **Implementación de XGBoost**
   - Configura XGBoost para predicción de resultados
   - Optimiza hiperparámetros usando Bayesian Optimization
   - Analiza importancia de features con SHAP values
   - Compara con Random Forest y Logistic Regression

2. **LightGBM para datos categóricos**
   - Implementa LightGBM con categorical features nativas
   - Analiza velocidad de entrenamiento vs precisión
   - Optimiza memory usage para datasets grandes
   - Implementa early stopping para prevenir overfitting

#### Parte B: Redes Neuronales Básicas (35%)
1. **Perceptron Multicapa**
   - Diseña red neuronal simple (2-3 capas ocultas)
   - Experimenta con diferentes activation functions
   - Implementa regularización (dropout, batch normalization)
   - Compara con algoritmos tradicionales

2. **Análisis de arquitectura**
   - Experimenta con diferentes números de neuronas
   - Analiza curvas de loss durante entrenamiento
   - Implementa callbacks para monitoring
   - Evalúa interpretabilidad vs performance

#### Parte C: Comparación Sistemática (25%)
1. **Benchmarking completo**
   - Compara todos los algoritmos implementados
   - Usa validación cruzada temporal consistente
   - Analiza trade-offs entre velocidad y precisión
   - Documenta cuándo usar cada algoritmo

2. **Análisis de casos específicos**
   - Identifica scenarios donde cada algoritmo excede
   - Analiza comportamiento con datos desbalanceados
   - Evalúa robustez ante outliers
   - Documenta recomendaciones prácticas

### Entregables
- **Notebook comparativo**: Implementación y análisis de todos los algoritmos
- **Reporte de benchmarking**: Comparación sistemática con recomendaciones
- **Código modular**: Funciones reutilizables para cada algoritmo
- **Visualizaciones**: Gráficos de performance y interpretabilidad

### Criterios de Evaluación
- **Implementación correcta** (40%): Algoritmos funcionando sin errores
- **Análisis comparativo** (30%): Comparación sistemática y insights
- **Interpretabilidad** (20%): Análisis de por qué funcionan los modelos
- **Documentación** (10%): Código limpio y explicaciones claras

---

## Ejercicio de Práctica 2: Feature Engineering Avanzado y Selección Automática

### Descripción
Desarrolla técnicas avanzadas de ingeniería de características específicas para datos deportivos, implementando métodos automáticos de selección y creación de variables.

### Objetivos de Aprendizaje
- Crear features complejas específicas para fútbol
- Implementar métodos automáticos de feature selection
- Desarrollar pipelines de transformación robustos
- Analizar impacto cuantitativo de diferentes tipos de features

### Datasets Proporcionados
- `partidos_completos_temporales.csv`: Datos temporales detallados
- `jugadores_eventos_partido.csv`: Eventos individuales por jugador
- `equipos_tacticas_formaciones.csv`: Datos tácticos y formaciones
- `factores_contextuales_extendidos.csv`: Variables contextuales amplias

### Tareas Específicas

#### Parte A: Feature Engineering Deportivo (50%)
1. **Variables de momentum y forma**
   - Crea variables de racha (últimos 3, 5, 10 partidos)
   - Implementa weighted moving averages por rendimiento
   - Desarrolla métricas de consistency (varianza de rendimiento)
   - Crea features de improvement trend (tendencia de mejora)

2. **Variables de contexto y presión**
   - Desarrolla métricas de importancia del partido
   - Crea features de pressure situations (situaciones de presión)
   - Implementa variables de rivalidad histórica
   - Desarrolla métricas de expectativa vs realidad

3. **Variables de interacción compleja**
   - Crea features de interacción entre equipos específicos
   - Desarrolla métricas de match-up favorability
   - Implementa variables de adaptación táctica
   - Crea features de factor cancha específicos

#### Parte B: Selección Automática de Features (30%)
1. **Métodos univariantes**
   - Implementa chi-square test para features categóricas
   - Usa mutual information para features continuas
   - Aplica ANOVA F-test para comparación de grupos
   - Compara resultados de diferentes métodos

2. **Métodos multivariantes**
   - Implementa Recursive Feature Elimination (RFE)
   - Usa LASSO regularization para selección automática
   - Implementa Random Forest feature importance
   - Aplica Boruta algorithm para selección robusta

#### Parte C: Pipeline de Transformación (20%)
1. **Preprocessing automatizado**
   - Desarrolla pipeline completo de transformación
   - Implementa manejo automático de missing values
   - Crea transformaciones específicas por tipo de variable
   - Implementa validation de consistencia de datos

2. **Optimización de pipeline**
   - Optimiza orden de transformaciones
   - Implementa caching para operaciones costosas
   - Desarrolla sistema de rollback para errores
   - Crea logging detallado de transformaciones

### Entregables
- **Librería de features**: Módulo Python con funciones de feature engineering
- **Pipeline automatizado**: Sistema completo de transformación
- **Análisis de impacto**: Documento analizando efectividad de cada tipo de feature
- **Casos de estudio**: Ejemplos específicos donde nuevas features mejoran predicción

### Criterios de Evaluación
- **Creatividad en features** (35%): Originalidad y relevancia deportiva
- **Implementación técnica** (25%): Código eficiente y robusto
- **Impacto medible** (25%): Mejoras cuantificables en modelos
- **Reusabilidad** (15%): Código modular y documentado

---

## Ejercicio de Práctica 3: Sistemas de Ensemble y Meta-Learning

### Descripción
Implementa técnicas avanzadas de ensemble learning y meta-learning para crear sistemas de predicción robustos que combinen múltiples modelos efectivamente.

### Objetivos de Aprendizaje
- Implementar diferentes tipos de ensemble methods
- Desarrollar sistemas de meta-learning para combinar predictores
- Analizar trade-offs entre diversidad y precisión en ensembles
- Crear sistemas de voting inteligentes

### Datasets Proporcionados
- `predicciones_multiples_modelos.csv`: Predicciones de 10 modelos base
- `metadatos_partidos.csv`: Información contextual para meta-learning
- `rendimiento_historico_modelos.csv`: Performance histórica de modelos
- `partidos_validacion_ensemble.csv`: Datos para validar ensembles

### Tareas Específicas

#### Parte A: Ensemble Methods Básicos (35%)
1. **Voting ensembles**
   - Implementa hard voting para clasificación
   - Desarrolla soft voting con weighted probabilities
   - Experimenta con diferentes esquemas de weights
   - Analiza cuándo voting mejora performance individual

2. **Bagging avanzado**
   - Implementa bagging con diferentes tipos de sampling
   - Experimenta con feature bagging además de row bagging
   - Desarrolla out-of-bag error estimation
   - Analiza bias-variance trade-off en bagging

#### Parte B: Stacking y Meta-Learning (40%)
1. **Stacking implementation**
   - Implementa 2-level stacking con cross-validation
   - Experimenta con diferentes meta-learners
   - Desarrolla feature engineering para meta-level
   - Previene data leakage en stacking

2. **Meta-learning avanzado**
   - Implementa dynamic ensemble selection
   - Desarrolla context-aware model selection
   - Crea meta-features basadas en características del partido
   - Implementa learning to rank para ensemble weights

#### Parte C: Ensemble Optimization (25%)
1. **Diversity optimization**
   - Implementa métricas de diversity entre modelos
   - Optimiza trade-off entre accuracy y diversity
   - Desarrolla algoritmos de model selection para ensembles
   - Analiza correlación entre errores de modelos

2. **Adaptive ensembles**
   - Implementa ensembles que se adaptan por tipo de partido
   - Desarrolla system para re-weighting dinámico
   - Crea monitoring de degradation de ensemble
   - Implementa sistema de retraining automático

### Entregables
- **Sistema de ensemble**: Pipeline completo de ensemble learning
- **Meta-learner**: Sistema inteligente de combinación de modelos
- **Análisis de diversidad**: Estudio de trade-offs en ensemble design
- **Dashboard de monitoring**: Herramienta para monitorear ensemble performance

### Criterios de Evaluación
- **Sofisticación técnica** (40%): Complejidad y correctness de implementación
- **Mejoras de performance** (30%): Gains measurables sobre modelos individuales
- **Análisis teórico** (20%): Comprensión de por qué funcionan los ensembles
- **Herramientas prácticas** (10%): Utilidad de sistemas desarrollados

---

## Ejercicio de Práctica 4: Análisis de Interpretabilidad y Explicabilidad

### Descripción
Desarrolla técnicas avanzadas para interpretar y explicar modelos de machine learning en el contexto deportivo, creando herramientas para comunicar insights a stakeholders no técnicos.

### Objetivos de Aprendizaje
- Implementar técnicas de interpretabilidad global y local
- Desarrollar visualizaciones efectivas para explicar modelos
- Crear narrativas comprensibles sobre decisiones del modelo
- Analizar sesgos y limitaciones de modelos en contextos deportivos

### Datasets Proporcionados
- `modelos_entrenados_pickles/`: Modelos pre-entrenados para análisis
- `casos_estudio_interpretabilidad.csv`: Casos específicos para análisis detallado
- `stakeholder_questions.json`: Preguntas típicas de diferentes audiencias
- `sesgo_evaluacion_datos.csv`: Datos para análisis de bias

### Tareas Específicas

#### Parte A: Interpretabilidad Global (40%)
1. **Feature importance avanzado**
   - Implementa permutation importance para diferentes métricas
   - Desarrolla feature importance stability analysis
   - Crea visualizaciones de importancia por contexto
   - Analiza consistencia de importancia entre modelos

2. **Análisis de interacciones**
   - Implementa H-statistic para medir interacciones
   - Desarrolla visualizaciones de partial dependence plots
   - Crea accumulated local effects plots
   - Analiza feature interactions específicas del fútbol

#### Parte B: Interpretabilidad Local (35%)
1. **LIME implementation**
   - Implementa LIME para instancias específicas
   - Adapta LIME para features deportivas específicas
   - Desarrolla estrategias de perturbation apropiadas
   - Crea visualizaciones intuitivas de explicaciones LIME

2. **SHAP values avanzado**
   - Implementa SHAP para diferentes tipos de modelos
   - Desarrolla explicaciones de fuerza (force plots)
   - Crea summary plots por diferentes segmentos
   - Implementa SHAP interaction values

#### Parte C: Comunicación y Narrativa (25%)
1. **Dashboards interactivos**
   - Desarrolla dashboard para explorar interpretabilidad
   - Crea interfaces específicas para diferentes stakeholders
   - Implementa explanations adaptadas por audiencia
   - Desarrolla templates de reportes automáticos

2. **Análisis de sesgos**
   - Implementa detección de bias en modelos
   - Analiza fairness across different team types
   - Desarrolla métricas de equidad en predicciones
   - Crea recomendaciones para mitigar sesgos

### Entregables
- **Toolkit de interpretabilidad**: Conjunto de herramientas para análisis
- **Dashboard interactivo**: Interface para explorar modelos
- **Casos de estudio**: Análisis detallados de decisiones específicas
- **Guía de comunicación**: Manual para explicar modelos a diferentes audiencias

### Criterios de Evaluación
- **Profundidad técnica** (35%): Sofisticación de análisis de interpretabilidad
- **Calidad de visualizaciones** (25%): Effectiveness de gráficos y dashboards
- **Claridad de comunicación** (25%): Capacidad de explicar conceptos complejos
- **Relevancia práctica** (15%): Utilidad para stakeholders reales

---

## Metodología de Trabajo y Soporte

### Estructura de Mentorías

#### Sesiones Grupales Semanales (1 hora)
- **Lunes**: Revisión de conceptos y resolución de dudas técnicas
- **Miércoles**: Presentación de avances y peer review
- **Viernes**: Troubleshooting y optimización de código

#### Mentorías Individuales (30 minutos cada 2 semanas)
- **Revisión personalizada** de progreso individual
- **Orientación específica** según intereses del estudiante
- **Feedback detallado** sobre calidad de implementación
- **Planificación** de siguientes pasos de aprendizaje

### Recursos de Apoyo

#### Documentación Técnica
- **Templates de código**: Estructuras base para cada ejercicio
- **Datasets documentados**: Diccionarios de datos completos
- **Guías de implementación**: Paso a paso para técnicas complejas
- **Referencias académicas**: Papers relevantes para profundizar

#### Herramientas Proporcionadas
- **Ambiente de desarrollo**: Jupyter Lab con extensiones
- **Librerías pre-instaladas**: sklearn, xgboost, lightgbm, shap, lime
- **Datasets preprocessados**: Datos listos para experimentación
- **Visualización tools**: Plotly, seaborn, matplotlib configurados

### Calendario y Entregas

#### Cronograma Flexible
- **Semanas 1-2**: Selección de ejercicios y planificación
- **Semanas 3-8**: Desarrollo de ejercicios elegidos
- **Semanas 9-10**: Refinamiento y documentación
- **Semana 11**: Presentaciones finales y peer review

#### Entregas Escalonadas
- **25% avance (Semana 4)**: Implementación básica funcionando
- **75% avance (Semana 7)**: Análisis completo con resultados preliminares
- **100% final (Semana 10)**: Documentación completa y presentación

### Evaluación y Feedback

#### Criterios Transversales
- **Rigor técnico**: Correctness y sophistication de implementación
- **Innovación**: Creatividad en enfoques y soluciones
- **Aplicabilidad**: Relevancia práctica para problemas reales
- **Comunicación**: Claridad en documentación y presentación

#### Feedback Continuo
- **Revisiones de código**: Comentarios en commits y pull requests
- **Evaluación de avances**: Feedback detallado en checkpoints
- **Peer review**: Evaluación entre compañeros con rúbricas
- **Auto-evaluación**: Reflexión estructurada sobre aprendizaje

---

## Integración con Proyecto Final

### Preparación para Proyecto Final
Los ejercicios de práctica están diseñados para **preparar directamente** para el proyecto final del bloque:

#### Conexiones Específicas
- **Ejercicio 1** → **Fase 2 del proyecto**: Modelado y optimización avanzada
- **Ejercicio 2** → **Fase 1 del proyecto**: Feature engineering estratégico
- **Ejercicio 3** → **Fase 3 del proyecto**: Sistemas robustos de producción
- **Ejercicio 4** → **Fase 4 del proyecto**: Comunicación y aplicación

#### Reutilización de Código
- **Librerías desarrolladas**: Módulos directamente reutilizables
- **Pipelines creados**: Infrastructura para proyecto final
- **Análisis realizados**: Insights aplicables a dataset final
- **Herramientas construidas**: Utilities para desarrollo rápido

### Portfolio Profesional
Los ejercicios de práctica contribuyen a construir un **portfolio sólido**:

#### Componentes de Portfolio
- **Diversidad técnica**: Múltiples técnicas y enfoques demostrados
- **Profundidad analítica**: Análisis detallados y insights valiosos
- **Herramientas prácticas**: Código reutilizable y bien documentado
- **Comunicación efectiva**: Capacidad de explicar conceptos complejos

#### Preparación Profesional
- **Experiencia práctica**: Trabajo con problemas reales complejos
- **Habilidades técnicas**: Competencias demandadas en la industria
- **Capacidad de innovación**: Desarrollo de soluciones creativas
- **Colaboración efectiva**: Trabajo en equipo y peer review

---

**Los ejercicios de práctica representan una oportunidad única para profundizar en machine learning avanzado mientras desarrollas un portfolio profesional sólido. ¡Aprovecha esta flexibilidad para explorar tus intereses específicos en data science deportivo!** 🚀⚽🤖

**Peso total:** 25% del Bloque 3 (6.25% de la calificación final del curso)  
**Modalidad:** Elección flexible de 3 de 4 ejercicios según intereses  
**Enfoque:** Experimentación y profundización en técnicas avanzadas  
**Objetivo:** Preparación intensiva para proyecto final y desarrollo profesional

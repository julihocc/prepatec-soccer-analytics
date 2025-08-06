# Ejercicios Semanales - Bloque 3

**Bloque:** 3 - Mi Primera Predicción con Datos de Fútbol  
**Enfoque:** Modelado Predictivo Básico para Preparatoria  
**Semanas:** 11-15 (5 semanas)  
**Duración total:** Aproximadamente 18-22 horas  

## Información General

Este directorio contiene los ejercicios semanales del Bloque 3, diseñados para introducir a estudiantes de preparatoria a los conceptos fundamentales del machine learning aplicado al análisis deportivo. Cada ejercicio construye progresivamente sobre el conocimiento adquirido en los bloques anteriores.

## Objetivos del Bloque

Al completar estos ejercicios, los estudiantes serán capaces de:

1. **Comprender** conceptos básicos de machine learning y predicción
2. **Implementar** modelos predictivos usando scikit-learn
3. **Evaluar** la calidad de modelos usando métricas apropiadas
4. **Optimizar** modelos mediante feature engineering y selección de variables
5. **Integrar** todas las habilidades del curso en un proyecto completo

## Estructura de Ejercicios

### Semana 11: Mi Primera Predicción
- **Archivo:** `ejercicio-semana-11-modelado.md`
- **Enfoque:** Introducción al machine learning con modelos simples
- **Tiempo:** 3-4 horas
- **Dificultad:** ⭐⭐⭐ (Intermedio-Alto)
- **Tecnologías:** scikit-learn, regresión logística, random forest
- **Conceptos clave:**
  - Supervised learning básico
  - Train/test split
  - Primera implementación de modelos
  - Interpretación de predicciones

### Semana 12: Modelos Más Inteligentes
- **Archivo:** `ejercicio-semana-12-modelos-avanzados.md`
- **Enfoque:** Comparación de múltiples algoritmos de machine learning
- **Tiempo:** 3-4 horas
- **Dificultad:** ⭐⭐⭐⭐ (Alto)
- **Tecnologías:** Múltiples algoritmos, ensemble methods, validación cruzada
- **Conceptos clave:**
  - Múltiples algoritmos (SVM, KNN, Naive Bayes, etc.)
  - Optimización de hiperparámetros
  - Ensemble learning
  - Comparación sistemática de modelos

### Semana 13: ¿Qué Tan Buena es Mi Predicción?
- **Archivo:** `ejercicio-semana-13-evaluacion.md`
- **Enfoque:** Métricas avanzadas de evaluación de modelos
- **Tiempo:** 3-4 horas
- **Dificultad:** ⭐⭐⭐⭐ (Alto)
- **Tecnologías:** Métricas múltiples, ROC curves, validación robusta
- **Conceptos clave:**
  - Precision, recall, F1-score
  - Matrices de confusión
  - Curvas ROC y AUC
  - Validación cruzada y confianza estadística

### Semana 14: Mejorando Mis Predicciones
- **Archivo:** `ejercicio-semana-14-optimizacion.md`
- **Enfoque:** Feature engineering y optimización avanzada
- **Tiempo:** 4-5 horas
- **Dificultad:** ⭐⭐⭐⭐⭐ (Muy Alto)
- **Tecnologías:** Feature engineering, pipelines, selección automática
- **Conceptos clave:**
  - Feature engineering temporal y contextual
  - Selección automática de variables
  - Pipelines de producción
  - Optimización sistemática

### Semana 15: Proyecto Final Integrador
- **Archivo:** `ejercicio-semana-15-proyecto-final.md`
- **Enfoque:** Proyecto capstone que integra todo el curso
- **Tiempo:** 6-8 horas
- **Dificultad:** ⭐⭐⭐⭐⭐ (Proyecto Capstone)
- **Tecnologías:** Integración completa del stack tecnológico
- **Conceptos clave:**
  - Sistema completo de análisis predictivo
  - Aplicaciones prácticas
  - Comunicación profesional
  - Reflexión sobre aprendizaje

## Progresión de Complejidad

### Nivel Técnico
- **Semana 11:** Introducción suave al machine learning
- **Semana 12:** Expansión a múltiples algoritmos y comparaciones
- **Semana 13:** Profundización en evaluación y métricas
- **Semana 14:** Técnicas avanzadas de optimización
- **Semana 15:** Integración completa y aplicación profesional

### Complejidad de Datos
- **Semana 11:** Datasets simples con variables básicas
- **Semana 12:** Datasets expandidos con más variables
- **Semana 13:** Datasets desbalanceados y realistas
- **Semana 14:** Feature engineering extensivo
- **Semana 15:** Datasets complejos con múltiples fuentes

### Expectativas de Resultados
- **Semana 11:** Modelos funcionales básicos (60-70% accuracy)
- **Semana 12:** Comparación sistemática y mejores modelos (65-75% accuracy)
- **Semana 13:** Evaluación robusta y comprensión de limitaciones
- **Semana 14:** Optimización significativa (70-80% accuracy)
- **Semana 15:** Sistema profesional completo

## Prerrequisitos

### Conocimientos Técnicos
- **Bloque 1 completo:** Programación Python, pandas, numpy, matplotlib
- **Bloque 2 completo:** Análisis exploratorio, estadística, visualización avanzada
- **Matemáticas:** Conceptos básicos de probabilidad y estadística
- **Lógica:** Capacidad de razonamiento secuencial y resolución de problemas

### Herramientas Necesarias
```python
# Librerías principales requeridas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
```

## Metodología de Evaluación

### Criterios Generales (Aplicables a todos los ejercicios)

#### Competencia Técnica (40-45%)
- **Implementación correcta:** Código ejecuta sin errores
- **Uso apropiado de librerías:** Aplicación correcta de scikit-learn
- **Buenas prácticas:** División de datos, validación apropiada
- **Eficiencia:** Código optimizado y comprensible

#### Análisis e Interpretación (35-40%)
- **Comprensión conceptual:** Entendimiento de algoritmos y métricas
- **Interpretación correcta:** Análisis apropiado de resultados
- **Pensamiento crítico:** Identificación de limitaciones y mejoras
- **Insights deportivos:** Conexión relevante con contexto futbolístico

#### Comunicación y Presentación (15-25%)
- **Claridad:** Explicaciones comprensibles
- **Organización:** Estructura lógica del análisis
- **Visualizaciones:** Gráficos informativos y profesionales
- **Documentación:** Comentarios apropiados en código

### Criterios Específicos por Semana

#### Semana 11: Enfoque en Implementación
- Primeras implementaciones exitosas de modelos
- Comprensión de conceptos básicos
- División apropiada de datos

#### Semana 12: Enfoque en Comparación
- Implementación de múltiples algoritmos
- Comparación sistemática
- Análisis de fortalezas/debilidades

#### Semana 13: Enfoque en Evaluación
- Cálculo correcto de múltiples métricas
- Interpretación profunda de resultados
- Validación robusta

#### Semana 14: Enfoque en Optimización
- Feature engineering creativo
- Mejoras cuantificables
- Pipelines profesionales

#### Semana 15: Enfoque en Integración
- Sistema completo funcional
- Aplicación práctica
- Comunicación profesional

## Recursos de Apoyo

### Documentación Técnica
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

### Conceptos Clave a Dominar
- **Supervised Learning:** Aprendizaje con ejemplos etiquetados
- **Classification:** Predicción de categorías
- **Train/Validation/Test:** División de datos para validación
- **Cross-validation:** Validación robusta de modelos
- **Feature Engineering:** Creación de variables predictivas
- **Model Selection:** Elección del mejor algoritmo
- **Hyperparameter Tuning:** Optimización de configuraciones
- **Ensemble Methods:** Combinación de múltiples modelos

### Datasets Utilizados
- Partidos de fútbol simulados con realismo deportivo
- Variables progresivamente más complejas
- Contexto siempre relevante al dominio futbolístico
- Datos balanceados y desbalanceados según objetivos pedagógicos

## Consideraciones Especiales

### Adaptación al Nivel Preparatoria
- **Conceptos simplificados:** Machine learning explicado de manera accesible
- **Ejemplos concretos:** Siempre en contexto deportivo familiar
- **Progresión gradual:** Complejidad incremental manejable
- **Enfoque práctico:** Más implementación que teoría matemática profunda

### Conexión con Aplicaciones Reales
- **Casos de uso:** Situaciones que enfrentarían analistas deportivos
- **Herramientas profesionales:** Introducción a stack tecnológico industrial
- **Metodología:** Prácticas estándar de la industria adaptadas
- **Comunicación:** Habilidades de presentación para audiencias diversas

### Flexibilidad en Implementación
- **Múltiples enfoques válidos:** No hay una única solución correcta
- **Creatividad valorada:** Enfoques originales son bienvenidos
- **Extensiones opcionales:** Ejercicios bonus para estudiantes avanzados
- **Adaptación local:** Posibilidad de usar equipos/ligas locales

## Notas para Instructores

### Tiempo de Preparación
- **Por ejercicio:** 2-3 horas de preparación instructor
- **Revisión:** 30-45 minutos por estudiante por ejercicio
- **Retroalimentación:** Enfoque en proceso más que solo resultados

### Errores Comunes Esperados
- **Semana 11:** Confusión sobre train/test split, interpretación de accuracy
- **Semana 12:** Dificultades con múltiples modelos, comparación sistemática
- **Semana 13:** Malinterpretación de métricas, confianza estadística
- **Semana 14:** Overfitting en feature engineering, pipelines complejos
- **Semana 15:** Integración de componentes, gestión de complejidad

### Adaptaciones Sugeridas
- **Tiempo flexible:** Ejercicios pueden extenderse 1-2 semanas si necesario
- **Soporte técnico:** Sesiones de troubleshooting recomendadas
- **Trabajo en pares:** Opcional para estudiantes que lo necesiten
- **Presentaciones:** Oportunidades de mostrar trabajo a compañeros

---

*El Bloque 3 representa la culminación del curso, donde los estudiantes aplican todo lo aprendido para crear sistemas predictivos reales. Al completarlo, habrán adquirido habilidades valiosas en data science aplicada al deporte.*

**Total de ejercicios:** 5  
**Duración total:** 18-22 horas  
**Nivel final alcanzado:** Data Scientist Junior en Deportes

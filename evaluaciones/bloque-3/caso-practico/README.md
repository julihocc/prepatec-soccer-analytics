# Caso Práctico Bloque 3: Sistema Básico de Análisis Predictivo

Este caso práctico sustituye la denominación previa de "proyecto integrador" dentro de evaluaciones para evitar confusión con el proyecto de aprendizaje en `contenido/bloque-3/semana-15`.

## Propósito
Evaluar de forma individual la integración de:
- Exploración de datos (EDA)
- Preparación simple de variables
- Modelo de predicción básico (clasificación o regresión simple según dataset elegido)
- Interpretación y comunicación de resultados

## Entregable
Notebook único: `caso_bloque3.ipynb` con las secciones:
1. Carga y exploración de datos
2. Limpieza y creación de variables simples
3. Modelo de predicción (1 modelo principal) y evaluación (precisión o métrica básica)
4. Visualizaciones de apoyo (3-5 gráficas)
5. Conclusiones y reflexiones (incluye: limitaciones y próximos pasos)

### Estructura Recomendada (Plantilla)
```
# Caso Práctico Bloque 3: Análisis Predictivo Básico

## 1. Exploración de Datos (40%)
### 1.1 Carga de Datos
### 1.2 Análisis Básico
### 1.3 Limpieza Simple

## 2. Visualización y Análisis (35%)
### 2.1 Gráficos Descriptivos
### 2.2 Análisis de Patrones
### 2.3 Estadísticas Básicas

## 3. Predicción Simple (25%)
### 3.1 Preparar Datos
### 3.2 Modelo
### 3.3 Interpretación

## 4. Conclusiones Finales
```

### Ejemplo de Código Inicial
```python
import pandas as pd, matplotlib.pyplot as plt, seaborn as sns
sns.set_theme(style="whitegrid", palette="viridis")
datos = pd.read_csv('champions_league_matches.csv')
print(datos.head())
print(datos.info())
datos['total_goles'] = datos['goles_local'] + datos['goles_visitante']
```

## Rúbrica (Resumen)
Ver rúbrica integrada completa en `evaluaciones/bloque-3/README.md`.
- Notebook (20% del curso total) subdividido en:
  - EDA (25%)
  - Modelado (35%)
  - Visualización / (Dashboard ligero opcional) (25%)
  - Documentación y Código (15%)
- Presentación (10% del curso) posterior al notebook.

## Diferencias con el Proyecto de Contenido Semana 15
| Aspecto | Caso Práctico (evaluaciones) | Proyecto Semana 15 (contenido) |
|---------|------------------------------|--------------------------------|
| Rol | Evidencia evaluativa formal | Actividad de aprendizaje aplicada |
| Estructura | Rúbrica oficial (20% curso) | Guía pedagógica de cierre |
| Alcance ML | Modelo simple | Integración narrativa + práctica guiada |
| Enfoque | Cumplimiento de criterios | Exploración formativa |

## Lineamientos Específicos
- Limitar complejidad del modelo a lo visto (p.ej. RandomForestClassifier simple)
- Evitar hiperparametrización avanzada
- Variables creadas deben ser explicables en < 2 oraciones
- Código en español, sin emojis, preguntas socráticas donde aporte reflexión

## Dataset Proporcionado
Archivo: `champions_league_matches.csv` (colocar en la misma carpeta del notebook).  
Incluir breve inspección: número de filas/columnas, variables clave, rango temporal.

## Integridad Académica
- Código debe ser entendible por el autor
- Declarar uso de herramientas de IA si aplican
- Explicar en conclusiones decisiones clave de preprocesamiento

## Autoevaluación Rápida (Checklist)
- [ ] Exploré y limpié los datos
- [ ] Creé al menos una variable derivada simple
- [ ] Entrené un modelo básico y calculé métrica
- [ ] Incluí 3-5 visualizaciones claras
- [ ] Escribí conclusiones y próximas preguntas
- [ ] Revisé la rúbrica integrada

## Registro de Cambio
2025-08-10: Creación inicial para renombrar y clarificar el caso práctico del Bloque 3.

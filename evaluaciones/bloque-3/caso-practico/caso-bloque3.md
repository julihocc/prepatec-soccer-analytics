# Caso Práctico Bloque 3: Análisis Predictivo de Resultados en la UEFA Champions League

## Contexto del Proyecto

Como analistas de datos de un equipo de fútbol europeo, habéis sido contratados para desarrollar un sistema predictivo que ayude a anticipar los resultados de los partidos de la UEFA Champions League. Vuestro objetivo es crear un modelo de machine learning que identifique los factores más determinantes para la victoria y proporcione recomendaciones tácticas basadas en datos históricos.

Este caso práctico representa el **25% de la calificación total del curso** y debe demostrar la integración completa de todos los conocimientos adquiridos en programación Python, análisis de datos y fundamentos de machine learning.

## Objetivos de Aprendizaje

Al completar este proyecto, deberás ser capaz de:

1. **Preparar y limpiar datos** reales de fútbol para análisis predictivo
2. **Crear un modelo de machine learning** que prediga resultados deportivos  
3. **Evaluar la calidad** y limitaciones de tus predicciones
4. **Interpretar resultados** en contexto futbolístico real
5. **Comunicar hallazgos** a audiencias no técnicas

## Dataset: UEFA Champions League

Trabajarás con un dataset real de partidos de la Champions League que incluye:

- **Información básica**: Equipos, fechas, resultados, goles
- **Estadísticas de juego**: Tiros, posesión, tarjetas, corners
- **Variables derivadas**: Eficiencias, diferencias, promedios por equipo

### Carga Inicial de Datos

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# TODO: Cargar el dataset
datos_champions = pd.read_csv('champions_league_data.csv')

# TAREA: Explorar la estructura básica
print(f"Dimensiones del dataset: {datos_champions._____}")  # ¿Cómo ves el tamaño?
print("\nPrimeras filas:")
# TODO: Mostrar las primeras 5 filas

print("\nInformación del dataset:")  
# TODO: Usar .info() para ver tipos de datos y valores faltantes

print("\nEstadísticas descriptivas:")
# TODO: Usar .describe() para estadísticas básicas
```

---

## Parte 1: Preparación y Exploración de Datos (30 puntos)

### 1.1 Análisis Exploratorio Inicial (15 puntos)

Comienza conociendo tus datos para tomar decisiones informadas:

```python
# TODO: ¿Cuántos partidos tenemos por temporada?
partidos_por_temporada = datos_champions._____(by='temporada').size()
print("Partidos por temporada:")
print(partidos_por_temporada)

# TAREA: ¿Cuál es la distribución de goles?
print("\nDistribución de goles locales:")
# Crear histograma de goles_local con plt.hist()

print("Distribución de goles visitantes:")  
# Crear histograma de goles_visitante

# TODO: ¿Hay ventaja de jugar en casa?
victorias_locales = (datos_champions['goles_local'] > datos_champions['goles_visitante']).sum()
total_partidos = len(datos_champions)
porcentaje_local = (victorias_locales / total_partidos) * 100

print(f"\nVictorias locales: {victorias_locales}/{total_partidos} ({porcentaje_local:.1f}%)")

# TAREA: Calcular también empates y victorias visitantes
empates = (datos_champions['_____'] == datos_champions['_____']).sum()  # ¿Cuándo los goles son iguales?
victorias_visitantes = total_partidos - victorias_locales - empates

print(f"Empates: {empates}/{total_partidos}")
print(f"Victorias visitantes: {victorias_visitantes}/{total_partidos}")
```

**Pregunta de reflexión:** ¿Existe realmente ventaja de campo en la Champions League? ¿Te sorprenden estos porcentajes comparados con lo que observas viendo partidos?

### 1.2 Crear Variables Objetivo y Derivadas (15 puntos)

Transforma los datos para que tu modelo pueda trabajar con ellos:

```python
# TODO: Crear variable objetivo binaria (1 = gana local, 0 = no gana local)  
datos_champions['gana_local'] = (datos_champions['_____'] > datos_champions['_____']).astype(int)

# TODO: Crear variables derivadas útiles para el modelo
datos_champions['total_goles'] = datos_champions['_____'] + datos_champions['_____']
datos_champions['diferencia_goles'] = datos_champions['_____'] - datos_champions['_____']

# TAREA: Calcular eficiencias (goles/tiros) 
# CUIDADO: ¿Qué pasa si hay divisiones por cero?
datos_champions['eficiencia_local'] = datos_champions['goles_local'] / datos_champions['_____']
datos_champions['eficiencia_visitante'] = datos_champions['_____'] / datos_champions['tiros_visitante']

# TODO: Verificar balanceamiento de clases
print("Distribución de resultados:")
print(datos_champions['gana_local']._____)  # Contar valores
print(f"Porcentaje de victorias locales: {datos_champions['gana_local'].mean():.2%}")
```

**Pregunta de reflexión:** ¿Por qué es importante que nuestras clases (gana/no gana local) estén relativamente balanceadas? ¿Qué pasaría si el 95% de los partidos los ganara siempre el equipo local?

### 1.3 Limpieza y Validación de Datos (15 puntos)

Asegúrate de que tus datos estén listos para el modelo:

```python
# TODO: Verificar valores faltantes
print("Valores faltantes por columna:")
# TAREA: Usar .isnull().sum() para contar valores faltantes

# TODO: Limpiar datos problemáticos
# Las divisiones por cero crean valores infinitos - reemplazarlos por 0
datos_champions['eficiencia_local'] = datos_champions['eficiencia_local'].replace([np.inf, -np.inf], _____)
datos_champions['eficiencia_visitante'] = datos_champions['eficiencia_visitante'].replace([np.inf, -np.inf], _____)

# TODO: Verificar que los rangos de goles sean lógicos
print("Verificación de rangos:")
print(f"Goles mínimos: _____") # Encontrar el mínimo de goles
print(f"Goles máximos: _____") # Encontrar el máximo de goles

# TODO: Eliminar filas con datos faltantes si las hay
datos_champions = datos_champions._____ # Método para eliminar filas con NaN
print(f"Dataset final: {len(datos_champions)} partidos")
```

**Pregunta de reflexión:** ¿Por qué eliminamos o corregimos valores infinitos en las eficiencias? ¿Cómo podrían estos valores "romper" nuestro modelo de machine learning?

---

## Parte 2: Modelado Predictivo (40 puntos)

### 2.1 Preparar Variables para el Modelo (10 puntos)

Selecciona las variables más importantes para predecir resultados:

```python
# TODO: Seleccionar variables predictoras
# NOTA: No incluir variables que dependan del resultado (como goles)
variables_predictoras = [
    'tiros_local', 'tiros_visitante',
    # TAREA: Agregar más variables relevantes de tu dataset
    # Sugerencias: posesion, tarjetas, eficiencias, etc.
]

# TODO: Preparar matrices X e y para el modelo
X = datos_champions[_____] # Variables independientes
y = datos_champions[_____] # Variable objetivo

print("Variables para el modelo:")
print(f"Características (X): {_____}")
print(f"Variable objetivo (y): {_____}")
print(f"Forma de X: {X.shape}")
print(f"Forma de y: {y.shape}")
```

**Pregunta de reflexión:** ¿Por qué seleccionamos estas variables específicas? ¿Qué otras variables futbolísticas podrían ser importantes para predecir el resultado de un partido?

### 2.2 Dividir Datos en Entrenamiento y Prueba (10 puntos)  

Separa tus datos para entrenar y evaluar el modelo correctamente:

```python
# TODO: Dividir datos (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(
    _____, _____, # X, y
    test_size=_____, # ¿Qué porcentaje para prueba?
    random_state=42, # Para reproducibilidad
    stratify=_____ # Para mantener proporciones de clases
)

print("División completada:")
print(f"Entrenamiento: _____ partidos") # Tamaño de X_train
print(f"Prueba: _____ partidos") # Tamaño de X_test
print(f"Proporción entrenar/total: _____") # Calcular porcentaje

# TODO: Verificar que ambos conjuntos mantengan balance de clases
print("Distribución en entrenamiento:")
# TAREA: Mostrar conteos de y_train

print("Distribución en prueba:")  
# TAREA: Mostrar conteos de y_test
```

**Pregunta de reflexión:** ¿Por qué dividimos los datos en entrenamiento y prueba? ¿Qué pasaría si evaluáramos el modelo con los mismos datos que usamos para entrenarlo?

### 2.3 Entrenar Modelo Random Forest (20 puntos)

Crea y entrena tu modelo de machine learning:

```python
# TODO: Crear el modelo Random Forest
modelo_rf = RandomForestClassifier(
    n_estimators=_____, # ¿Cuántos árboles?
    random_state=42,
    max_depth=_____ # Para evitar sobreajuste
)

print("Entrenando modelo Random Forest...")
# TAREA: Entrenar el modelo con X_train e y_train

print("¡Modelo entrenado exitosamente!")

# TODO: Hacer predicciones en ambos conjuntos
predicciones_train = modelo_rf._____(X_train)
predicciones_test = modelo_rf._____(X_test)

# TODO: Evaluar precisión
precision_train = accuracy_score(_____, _____)
precision_test = accuracy_score(_____, _____)

print(f"Precisión en entrenamiento: {precision_train:.3f} ({precision_train:.1%})")
print(f"Precisión en prueba: {precision_test:.3f} ({precision_test:.1%})")
```

**Pregunta de reflexión:** ¿Qué significa que nuestro modelo tenga 75% de precisión? ¿Es mejor o peor que adivinar al azar? ¿Por qué la precisión en entrenamiento suele ser mayor que en prueba?

---

## Parte 3: Evaluación y Análisis (30 puntos)

### 3.1 Análisis de Importancia de Variables (15 puntos)

Descubre cuáles variables son más importantes para tu modelo:

```python
# TODO: Extraer importancias de las variables
importancias = modelo_rf._____  # ¿Qué atributo guarda las importancias?
nombres_variables = X.columns.tolist()

# TAREA: Crear DataFrame con importancias
df_importancias = pd.DataFrame({
    'Variable': _____,
    'Importancia': _____
})

# TODO: Ordenar por importancia (de mayor a menor)
df_importancias = df_importancias._____(by='_____', ascending=_____)

print("Importancia de variables:")
print(df_importancias)

# TODO: Crear gráfico de importancias
plt.figure(figsize=(10, 6))
plt.barh(df_importancias['Variable'], df_importancias['_____'])
plt.title('¿Qué Variables son más Importantes para Predecir Resultados?')
plt.xlabel('Importancia')
# TAREA: Ajustar el gráfico para que se vea mejor
plt.tight_layout()
plt.show()
```

**Pregunta de reflexión:** ¿Cuáles son las 3 variables más importantes según tu modelo? ¿Esto tiene sentido futbolísticamente? ¿Por qué algunas variables tienen más peso que otras?

### 3.2 Matriz de Confusión y Análisis Detallado (15 puntos)

Analiza dónde se equivoca tu modelo:

```python
# TODO: Crear matriz de confusión
matriz_confusion = confusion_matrix(_____, _____)  # y_test, predicciones_test

print("Matriz de Confusión:")
print("Filas: Realidad | Columnas: Predicción")
print(matriz_confusion)

# TAREA: Analizar los tipos de errores
verdaderos_negativos = matriz_confusion[0, 0]  # Predijo derrota local, fue derrota local
falsos_positivos = matriz_confusion[_____, _____]   # Predijo victoria local, fue derrota local  
falsos_negativos = matriz_confusion[_____, _____]   # Predijo derrota local, fue victoria local
verdaderos_positivos = matriz_confusion[_____, _____] # Predijo victoria local, fue victoria local

print(f"Verdaderos Negativos (Derrota local predicha correctamente): {_____}")
print(f"Falsos Positivos (Predijo victoria local, fue derrota): {_____}")  
print(f"Falsos Negativos (Predijo derrota local, fue victoria): {_____}")
print(f"Verdaderos Positivos (Victoria local predicha correctamente): {_____}")

# TODO: Visualizar matriz de confusión
plt.figure(figsize=(8, 6))
# TAREA: Usar seaborn para crear un heatmap de la matriz
# Sugerencia: sns.heatmap(matriz_confusion, annot=True, ...)

plt.title('¿Dónde se Equivoca Nuestro Modelo?')
plt.ylabel('Resultado Real')
plt.xlabel('Resultado Predicho')
plt.show()
```

**Pregunta de reflexión:** ¿En qué tipo de predicciones se equivoca más tu modelo? ¿Es peor predecir falsas victorias o falsas derrotas? ¿Por qué?

---

## Entregables Finales

### 1. Archivo de Código (.py o .ipynb)
Tu notebook o script debe incluir:
- Análisis exploratorio completo
- Código de modelado funcional  
- Todas las visualizaciones
- Comentarios explicando cada paso

### 2. Reflexiones Escritas (1-2 páginas)
Responde por escrito:
1. **Análisis de Datos**: ¿Qué patrones encontraste más interesantes en los datos de la Champions League?
2. **Selección de Variables**: ¿Por qué elegiste esas variables para tu modelo? ¿Descartaste alguna? ¿Por qué?
3. **Evaluación del Modelo**: ¿Qué tan bueno es tu modelo para predecir resultados? ¿En qué situaciones es más confiable?
4. **Aplicación Real**: Si fueras entrenador o analista deportivo, ¿cómo usarías este modelo para tomar decisiones?
5. **Limitaciones**: ¿Qué limitaciones tiene tu análisis? ¿Qué datos adicionales te gustaría tener?

---

## Criterios de Evaluación

**Técnico (40%)**
- Código funcional sin errores
- Uso correcto de pandas, sklearn y matplotlib
- Implementación completa del flujo de machine learning
- Limpieza y preparación adecuada de datos

**Aplicación (30%)**  
- Selección justificada de variables
- Interpretación correcta de resultados
- Análisis de importancia de variables
- Evaluación crítica del modelo

**Comunicación (30%)**
- Reflexiones bien desarrolladas
- Explicación clara del proceso
- Conexión entre análisis técnico y contexto futbolístico
- Identificación de limitaciones y mejoras

---

**¡Recuerda:** Este caso práctico integra todo lo aprendido en el curso. No tengas miedo de experimentar con diferentes variables o enfoques. Lo más importante es que entiendas el proceso completo: desde explorar datos hasta evaluar si tu modelo es útil en la realidad.

**Tiempo sugerido**: 6-8 horas de trabajo a lo largo de 2 semanas.
**Fecha de entrega**: [Fecha definida por el profesor]
**Modalidad**: Individual con consultas permitidas entre compañeros.

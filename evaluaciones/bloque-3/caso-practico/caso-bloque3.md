# Caso Práctico Colaborativo - Bloque 3

## Predicción de Resultados de Fútbol con Machine Learning

**Modalidad:** Colaborativa (equipos de 2-3 estudiantes)  
**Ponderación:** 15% del curso total  
**Duración:** 1 semana  
**Entrega:** Notebook de Jupyter + video de exposición (YouTube)

---

## Contexto del Problema

Eres parte de un equipo que ayuda a un club deportivo a utilizar inteligencia artificial para mejorar sus decisiones estratégicas. Necesitan un sistema básico de predicción de resultados de partidos usando datos históricos de Champions League.

**Situación:** Tienen un dataset con información de partidos históricos y quieren construir un modelo simple de machine learning que pueda predecir si el equipo local ganará o no, usando conceptos básicos de clasificación y evaluación de modelos.

---

## Objetivos de Aprendizaje

Al completar este caso práctico, los estudiantes serán capaces de:

- Preparar datos deportivos para machine learning básico
- Crear variables objetivo binarias para problemas de clasificación
- Entrenar modelos simples de clasificación (Random Forest)
- Evaluar modelos usando métricas básicas de precisión
- Interpretar resultados de predicciones en contexto deportivo
- Trabajar en equipo para resolver problemas de inteligencia artificial
- Comunicar hallazgos de machine learning de forma clara

---

## Datos Que Van a Usar

Trabajarán con un dataset CSV real de partidos de Champions League con información histórica.

### Dataset Principal: `champions_league_matches.csv`

Archivo CSV con información de partidos históricos de Champions League.

```csv
equipo_local,equipo_visitante,goles_local,goles_visitante,temporada,fase_competicion,tiros_local,tiros_visitante,tiros_arco_local,tiros_arco_visitante
Barcelona,Real Madrid,2,1,2023-24,Semifinal,15,12,8,5
Manchester City,Liverpool,1,3,2023-24,Cuartos,18,14,6,9
Bayern Munich,PSG,3,0,2023-24,Octavos,20,8,11,3
...
```

**Descripción de columnas:**

- `equipo_local`: Equipo que juega en casa
- `equipo_visitante`: Equipo que juega de visita  
- `goles_local`: Goles marcados por el equipo local
- `goles_visitante`: Goles marcados por el equipo visitante
- `temporada`: Temporada del partido (ej. 2023-24)
- `fase_competicion`: Fase del torneo (Octavos, Cuartos, Semifinal, Final)
- `tiros_local`: Total de tiros del equipo local
- `tiros_visitante`: Total de tiros del equipo visitante
- `tiros_arco_local`: Tiros a portería del equipo local
- `tiros_arco_visitante`: Tiros a portería del equipo visitante

**Características del dataset:**
- **Partidos históricos**: Datos reales de Champions League de múltiples temporadas
- **Variables de rendimiento**: Goles, tiros y tiros a portería para análisis
- **Contexto competitivo**: Diferentes fases del torneo para comparar
- **Ideal para ML**: Estructura perfecta para problemas de clasificación binaria

---

## Tareas Requeridas

> NOTA IMPORTANTE: Cada subtarea incluye (a) Acción técnica y (b) Pregunta de reflexión breve. Responde siempre estas preguntas antes de continuar al siguiente bloque - te ayudarán a profundizar tu comprensión.

### Parte 1: Preparación de Datos para Machine Learning (40 puntos)

#### 1.1 Cargar y Explorar el Dataset (10 puntos)

---

## Rúbrica de Evaluación

### Criterios Técnicos (40%)

| Criterio | Excelente (~100%) | Suficiente (~70%) | Insuficiente (~30%) | No presentó (0%) |
|----------|-------------------|-------------------|---------------------|-------------------|
| **Código funcional** | Ejecuta sin errores, sintaxis perfecta, cumple objetivos | Ejecuta con errores menores, cumple objetivos principales | Errores significativos, objetivos parcialmente logrados | No ejecuta o no entregado |
| **Uso de librerías ML** | sklearn, pandas, numpy usados correctamente y eficientemente | Uso básico correcto con pequeñas ineficiencias | Uso incorrecto o confuso de algunas funciones | No usa las librerías requeridas |
| **Calidad del modelo** | Modelo bien configurado, evaluación completa, precisión razonable | Modelo básico funcional, evaluación simple | Modelo problemático, evaluación incompleta | No crea modelo válido |

### Criterios de Aplicación (30%)

| Criterio | Excelente (~100%) | Suficiente (~70%) | Insuficiente (~30%) | No presentó (0%) |
|----------|-------------------|-------------------|---------------------|-------------------|
| **Contexto futbolístico** | Excelente conexión entre análisis y conceptos deportivos reales | Conexión básica adecuada con el contexto | Conexión débil o superficial | Sin conexión deportiva |
| **Interpretación resultados** | Análisis profundo y significativo de patrones y predicciones | Interpretación básica correcta | Interpretación superficial o incorrecta | No interpreta resultados |
| **Casos prácticos** | Escenarios realistas, análisis completo de implicaciones | Escenarios básicos, análisis simple | Escenarios poco realistas o análisis pobre | No incluye casos prácticos |

### Criterios de Comunicación y Razonamiento (30%)

| Criterio | Excelente (~100%) | Suficiente (~70%) | Insuficiente (~30%) | No presentó (0%) |
|----------|-------------------|-------------------|---------------------|-------------------|
| **Reflexiones escritas** | Respuestas profundas, pensamiento crítico evidente | Respuestas adecuadas, comprensión básica | Respuestas superficiales o incorrectas | No responde preguntas |
| **Colaboración en equipo** | Excelente distribución de tareas, trabajo cohesivo | Colaboración básica funcional | Colaboración limitada o desbalanceada | Sin evidencia de trabajo en equipo |
| **Video de presentación** | Comunicación clara, técnicamente precisa, audiencia apropiada | Presentación básica comprensible | Presentación confusa o técnicamente incorrecta | No presenta video |

### Notas Importantes:
- **Requisito mínimo**: Código debe ejecutar sin errores fatales para obtener calificación aprobatoria
- **Trabajo en equipo**: Cada miembro debe contribuir activamente y esto debe ser evidente en el resultado final
- **Video obligatorio**: 3-4 minutos explicando resultados a audiencia no técnica (directiva del club)
- **Pregunta clave**: La reflexión crítica final debe demostrar comprensión madura de limitaciones y aplicaciones de ML

---

## Cronograma Sugerido

### Semana 1: Preparación y Exploración
- **Días 1-2**: Formar equipos, familiarizarse con dataset
- **Días 3-4**: Completar Parte 1 (Preparación de datos)
- **Días 5-7**: Iniciar Parte 2 (Modelado)

### Semana 2: Modelado y Análisis  
- **Días 1-3**: Completar Parte 2 (Modelado predictivo)
- **Días 4-5**: Parte 3 (Análisis e interpretación)
- **Días 6-7**: Revisión técnica y depuración

### Semana 3: Síntesis y Presentación
- **Días 1-2**: Reflexión final y documentación
- **Días 3-4**: Preparación y grabación de video
- **Días 5-7**: Revisión final y entrega

---

## Consejos Útiles

### Para el Trabajo en Equipo
- **Dividir responsabilidades**: Un miembro enfocado en limpieza de datos, otro en modelado, otro en interpretación
- **Reuniones regulares**: Al menos 2-3 sesiones de trabajo conjunto por semana
- **Documento compartido**: Usar Google Colab o GitHub para colaboración en tiempo real
- **Revisión cruzada**: Cada miembro debe revisar y entender el trabajo de los demás

### Para el Machine Learning
- **Comenzar simple**: No complejizar el modelo sin necesidad
- **Validar paso a paso**: Verificar que cada etapa funciona antes de continuar
- **Interpretar siempre**: Cada resultado numérico debe tener explicación futbolística
- **Documentar decisiones**: Explicar por qué eligieron ciertos parámetros o variables

### Para la Presentación
- **Audiencia objetivo**: Directivos de club sin conocimiento técnico
- **Estructura clara**: Problema → Método → Resultados → Recomendaciones
- **Visuales simples**: Gráficos comprensibles, evitar jerga técnica
- **Tiempo específico**: Practicar para mantenerse en 3-4 minutos exactos

### Recursos de Apoyo
- **Documentación oficial**: scikit-learn, pandas, matplotlib
- **Consultas al profesor**: Horario de oficina disponible
- **Datos de prueba**: Dataset verificado y documentado
- **Ejemplos de código**: Proporcionados en cada sección del caso práctico

**Pregunta de reflexión:** ¿Por qué necesitamos conocer la estructura de los datos antes de crear un modelo de machine learning? ¿Qué problemas podríamos tener si no exploramos primero?

#### 1.2 Crear Variables Objetivo y Derivadas (15 puntos)

```python
# Crear variable objetivo binaria
datos_champions['gana_local'] = (datos_champions['goles_local'] > datos_champions['goles_visitante']).astype(int)

# Crear variables derivadas útiles
datos_champions['total_goles'] = datos_champions['goles_local'] + datos_champions['goles_visitante']
datos_champions['diferencia_goles'] = datos_champions['goles_local'] - datos_champions['goles_visitante']
datos_champions['eficiencia_local'] = datos_champions['goles_local'] / datos_champions['tiros_local']
datos_champions['eficiencia_visitante'] = datos_champions['goles_visitante'] / datos_champions['tiros_visitante']

# Verificar balanceamiento de clases
print("Distribución de resultados:")
print(datos_champions['gana_local'].value_counts())
print(f"Porcentaje de victorias locales: {datos_champions['gana_local'].mean():.2%}")
```

**Pregunta de reflexión:** ¿Por qué es importante que nuestras clases (gana/no gana local) estén relativamente balanceadas? ¿Qué pasaría si el 95% de los partidos los ganara siempre el equipo local?

#### 1.3 Limpieza y Validación de Datos (15 puntos)

```python
# Verificar valores faltantes
print("Valores faltantes por columna:")
print(datos_champions.isnull().sum())

# Limpiar datos problemáticos
# Reemplazar divisiones por cero en eficiencias
datos_champions['eficiencia_local'] = datos_champions['eficiencia_local'].replace([np.inf, -np.inf], 0)
datos_champions['eficiencia_visitante'] = datos_champions['eficiencia_visitante'].replace([np.inf, -np.inf], 0)

# Verificar rangos lógicos
print("Verificación de rangos:")
print(f"Goles mínimos: {datos_champions[['goles_local', 'goles_visitante']].min().min()}")
print(f"Goles máximos: {datos_champions[['goles_local', 'goles_visitante']].max().max()}")

# Eliminar filas con datos faltantes si las hay
datos_champions = datos_champions.dropna()
print(f"Dataset final: {len(datos_champions)} partidos")
```

**Pregunta de reflexión:** ¿Por qué eliminamos o corregimos valores infinitos en las eficiencias? ¿Cómo podrían estos valores "romper" nuestro modelo de machine learning?

### Parte 2: Modelado Predictivo (40 puntos)

#### 2.1 Preparar Variables para el Modelo (10 puntos)

```python
# Seleccionar variables predictoras
variables_predictoras = [
    'tiros_local', 'tiros_visitante',
    'tarjetas_local', 'tarjetas_visitante', 
    'posesion_local',
    'eficiencia_local', 'eficiencia_visitante'
]

# Preparar X (variables independientes) y y (variable objetivo)
X = datos_champions[variables_predictoras]
y = datos_champions['gana_local']

print("Variables para el modelo:")
print(X.columns.tolist())
print(f"Tamaño de X: {X.shape}")
print(f"Tamaño de y: {y.shape}")
```

**Pregunta de reflexión:** ¿Por qué seleccionamos estas variables específicas? ¿Qué otras variables futbolísticas podrían ser importantes para predecir el resultado de un partido?

#### 2.2 Dividir Datos en Entrenamiento y Prueba (10 puntos)

```python
# Dividir datos (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42,
    stratify=y  # Mantiene proporciones de clases
)

print("División completada:")
print(f"Entrenamiento: {len(X_train)} partidos")
print(f"Prueba: {len(X_test)} partidos")
print(f"Proporción entrenar/total: {len(X_train)/len(X):.1%}")

# Verificar balanceamiento
print("\nDistribución en entrenamiento:")
print(y_train.value_counts(normalize=True))
print("\nDistribución en prueba:")
print(y_test.value_counts(normalize=True))
```

**Pregunta de reflexión:** ¿Por qué dividimos los datos en entrenamiento y prueba? ¿Qué pasaría si evaluáramos el modelo con los mismos datos que usamos para entrenarlo?

#### 2.3 Entrenar Modelo Random Forest (20 puntos)

```python
# Crear y entrenar el modelo
modelo_rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    max_depth=10
)

print("Entrenando modelo Random Forest...")
modelo_rf.fit(X_train, y_train)
print("¡Modelo entrenado exitosamente!")

# Hacer predicciones
predicciones_train = modelo_rf.predict(X_train)
predicciones_test = modelo_rf.predict(X_test)

# Evaluar precisión
precision_train = accuracy_score(y_train, predicciones_train)
precision_test = accuracy_score(y_test, predicciones_test)

print(f"Precisión en entrenamiento: {precision_train:.3f} ({precision_train:.1%})")
print(f"Precisión en prueba: {precision_test:.3f} ({precision_test:.1%})")
```

### Parte 3: Análisis e Interpretación de Resultados (20 puntos)

#### 3.1 Evaluación Detallada del Modelo (10 puntos)

```python
# Reporte de clasificación detallado
print("Reporte de clasificación:")
print(classification_report(y_test, predicciones_test, target_names=['No gana local', 'Gana local']))

# Importancia de variables
importancias = modelo_rf.feature_importances_
variables_importancia = pd.DataFrame({
    'Variable': variables_predictoras,
    'Importancia': importancias
}).sort_values('Importancia', ascending=False)

print("\nImportancia de variables:")
print(variables_importancia)

# Visualizar importancia
plt.figure(figsize=(10, 6))
sns.barplot(data=variables_importancia, x='Importancia', y='Variable', palette='viridis')
plt.title('Importancia de Variables en el Modelo')
plt.xlabel('Importancia')
plt.tight_layout()
plt.show()
```

**Pregunta de reflexión:** ¿Cuáles variables son más importantes para predecir victorias? ¿Tiene sentido desde el punto de vista futbolístico? ¿Te sorprende algún resultado?

#### 3.2 Predicciones en Casos Específicos (10 puntos)

```python
# Crear escenarios hipotéticos para probar el modelo
escenario_1 = pd.DataFrame({
    'tiros_local': [15], 'tiros_visitante': [8],
    'tarjetas_local': [2], 'tarjetas_visitante': [4],
    'posesion_local': [65],
    'eficiencia_local': [0.20], 'eficiencia_visitante': [0.125]
})

escenario_2 = pd.DataFrame({
    'tiros_local': [6], 'tiros_visitante': [12],
    'tarjetas_local': [1], 'tarjetas_visitante': [2],
    'posesion_local': [40],
    'eficiencia_local': [0.33], 'eficiencia_visitante': [0.17]
})

# Hacer predicciones
pred_1 = modelo_rf.predict(escenario_1)[0]
prob_1 = modelo_rf.predict_proba(escenario_1)[0]

pred_2 = modelo_rf.predict(escenario_2)[0]
prob_2 = modelo_rf.predict_proba(escenario_2)[0]

print("ESCENARIO 1 (Equipo local dominante):")
print(f"Predicción: {'Gana local' if pred_1 == 1 else 'No gana local'}")
print(f"Probabilidades: No gana {prob_1[0]:.2%}, Gana {prob_1[1]:.2%}")

print("\nESCENARIO 2 (Equipo visitante con más tiros):")
print(f"Predicción: {'Gana local' if pred_2 == 1 else 'No gana local'}")
print(f"Probabilidades: No gana {prob_2[0]:.2%}, Gana {prob_2[1]:.2%}")
```

**Pregunta de reflexión:** ¿Cómo explicarías estos resultados a un entrenador de fútbol? ¿Qué recomendaciones tácticas podrías dar basándote en lo que "aprende" el modelo?

---

## Reflexión Final

### Síntesis de Aprendizajes (Obligatorio - incluir en video)

Al finalizar este proyecto, reflexiona sobre:

1. **Comprensión técnica**: ¿Qué diferencias encuentras entre este enfoque predictivo y los análisis descriptivos de bloques anteriores?

2. **Aplicabilidad práctica**: ¿Cómo podrían usar estos modelos los equipos profesionales en su planificación estratégica?

3. **Limitaciones identificadas**: ¿Qué factores importantes del fútbol NO captura nuestro modelo? (Ej: lesiones, moral del equipo, condiciones climáticas)

4. **Colaboración en equipo**: ¿Cómo se dividieron las tareas técnicas? ¿Qué ventajas tiene trabajar en equipo para proyectos de ML?

5. **Comunicación de resultados**: ¿Cómo adaptaron su lenguaje técnico para explicar los resultados a una audiencia no técnica?

### Pregunta de Reflexión Crítica

**¿En qué medida los modelos de machine learning pueden mejorar las decisiones en el fútbol, y cuáles son los riesgos de depender excesivamente de las predicciones algorítmicas en un deporte tan impredecible?**

Esta reflexión debe aparecer tanto en su documento final como en su video de presentación, mostrando una comprensión madura de las posibilidades y limitaciones de la ciencia de datos en el contexto deportivo.
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

- Ponderación Caso (25% curso):
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
| Estructura | Rúbrica oficial (25% curso) | Guía pedagógica de cierre |
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

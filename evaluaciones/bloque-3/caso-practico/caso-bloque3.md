# Caso Práctico Colaborativo - Bloque 3

## Predicción de Resultados de Fútbol con Machine Learning

**Modalidad:** Colaborativa (equipos de 3-4 estudiantes)  
**Ponderación:** 25% del curso total  
**Duración:** 2 semanas completas  
**Entrega:** Notebook de Jupyter + video de exposición (YouTube)

---

## Contexto del Problema

Eres parte de un equipo de **analistas de datos junior** que ha sido contratado por un club profesional de fútbol para desarrollar su **primer sistema de inteligencia artificial** para apoyo en decisiones estratégicas. Este es un proyecto **piloto de alta visibilidad** que determinará si el club continuará invirtiendo en ciencia de datos.

**Situación crítica:** La directiva necesita evidencia concreta del valor de la analítica deportiva. Deben construir un sistema completo de predicción de resultados que no solo funcione técnicamente, sino que genere **insights accionables** para entrenadores y directivos.

**Expectativas del club:**
- Sistema predictivo que supere significativamente las predicciones por intuición
- Análisis profundo de factores que determinan victorias
- Recomendaciones tácticas basadas en datos
- Presentación ejecutiva clara para stakeholders no técnicos
- Documentación completa para futuras expansiones del sistema

**Complejidad del reto:** Este proyecto integra **todos los conocimientos del curso** (Python, pandas, visualización, machine learning) en un entregable de **calidad profesional** que simula un encargo real de la industria deportiva.

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
| **Video de presentación** | Comunicación clara, técnicamente precisa, audiencia apropiada, enlace funcional en notebook | Presentación básica comprensible, enlace incluido | Presentación confusa o técnicamente incorrecta, enlace faltante/no funcional | No presenta video o enlace |

### Notas Importantes:
- **Requisito mínimo**: Código debe ejecutar sin errores fatales para obtener calificación aprobatoria
- **Trabajo en equipo**: Cada miembro debe contribuir activamente y esto debe ser evidente en el resultado final
- **Video obligatorio**: 3-4 minutos explicando resultados a audiencia no técnica (directiva del club)
- **Pregunta clave**: La reflexión crítica final debe demostrar comprensión madura de limitaciones y aplicaciones de ML

---

## Cronograma Sugerido

### Semana 1: Preparación Integral y Modelado Inicial

- **Días 1-2**: Formación de equipos, análisis detallado del dataset, definición de roles específicos
- **Días 3-4**: Completar Parte 1 (Preparación de datos) con exploración exhaustiva
- **Días 5-7**: Iniciar Parte 2 (Modelado predictivo) con experimentos preliminares

### Semana 2: Modelado Avanzado, Análisis y Síntesis Final

- **Días 1-3**: Completar Parte 2 (Modelado) y Parte 3 (Análisis e interpretación)
- **Días 4-5**: Optimización de modelos, validación rigurosa, documentación técnica completa
- **Días 6-7**: Reflexión final integral, grabación de video profesional, entrega final

---

## Consejos Útiles

### Para el Trabajo en Equipo

- **Distribución de roles especializados**: Líder técnico, especialista en datos, analista de modelos, comunicador ejecutivo
- **Reuniones de seguimiento**: Mínimo 4-5 sesiones de trabajo conjunto durante las 2+ semanas
- **Documento compartido avanzado**: Usar Google Colab con control de versiones para colaboración simultánea
- **Revisión cruzada especializada**: Cada miembro debe dominar y validar el trabajo de los demás
- **Gestión de proyecto**: Establecer milestones claros y distribución equitativa de carga de trabajo

### Para el Machine Learning Avanzado

- **Experimentación sistemática**: Probar múltiples configuraciones de modelos y documentar resultados
- **Validación rigurosa**: Implementar validación cruzada y análisis de robustez del modelo
- **Interpretación profunda**: No solo reportar métricas, sino explicar qué aprende el modelo
- **Optimización iterativa**: Refinar modelos basándose en análisis de errores y limitaciones
- **Documentación técnica**: Justificar cada decisión metodológica con razonamiento sólido

### Para la Presentación Ejecutiva

- **Audiencia objetivo**: Directivos de club y stakeholders que toman decisiones estratégicas
- **Narrativa persuasiva**: Problema → Solución → Valor → Recomendaciones → ROI potencial
- **Visuales de impacto**: Gráficos ejecutivos claros, evitar jerga técnica, enfocarse en insights
- **Casos de uso específicos**: Demostrar aplicaciones concretas para decisiones tácticas
- **Cronometraje estricto**: Practicar múltiples veces para mantener precisión en 3-4 minutos exactos

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

## Video de Presentación (OBLIGATORIO)

### Instrucciones para el Video

1. **Duración**: 3-4 minutos exactos
2. **Plataforma**: YouTube (puede ser no listado, pero debe ser accesible)
3. **Contenido**: Presentación ejecutiva dirigida a directivos del club
4. **Participación**: Todos los miembros del equipo deben participar visiblemente

### IMPORTANTE: Enlace en el Notebook

**Al final de su notebook, en una celda de Markdown claramente identificada, deben incluir:**

```markdown
## 📹 Video de Presentación del Equipo

**Enlace al video de YouTube:** [TÍTULO DEL VIDEO](URL_DEL_VIDEO_DE_YOUTUBE)

**Integrantes del equipo:**
- Nombre Completo 1 (Matrícula)
- Nombre Completo 2 (Matrícula) 
- Nombre Completo 3 (Matrícula)
- Nombre Completo 4 (Matrícula)

**Fecha de grabación:** DD/MM/AAAA
```

### Estructura Sugerida del Video

1. **Introducción** (30 seg): Presentación del equipo y contexto del problema
2. **Metodología** (60 seg): Explicación simple de los datos y el modelo usado
3. **Resultados clave** (90 seg): 2-3 insights principales con visualizaciones
4. **Recomendaciones** (60 seg): Aplicaciones prácticas para el club

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

# Banco de Preguntas Canvas - Bloque 3

## Introducción al Modelado Predictivo Simple en Fútbol

**Instrucciones para Canvas:**

- Preguntas de opción múltiple: 4 opciones (A, B, C, D)
- Preguntas numéricas: respuesta exacta o calculable (tolerancia 5% si aplica)
- Selección aleatoria de 20-25 preguntas por examen
- Tiempo sugerido: 45-50 minutos
- Etiquetas cognitivas: [R]=Recuerdo, [C]=Concepto, [A]=Aplicación, [S]=Socrática/Interpretativa

---

## Alcance y Cobertura del Bloque 3

Conceptos esenciales (permitidos por lineamientos):

1. Vocabulario ML básico (modelo, entrenamiento, predicción, precisión, datos de prueba)
2. Preparación simple de datos (selección columnas, variables derivadas simples)
3. División train/test
4. Modelos permitidos: Regresión Lineal, Regresión Logística, Random Forest básico
5. Métrica básica: precisión (clasificación) o error absoluto medio simplificado (si se desea 1-2 ítems)
6. Overfitting como "memorizar" vs generalizar
7. Interpretación simple de importancia de variables (solo con bosque aleatorio de forma cualitativa)

---

## Segmentación Núcleo (Core) vs Banco Extendido

Tamaño inicial propuesto: 80 preguntas (Core 60 + Extended 20). Se podrá ampliar a 100+ tras primeras aplicaciones.

### Núcleo (60 preguntas)

Cobertura balanceada: vocabulario, flujo de trabajo, preparación, división, uso de 1 modelo, interpretación básica, overfitting, precisión.
Preguntas Núcleo: 1–60.

### Banco Extendido (20 preguntas)

Preguntas 61–80: escenarios interpretativos [S], comparaciones entre modelos, matices sobre mejoras simples y reflexión ética básica (uso responsable de datos deportivos juveniles).

### Distribución Cognitiva Objetivo (aprox)

- [R] Recuerdo: ~22
- [C] Concepto: ~20
- [A] Aplicación: ~25
- [S] Socrática/Interpretativa: ~13
(La suma excede 60 porque Extended añade parte de [S]; dentro del Núcleo se mantienen ~5–6 [S]).

### Uso Sugerido

- Evaluaciones formales iniciales: muestrear mayormente Núcleo (≥85%).
- Conforme avanza la semana 14–15 se añaden más ítems Extended.

---

## SEMANA 11: FUNDAMENTOS DE MODELADO

### Vocabulario y Flujo

**1. [R]** En este curso, "modelo" se compara con:
A) Un estadio
B) Un entrenador que aprende patrones
C) Un árbitro
D) Un aficionado
**Respuesta: B**

**2. [C]** "Entrenar un modelo" significa:
A) Memorizar únicamente los resultados exactos
B) Ajustar parámetros internos usando datos históricos
C) Editar manualmente las respuestas
D) Mezclar datos de prueba y entrenamiento sin orden
**Respuesta: B**

**3. [R]** ¿Qué parte de los datos usamos para evaluar si el modelo generaliza?
A) Datos de entrenamiento
B) Datos de prueba
C) Datos eliminados
D) Variables derivadas
**Respuesta: B**

**4. [C]** ¿Qué acción se realiza primero en un flujo simple de ML?
A) Entrenar
B) Dividir train/test
C) Interpretar importancia de variables
D) Instalar librerías
**Respuesta: B**

**5. [R]** En scikit-learn, la función para dividir datos es:
A) `split_train_test()`
B) `train_test_split()`
C) `make_split()`
D) `test_train_division()`
**Respuesta: B**

**6. [A] (Numérica)** Si divides datos con `test_size=0.2` y tienes 250 partidos, ¿cuántos quedan para entrenamiento (aprox)?
**Respuesta: 200**

**7. [C]** Usar `random_state=42` ayuda a:
A) Aumentar precisión siempre
B) Reproducir el mismo corte en múltiples ejecuciones
C) Evitar overfitting automáticamente
D) Reducir el tamaño del dataset
**Respuesta: B**

**8. [R]** La variable objetivo al predecir victoria local se suele codificar como:
A) Texto "sí" / "no"
B) 1 para gana local, 0 para no gana
C) -1 para derrota, 0 empate, 1 victoria (siempre)
D) Un número aleatorio
**Respuesta: B**

**9. [C]** Una métrica adecuada para clasificación binaria básica aquí es:
A) Precisión
B) Media harmónica de goles
C) Varianza de los tiros
D) Promedio de temporadas
**Respuesta: A**

**10. [R]** ¿Qué método entrenaría un RandomForestClassifier?
A) `modelo.learn()`
B) `modelo.train()`
C) `modelo.fit()`
D) `modelo.run()`
**Respuesta: C**

### Overfitting y Generalización

**11. [C]** Overfitting en analogía futbolística es como:
A) Un entrenador que prueba nuevas tácticas
B) Un entrenador que memoriza jugadas sin entender el juego
C) Un aficionado que ve el marcador final
D) Un jugador lesionado
**Respuesta: B**

**12. [R]** Un síntoma de overfitting sería:
A) Alta precisión en entrenamiento y baja en prueba
B) Baja en entrenamiento y alta en prueba
C) Ambas bajas
D) Ambas altas y estables
**Respuesta: A**

**13. [A]** Si tu modelo tiene 95% precisión en entrenamiento y 62% en prueba, ¿qué sospechas?
A) Dataset balanceado
B) Overfitting
C) Subentrenamiento imposible
D) Nada, es normal
**Respuesta: B**

**14. [S]** Si solo agregas más árboles a un Random Forest, ¿qué podría pasar si ya sobreajusta?
A) Siempre se arregla
B) Empeora o no mejora generalización
C) Se convierte en regresión
D) Pierde datos
**Respuesta: B**

**15. [C]** Reducir overfitting puede incluir:
A) Eliminar división train/test
B) Añadir variables irrelevantes
C) Limitar profundidad del bosque
D) Mezclar etiquetas
**Respuesta: C**

### Preparación de Datos

**16. [R]** Crear `total_goles = goles_local + goles_visitante` es un ejemplo de:
A) Modelado avanzado
B) Variable derivada simple
C) Ruido
D) División de datos
**Respuesta: B**

**17. [A]** Si tu DataFrame tiene columnas `goles_local`, `goles_visitante`, `tiros_local`, ¿cuál lista de características es válida?
A) `['goles_local','goles_visitante','tiros_local']`
B) `['resultado_final']` siempre
C) `[goles_local, goles_visitante, tiros_local]` sin comillas
D) `['goles_local + goles_visitante']`
**Respuesta: A**

**18. [C]** ¿Por qué no usarías demasiadas columnas irrelevantes?
A) Aumenta interpretabilidad
B) Puede introducir ruido y empeorar generalización
C) Disminuye tiempo de cómputo siempre
D) Asegura mejor precisión en prueba
**Respuesta: B**

**19. [A] (Numérica)** Si creas `gana_local` como 1 cuando goles_local > goles_visitante y tienes 18 victorias locales de 40 partidos, ¿qué proporción (baseline) tendrías? (Respuesta en decimal redondeada a 2)
**Respuesta: 0.45**

**20. [S]** ¿Por qué comparar tu precisión con la baseline es importante?
A) Para inflar resultados
B) Para saber si el modelo supera predecir siempre la clase mayoritaria
C) Para eliminar datos de prueba
D) Para usar más árboles
**Respuesta: B**

### Modelos Permitidos

**21. [R]** ¿Qué clase de scikit-learn usas para clasificación binaria básica (además de Random Forest)?
A) `LinearRegression`
B) `LogisticRegression`
C) `KMeans`
D) `PCA`
**Respuesta: B**

**22. [C]** Regresión Lineal se usa en este curso para:
A) Predecir categoría de victoria
B) Predecir un valor numérico (ej. goles totales futuros)
C) Reducir dimensiones
D) Agrupar equipos
**Respuesta: B**

**23. [A]** Si deseas predecir número de goles totales y obtienes error medio absoluto (MAE) de 0.8, ¿qué significa?
A) En promedio te equivocas en 0.8 goles
B) Siempre aciertas exacto
C) Error sin interpretación
D) El modelo es inválido
**Respuesta: A**

**24. [R]** ¿Qué parámetro fija el número de árboles en RandomForestClassifier?
A) `n_trees`
B) `n_estimators`
C) `trees`
D) `n_random`
**Respuesta: B**

**25. [C]** Limitar `max_depth` en un bosque ayuda a:
A) Ignorar variables
B) Reducir overfitting
C) Aumentar sobreajuste
D) Mezclar etiquetas
**Respuesta: B**

### Métricas y Evaluación

**26. [R]** "Precisión" en clasificación es:
A) (Predicciones correctas) / (Total predicciones)
B) (Goles locales) / (Goles visitantes)
C) (Errores) / (Total goles)
D) (Victorias) / (Empates)
**Respuesta: A**

**27. [A] (Numérica)** Si tu modelo acierta 34 de 50 partidos, ¿precisión? (decimal 2)
**Respuesta: 0.68**

**28. [C]** Una matriz de confusión muestra:
A) Importancia exacta de cada variable
B) Verdaderos/ falsos positivos y negativos
C) Solo precisión
D) Árboles del bosque
**Respuesta: B**

**29. [A]** Si tu baseline (mayoría clase) es 0.60 y tu modelo 0.62, ¿qué conclusión cautelosa?
A) Mejora marginal que debe analizarse si vale el esfuerzo
B) Victoria aplastante
C) Sobreajuste severo
D) Precisión perfecta
**Respuesta: A**

**30. [S]** Si tu precisión cae al añadir una variable irrelevante, ¿qué aprendiste?
A) Que siempre se deben añadir más columnas
B) Que variables irrelevantes pueden introducir ruido
C) Que la métrica es inútil
D) Que debes eliminar train/test split
**Respuesta: B**

### Interpretación Básica

**31. [R]** En Random Forest, importancia de variables indica:
A) Orden alfabético
B) Contribución a reducir errores de predicción
C) Tamaño del dataset
D) Número de iteraciones
**Respuesta: B**

**32. [A]** Si `total_goles` tiene mayor importancia que `tiros_local`, interpretas que:
A) No sirve para nada
B) Aporta más a las divisiones internas de los árboles
C) Debe eliminarse
D) Es ruido puro
**Respuesta: B**

**33. [S]** Si dos variables tienen importancias casi iguales, ¿qué haces?
A) Eliminar ambas
B) Considerar que aportan señal similar y evaluar redundancia gradual
C) Forzar quedarse con una ciegamente
D) Añadir más árboles sin revisar
**Respuesta: B**

**34. [A]** Si tras eliminar una variable irrelevante la precisión se mantiene igual, ¿qué concluyes?
A) La variable no aportaba
B) Eliminación dañó el modelo
C) Métrica rota
D) Perdió reproducibilidad
**Respuesta: A**

**35. [C]** ¿Por qué limitar el número de modelos probados en este curso?
A) Para evitar confundir con exceso de complejidad y centrarse en fundamentos
B) Porque scikit no soporta más
C) Para subir artificialmente precisión
D) Para usar menos memoria
**Respuesta: A**

### Comparaciones y Mejora Simple

**36. [A]** Entrenas Regresión Logística y Random Forest; RF obtiene 0.70 y RL 0.68. ¿Acción razonable inicial?
A) Conservar ambos y explicar diferencia ligera
B) Declarar RL inválida
C) Ajustar hiperparámetros avanzados ya
D) Fusionar modelos
**Respuesta: A**

**37. [S]** Si un modelo más sencillo (RL) rinde casi igual que RF, ¿por qué podría preferirse?
A) Siempre gana en precisión máxima
B) Suele ser más interpretable y suficiente
C) Es obligatorio
D) Genera más overfitting
**Respuesta: B**

**38. [R]** Agregar una sola nueva variable derivada debe:
A) Exigir tuning masivo
B) Poder implementarse en pocas líneas y explicar su aporte
C) Requerir 100 árboles extra
D) Eliminar baseline
**Respuesta: B**

**39. [A] (Numérica)** Si añadido `diferencia_goles = goles_local - goles_visitante` y precisión sube de 0.62 a 0.66, incremento absoluto:
**Respuesta: 0.04**

**40. [C]** Un pequeño incremento de 0.02 en precisión puede ser:
A) Ignorado siempre
B) Valioso si es consistente y supera baseline
C) Evidencia de error irreparable
D) Demostración de sobreajuste
**Respuesta: B**

### Ética y Uso Responsable (Extended Inicio)

**41. [S]** ¿Por qué evitar usar datos personales sensibles de jugadores jóvenes?
A) No dan precisión
B) Protección de privacidad y ética educativa
C) Porque lo exige siempre el modelo
D) Bloquea scikit
**Respuesta: B**

**42. [C]** Un riesgo de usar datos sin anonimizar es:
A) Mejora la precisión garantizada
B) Exponer información privada
C) Aumentar reproducibilidad
D) Reducir tamaño de dataset
**Respuesta: B**

**43. [R]** "Baseline" se refiere a:
A) Modelo optimizado al máximo
B) Referencia simple (como predecir la clase mayoritaria)
C) Error mínimo posible
D) Cualquier valor al azar
**Respuesta: B**

**44. [A]** Si tu baseline es 0.55 y modelo 0.70, mejora absoluta:
**Respuesta: 0.15**

**45. [S]** ¿Por qué no reportar solo precisión sin contexto baseline?
A) Porque siempre es mala
B) Porque puede exagerar logros reales
C) Porque baseline reemplaza al modelo
D) Porque Canvas lo prohíbe
**Respuesta: B**

### Escenarios de Interpretación (Extended)

**46. [A]** Tienes importancias: total_goles 0.40, tiros_local 0.25, tiros_arco_local 0.23, goles_visitante 0.12. ¿Qué variable añadirías para explorar? (Respuesta abierta sugerida: quizá posesión si existiera)
**Respuesta: posesion (u otra justificable)**

**47. [S]** Si tu modelo sube de 0.60 a 0.90 tras añadir una variable futura (resultado final), ¿qué detectas?
A) Mejora legítima
B) Fuga de datos (data leakage)
C) Falta de entrenamiento
D) Métrica rota
**Respuesta: B**

**48. [C]** Data leakage significa:
A) Modelo con pocos árboles
B) Usar información que no estaría disponible al momento de predecir
C) Bajar precisión
D) Guardar el modelo sin extensión
**Respuesta: B**

**49. [A]** Con 100 partidos: victorias local 58, resto 42. Baseline decimal (2):
**Respuesta: 0.58**

**50. [R]** Para obtener probabilidades en Regresión Logística usas:
A) `predict_proba()`
B) `predict_log()`
C) `probabilities()`
D) `score_prob()`
**Respuesta: A**

### Matriz de Confusión y Error (Extended)

**51. [A]** Matriz de confusión muestra 10 FN y 40 VP. ¿Qué significa uno de esos FN?
A) Predijo victoria local y ocurrió victoria local
B) Predijo no victoria local pero sí ganó
C) Predijo no victoria local y no ganó
D) Ninguna clase evaluada
**Respuesta: B**

**52. [S]** Si tienes 30 FP (predijo victoria local pero no ganó) ¿qué reflexión haces?
A) Modelo muy conservador
B) Podría estar sesgado hacia clase positiva
C) Modelo perfecto
D) Precisión siempre mejora
**Respuesta: B**

**53. [C]** Para reducir FP podrías:
A) Eliminar train/test split
B) Probar ajustar umbral de decisión (si tuvieras probabilidades)
C) Aumentar baseline
D) Mezclar etiquetas
**Respuesta: B**

**54. [A] (Numérica)** 38 aciertos de 55 predicciones. Precisión (2 decimales):
**Respuesta: 0.69**

**55. [S]** Si tu precisión apenas sube al añadir variable compleja, ¿la mantienes?
A) Sí solo si añade interpretación útil
B) Siempre sí
C) Siempre no
D) Nunca revisar
**Respuesta: A**

**56. [R]** Variable categórica codificada como 0/1 representa:
A) Regresión avanzada
B) Conversión simple a indicador binario
C) Eliminación de sesgo
D) Reducción de precisión
**Respuesta: B**

**57. [A]** Si cambias test_size de 0.2 a 0.4 ¿qué efecto inmediato?
A) Más datos para entrenar
B) Menos datos para entrenar y evaluación con más casos
C) Divisiones múltiples simultáneas
D) Quita baseline
**Respuesta: B**

**58. [C]** Limitar número de variables reduce:
A) Riesgo de ruido y sobreajuste potencial
B) Claridad del modelo
C) Reproducibilidad
D) Interpretabilidad
**Respuesta: A**

**59. [R]** `accuracy_score(y_test, preds)` devuelve:
A) Vector de errores
B) Porcentaje (decimal) de aciertos
C) Número de columnas
D) Lista de variables
**Respuesta: B**

**60. [S]** Si dos estudiantes reportan misma precisión pero uno no muestra baseline ni matriz de confusión, ¿qué falta?
A) Nada
B) Contexto para evaluar el valor real de la precisión
C) Más árboles
D) Eliminación de variables
**Respuesta: B**

---

## BLOQUE 3 EXTENDED (61–80)

### Interpretación Avanzada Ligera y Escenarios

**61. [S]** Un modelo extra complejo obtiene +0.01 sobre RL simple. ¿Qué preguntas hacerte antes de adoptarlo?
A) Ninguna, siempre elegir complejidad
B) ¿Aporta interpretabilidad? ¿Es consistente la mejora? ¿Coste justificable?
C) ¿Puede memorizar todavía más?
D) ¿Cuántos goles faltan?
**Respuesta: B**

**62. [C]** Valor principal de mantener división reproducible:
A) Es obligatorio solo por convención
B) Permite comparar resultados de forma justa
C) Aumenta automáticamente precisión
D) Elimina ruido
**Respuesta: B**

**63. [A]** Precisión pasa 0.65 → 0.72 tras añadir `diferencia_tiros`. Mejora absoluta:
**Respuesta: 0.07**

**64. [S]** Si mejoras precisión sacrificando claridad (modelo opaco), ¿qué riesgo educativo hay?
A) Estudiantes comprenden más
B) Se pierde entendimiento de patrones reales
C) Notebook más corto
D) Menos baseline
**Respuesta: B**

**65. [R]** `LogisticRegression()` por defecto aplica qué tipo de modelo:
A) Clasificación binaria probabilística
B) Bosque de árboles
C) Agrupamiento
D) Red neuronal profunda
**Respuesta: A**

**66. [A]** Si tu baseline es 0.52 y modelo 0.70, mejora relativa (% sobre baseline, redondear 2): ((0.70-0.52)/0.52)
**Respuesta: 0.35**

**67. [S]** ¿Por qué documentar cada variable añadida?
A) Para extender código innecesariamente
B) Para justificar su aporte y mantener trazabilidad
C) Para aumentar complejidad
D) Para ocultar supuestos
**Respuesta: B**

**68. [C]** Diferencia clave entre precisión y baseline:
A) Baseline siempre mayor
B) Baseline es referencia simple, precisión mide desempeño del modelo real
C) Son idénticas
D) Baseline ignora datos
**Respuesta: B**

**69. [A] (Numérica)** Aciertos: 48 de 80. Precisión (2 decimales):
**Respuesta: 0.60**

**70. [S]** Si reduces demasiadas variables y precisión cae mucho, ¿qué aprendiste?
A) Variables aportaban señal útil
B) Sobran variables
C) Baseline incorrecta
D) No importa dividir datos
**Respuesta: A**

**71. [C]** Objetivo principal de usar variables derivadas simples:
A) Aumentar complejidad
B) Capturar relaciones básicas explicables
C) Eliminar baseline
D) Duplicar columnas
**Respuesta: B**

**72. [S]** Si dos variables derivadas están muy correlacionadas, ¿qué efecto posible?
A) Ruido redundante sin beneficio claro
B) Siempre mejor precisión
C) Elimina overfitting
D) Quita reproducibilidad
**Respuesta: A**

**73. [A]** Después de añadir variable irrelevante precisión cae 0.66→0.63. Variación:
**Respuesta: -0.03**

**74. [R]** Función scikit para obtener probabilidades en Random Forest:
A) `predict()`
B) `predict_prob()`
C) `predict_proba()`
D) `probabilities()`
**Respuesta: C**

**75. [C]** ¿Por qué comparar dos modelos sencillos antes de complejizar?
A) Para evitar trabajo
B) Para tener base clara de mejora incremental
C) Para inflar baseline
D) Para eliminar train/test
**Respuesta: B**

**76. [S]** ¿Qué indica que tu modelo y baseline están muy cerca (<0.02)?
A) Modelo quizá no extrae patrones relevantes aún
B) Modelo perfecto
C) Overfitting extremo
D) Baseline inválida
**Respuesta: A**

**77. [A] (Numérica)** Baseline 0.58, modelo 0.65. Diferencia absoluta:
**Respuesta: 0.07**

**78. [S]** ¿Cuándo vale la pena añadir explicación de importancia de variables?
A) Cuando ayuda a justificar decisiones y seleccionar mejoras simples
B) Nunca en modelos simples
C) Siempre aunque no aporte
D) Solo si precisión < baseline
**Respuesta: A**

**79. [C]** "Datos de prueba" se usan para:
A) Entrenar
B) Evaluar generalización
C) Crear variables derivadas
D) Ajustar hiperparámetros profundos
**Respuesta: B**

**80. [S]** Si precisión sube 0.05 pero modelo pierde interpretabilidad, ¿qué debería discutirse en un contexto educativo?
A) Balance entre claridad y mejora real
B) Solo la cifra final
C) Cómo ocultar variables
D) Eliminar baseline
**Respuesta: A**

---

## Resumen Distribución (Inicial)

- Total preguntas: 80
- Núcleo: 1–60 (60)
- Extended: 61–80 (20)
- Opción múltiple: 72
- Numéricas: 8 (preguntas: 6, 19, 27, 39, 44, 49, 54, 63, 66, 69, 73, 77) *ajustar conteo si se mueve alguna*
- Etiquetas aproximadas: [R] 22, [C] 20, [A] 25, [S] 13 (Extended concentra parte de [S])

### Próximos Pasos Sugeridos

- Monitorear desempeño por etiqueta (ajustar balance si [S] resulta demasiado desafiante).
- Ampliar a 100 preguntas añadiendo escenarios de mejora incremental y errores comunes.
- Revisar si se requiere separar precisión y baseline en ejercicios adicionales.

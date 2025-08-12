# Banco de Preguntas Canvas - Bloque 3

## Introducción al Modelado Predictivo Simple en Fútbol

**Instrucciones para Canvas:**

- Todas las preguntas son de opción múltiple: 4 opciones (A, B, C, D)
- 25 preguntas por examen (5 por cada semana del Bloque 3)
- Tiempo sugerido: 45-50 minutos
- Etiquetas cognitivas: [R]=Recuerdo, [C]=Concepto, [A]=Aplicación

---

## Distribución de Preguntas por Semana

**Semana 11: Fundamentos de modelado** (5 preguntas)
**Semana 12: Modelos avanzados y clasificación** (5 preguntas)  
**Semana 13: Métricas avanzadas y evaluación** (5 preguntas)
**Semana 14: Feature engineering y optimización** (5 preguntas)
**Semana 15: Proyecto final integrador** (5 preguntas)

### Distribución Cognitiva

- [R] Recuerdo: 8 preguntas
- [C] Concepto: 12 preguntas  
- [A] Aplicación: 5 preguntas

**Nota:** Todas las preguntas son de opción múltiple para facilitar la evaluación automática en Canvas.

---

## SEMANA 11: FUNDAMENTOS DE MODELADO

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

**3. [R]** En scikit-learn, la función para dividir datos es:
A) `split_train_test()`
B) `train_test_split()`
C) `make_split()`
D) `test_train_division()`
**Respuesta: B**

**4. [A]** Si divides datos con `test_size=0.2` y tienes 250 partidos, ¿cuántos quedan para entrenamiento aproximadamente?
A) 50
B) 200
C) 250
D) 300
**Respuesta: B**

**5. [C]** Overfitting en analogía futbolística es como:
A) Un entrenador que prueba nuevas tácticas
B) Un entrenador que memoriza jugadas sin entender el juego
C) Un aficionado que ve el marcador final
D) Un jugador lesionado
**Respuesta: B**

---

## SEMANA 12: MODELOS AVANZADOS Y CLASIFICACIÓN

**6. [R]** ¿Qué clase de scikit-learn usas para clasificación binaria básica (además de Random Forest)?
A) LinearRegression
B) LogisticRegression
C) KMeans
D) DecisionTreeRegressor
**Respuesta: B**

**7. [A]** Si tu DataFrame tiene columnas `goles_local`, `goles_visitante`, `tiros_local`, ¿cuál lista de características es válida?
A) `['goles_local','goles_visitante','tiros_local']`
B) `['resultado_final']` siempre
C) `[goles_local, goles_visitante, tiros_local]` sin comillas
D) `['goles_local + goles_visitante']`
**Respuesta: A**

**8. [C]** ¿Por qué no usarías demasiadas columnas irrelevantes?
A) Aumenta interpretabilidad
B) Puede introducir ruido y empeorar generalización
C) Disminuye tiempo de cómputo siempre
D) Asegura mejor precisión en prueba
**Respuesta: B**

**9. [R]** En Random Forest, importancia de variables indica:
A) Orden alfabético
B) Contribución a reducir errores de predicción
C) Tamaño del dataset
D) Número de iteraciones
**Respuesta: B**

**10. [A]** Entrenas Regresión Logística y Random Forest; RF obtiene 0.70 y RL 0.68. ¿Acción razonable inicial?
A) Conservar ambos y explicar diferencia ligera
B) Declarar RL inválida
C) Ajustar hiperparámetros avanzados ya
D) Fusionar modelos
**Respuesta: A**

---

## SEMANA 13: MÉTRICAS AVANZADAS Y EVALUACIÓN

**11. [R]** "Precisión" en clasificación es:
A) (Predicciones correctas) / (Total predicciones)
B) (Goles locales) / (Goles visitantes)
C) (Errores) / (Total goles)
D) (Victorias) / (Empates)
**Respuesta: A**

**12. [A]** Si tu modelo acierta 34 de 50 partidos, ¿cuál es la precisión aproximada?
A) 0.50
B) 0.68
C) 0.75
D) 0.85
**Respuesta: B**

**13. [C]** Una matriz de confusión muestra:
A) Importancia exacta de cada variable
B) Verdaderos/ falsos positivos y negativos
C) Solo precisión
D) Árboles del bosque
**Respuesta: B**

**14. [A]** Si tu baseline (mayoría clase) es 0.60 y tu modelo 0.62, ¿qué conclusión cautelosa?
A) Mejora marginal que debe analizarse si vale el esfuerzo
B) Victoria aplastante
C) Sobreajuste severo
D) Precisión perfecta
**Respuesta: A**

**15. [R]** Un síntoma de overfitting sería:
A) Alta precisión en entrenamiento y baja en prueba
B) Baja en entrenamiento y alta en prueba
C) Ambas bajas
D) Ambas altas y estables
**Respuesta: A**

---

## SEMANA 14: FEATURE ENGINEERING Y OPTIMIZACIÓN

**16. [R]** Crear `total_goles = goles_local + goles_visitante` es un ejemplo de:
A) Modelado avanzado
B) Variable derivada simple
C) Ruido
D) División de datos
**Respuesta: B**

**17. [A]** Si `total_goles` tiene mayor importancia que `tiros_local`, interpretas que:
A) No sirve para nada
B) Aporta más a las divisiones internas de los árboles
C) Debe eliminarse
D) Es ruido puro
**Respuesta: B**

**18. [A]** Si tras eliminar una variable irrelevante la precisión se mantiene igual, ¿qué concluyes?
A) La variable no aportaba
B) Eliminación dañó el modelo
C) Métrica rota
D) Perdió reproducibilidad
**Respuesta: A**

**19. [C]** Si añades `diferencia_goles = goles_local - goles_visitante` y la precisión mejora, esto sugiere que:
A) La variable es irrelevante
B) La diferencia de goles es predictiva para el resultado
C) El modelo está roto
D) Necesitas más datos
**Respuesta: B**

**20. [A]** Si añadido `diferencia_goles` la precisión sube de 0.62 a 0.66, ¿cuál es el incremento absoluto?
A) 0.04
B) 0.4
C) 4%
D) 0.94
**Respuesta: A**

---

## SEMANA 15: PROYECTO FINAL INTEGRADOR

**21. [C]** ¿Por qué limitar el número de modelos probados en este curso?
A) Para evitar confundir con exceso de complejidad y centrarse en fundamentos
B) Porque scikit no soporta más
C) Para subir artificialmente precisión
D) Para usar menos memoria
**Respuesta: A**

**22. [C]** Si un modelo más sencillo (RL) rinde casi igual que RF, ¿por qué podría preferirse?
A) Siempre gana en precisión máxima
B) Suele ser más interpretable y suficiente
C) Es obligatorio
D) Genera más overfitting
**Respuesta: B**

**23. [A]** ¿Por qué comparar tu precisión con la baseline es importante?
A) Para inflar resultados
B) Para saber si el modelo supera predecir siempre la clase mayoritaria
C) Para eliminar datos de prueba
D) Para usar más árboles
**Respuesta: B**

**24. [A]** Si creas `gana_local` como 1 cuando goles_local > goles_visitante y tienes 18 victorias locales de 40 partidos, ¿qué proporción baseline tendrías?
A) 0.45
B) 0.55
C) 0.18
D) 0.40
**Respuesta: A**

**25. [C]** Si tu precisión cae al añadir una variable irrelevante, ¿qué aprendiste?
A) Que siempre se deben añadir más columnas
B) Que variables irrelevantes pueden introducir ruido
C) Que la métrica es inútil
D) Que debes eliminar train/test split
**Respuesta: B**

---

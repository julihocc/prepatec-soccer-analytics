# Caso Práctico Bloque 3: ¿Podemos Predecir Quién Ganará la Champions League?

## El Desafío

Imagina que trabajas para el Real Madrid, Barcelona, o tu equipo favorito. El director técnico te hace una pregunta directa:

> *"¿Puedes crear un sistema que nos ayude a entender qué factores realmente determinan si ganamos o perdemos un partido? Necesito datos, no solo intuición."*

Tu misión es **construir desde cero** un sistema predictivo que analice partidos históricos de la Champions League y descubra los secretos ocultos en los datos.

## ¿Qué Vas a Descubrir?

Este proyecto te desafiará a:

1. **Investigar como detective**: ¿Qué patrones ocultos hay en los datos de fútbol?
2. **Pensar como estratega**: ¿Qué variables realmente importan para ganar?
3. **Experimentar libremente**: Probar diferentes enfoques y ver qué funciona
4. **Comunicar como profesional**: Explicar tus hallazgos a gente no técnica
5. **Ser crítico contigo mismo**: Reconocer limitaciones y proponer mejoras

## Los Datos: Tu Materia Prima

Tienes acceso a un dataset real de la UEFA Champions League con información de cientos de partidos. Incluye desde lo básico (goles, equipos) hasta estadísticas avanzadas (posesión, eficiencia, tarjetas).

**Pero aquí está el reto**: Nadie te va a decir exactamente cómo usarlos. Eres libre de explorar, crear nuevas variables, descartar las que no sirven, y experimentar con diferentes combinaciones.

---

## Parte 1: Detective de Datos (30 puntos)

### Misión: Descubre los Secretos Ocultos

Tu primera misión es convertirte en un detective de datos. No te voy a decir exactamente qué buscar - eso es lo emocionante. Tu trabajo es explorar libremente y encontrar patrones que ni siquiera sabías que existían.

#### Preguntas que Debes Responder (15 puntos)

**Elige 3 de estas preguntas y respóndelas de manera creativa:**

1. ¿Existe realmente la "ventaja de casa" en la Champions? ¿Es igual para todos los equipos?
2. ¿Hay equipos que son sistemáticamente mejores "cerrando" partidos en la segunda mitad?
3. ¿Los equipos que reciben más tarjetas tienden a perder más seguido? ¿O es al revés?
4. ¿Qué combinaciones de estadísticas predicen mejor una victoria aplastante (3+ goles de diferencia)?
5. ¿Hay patrones temporales? ¿Los equipos juegan diferente en fases grupales vs eliminatorias?

**La clave**: No me muestres solo números. Cuenta una historia con tus datos. Usa gráficos creativos, analogías deportivas, y descubrimientos que te sorprendieron.

#### Tu Análisis Exploratorio Personal (15 puntos)

Aquí tienes **libertad total**. Explora los datos como quieras y encuentra algo interesante que nadie más haya notado. Algunas ideas para inspirarte (pero no te limites a esto):

- Crear nuevas variables que combinen estadísticas existentes
- Comparar diferentes tipos de equipos (ofensivos vs defensivos)  
- Analizar cómo cambian las tácticas entre temporadas
- Investigar si ciertos estilos de juego son más exitosos

**Criterio de evaluación**: Originalidad de tu análisis + Calidad de las conclusiones + Creatividad en la presentación

---

## Parte 2: Arquitecto de Predicciones (40 puntos)

### Misión: Construye Tu Propio Sistema Predictivo

Ahora viene la parte emocionante: crear un modelo que pueda predecir resultados. Pero aquí está el twist - **no hay una forma "correcta" de hacerlo**. Tu creatividad y experimentación valen más que seguir un tutorial.

#### El Desafío Central (25 puntos)

**Tu objetivo**: Crear un sistema que prediga si el equipo local ganará o no. Pero las decisiones importantes las tomas tú:

- **¿Qué variables usarás?** Puedes usar todas, algunas, o crear nuevas combinaciones
- **¿Qué tipo de modelo?** Random Forest, regresión logística, o experimenta con varios
- **¿Cómo definirás "éxito"?** ¿Solo te importa la precisión? ¿O prefieres no equivocarte en ciertos tipos de partidos?

**Lo que SÍ necesitas hacer**:
1. Dividir tus datos en entrenamiento y prueba (tú decides la proporción)
2. Entrenar al menos un modelo de machine learning
3. Evaluar qué tan bueno es tu modelo
4. **Ser honesto** sobre sus limitaciones

#### Experimentación Libre (15 puntos)  

Aquí es donde puedes brillar siendo creativo:

- **Prueba diferentes enfoques**: ¿Qué pasa si predices solo partidos de equipos grandes? ¿O si creas modelos separados para fases grupales vs eliminatorias?
- **Innova con las variables**: ¿Qué tal si creas un "índice de agresividad" combinando tarjetas y faltas? ¿O una "eficiencia ofensiva" que vaya más allá de goles/tiros?
- **Experimenta con el modelo**: ¿Funciona mejor con muchas variables o pocas? ¿Hay configuraciones que mejoran los resultados?

**La regla de oro**: Documenta tus experimentos. Cuenta qué probaste, qué funcionó, qué no, y por qué crees que pasó.

---

## Parte 3: Intérprete Estratégico (30 puntos)

### Misión: Convierte Datos en Sabiduría Táctica

Los números por sí solos no significan nada si no puedes explicar qué implican para el mundo real. Esta es tu oportunidad de demostrar que entiendes tanto la técnica como el fútbol.

#### Análisis de Tu Modelo (15 puntos)

**Responde estas preguntas con profundidad**:

1. **¿Qué aprendió tu modelo?** ¿Cuáles variables considera más importantes? ¿Te sorprende?
2. **¿Dónde se equivoca más?** Usa matriz de confusión y ejemplos concretos
3. **¿Qué tipo de partidos predice mejor?** ¿Los cerrados? ¿Los de muchos goles?
4. **¿Cómo cambiarían las tácticas basándose en tu modelo?** Si fueras entrenador, ¿qué harías diferente?

#### Aplicación al Mundo Real (15 puntos)

**Elige UNA de estas situaciones y desarrollala completamente**:

**Situación A**: Eres analista del Real Madrid antes de la final de Champions. Basándote en tu modelo, ¿qué recomendaciones tácticas específicas darías al entrenador?

**Situación B**: Un equipo de la Premier League te contrata para ayudarles a clasificar a Champions. ¿Cómo adaptarías tu modelo? ¿Qué limitaciones tendría?

**Situación C**: Una casa de apuestas quiere usar tu modelo para establecer cuotas. ¿Qué les dirías sobre su confiabilidad? ¿Cuáles son los riesgos?

**Criterio clave**: Demuestra que entiendes las limitaciones de tu modelo y puedes comunicar hallazgos técnicos en lenguaje futbolístico.

---

## Tu Producto Final

### Lo Que Debes Entregar

**1. Tu Notebook/Script Completo**
- Tu análisis exploratorio con hallazgos originales
- El código de tu modelo predictivo (con comentarios que expliquen tus decisiones)
- Visualizaciones que cuenten historias interesantes
- Experimentación documentada: qué probaste y por qué

**2. Reporte Ejecutivo (1-2 páginas)**
Escribe como si fueras a presentar esto al director técnico de un equipo profesional:
- ¿Qué descubriste que no sabíamos antes?
- ¿Qué tan confiable es tu sistema predictivo?
- ¿Cómo podría un equipo usar estos hallazgos en la práctica?
- ¿Cuáles son las limitaciones y riesgos de tu modelo?

### Cómo Te Evaluaremos

**Creatividad y Experimentación (40%)**
- Originalidad en tu análisis exploratorio
- Innovación en tu enfoque de modelado
- Calidad de tus experimentos y variaciones
- Pensamiento crítico sobre tus resultados

**Aplicación Futbolística (30%)**
- Conexión entre hallazgos técnicos y realidad deportiva
- Recomendaciones prácticas y viables
- Comprensión de las limitaciones del modelo
- Comunicación clara a audiencia no técnica

**Rigor Técnico (30%)**
- Código funcional y bien documentado
- Uso apropiado de técnicas de machine learning
- Evaluación honesta de la calidad del modelo
- Metodología sólida en experimentación

### Consejos para Destacar

1. **Sé curioso**: Las mejores notas van para quienes encuentran patrones inesperados
2. **Experimenta libremente**: Prueba enfoques diferentes, documenta qué funciona y qué no
3. **Piensa como entrenador**: Conecta tus hallazgos con decisiones tácticas reales
4. **Sé honesto**: Reconocer limitaciones demuestra más madurez que pretender perfección
5. **Cuenta historias**: Los datos sin contexto deportivo son solo números

---

**¡Esto es TU proyecto!** No hay una respuesta "correcta". Los mejores trabajos serán los más creativos, reflexivos y conectados con la realidad del fútbol.

**Tiempo sugerido**: 6-8 horas de exploración, experimentación y análisis.  
**Modalidad**: Individual, pero puedes discutir ideas con compañeros.  
**Fecha límite**: [Definida por el profesor]

---

## Rúbrica de Evaluación Detallada

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
| **Documentación del proceso** | Experimentos bien documentados, decisiones justificadas | Documentación básica, algunas justificaciones | Documentación limitada o confusa | Sin documentación del proceso |
| **Comunicación técnica** | Explica conceptos complejos claramente, audiencia apropiada | Comunicación básica comprensible | Comunicación confusa o técnicamente incorrecta | No comunica hallazgos |

### Notas Importantes:
- **Requisito mínimo**: Código debe ejecutar sin errores fatales para obtener calificación aprobatoria
- **Creatividad valorada**: Enfoques innovadores recibirán puntuación adicional
- **Honestidad académica**: Reconocer limitaciones es más valioso que pretender perfección

---

## Cronograma Sugerido

### Semana 1: Exploración y Experimentación Inicial

- **Días 1-2**: Análisis exploratorio libre, identificación de patrones interesantes
- **Días 3-4**: Experimentación con diferentes variables y combinaciones
- **Días 5-7**: Construcción inicial de modelos, pruebas de diferentes enfoques

### Semana 2: Refinamiento y Análisis Profundo

- **Días 1-3**: Optimización de modelos, análisis de importancia de variables
- **Días 4-5**: Interpretación de resultados, conexión con contexto futbolístico
- **Días 6-7**: Documentación final, reflexiones críticas, preparación de entregables

---

## Recursos de Apoyo

### Dataset y Herramientas
- **Dataset Champions League**: Proporcionado por el profesor con documentación incluida
- **Librerías requeridas**: pandas, numpy, sklearn, matplotlib, seaborn
- **Entorno sugerido**: Jupyter Notebook o Google Colab

### Consultas y Soporte
- **Horario de oficina**: Disponible para dudas técnicas y metodológicas
- **Foros de discusión**: Para intercambio de ideas entre estudiantes (sin compartir código)
- **Documentación oficial**: Links a recursos de sklearn, pandas, etc.

### Ejemplos de Referencia

- **Análisis exploratorios**: Ejemplos de visualizaciones efectivas para datos deportivos
- **Interpretación de modelos**: Cómo explicar importancia de variables en contexto futbolístico
- **Presentación de resultados**: Formatos para comunicar hallazgos a audiencias no técnicas

---

## Entregables Específicos

### 1. Notebook Principal (`caso_bloque3_[TuNombre].ipynb`)

**Estructura mínima requerida:**

1. **Introducción y Objetivos** (1 sección)
   - Descripción de tu enfoque personal al problema
   - Hipótesis iniciales sobre qué factores pueden predecir mejor

2. **Análisis Exploratorio** (2-3 secciones)
   - Visualizaciones que revelen patrones interesantes
   - Estadísticas descriptivas relevantes para tu análisis
   - Al menos 3 insights únicos sobre los datos

3. **Construcción y Evaluación de Modelos** (2-3 secciones)
   - Experimentación con al menos 2 algoritmos diferentes
   - Evaluación comparativa de rendimiento
   - Análisis de importancia de variables/características

4. **Interpretación Futbolística** (1-2 secciones)
   - Conexión entre resultados técnicos y realidad deportiva
   - Casos específicos donde el modelo acierta o falla
   - Implicaciones para entrenadores, analistas o aficionados

5. **Reflexiones Finales** (1 sección)
   - Limitaciones de tu análisis
   - Posibles mejoras futuras
   - Aprendizajes personales del proceso

### 2. Documento de Reflexión (`reflexion_caso3_[TuNombre].pdf`)

**Extensión**: 2-3 páginas máximo, formato libre

**Preguntas guía para la reflexión** (no es cuestionario rígido):
- ¿Qué fue lo más sorprendente que descubriste en los datos?
- ¿Qué variables resultaron más importantes y por qué crees que es así?
- Si fueras un director técnico, ¿cómo usarías estos insights?
- ¿Qué limitaciones encontraste en tu análisis?
- ¿Cómo ha cambiado tu perspectiva sobre el análisis deportivo?

### 3. Presentación de Hallazgos (`presentacion_caso3_[TuNombre].pptx/pdf`)

**Formato**: 8-10 diapositivas máximo

**Contenido sugerido**:
- Slide 1: Tu enfoque único al problema
- Slides 2-4: Hallazgos clave del análisis exploratorio
- Slides 5-6: Comparación de modelos y mejores resultados
- Slides 7-8: Interpretación futbolística e implicaciones prácticas
- Slides 9-10: Limitaciones y oportunidades futuras

---

## Criterios de Evaluación por Entregable

### Notebook Principal (50% de la calificación total)
- **Código funcional y bien organizado** (20%)
- **Análisis técnico profundo** (15%)  
- **Creatividad en el enfoque** (10%)
- **Documentación clara** (5%)

### Documento de Reflexión (30% de la calificación total)
- **Profundidad de reflexión** (15%)
- **Conexión teoría-práctica** (10%)
- **Autocrítica y reconocimiento de limitaciones** (5%)

### Presentación de Hallazgos (20% de la calificación total)
- **Claridad comunicativa** (10%)
- **Síntesis efectiva de resultados** (5%)
- **Impacto visual y profesionalismo** (5%)

---

## Consejos Prácticos para el Éxito

### Gestión del Tiempo
- **No te obsesiones con la perfección técnica**: Enfócate en insights interesantes
- **Documenta mientras trabajas**: No dejes la reflexión para el final
- **Prueba rápido, itera frecuentemente**: Mejor varios enfoques simples que uno complejo

### Enfoque Analítico
- **Comienza con preguntas simples**: "¿Qué equipos tienen mejor rendimiento local vs visitante?"
- **Visualiza antes de modelar**: Las gráficas revelan patrones que guían el análisis
- **No ignores resultados inesperados**: Los "errores" del modelo pueden ser los insights más valiosos

### Comunicación Efectiva
- **Habla como analista deportivo, no como programador**: Tu audiencia ama el fútbol
- **Usa analogías deportivas**: "Este modelo es como un scout que identifica patrones..."
- **Sé honesto sobre limitaciones**: Reconocer problemas demuestra madurez analítica

### Conexión con el Contexto Real
- **Investiga un poco sobre los equipos**: Conocer su historia enriquece el análisis
- **Piensa como diferentes stakeholders**: ¿Qué le importaría a un entrenador vs un aficionado?
- **Propón aplicaciones concretas**: "Los equipos podrían usar esto para..."

---

## Apoyo Durante el Desarrollo

### ¿Cuándo Buscar Ayuda?
- **Errores técnicos bloqueantes**: Si tu código no ejecuta después de varios intentos
- **Interpretación de resultados confusos**: Cuando los números no tienen sentido deportivo
- **Dirección del análisis**: Si sientes que te perdiste o no sabes cómo continuar

### ¿Qué NO es Válido para Ayuda?
- **Escribir código por ti**: El análisis debe ser tu trabajo original
- **Elegir tu enfoque**: La creatividad y decisiones analíticas deben ser tuyas
- **Garantizar resultados**: No todos los experimentos funcionan, y eso está bien

### Recursos Disponibles
- **Documentación técnica**: Links directos a pandas, sklearn, etc.
- **Ejemplos metodológicos**: Patrones generales de análisis (sin soluciones específicas)
- **Sesiones de consulta**: Para discutir enfoques e interpretar resultados

---

## Fecha de Entrega y Modalidades

**Fecha límite**: [A definir por el profesor - mínimo 2 semanas de desarrollo]

**Modalidad de entrega**: 
- Subir archivos al LMS institucional
- Nombrar archivos con tu nombre: `caso_bloque3_[TuNombre].*`
- Formato aceptado: `.ipynb`, `.pdf`, `.pptx`

**Presentaciones orales**: [Opcional - a definir por el profesor]
- 5 minutos por estudiante
- Enfoque en hallazgos más interesantes
- Q&A breve con compañeros

---

**¡Recuerda**: Este caso práctico vale 25% de tu calificación total del curso. Invierte el tiempo necesario, pero sobre todo... ¡disfruta explorando el fascinante mundo donde el fútbol se encuentra con los datos!

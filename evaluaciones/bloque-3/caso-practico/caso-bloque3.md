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

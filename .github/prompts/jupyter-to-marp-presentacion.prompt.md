# Prompt para transformar una libreta Jupyter en presentación Marp/Markdown

Convierte la libreta Jupyter proporcionada en una presentación Markdown para Marp siguiendo estas reglas:

1. **Estructura socrática y pedagógica**:
   - Divide el contenido en 3 sesiones de 50 minutos, cada una con su propia sección y pregunta guía.
   - Cada sesión debe contener: introducción breve, teoría con analogía deportiva, práctica con código, reflexiones intermedias y síntesis.
   - Usa títulos claros para cada sesión y subsecciones para teoría, práctica, reflexión y síntesis.

2. **Formato de presentación**:
   - Usa `---` para separar cada slide.
   - El primer slide debe tener el título de la semana, pregunta motivadora y nombre oficial del curso/prepa.
   - Cada slide debe ser breve, visual y contener solo 1-2 ideas principales.
   - Incluye bloques de código solo cuando sean esenciales para la comprensión.

3. **Estilo y contenido**:
   - Todo en español, profesional y accesible para estudiantes de preparatoria.
   - Prohibido el uso de emojis.
   - Usa ejemplos y analogías futbolísticas en teoría y práctica.
   - Incluye preguntas reflexivas antes y después de los bloques de código.
   - Termina cada sesión con una síntesis y preguntas de autoevaluación.

4. **Nomenclatura y archivos**:
   - El archivo debe llamarse `[tema]-presentacion.md` y nunca sobrescribir el `.md` generado automáticamente por Jupytext.
   - Mantén la progresión gradual y no agregues contenido que exceda los 50 minutos por sesión.

5. **Ejemplo de slide**:

   ---
   # SESIÓN 1: ¿Por qué es importante explorar los datos antes de analizarlos? (50 min)
   ---
   ## Pregunta guía
   ¿Te has preguntado cómo un club de fútbol decide qué datos analizar primero?
   ---
   ### Teoría: El primer contacto con los datos
   - Antes de cualquier análisis, hay que conocer los datos
   - La exploración permite detectar errores, patrones y oportunidades
   ---
   ### Analogía deportiva
   Explorar datos es como un entrenador que observa a sus jugadores en el primer entrenamiento.
   ---
   ### Práctica: Cargando y observando un dataset real
   ```python
   import pandas as pd
   partidos = pd.DataFrame({...})
   print(partidos)
   ```
   ---
   ### Reflexión
   ¿Qué información puedes obtener solo con ver la tabla?
   ---
   ### Síntesis de la sesión 1
   - Exploración: primer paso crítico en ciencia de datos

6. **Revisa que la presentación resultante sea clara, breve y didáctica, lista para usarse en clase.**

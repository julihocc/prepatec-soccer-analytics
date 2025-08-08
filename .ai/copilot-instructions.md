# Instrucciones para GitHub Copilot

## Contexto Centralizado del Proyecto

**Para información completa del proyecto, consulta: [AI-CONTEXT.md](./AI-CONTEXT.md)**

## Instrucciones Específicas para GitHub Copilot

### Contexto del Proyecto
Este es un curso educativo de ciencia de datos aplicada al fútbol en **español** dirigido a estudiantes de preparatoria del Tecnológico de Monterrey.

### Directrices de Código
- **Variables en español:** `goles_por_partido`, `equipos_favoritos`, `datos_futbol`
- **Contexto futbolístico:** Usar equipos reales (Barcelona, Real Madrid, Manchester City)
- **Nivel educativo:** Explicaciones claras para estudiantes de preparatoria
- **ABSOLUTAMENTE SIN EMOJIS:** Mantener tono profesional y limpio sin emojis

### Patrones de Código Preferidos

```python
# Patrón de importación estándar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de seaborn
sns.set_theme(style="whitegrid", palette="viridis")

# Variables descriptivas en español
datos_futbol = pd.DataFrame(...)
goles_por_equipo = datos_futbol.groupby('equipo')['goles'].sum()

# Comentarios educativos
print("Este análisis nos muestra los patrones de goles!")
```

### Estructura de Notebooks
- Título en español: `# Semana X: [Título Descriptivo]`
- Objetivos de aprendizaje: `**Lo que aprenderemos hoy:**`
- Resumen: `### Lo que Aprendimos Hoy`
- Vista previa: `### Próxima Semana`

### Datasets y Referencias
- Dataset principal: "champs" en Kaggle
- Datos de ligas europeas para ejercicios avanzados
- Ejemplos con equipos reconocibles internacionalmente

---

**Contexto completo en:** [AI-CONTEXT.md](./AI-CONTEXT.md)

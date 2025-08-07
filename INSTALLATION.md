# Instalación de Dependencias

## Métodos de Instalación

### Método 1: Script Automático (Recomendado)
```bash
python install_dependencies.py
```

### Método 2: Instalación Manual
```bash
pip install -r requirements.txt
```

### Método 3: Desde Notebook
Si estás ejecutando un notebook, la primera celda instalará automáticamente todas las dependencias necesarias.

## Paquetes Incluidos

- **pandas**: Manipulación y análisis de datos
- **numpy**: Computación numérica
- **matplotlib**: Visualización básica
- **seaborn**: Visualización estadística avanzada
- **scikit-learn**: Machine learning
- **scipy**: Computación científica
- **jupyter**: Entorno de notebooks
- **plotly**: Visualización interactiva

## Verificación

Después de la instalación, verifica que todo funcione ejecutando:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

print("Todas las librerías instaladas correctamente")
```

## Solución de Problemas

Si encuentras errores durante la instalación:

1. **Actualiza pip**: `python -m pip install --upgrade pip`
2. **Verifica tu versión de Python**: Requiere Python 3.8+
3. **Instala individualmente**: `pip install pandas numpy matplotlib seaborn scikit-learn`

## Entorno Virtual (Opcional pero Recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

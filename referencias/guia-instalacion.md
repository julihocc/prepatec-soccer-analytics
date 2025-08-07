# Guía de Instalación y Configuración

## Requisitos del Sistema

### Requisitos Mínimos
- **Sistema Operativo:** Windows 10, macOS 10.14, o Linux Ubuntu 18.04+
- **RAM:** 4GB (recomendado 8GB+)
- **Espacio en disco:** 2GB libres
- **Procesador:** Intel i3 o equivalente AMD

### Requisitos Recomendados
- **RAM:** 8GB o más
- **Espacio en disco:** 5GB libres
- **Procesador:** Intel i5 o equivalente AMD
- **Conexión a internet:** Para descargar datasets y librerías

## Instalación de Python

### Opción 1: Anaconda (Recomendado)
1. Descargar Anaconda desde [anaconda.com](https://www.anaconda.com/)
2. Ejecutar el instalador
3. Seguir las instrucciones en pantalla
4. Verificar instalación:
   ```bash
   conda --version
   python --version
   ```

### Opción 2: Python.org
1. Descargar Python 3.8+ desde [python.org](https://www.python.org/)
2. Durante la instalación, marcar "Add Python to PATH"
3. Verificar instalación:
   ```bash
   python --version
   pip --version
   ```

## Configuración del Entorno

### Crear Entorno Virtual
```bash
# Con conda
conda create -n football-analytics python=3.8
conda activate football-analytics

# Con pip
python -m venv football-analytics
# En Windows
football-analytics\Scripts\activate
# En macOS/Linux
source football-analytics/bin/activate
```

## Instalación de Librerías

### Librerías Esenciales
```bash
pip install pandas numpy matplotlib seaborn jupyter scikit-learn
```

### Librerías Adicionales
```bash
pip install plotly dash streamlit requests beautifulsoup4
```

### Verificar Instalación
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
print(" Todas las librerías instaladas correctamente")
```

## Configuración de Jupyter Notebook

### Instalación
```bash
pip install jupyter notebook
```

### Configuración Básica
```bash
# Generar archivo de configuración
jupyter notebook --generate-config

# Instalar extensiones útiles
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable --py widgetsnbextension
```

### Extensiones Recomendadas
- **Variable Inspector:** Ver variables en tiempo real
- **Table of Contents:** Navegación por el notebook
- **Code Folding:** Colapsar secciones de código

## Descarga del Dataset

### Desde Kaggle
1. Crear cuenta en [kaggle.com](https://www.kaggle.com/)
2. Descargar dataset "champs": [kaggle.com/datasets/julihocc/champs](https://www.kaggle.com/datasets/julihocc/champs)
3. Colocar en carpeta `material-didactico/bloque-1/recursos/`

### Usando Kaggle API
```bash
# Instalar API de Kaggle
pip install kaggle

# Configurar credenciales (desde kaggle.com/account)
# Descargar kaggle.json y colocar en ~/.kaggle/

# Descargar dataset
kaggle datasets download -d julihocc/champs
```

## Estructura de Carpetas

```
material-didactico/
├── bloque-1/
│   ├── recursos/
│   │   └── champs.csv
│   ├── practica/
│   └── teoria/
├── bloque-2/
├── bloque-3/
├── videos/
└── referencias/
```

## Configuración de Git (Opcional)

```bash
# Instalar Git
# Windows: descargar de git-scm.com
# macOS: brew install git
# Linux: sudo apt-get install git

# Configurar usuario
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Clonar repositorio (si existe)
git clone [URL_DEL_REPOSITORIO]
```

## Solución de Problemas Comunes

### Error: "No module named 'pandas'"
```bash
# Verificar que el entorno virtual esté activado
conda activate football-analytics
# Reinstalar pandas
pip install pandas
```

### Error: "Jupyter command not found"
```bash
# Reinstalar jupyter
pip install --upgrade jupyter
# Verificar PATH
echo $PATH
```

### Error: "Permission denied"
```bash
# En Linux/macOS
sudo pip install [paquete]
# O usar --user
pip install --user [paquete]
```

### Error: "SSL Certificate"
```bash
# Actualizar pip
pip install --upgrade pip
# Usar trusted host
pip install --trusted-host pypi.org --trusted-host pypi.python.org [paquete]
```

## Configuración de VS Code (Opcional)

### Extensiones Recomendadas
- **Python:** Soporte completo para Python
- **Jupyter:** Soporte para notebooks
- **Python Docstring Generator:** Generar docstrings
- **GitLens:** Funcionalidades avanzadas de Git

### Configuración
```json
{
    "python.defaultInterpreterPath": "./football-analytics/bin/python",
    "jupyter.askForKernelRestart": false,
    "python.formatting.provider": "black"
}
```

## Verificación Final

### Script de Verificación
```python
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import jupyter

print(" Verificación del Entorno")
print("="*30)
print(f"Python version: {sys.version}")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")
print(f"Matplotlib version: {plt.matplotlib.__version__}")
print(f"Seaborn version: {sns.__version__}")
print(f"Scikit-learn version: {sklearn.__version__}")
print("\n ¡Entorno configurado correctamente!")
```

## Recursos de Ayuda

- **Documentación oficial:** [python.org](https://www.python.org/)
- **Anaconda:** [docs.anaconda.com](https://docs.anaconda.com/)
- **Jupyter:** [jupyter.org](https://jupyter.org/)
- **Stack Overflow:** Para problemas específicos

## Contacto

Para problemas de instalación o configuración, contacta al equipo docente durante las horas de oficina.

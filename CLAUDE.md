# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Spanish-language educational course** on data science applied to football/soccer analysis. The repository contains comprehensive course materials for a 15-week program teaching Python fundamentals, data science basics, and predictive modeling specifically within the context of football data.

**Target Audience:** High school level students (preparatoria)
**Language:** Spanish (all variables, comments, and content)
**Context:** Football/soccer data analysis throughout all exercises

## Repository Structure

### Main Course Blocks (3 progressive levels)

Located in `contenido/` directory:

1. **`contenido/bloque-1/`** - Python Programming Prerequisites (Weeks 1-5)
   - Basic Python fundamentals with sports context
   - Jupyter notebooks covering variables, control structures, functions, pandas/numpy basics, and matplotlib

2. **`contenido/bloque-2/`** - Data Science Fundamentals with Football Data (Weeks 6-10)
   - Exploratory data analysis of real football datasets
   - Statistical analysis and visualization with seaborn

3. **`contenido/bloque-3/`** - First Predictions with Football Data (Weeks 11-15)
   - Introduction to basic machine learning concepts
   - Simple predictive models using scikit-learn

### Evaluation System (`evaluaciones/`)

**Key Feature:** Recently refactored to have **one exercise per week** with detailed instructions and precise rubrics.

- Each block has simplified evaluation structure: `ejercicios/`, `proyecto/`, and `rubricas/`
- Unified scoring rubric: 40% technical correctness + 30% practical application + 30% documentation
- 60-minute estimated completion time per exercise
- All exercises use Spanish variable names and football context

### Supporting Materials

- **`referencias/`** - Bibliography and installation guides
- **Course-specific datasets** - Football/soccer data for practical exercises
- **Progressive difficulty** - Each week builds on previous concepts

### Complete Repository Structure

```
/
├── contenido/                    # Main course content
│   ├── bloque-1/                # Python Programming Prerequisites (Weeks 1-5)
│   │   ├── README.md
│   │   ├── semana-1/            # Configuration and fundamentals
│   │   ├── semana-2/            # Data structures and control flow
│   │   ├── semana-3/            # Functions and modules
│   │   ├── semana-4/            # Pandas and NumPy introduction
│   │   └── semana-5/            # Basic visualization
│   ├── bloque-2/                # Data Science Fundamentals (Weeks 6-10)
│   │   ├── README.md
│   │   ├── semana-6/            # Data exploration
│   │   ├── semana-7/            # Football data types
│   │   ├── semana-8/            # Descriptive statistics
│   │   ├── semana-9/            # Data visualization
│   │   └── semana-10/           # Analysis and interpretation
│   └── bloque-3/                # First Predictions (Weeks 11-15)
│       ├── README.md
│       ├── semana-11/           # Predictive modeling introduction
│       ├── semana-12/           # Advanced classification models
│       ├── semana-13/           # Advanced evaluation metrics
│       ├── semana-14/           # Feature engineering and optimization
│       └── semana-15/           # Final integrative project
├── evaluaciones/                # Complete evaluation system
│   ├── bloque-1/
│   │   ├── ejercicios/          # Weekly exercises (simplified structure)
│   │   ├── proyecto/            # Block project (simplified structure)
│   │   ├── datasets/            # Block-specific datasets
│   │   └── rubricas/            # Evaluation rubrics
│   ├── bloque-2/
│   │   ├── ejercicios/          # Preparatory exercises
│   │   ├── proyecto/            # Analysis project
│   │   ├── datasets/            # European leagues data
│   │   └── rubricas/            # Evaluation rubrics
│   └── bloque-3/
│       ├── ejercicios/          # Practice exercises
│       ├── proyecto/            # Predictive project
│       ├── datasets/            # Advanced datasets
│       └── rubricas/            # Evaluation rubrics
├── referencias/                 # Supporting documentation
│   ├── guia-instalacion.md      # Installation guide
│   └── bibliografia-recursos.md # Bibliography and resources
└── CLAUDE.md                    # This file - Complete guidance for AI assistants
```

## Development Environment Setup

### Required Software

```bash
# Create virtual environment
python -m venv football-analytics
source football-analytics/bin/activate  # Linux/Mac
# football-analytics\Scripts\activate   # Windows

# Install core dependencies
pip install pandas numpy matplotlib seaborn jupyter scikit-learn plotly
```

### Environment Verification

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
print("✅ All libraries installed correctly")
```

## Key Datasets and References

- **Main Dataset:** ["champs" on Kaggle](https://www.kaggle.com/datasets/julihocc/champs)
- **Reference Notebook:** ["La Remontada" on Kaggle](https://www.kaggle.com/code/julihocc/la-remontada)
- **European leagues data:** `equipos-europa-2023-24.csv`, `jugadores-estrellas-2024.csv`

## Educational Standards and Style

### Target Audience and Context

This course is directed at **Tecnológico de Monterrey preparatoria students** in their final year, exploring career options in technology and data. The objective is to introduce basic programming and data analysis concepts using football context to make learning more attractive and relevant.

### Code Style Requirements

- **Spanish variable names:** `goles_por_partido`, `equipos_favoritos`, `datos_futbol`
- **Educational comments:** Explain the purpose and context of each code section in Spanish
- **Football context:** All examples use real teams (Barcelona, Real Madrid, Manchester City, Bayern Munich)
- **Preparatoria level:** Explanations suitable for high school students
- **Professional tone:** Clear, concise explanations without jargon unless defined
- **No emojis:** Maintain professional yet engaging tone
- **Seaborn theme:** Always use `sns.set_theme(style="whitegrid", palette="viridis")`

### Content Guidelines

- Each notebook combines theory + practice + laboratory exercises
- Progressive complexity from basic Python to machine learning
- Consistent football theme throughout all materials
- Interactive Jupyter notebook format for hands-on learning
- **Incremental changes:** Make small improvements rather than large rewrites
- **Executable code:** Ensure all code works in Jupyter notebook environment
- **Time constraints:** Weekly exercises ≤ 60 minutes, block projects 2-3 hours

### Language and Communication Patterns

- **Excitement:** Use `¡` and motivational language (`¡Es como ser un analista deportivo!`)
- **Questions:** Frame concepts as questions (`¿Es mejor jugar en casa?`)
- **Explanations:** Always explain what code does (`¡Este gráfico nos muestra...!`)
- **Encouragement:** End with positive reinforcement (`¡Felicitaciones!`, `¡Excelente progreso!`)

### Notebook Structure Standards

#### Standard Cell Structure
1. **Markdown title:** `# Semana X: [Descriptive Spanish Title]`
2. **Learning objectives:** `**Lo que aprenderemos hoy:**`
3. **Import section** with educational comments
4. **Progressive examples** building complexity
5. **Summary:** `### Lo que Aprendimos Hoy`
6. **Preview:** `### Próxima Semana`

#### Code Cell Conventions
```python
# Import pattern with educational comments
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Always configure seaborn theme
sns.set_theme(style="whitegrid", palette="viridis")

print("¡Herramientas listas!")
```

#### Data Generation Pattern
```python
# Create realistic football datasets for every exercise
import random
equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']
partidos = []
for i in range(30):
    equipo_local = random.choice(equipos)
    equipo_visitante = random.choice([e for e in equipos if e != equipo_local])
    partidos.append({
        'Equipo_Local': equipo_local,
        'Equipo_Visitante': equipo_visitante,
        'Goles_Local': random.randint(0, 3),
        'Goles_Visitante': random.randint(0, 3),
        'Temporada': random.choice(['2023-24', '2024-25'])
    })
datos_futbol = pd.DataFrame(partidos)
```

#### Visualization Standards
```python
# Standard plotting with Spanish labels
plt.figure(figsize=(10, 6))
sns.countplot(data=datos, x='variable', palette='viridis')
plt.title('¿[Question in Spanish]?', fontsize=16, fontweight='bold')
plt.xlabel('[Spanish label]')
plt.ylabel('[Spanish label]')
plt.show()
print("¡Este gráfico nos muestra [explanation]!")
```

## Course Management Commands

### Running Course Materials

```bash
# Start Jupyter environment
jupyter notebook

# Navigate to specific week
cd contenido/bloque-1/semana-1
jupyter notebook configuracion-fundamentos.ipynb
```

### Dataset Operations

```bash
# Download from Kaggle (requires API setup)
pip install kaggle
kaggle datasets download -d julihocc/champs

# Verify dataset integrity
python -c "import pandas as pd; df = pd.read_csv('champs.csv'); print(f'Dataset loaded: {df.shape}')"
```

## Architecture Notes

### Educational Design Pattern

- **Scaffolded Learning:** Each week builds on previous concepts
- **Contextual Learning:** All programming concepts taught through football examples  
- **Project-Based:** Culminates in integrated projects per block
- **Assessment-Driven:** Clear rubrics and structured evaluations

### Technical Architecture

- **Jupyter-Centric:** All course content delivered via interactive notebooks
- **Library Progression:** matplotlib → seaborn → scikit-learn as complexity increases
- **Data Pipeline:** CSV files → pandas DataFrames → visualizations/models
- **Modular Design:** Each week stands alone but connects to overall progression

### Evaluation Architecture

- **Formative Assessment:** Weekly exercises with immediate feedback
- **Summative Assessment:** Block-level integrated projects
- **Competency-Based:** Technical skills + practical application + communication

## Working with This Repository

### Educational Methodology

This course follows a specific pedagogical approach:

- **Theoretical classes:** Introduction to key concepts
- **Practical exercises:** Application of learning in sports contexts
- **Integrative projects:** Development of final projects combining all acquired knowledge
- **Continuous evaluations:** Weekly mini-assessments to reinforce learning

### Evaluation Criteria

- **Technical correctness:** Functional code and appropriate use of tools
- **Quality of analysis:** Depth and rigor in data analysis
- **Presentation and communication:** Clarity in visualizations and explanations
- **Contextual application:** Relevance and pertinence of sports analysis

### When Modifying Course Materials

1. **Maintain Spanish language** throughout all content
2. **Preserve football context** in examples and datasets  
3. **Follow educational progression** from basic to advanced
4. **Use consistent rubric structure** for all assessments
5. **Test notebooks interactively** before finalizing changes
6. **Maintain 60-minute exercise completion** time target
7. **Make incremental improvements** rather than large rewrites
8. **Always run entire notebook** to ensure everything works
9. **Use descriptive commit messages** reflecting changes made

### When Creating New Content

- Use existing notebooks as templates for structure and style
- Source football examples from recognizable teams and players
- Include both theoretical concepts and practical applications
- Provide clear learning objectives and assessment criteria
- Test with target audience (high school level) understanding
- Ensure consistent naming conventions (preferably Spanish)
- Include well-documented comments explaining purpose of each section

### Function and Variable Naming Patterns

```python
# Functions with Spanish names and docstrings
def quien_gano(fila):
    """Determina el ganador de un partido"""
    if fila['Goles_Local'] > fila['Goles_Visitante']:
        return 'Ganó Local'
    elif fila['Goles_Local'] < fila['Goles_Visitante']:
        return 'Ganó Visitante'
    else:
        return 'Empate'

# Educational print statements explaining results
print("¡Este gráfico nos muestra qué tan seguido los equipos marcan goles!")
print(f"Promedio de goles por partido: {promedio:.1f}")
```

## Custom Commands

### `/commit` Command

Performs intelligent git commits with automatic change analysis and appropriate Spanish messages for this educational repository.

#### Usage
```
/commit                           # Automatic commit with generated message
/commit "mensaje personalizado"   # Commit with specific message
```

#### Workflow Process
1. **Pre-analysis:** Run `git status`, `git diff`, and `git log --oneline -3`
2. **Message generation:** Analyze changes considering educational context
3. **Spanish style:** Use infinitive verbs (Agregar, Actualizar, Corregir)
4. **Specificity:** Mention specific blocks/weeks/exercises when applicable

#### Commit Message Format
```
[Descriptive Spanish title - max 50 characters]

[Optional detailed description]
- Specific change 1
- Specific change 2
- Specific change 3

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

#### Repository-Specific Rules
- **Always use Spanish** in titles and descriptions
- **Mention sports context** when relevant
- **Specify block/week** if changes are specific to course sections
- **Prioritize educational clarity** over technical jargon

#### Example Messages
```bash
# Exercise changes
"Actualizar ejercicios Semana 3: mejorar instrucciones de funciones"

# Documentation changes  
"Mejorar documentación de instalación y configuración"

# Dataset changes
"Agregar nuevos datasets para análisis Bloque 2"
```

## Support Resources

- Installation guide: `referencias/guia-instalacion.md`
- Bibliography: `referencias/bibliografia-recursos.md`
- Refactored evaluation overview: `evaluaciones/RESUMEN-EJECUTIVO-REFACTORIZACION.md`
- Block-specific README files for detailed learning objectives

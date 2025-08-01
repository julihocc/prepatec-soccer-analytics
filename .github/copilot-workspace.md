# Copilot Workspace Configuration

## Project Context for AI Assistance

This workspace contains a **Spanish-language educational course** teaching data science applied to football/soccer analysis using Python. The repository includes 15 weeks of structured learning materials organized into 3 progressive blocks, plus a comprehensive evaluation system.

### Repository Structure
- **Course Content**: 3 blocks with 5 weekly Jupyter notebooks each (`bloque-1/`, `bloque-2/`, `bloque-3/`)
- **Evaluation System**: Complete assessment materials (`evaluaciones/`) with exercises, projects, and rubrics
- **References**: Installation guides and resources (`referencias/`)

## AI Assistant Guidelines

### Language and Context
- **Primary Language**: All content, comments, and variables must be in **Spanish**
- **Educational Level**: High school preparatoria students (beginner-friendly)
- **Domain Context**: Football/soccer data analysis throughout all examples
- **Tone**: Professional yet engaging, encouraging for learning

### Code Generation Rules
- Use Spanish variable names: `datos_futbol`, `equipos_favoritos`, `goles_por_partido`
- Always include educational comments explaining what code does
- Generate realistic football datasets for examples
- Use `sns.set_theme(style="whitegrid", palette="viridis")` for visualizations
- End notebooks with summary section: `### Lo que Aprendimos Hoy`

### Content Structure for New Notebooks
1. **Markdown title**: `# Semana X: [Descriptive Spanish Title]`
2. **Learning objectives**: `**Lo que aprenderemos hoy:**`
3. **Import section** with educational comments
4. **Progressive examples** building complexity
5. **Summary and preview**: `### Próxima Semana`

### When Helping with This Project
- Maintain the educational Spanish focus
- Use football context for all data examples
- Keep explanations appropriate for beginners
- Follow the established progressive difficulty pattern
- Generate complete notebook cells in VSCode.Cell XML format when requested

### Course Organization
- **Block 1** (`bloque-1/`): Python programming prerequisites (weeks 1-5)
- **Block 2** (`bloque-2/`): Data science fundamentals with sports data (weeks 1-5) 
- **Block 3** (`bloque-3/`): Basic predictive modeling for high school level (weeks 1-5)

### Content Patterns
Each week follows: `bloque-X/semana-Y/topic-name.ipynb` where:
- All content is in **Spanish** 
- Each notebook has structured sections: Theory → Practice → Exercises → Sports Applications
- Sports examples use football/soccer context throughout (players, teams, matches, statistics)

## Key Development Patterns

### Notebook Cell Structure (VSCode.Cell XML format)
```xml
<VSCode.Cell id="#VSC-xxxxxxxx" language="markdown">
# Semana X: [Descriptive Title]
## [Section Header]
**Lo que aprenderemos hoy:**
- [Learning objectives in Spanish]
</VSCode.Cell>
<VSCode.Cell id="#VSC-xxxxxxxx" language="python">
# Import pattern with educational comments
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Always configure seaborn theme
sns.set_theme(style="whitegrid", palette="viridis")

print("¡Herramientas listas!")
</VSCode.Cell>
```

### Educational Progression Pattern
- **Block 1**: Basic Python → Data structures → Functions → pandas/numpy → matplotlib
- **Block 2**: Data exploration → Data types → Descriptive statistics → Visualization → Analysis
- **Block 3**: Simple predictions → Model comparison → Evaluation metrics → Optimization → Course closure

### Sports Data Creation Pattern
```python
# Always create realistic football datasets
equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']
partidos = []
for i in range(30):  # Generate educational datasets
    partidos.append({
        'Equipo_Local': random.choice(equipos),
        'Goles_Local': random.randint(0, 3),
        'Temporada': random.choice(['2023-24', '2024-25'])
    })
datos_futbol = pd.DataFrame(partidos)
```

### Visualization Conventions
```python
# Standard seaborn plotting with Spanish labels
plt.figure(figsize=(10, 6))
sns.countplot(data=datos, x='variable', palette='viridis')
plt.title('¿[Question in Spanish]?', fontsize=16, fontweight='bold')
plt.xlabel('[Spanish label]')
plt.ylabel('[Spanish label]')
plt.show()
```

## Development Workflows

### Notebook Creation Workflow
1. **Start with VSCode.Cell XML format** for all notebook content
2. **Cell 1**: Markdown title with learning objectives (`**Lo que aprenderemos hoy:**`)
3. **Cell 2**: Import libraries with `sns.set_theme()` configuration
4. **Cells 3-N**: Progressive examples building complexity
5. **Final cells**: Summary (`### Lo que Aprendimos Hoy`) and next week preview

### Data Generation Pattern
```python
# Create educational datasets in every notebook
import random
equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']
# Generate 30 realistic matches
for i in range(30):
    # Ensure no team plays against itself
    equipo_visitante = random.choice([e for e in equipos if e != equipo_local])
```

### Environment Setup
- Python 3.10.12 with virtual environment (`.venv/`)
- Required packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `jupyter`
- Always use `sns.set_theme(style="whitegrid", palette="viridis")` in imports
- All notebooks designed for Jupyter environment

### Code Style Patterns
```python
# Spanish variable names with educational context
equipos_favoritos = ['Barcelona', 'Real Madrid', 'Manchester City']
goles_por_partido = [2, 1, 3]
datos_futbol = pd.DataFrame(partidos)

# Functions with Spanish docstrings
def quien_gano(fila):
    """Determina el ganador de un partido"""
    if fila['Goles_Local'] > fila['Goles_Visitante']:
        return 'Ganó Local'
    else:
        return 'Ganó Visitante'

# Educational print statements explaining results
print("¡Este gráfico nos muestra qué tan seguido los equipos marcan goles!")
print(f"Promedio de goles por partido: {promedio:.1f}")
```

### Markdown Cell Conventions
- Start with `# Semana X: [Descriptive Spanish Title]`
- Use `**Lo que aprenderemos hoy:**` for learning objectives
- Include `¿Por qué es interesante?` sections to motivate learning
- End with summary sections: `### Lo que Aprendimos Hoy`
- Always include "next week" preview: `### Próxima Semana`

## Integration Points

### Cross-Block Dependencies
- Block 2 assumes completion of Block 1 Python skills
- Block 3 builds on Block 2 data analysis foundation
- Each week references previous concepts progressively

### External Resources
- Dataset: "Champs" from Kaggle for real football data
- Reference notebook: "La Remontada" on Kaggle
- Installation guides in `referencias/` directory

## Course-Specific Conventions

### Educational Language Patterns
- **Excitement**: Use `¡` and motivational language (`¡Es como ser un analista deportivo!`)
- **Questions**: Frame concepts as questions (`¿Es mejor jugar en casa?`)
- **Explanations**: Always explain what code does (`¡Este gráfico nos muestra...!`)
- **Encouragement**: End with positive reinforcement (`¡Felicitaciones!`, `¡Excelente progreso!`)

### Content Adaptation Approach
- Originally designed for advanced ML but simplified to preparatoria level
- Block 3 focuses on "Mi Primera Predicción" (My First Prediction) approach
- No separate assessment projects - learning through exploration
- Each notebook is self-contained but builds on previous concepts

### File and Variable Naming
- Notebooks: `topic-description.ipynb` (hyphen-separated, Spanish descriptive)
- Variables: Always in Spanish (`datos_futbol`, `equipos_favoritos`, `goles_por_partido`)
- Functions: Spanish names with Spanish docstrings (`quien_gano`, `analizar_rendimiento`)
- Cell IDs: Use VSCode.Cell format with `#VSC-xxxxxxxx` pattern

When working on this codebase, maintain the educational Spanish-language focus, progressive difficulty, and consistent football/soccer context throughout all materials.

### Additional Guidelines
- Use clear, concise explanations and avoid jargon unless defined
- Maintain a professional yet engaging tone suitable for high school students
- Ensure all content is accessible and understandable for beginners
- Keep the focus on practical applications in sports data analysis  
- Do not use emojis or informal language
- Maintain a professional yet engaging tone suitable for high school students
- Ensure all content is accessible and understandable for beginners
- Use clear, concise explanations and avoid jargon unless defined
- Keep the focus on practical applications in sports data analysis
- Make small incremental changes to existing code rather than large rewrites
- Use comments to explain complex logic or calculations
- Ensure all code is executable in a Jupyter notebook environment
- After making changes, always run the entire notebook to ensure everything works as expected
- Avoid making large rewrites; instead, focus on small, incremental improvements
- After making changes, propose a commit with a clear message summarizing the changes made
- If proposing a commit, offer to sync the changes with the current branch
- Use descriptive commit messages that reflect the changes made, e.g., "Added data visualization for team performance"
- Ensure all code is well-documented with comments explaining the purpose of each section
- Use consistent naming conventions for variables and functions, preferably in Spanish

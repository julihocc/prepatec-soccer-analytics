# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Spanish-language educational course** on data science applied to football/soccer analysis. The repository contains comprehensive course materials for a 15-week program teaching Python fundamentals, data science basics, and predictive modeling specifically within the context of football data.

**Target Audience:** High school level students (preparatoria)
**Language:** Spanish (all variables, comments, and content)
**Context:** Football/soccer data analysis throughout all exercises

## Repository Structure

### Main Course Blocks (3 progressive levels)

1. **`bloque-1/`** - Python Programming Prerequisites (Weeks 1-5)
   - Basic Python fundamentals with sports context
   - Jupyter notebooks covering variables, control structures, functions, pandas/numpy basics, and matplotlib

2. **`bloque-2/`** - Data Science Fundamentals with Football Data (Weeks 6-10)
   - Exploratory data analysis of real football datasets
   - Statistical analysis and visualization with seaborn

3. **`bloque-3/`** - First Predictions with Football Data (Weeks 11-15)
   - Introduction to basic machine learning concepts
   - Simple predictive models using scikit-learn

### Evaluation System (`evaluaciones/`)

**Key Feature:** Recently refactored to have **one exercise per week** with detailed instructions and precise rubrics.

- Each block has its own evaluation structure: `ejercicios-semanales/`, `proyecto-integrador/`, and `rubricas/`
- Unified scoring rubric: 40% technical correctness + 30% practical application + 30% documentation
- 60-minute estimated completion time per exercise
- All exercises use Spanish variable names and football context

### Supporting Materials

- **`referencias/`** - Bibliography and installation guides
- **Course-specific datasets** - Football/soccer data for practical exercises
- **Progressive difficulty** - Each week builds on previous concepts

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

### Code Style Requirements

- **Spanish variable names:** `goles_por_partido`, `equipos_favoritos`, `datos_futbol`
- **Educational comments:** Explain the purpose and context of each code section
- **Football context:** All examples use real teams (Barcelona, Real Madrid, Manchester City)
- **Preparatoria level:** Explanations suitable for high school students

### Content Guidelines

- Each notebook combines theory + practice + laboratory exercises
- Progressive complexity from basic Python to machine learning
- Consistent football theme throughout all materials
- Interactive Jupyter notebook format for hands-on learning

## Course Management Commands

### Running Course Materials

```bash
# Start Jupyter environment
jupyter notebook

# Navigate to specific week
cd bloque-1/semana-1
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

When modifying course materials:

1. **Maintain Spanish language** throughout all content
2. **Preserve football context** in examples and datasets  
3. **Follow educational progression** from basic to advanced
4. **Use consistent rubric structure** for all assessments
5. **Test notebooks interactively** before finalizing changes
6. **Maintain 60-minute exercise completion** time target

When creating new content:

- Use existing notebooks as templates for structure and style
- Source football examples from recognizable teams and players
- Include both theoretical concepts and practical applications
- Provide clear learning objectives and assessment criteria
- Test with target audience (high school level) understanding

## Support Resources

- Installation guide: `referencias/guia-instalacion.md`
- Bibliography: `referencias/bibliografia-recursos.md`
- Refactored evaluation overview: `evaluaciones/RESUMEN-EJECUTIVO-REFACTORIZACION.md`
- Block-specific README files for detailed learning objectives

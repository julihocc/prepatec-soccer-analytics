# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational project called "Ciencia de Datos Aplicada al Fútbol" (Data Science Applied to Football) for high school students (15-18 years old) at Tecnológico de Monterrey. It's a 15-week course teaching Python programming fundamentals, data exploration, and basic predictive modeling using football/soccer datasets and contexts.

The course uses Socratic methodology with football analogies to make data science concepts accessible to preparatoria students.

## Course Structure

The content is organized into 3 blocks:
- **Bloque 1** (Weeks 1-5): Python programming fundamentals
- **Bloque 2** (Weeks 6-10): Data exploration and analysis with football data
- **Bloque 3** (Weeks 11-15): Basic predictive modeling and machine learning

Each week contains Jupyter notebooks (`.ipynb` files) for interactive learning, along with PDF versions and Python presentation files.

## Key Development Commands

### Environment Setup
```bash
# Install dependencies automatically
python install_dependencies.py

# Or manually install from requirements.txt
pip install -r requirements.txt

# For full project setup (includes txttoqti from GitHub)
pip install -e .

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
```

### Content Generation Commands

#### PDF Generation from Notebooks
```bash
# Smart conversion (recommended) - only regenerates when needed
python herramientas/notebook-to-pdf/smart_convert.py contenido/

# Status check
python herramientas/notebook-to-pdf/smart_convert.py contenido/ --status

# Force regeneration
python herramientas/notebook-to-pdf/smart_convert.py contenido/ --force

# Using Make commands
make notebook-tools    # Convert notebooks with professional tools
make notebook-status   # Check conversion status
make notebook-update   # Force regenerate all PDFs
make notebook-clean    # Remove generated PDFs
```

#### Presentation Generation (py to Marp)
```bash
# Convert Python files to Marp presentations
python herramientas/py-to-marp/convert.py contenido/bloque-1/semana-1/archivo.py --config educativo

# Available configs: educativo, ejecutivo, taller, evaluacion, dark
python herramientas/py-to-marp/convert.py --list-configs
```

#### Assessment Generation (TXT to QTI Canvas)
```bash
# Convert question banks to Canvas QTI format using embedded scripts
cd evaluaciones/bloque-1/canvas/ && python generar_qti.py

# Check conversion status
cd evaluaciones/bloque-1/canvas/ && python generar_qti.py --status

# Force regeneration (Python API - txttoqti v0.2.0+ is installed as dependency)
python -c "from txttoqti import TxtToQtiConverter; converter = TxtToQtiConverter(); converter.convert_file('file.txt')"
```

### Testing Commands
```bash
# Run tests for conversion tools
python herramientas/notebook-to-pdf/tests/run_tests.py
python herramientas/py-to-marp/tests/run_tests.py

# Test txttoqti v0.2.0+ functionality (installed as external dependency)
python -c "from txttoqti import TxtToQtiConverter; print('txttoqti v0.2.0+ OK')"
```

### Make Commands (Comprehensive)
```bash
make help           # Show all available commands
make pdfs           # Convert all notebooks to PDF  
make clean-pdfs     # Remove all generated PDFs
make check-deps     # Verify dependencies are installed
make install-deps   # Install system dependencies (Ubuntu/Debian)
make stats          # Show project statistics
```

## Repository Architecture

### Content Structure
```
contenido/
├── bloque-1/          # Python fundamentals (weeks 1-5)
│   ├── semana-1/      # Variables, data types, basic operations
│   ├── semana-2/      # Control structures (if/else, loops)
│   ├── semana-3/      # Functions and modules
│   ├── semana-4/      # Pandas and NumPy introduction
│   └── semana-5/      # Basic data visualization
├── bloque-2/          # Data exploration (weeks 6-10)
│   ├── semana-6/      # Introduction to data exploration
│   ├── semana-7/      # Types of football data
│   ├── semana-8/      # Descriptive statistics
│   ├── semana-9/      # Data visualization
│   └── semana-10/     # Analysis and interpretation
└── bloque-3/          # Predictive modeling (weeks 11-15)
    ├── semana-11/     # Introduction to predictive modeling
    ├── semana-12/     # Advanced classification models
    ├── semana-13/     # Advanced evaluation metrics
    ├── semana-14/     # Feature engineering and optimization
    └── semana-15/     # Final integrative project
```

Each week contains:
- `.ipynb` notebook (main content)
- `.py` files (presentation format)
- `.pdf` files (generated from notebooks)

### Assessment Structure
```
evaluaciones/
├── bloque-1/
│   ├── canvas/        # Canvas LMS question banks
│   ├── caso-practico/ # Practical case studies
│   └── datasets/      # Data files for assessments
├── bloque-2/          # Similar structure for block 2
└── bloque-3/          # Similar structure for block 3
```

### Tools Directory
```
herramientas/
├── notebook-to-pdf/   # Professional notebook to PDF conversion
│   ├── convert.py     # Core conversion functionality
│   ├── smart_convert.py # Intelligent conversion with change detection
│   └── tests/         # Conversion test suite
└── py-to-marp/        # Python percent format to Marp presentations
    ├── convert.py     # Main conversion script
    ├── py_to_marp.py  # Core conversion logic
    ├── configs.py     # Presentation configurations
    └── tests/         # Marp conversion tests

# txttoqti v0.2.0+ is installed as external dependency from PyPI
# Available via: pip install txttoqti>=0.2.0
```

## Pedagogical Architecture

### Socratic Methodology
- Each session begins with a thought-provoking question related to football
- Learning occurs through guided discovery rather than direct instruction
- Concepts are introduced through football analogies and real-world scenarios
- Students build understanding progressively through reflection and questioning

### Football Context Integration
- All examples use real football teams (Barcelona, Real Madrid, Manchester City, etc.)
- Statistical concepts are taught using player performance data
- Programming challenges involve solving actual sports analytics problems
- Final project analyzes Champions League data for practical application

### Content Delivery Format
Each notebook follows this structure:
1. **Opening Question**: Hooks student curiosity with football-related query
2. **Guided Discovery**: Step-by-step exploration with Socratic questioning
3. **Practical Application**: Hands-on coding with football data
4. **Reflection**: Synthesis questions connecting concepts to broader understanding

## Technical Stack

### Core Libraries
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib/seaborn**: Data visualization
- **scikit-learn**: Machine learning (Block 3 only)
- **jupyter**: Interactive development environment

### File Formats
- **Primary**: Jupyter notebooks (`.ipynb`) for interactive learning
- **Secondary**: Python files (`.py`) in jupytext percent format for version control
- **Output**: PDF files generated from notebooks for distribution
- **Presentations**: Markdown files compatible with Marp for slideshows

### Data Sources
- Main dataset: [Champs - Kaggle](https://www.kaggle.com/datasets/julihocc/champs)
- Reference notebook: [La Remontada](https://www.kaggle.com/code/julihocc/la-remontada)
- Various CSV files for specific exercises and assessments

## Development Workflow

### Content Creation
1. Develop content in Jupyter notebooks with embedded Socratic questions
2. Test all code cells to ensure they run within 50-minute class sessions
3. Generate PDF versions using the smart conversion tools
4. Create presentation versions if needed for classroom projection

### Assessment Development
1. Write question banks in simple text format
2. Convert to Canvas QTI format using the txttoqti library (`txt-to-qti` command)
3. Test practical cases with real football datasets
4. Ensure all assessments align with learning objectives

### Quality Assurance
- All notebooks must execute completely within time constraints
- Code examples use realistic football data and scenarios
- Spanish variable names and comments for accessibility
- Professional documentation standards maintained

## Working with the Codebase

### When Adding New Content
1. Follow the existing naming convention: `tema-subtema.ipynb`
2. Include Socratic questions throughout the content
3. Use football analogies and real team examples
4. Test execution time to fit 50-minute sessions
5. Generate PDF versions after completing content

### When Modifying Tools
1. Update relevant tool in the `herramientas/` directory
2. Run the test suites to ensure functionality
3. Update documentation if interface changes
4. Test with actual course content files

### When Working with Assessments
1. Use the established formats in the `evaluaciones/` directory
2. Ensure Canvas compatibility for digital assessments
3. Include rubrics and evaluation criteria
4. Test with sample student responses

## Important Technical Notes

### File Processing
- The notebook-to-PDF converter supports multiple LaTeX engines (XeLaTeX recommended)
- Smart conversion only regenerates files when source content changes
- All tools are designed to handle Spanish text and accented characters properly

### Content Guidelines
- Sessions are designed for exactly 50 minutes each
- Spanish variable names and comments enhance student comprehension
- No emojis used to maintain professional academic tone
- All code examples must be executable and produce meaningful output

### Infrastructure Requirements
- Python 3.10+ required (updated for txttoqti compatibility)
- LaTeX installation needed for PDF generation (XeLaTeX recommended for Spanish text)
- Node.js required only if generating presentations
- Git for version control and collaboration
- txttoqti v0.2.0+ from PyPI (automatically installed via pyproject.toml)

## Critical Development Constraints

### Time Constraints (STRICTLY ENFORCED)
- **Maximum session duration**: 50 minutes of executable content
- **Validation requirement**: All notebooks must complete execution within 45 minutes
- **Planning structure**: 15 min theory + 25 min practice + 10 min synthesis

### Language and Content Rules
- **NO EMOJIS POLICY**: Strictly prohibited in all code, documentation, comments, and commit messages
- **Spanish naming convention**: All variables, functions, and comments must be in Spanish
- **Professional tone**: Academic level appropriate for 15-18 year old students

### Educational Context
- **Target audience**: Preparatoria students (15-18 years) with ZERO programming experience
- **Mathematical level**: Basic algebra only
- **Session constraint**: If content doesn't fit in 50 minutes, it must be split

### Code Patterns (MANDATORY)
```python
# CORRECT - Spanish naming
goles_por_partido = df['goles'].mean()
jugadores_barcelona = df[df['equipo'] == 'Barcelona']
modelo_prediccion = LogisticRegression()

# INCORRECT - English naming  
goals_per_match = df['goals'].mean()
barcelona_players = df[df['team'] == 'Barcelona']
```

### Visualization Standards
```python
# Required configuration for all plots
sns.set_theme(style="whitegrid", palette="viridis")
plt.figure(figsize=(10, 6))
plt.title('Distribución de Goles por Jugador - Barcelona 2023')
plt.xlabel('Minutos Jugados')
plt.ylabel('Goles Marcados')
```

This educational repository represents a complete, production-ready curriculum for teaching data science to Spanish-speaking high school students using football as the engaging context.
- Commit changes in suitable chunks to preserve a clean git history
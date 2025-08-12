# Markdown Question Bank Format Specification

This document defines the markdown format used for authoring question banks that can be converted to Canvas QTI packages.

## Format Overview

The markdown format provides a structured, human-readable way to author multiple-choice questions organized by learning modules or weeks.

## Basic Structure

```markdown
SEMANA: [number]
TITULO: [descriptive title]

Q[number]: [question text]
A) [option A text]
B) [option B text]
C) [option C text]
D) [option D text]
RESPUESTA: [correct letter]

Q[number+1]: [next question text]
...
```

## Detailed Specification

### Week/Module Headers

#### Syntax
```markdown
SEMANA: [integer]
TITULO: [string]
```

#### Purpose
- Organizes questions into logical groups
- Provides context for question sets
- Used for documentation and organization (not imported to Canvas)

#### Example
```markdown
SEMANA: 1
TITULO: Configuracion y Fundamentos de Python
```

### Question Format

#### Question Declaration
```markdown
Q[number]: [question text]
```

**Rules:**
- Numbers must be sequential starting from 1
- No gaps in numbering allowed
- Question text can span multiple lines if needed
- Special characters should be avoided or properly escaped

#### Answer Options
```markdown
A) [option text]
B) [option text]  
C) [option text]
D) [option text]
```

**Rules:**
- Minimum 2 options required (A and B)
- Maximum 4 options supported (A, B, C, D)
- Options C and D are optional
- Option text should be concise and clear
- Avoid quotation marks and special characters when possible

#### Correct Answer
```markdown
RESPUESTA: [A|B|C|D]
```

**Rules:**
- Must specify exactly one correct answer
- Letter must match an existing option
- Case sensitive (use uppercase)

## Complete Example

```markdown
# Banco de Preguntas Bloque 1

SEMANA: 1
TITULO: Configuracion y Fundamentos de Python

Q1: Cual es el resultado de ejecutar type(42) en Python?
A) <class 'float'>
B) <class 'int'>
C) <class 'str'>
D) <class 'number'>
RESPUESTA: B

Q2: Si ejecuto nombre = "Barcelona" y luego print(len(nombre)), que se imprime?
A) 8
B) 9
C) 10
D) Error
RESPUESTA: B

Q3: Cual de estos nombres de variable cumple las reglas de Python y es legible?
A) 2equipo
B) equipo-favorito
C) equipo_favorito
D) equipo.favorito
RESPUESTA: C

SEMANA: 2
TITULO: Estructuras de Control

Q4: Cual es la sintaxis correcta para una estructura condicional en Python?
A) if (condicion) then:
B) if condicion:
C) if [condicion]:
D) if condicion then:
RESPUESTA: B
```

## Best Practices

### Question Writing

1. **Clear and Concise**: Write questions that are easy to understand
2. **Avoid Ambiguity**: Each question should have one clearly correct answer
3. **Consistent Style**: Maintain consistent formatting throughout
4. **Proper Encoding**: Use UTF-8 encoding for the markdown file

### Technical Considerations

1. **Character Limitations**: 
   - Avoid characters that don't convert well to ISO-8859-1
   - Be cautious with accented characters and symbols
   - Test special characters in Canvas if needed

2. **Length Limits**:
   - Questions: Recommended maximum 200 characters
   - Options: Recommended maximum 100 characters each
   - These limits ensure good display in Canvas

3. **Formatting**:
   - Use simple text formatting
   - Avoid markdown formatting within questions (bold, italic, etc.)
   - Code snippets should use backticks sparingly

### Organization Tips

1. **Logical Grouping**: Group related questions by topic/week
2. **Sequential Numbering**: Always maintain sequential question numbers
3. **Descriptive Titles**: Use clear, descriptive week titles
4. **Version Control**: Mark file with version information in comments

## Advanced Features

### Code in Questions

When including code snippets:

```markdown
Q15: Que hace el siguiente codigo: print(len("Python"))?
A) Imprime "Python"
B) Imprime 6
C) Imprime 5
D) Genera error
RESPUESTA: B
```

### Multi-line Questions

For longer questions:

```markdown
Q20: En el siguiente fragmento de codigo:
x = 10
y = 20
print(x + y)
Cual es la salida?
A) 10
B) 20
C) 30
D) Error
RESPUESTA: C
```

### Mathematical Expressions

```markdown
Q25: Cual es el resultado de 5 * 3 + 2?
A) 25
B) 17
C) 21
D) 15
RESPUESTA: B
```

## Validation Rules

The conversion script validates:

1. **Sequential Numbering**: Questions must be numbered 1, 2, 3... without gaps
2. **Required Elements**: Each question must have question text, options, and answer
3. **Answer Validity**: The correct answer letter must correspond to an existing option
4. **Minimum Options**: At least options A and B must be provided
5. **Format Compliance**: Proper use of Q[number]:, A), B), etc.

## Common Errors and Solutions

### Error: "Numeración no secuencial"
- **Cause**: Question numbers have gaps (Q1, Q3, Q5...)
- **Solution**: Renumber questions sequentially

### Error: "Sin respuesta correcta"
- **Cause**: Missing or malformed RESPUESTA line
- **Solution**: Add `RESPUESTA: [letter]` after each question

### Error: "Menos de 2 opciones"
- **Cause**: Question has only option A or missing options
- **Solution**: Add at least option B

### Error: "Respuesta no corresponde a opción"
- **Cause**: RESPUESTA specifies letter not in options (e.g., RESPUESTA: D but only A,B,C exist)
- **Solution**: Fix answer letter or add missing option

## Character Encoding Guidelines

### Recommended Characters
- Standard ASCII letters and numbers
- Basic punctuation: . , ? ! : ; ' "
- Mathematical symbols: + - * / = < > 
- Parentheses and brackets: ( ) [ ] { }

### Characters to Avoid
- Extended Unicode symbols
- Special formatting characters
- Non-standard quotation marks (" " ' ')
- Em dashes and special hyphens

### Spanish Character Support
Most Spanish accented characters work well:
- á, é, í, ó, ú
- ñ
- ¿, ¡

Test in Canvas if using extensive accented text.

## File Management

### Naming Convention
- Use descriptive names: `banco-preguntas-bloque1.md`
- Include version numbers if needed: `preguntas-v2.md`
- Use hyphens instead of spaces

### Version Control
- Keep markdown files in version control (git)
- Track changes to question content
- Maintain backup copies before major edits

### File Organization
```
evaluaciones/
├── bloque-1/
│   ├── canvas/
│   │   ├── banco-preguntas-bloque1.md
│   │   ├── md_to_csv_direct.py
│   │   └── csv_to_kansas_qti.py
│   └── other-formats/
└── bloque-2/
    └── canvas/
        └── banco-preguntas-bloque2.md
```
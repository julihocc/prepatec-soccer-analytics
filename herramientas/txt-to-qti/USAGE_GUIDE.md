# Usage Guide and Troubleshooting

This guide provides step-by-step instructions for using the MD to QTI conversion tools and resolving common issues.

## Quick Start Guide

### Prerequisites

- Python 3.7 or higher installed
- Text editor for creating/editing markdown files
- Access to Canvas LMS for importing questions

### Basic Workflow

#### Step 1: Create Question Bank in Markdown

Create a new file (e.g., `my-questions.md`) following the format:

```markdown
SEMANA: 1
TITULO: Introduction to Programming

Q1: What is Python?
A) A snake
B) A programming language
C) A web browser
D) An operating system
RESPUESTA: B

Q2: Which symbol is used for comments in Python?
A) //
B) #
C) /* */
D) --
RESPUESTA: B
```

#### Step 2: Convert to CSV

```bash
python md_to_csv_direct.py my-questions.md
```

**Output**: `my-questions_kansas.csv`

#### Step 3: Generate QTI Package

```bash
python csv_to_kansas_qti.py my-questions_kansas.csv
```

**Output**: `my-questions_kansas_qti.zip`

#### Step 4: Import to Canvas

1. Log into Canvas
2. Go to your course
3. Navigate to Settings → Import Content
4. Select "QTI Package" as import type
5. Upload the generated ZIP file
6. Complete the import process

## Detailed Instructions

### Creating Markdown Question Banks

#### File Structure

```markdown
# [Optional title - ignored by converter]

SEMANA: [number]
TITULO: [description]

Q[sequential_number]: [question text]
A) [first option]
B) [second option]
C) [third option - optional]
D) [fourth option - optional]
RESPUESTA: [A|B|C|D]

[Repeat for additional questions]
```

#### Writing Effective Questions

**Good Example**:
```markdown
Q1: What is the output of print(len("Hello"))?
A) 4
B) 5
C) 6
D) Error
RESPUESTA: B
```

**Avoid**:
```markdown
Q1: What does len() do to "Hello"?
A) Something
B) The right thing
C) I don't know
D) Maybe this
RESPUESTA: B
```

#### Best Practices

1. **Clear Questions**: Write unambiguous questions
2. **Distinct Options**: Make each option clearly different
3. **One Correct Answer**: Ensure only one option is definitively correct
4. **Appropriate Difficulty**: Match question difficulty to learning objectives

### Command Line Usage

#### Basic Commands

```bash
# Convert markdown to CSV
python md_to_csv_direct.py input.md

# Convert CSV to QTI
python csv_to_kansas_qti.py input_kansas.csv

# Specify custom output names
python md_to_csv_direct.py input.md custom_output.csv
python csv_to_kansas_qti.py input.csv custom_output.zip
```

#### Processing Multiple Files

**Bash script for multiple files**:
```bash
#!/bin/bash
for file in *.md; do
    echo "Processing $file..."
    python md_to_csv_direct.py "$file"
    python csv_to_kansas_qti.py "${file%.md}_kansas.csv"
    echo "Generated: ${file%.md}_kansas_qti.zip"
done
```

**Windows batch script**:
```cmd
@echo off
for %%f in (*.md) do (
    echo Processing %%f...
    python md_to_csv_direct.py "%%f"
    python csv_to_kansas_qti.py "%%~nf_kansas.csv"
    echo Generated: %%~nf_kansas_qti.zip
)
```

### Understanding Output

#### CSV Format Explanation

```csv
MC,,1.0,What is Python?,2,A snake,A programming language,A web browser,An operating system
```

Fields breakdown:
- `MC`: Multiple Choice question type
- Empty field: Required by Kansas State format
- `1.0`: Points per question  
- `What is Python?`: Question text
- `2`: Correct answer number (B = 2)
- `A snake,A programming language,A web browser,An operating system`: Options A,B,C,D

#### QTI ZIP Contents

The generated ZIP file contains:
- Single XML file (e.g., `questions_123456789.xml`)
- No manifest file (Kansas State style)
- ISO-8859-1 encoding

### Canvas Import Process

#### Detailed Import Steps

1. **Access Import Tool**
   - Go to Course Settings
   - Click "Import Course Content"
   - Select "QTI Package" from dropdown

2. **Upload File**
   - Click "Choose File"
   - Select your `*_kansas_qti.zip` file
   - Do NOT unzip the file first

3. **Import Options**
   - Select question bank destination
   - Choose whether to import into existing bank or create new one
   - Click "Import"

4. **Verify Import**
   - Go to Quizzes → Manage Question Banks
   - Confirm questions imported correctly
   - Check question formatting and options

#### Canvas Question Bank Management

**Creating Quiz from Imported Questions**:
1. Create new quiz
2. Go to "Questions" tab
3. Click "Find Questions"
4. Select your question bank
5. Choose questions to add
6. Configure quiz settings

**Editing Imported Questions**:
1. Go to question bank
2. Click question to edit
3. Modify text, options, or settings
4. Save changes

## Troubleshooting Guide

### Common Conversion Errors

#### Error: "Archivo no encontrado"

**Cause**: File path incorrect or file doesn't exist

**Solutions**:
- Check file name spelling
- Verify file is in current directory
- Use absolute path if needed: `python md_to_csv_direct.py /full/path/to/file.md`

#### Error: "Numeración no secuencial"

**Cause**: Question numbers have gaps (Q1, Q3, Q5...)

**Solution**: Renumber questions sequentially
```markdown
Q1: First question...
Q2: Second question...
Q3: Third question...
```

#### Error: "Sin respuesta correcta"

**Cause**: Missing or malformed `RESPUESTA:` line

**Solutions**:
- Add `RESPUESTA: A` (or B, C, D) after each question
- Check spelling: `RESPUESTA:` not `RESPUESTAS:` or `RESPUESTA:`
- Ensure space after colon: `RESPUESTA: B` not `RESPUESTA:B`

#### Error: "Menos de 2 opciones"

**Cause**: Question has only option A or missing options

**Solution**: Add at least option B
```markdown
Q1: Question text?
A) First option
B) Second option
RESPUESTA: A
```

### Character Encoding Issues

#### Problem: Special characters display incorrectly in Canvas

**Cause**: Character encoding incompatibility

**Solutions**:

1. **Use ASCII alternatives**:
   - Replace `"smart quotes"` with `"regular quotes"`
   - Replace `—` (em dash) with `-` (hyphen)
   - Replace `…` (ellipsis) with `...`

2. **Test problematic characters**:
   ```markdown
   Q1: Test: ¿Qué es Python?
   A) Una serpiente
   B) Un lenguaje de programación
   RESPUESTA: B
   ```

3. **Character replacement script**:
   ```python
   def clean_special_chars(text):
       replacements = {
           '"': '"', '"': '"',  # Smart quotes
           ''': "'", ''': "'",  # Smart apostrophes  
           '—': '-', '–': '-',  # Dashes
           '…': '...'           # Ellipsis
       }
       for old, new in replacements.items():
           text = text.replace(old, new)
       return text
   ```

### Canvas Import Issues

#### Problem: Questions not appearing in Canvas

**Possible Causes & Solutions**:

1. **Wrong file format uploaded**
   - Ensure you upload the ZIP file, not the XML file
   - Don't unzip the file before uploading

2. **QTI version incompatibility**
   - Our tools generate QTI 1.2 (Canvas compatible)
   - If issues persist, contact Canvas support

3. **File size limits**
   - Large question banks may exceed Canvas limits
   - Split into smaller files if needed

#### Problem: Questions import but formatting is wrong

**Solutions**:

1. **Check question text encoding**
   - Look for garbled characters
   - Regenerate with simpler characters

2. **Verify option formatting**
   - Ensure options A, B, C, D are distinct
   - Check for empty options

3. **Test with simple question**
   ```markdown
   Q1: Test question?
   A) Option A
   B) Option B  
   RESPUESTA: A
   ```

### Validation and Debugging

#### Enable Debug Mode

**Modify scripts for detailed output**:

```python
# In md_to_csv_direct.py, add after line 64:
print(f"DEBUG: Processing Q{question_num}: {question_text[:30]}...")

# In csv_to_kansas_qti.py, add after line 74:
print(f"DEBUG: Generated item ID: {item_id}")
```

#### Manual Validation Steps

1. **Check CSV output**:
   ```bash
   head -5 my-questions_kansas.csv
   ```
   - Verify format: `MC,,1.0,question,answer_num,A,B,C,D`
   - Check answer numbers are 1-4
   - Ensure no missing commas

2. **Validate XML structure**:
   ```bash
   unzip -l my-questions_kansas_qti.zip
   ```
   - Should show single XML file
   - No manifest.xml file

3. **Test with minimal example**:
   ```markdown
   SEMANA: 1
   TITULO: Test
   
   Q1: Simple test?
   A) Yes
   B) No
   RESPUESTA: A
   ```

#### Common Validation Issues

**CSV has wrong number of columns**:
- Check for commas in question text
- Escape quotes properly
- Ensure exactly 9 columns per row

**XML validation fails**:
- Check for special characters in text
- Verify proper encoding conversion
- Use XML validator online if needed

### Performance Issues

#### Large Files (100+ Questions)

**Symptoms**: Slow processing, memory issues

**Solutions**:
1. Split into smaller files (25-50 questions each)
2. Process in batches
3. Increase available memory: `python -Xmx2g script.py`

#### Processing Time Optimization

**Typical processing times**:
- 25 questions: < 1 second
- 50 questions: 1-2 seconds  
- 100 questions: 3-5 seconds

**If slower than expected**:
- Check disk space availability
- Ensure no antivirus scanning interference
- Close other applications

### Getting Help

#### Debug Information to Collect

When reporting issues, include:

1. **Input file sample** (first few questions)
2. **Error message** (complete text)
3. **Python version**: `python --version`
4. **Operating system**
5. **File sizes** of input and output

#### Self-Help Checklist

Before seeking help:

- [ ] Verified Python 3.7+ installed
- [ ] Checked file exists and is readable
- [ ] Ensured sequential question numbering
- [ ] Verified all questions have RESPUESTA lines
- [ ] Tested with simple 2-question example
- [ ] Checked CSV output format
- [ ] Attempted Canvas import with generated file

#### Contact Information

For technical issues with the conversion tools:
- Check existing documentation files
- Create minimal test case that reproduces issue
- Document exact error messages and steps to reproduce

For Canvas-specific import issues:
- Contact your institution's Canvas support
- Provide the generated QTI ZIP file for analysis
- Include screenshots of error messages
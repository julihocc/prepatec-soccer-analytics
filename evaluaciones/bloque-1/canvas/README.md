# Plain Text to QTI Conversion Solution

This solution provides a complete pipeline for converting simple text-formatted question banks to Canvas-compatible QTI packages, enabling educators to author questions in the simplest possible format and deploy them directly to Canvas LMS.

## Overview

The solution consists of a two-stage conversion pipeline:

1. **TXT → CSV**: Convert simple plain text to Kansas State CSV format
2. **CSV → QTI**: Generate Canvas-compatible QTI packages

This approach leverages the Kansas State University's proven CSV-to-QTI conversion methodology while adding support for ultra-simple plain text authoring.

## Solution Components

### Files in this Directory

- `banco-preguntas-bloque1.txt` - Source question bank in plain text format
- `txt_to_csv_direct.py` - Plain text to CSV converter
- `csv_to_kansas_qti.py` - CSV to QTI package generator
- `banco-preguntas-bloque1_kansas.csv` - Generated CSV output
- `README.md` - This documentation

## Quick Start

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Basic Usage

1. **Convert TXT to CSV**:
   ```bash
   python txt_to_csv_direct.py banco-preguntas-bloque1.txt
   ```

2. **Generate QTI Package**:
   ```bash
   python csv_to_kansas_qti.py banco-preguntas-bloque1_kansas.csv
   ```

3. **Import to Canvas**:
   - Go to Course Settings → Import Content
   - Select "QTI Package"
   - Upload the generated ZIP file

## Plain Text Format Specification

### Structure

Questions are written in simple plain text format:

```
Q[number]: [question text]
A) [option A]
B) [option B]
C) [option C]
D) [option D]
RESPUESTA: [correct letter]

[blank line separates questions]
```

### Example

```
Q1: Cual es el resultado de ejecutar type(42) en Python?
A) <class 'float'>
B) <class 'int'>
C) <class 'str'>
D) <class 'number'>
RESPUESTA: B

Q2: Que simbolo se usa para comentarios en Python?
A) //
B) #
C) /* */
D) --
RESPUESTA: B
```

### Format Rules

- Questions must be numbered sequentially (Q1, Q2, Q3...)
- Each question must have at least 2 options (A, B required; C, D optional)
- Correct answer must be specified using `RESPUESTA: [A|B|C|D]`
- Blank lines separate questions (optional but recommended)
- Text should avoid problematic characters for CSV/XML compatibility

## Technical Implementation

### Conversion Pipeline

#### Stage 1: TXT → CSV (`txt_to_csv_direct.py`)

**Purpose**: Parse plain text and generate Kansas State CSV format

**Features**:
- Simple regex-based text parsing
- Text normalization and cleaning
- Answer mapping (A→1, B→2, C→3, D→4)
- Validation and error reporting
- Sequential numbering verification

**Output Format**:
```csv
MC,,1.0,question_text,correct_answer_number,option_a,option_b,option_c,option_d
```

#### Stage 2: CSV → QTI (`csv_to_kansas_qti.py`)

**Purpose**: Generate Canvas-compatible QTI packages

**Features**:
- QTI 1.2 specification compliance
- Kansas State University structure emulation
- MD5-based reproducible ID generation
- ISO-8859-1 encoding (Canvas standard)
- Minimalist ZIP structure (XML only, no manifest)

**QTI Structure**:
- Proper `questestinterop` root element
- Canvas-specific metadata fields
- Multiple choice question formatting
- Response processing with scoring

### Key Design Decisions

#### Kansas State Compatibility

The solution emulates the Kansas State University CSV-to-QTI converter because:

1. **Proven Track Record**: Kansas State's format is well-tested with Canvas
2. **Minimal Structure**: Uses only essential QTI elements
3. **Canvas Optimization**: Includes Canvas-specific metadata
4. **Encoding Standards**: Uses ISO-8859-1 encoding as expected by Canvas

#### Two-Stage Pipeline

Benefits of the TXT→CSV→QTI approach:

1. **Modularity**: Each stage can be modified independently
2. **Debugging**: CSV intermediate format is human-readable
3. **Flexibility**: CSV can be manually edited if needed
4. **Reusability**: CSV stage leverages existing Kansas State methodology
5. **Simplicity**: Plain text format is the simplest possible authoring format

## Advanced Usage

### Batch Processing

Process multiple question banks:

```bash
for file in *.txt; do
    python txt_to_csv_direct.py "$file"
    python csv_to_kansas_qti.py "${file%.txt}_kansas.csv"
done
```

### Custom Output Names

```bash
python txt_to_csv_direct.py input.txt output.csv
python csv_to_kansas_qti.py input.csv output.zip
```

### Validation and Quality Control

Both scripts include validation features:

- **TXT Converter**: Checks sequential numbering, minimum options, answer validity
- **QTI Generator**: Validates CSV structure, generates reproducible IDs
- **Error Reporting**: Detailed feedback on parsing issues

## Troubleshooting

### Common Issues

1. **Encoding Problems**:
   - Ensure TXT files are UTF-8 encoded
   - Avoid special characters that don't translate to ISO-8859-1

2. **Parsing Errors**:
   - Check question numbering is sequential
   - Verify RESPUESTA: format exactly
   - Ensure proper plain text structure

3. **Canvas Import Issues**:
   - Verify QTI package is not corrupted
   - Check Canvas supports QTI 1.2 format
   - Ensure file size limits are not exceeded

### Debug Mode

Add debug output by modifying the scripts:

```python
# In txt_to_csv_direct.py
print(f"Processing question {question_num}: {question_text[:50]}...")

# In csv_to_kansas_qti.py  
print(f"Generated item ID: {item_id}")
```

## Sources and References

### Original Solutions

This implementation is based on and inspired by:

1. **Kansas State University QTI Converter**
   - Source: [Kansas State Classic to Canvas Converter](https://canvas.k-state.edu/info/tools/scantron/faq/build-a-scantron-quiz.html)
   - Contribution: CSV-to-QTI conversion methodology, Canvas-specific QTI structure
   - License: Public domain educational tool

2. **QTI 1.2 Specification**
   - Source: [IMS Global Learning Consortium](https://www.imsglobal.org/question/)
   - Contribution: QTI XML schema and structure requirements
   - License: IMS specification (freely implementable)

3. **Canvas LMS Documentation**
   - Source: [Canvas API Documentation](https://canvas.instructure.com/doc/api/)
   - Contribution: Canvas-specific metadata requirements and import behavior
   - License: Instructure documentation

### Implementation Details

#### Kansas State Structure Emulation

The `csv_to_kansas_qti.py` script specifically emulates:

- **Namespace Declaration**: Uses exact QTI 1.2 namespace URLs
- **ID Generation**: MD5-based item and assessment IDs
- **Encoding**: ISO-8859-1 character encoding
- **Metadata Fields**: Canvas-specific qtimetadata fields
- **ZIP Structure**: Single XML file without manifest

#### Plain Text Format Design

The plain text format was designed for:

- **Maximum Simplicity**: Absolute minimal formatting requirements
- **Educator Friendliness**: Human-readable and editable in any text editor
- **Version Control**: Git-friendly plain text format
- **No Overhead**: No metadata or structural markup to distract from content
- **Parsing Reliability**: Unambiguous delimiters and format rules

## Contributing

### Extending the Solution

To add new question types:

1. **Modify TXT Format**: Add new question type indicators
2. **Update Parser**: Extend regex patterns in `txt_to_csv_direct.py`
3. **Add QTI Support**: Implement new item types in `csv_to_kansas_qti.py`

### Testing

Create test cases for:

- Edge case text formats
- Unicode character handling
- Large question banks (100+ questions)
- Various Canvas configurations

## License and Acknowledgments

This solution builds upon publicly available educational tools and specifications:

- Kansas State University's converter methodology (public domain)
- IMS QTI specification (freely implementable)
- Canvas LMS compatibility knowledge (community documentation)

The implementation is provided as an educational tool for creating Canvas-compatible question banks from simple plain text sources.
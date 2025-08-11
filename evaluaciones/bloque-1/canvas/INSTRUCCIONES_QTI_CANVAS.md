# Instrucciones para Importar Banco de Preguntas QTI en Canvas

## Archivo Generado
- **Nombre**: `banco-preguntas-bloque1_QTI_CANVAS.zip`
- **Preguntas**: 120 preguntas del Bloque 1 (Python Fundamentals)
- **Tipos**: Opción múltiple y numéricas
- **Categorías**: Recordar (R), Aplicar (A), Comprender (C)

## Pasos para Importar en Canvas

### 1. Acceder a Canvas
- Inicia sesión en tu curso de Canvas
- Ve a la página principal del curso

### 2. Importar Contenido
- Haz clic en **"Configuración"** (Settings) en el menú lateral
- Selecciona **"Importar contenido del curso"** (Import Course Content)

### 3. Configurar Importación
- **Tipo de contenido**: Selecciona **"Paquete QTI"** (QTI Package)
- **Archivo**: Sube `banco-preguntas-bloque1_QTI_CANVAS.zip`
- Deja las demás opciones por defecto

### 4. Ejecutar Importación
- Haz clic en **"Importar"**
- Espera a que se complete el proceso (puede tomar 1-2 minutos)

### 5. Verificar Importación
- Ve a **"Exámenes"** (Quizzes) en el menú lateral
- Las preguntas aparecerán en tu **Banco de Preguntas** (Question Bank)
- Puedes organizarlas por categorías según los temas

## Configuración Predeterminada del Examen

El paquete QTI incluye configuración automática:
- **Intentos máximos**: 3
- **Tiempo límite**: 60 minutos
- **Mostrar retroalimentación**: Sí
- **Mostrar resultados**: Sí
- **Preguntas sugeridas para examen**: 25 (de las 120 disponibles)

## Crear Examen desde Banco de Preguntas

### 1. Nuevo Examen
- Ve a **"Exámenes"** → **"Nuevo Examen"**
- Configura título, descripción y fechas

### 2. Agregar Preguntas
- Haz clic en **"Preguntas"** → **"Nuevo Grupo de Preguntas"**
- Selecciona **"Encontrar Preguntas"** (Find Questions)
- Elige preguntas del banco importado

### 3. Configuración Recomendada
- **Preguntas por examen**: 20-25 preguntas
- **Selección aleatoria**: Activar para mayor seguridad
- **Tiempo**: 45-60 minutos
- **Intentos**: 2-3 máximo

## Distribución Sugerida por Categoría

Para un examen balanceado de 25 preguntas:
- **Recordar (R)**: 10-12 preguntas (40%)
- **Comprender (C)**: 8-10 preguntas (35%)  
- **Aplicar (A)**: 5-7 preguntas (25%)

## Temas Incluidos

1. Variables y Tipos de Datos
2. Estructuras de Control
3. Funciones
4. Listas y Diccionarios
5. Introducción a Pandas
6. NumPy Básico
7. Matplotlib Básico
8. Análisis de Datos Futbolísticos
9. Estadísticas Deportivas
10. Debugging y Errores Comunes
11. Pensamiento Computacional
12. Manipulación de Datos
13. Visualización Avanzada

## Solución de Problemas

### Error de Importación
- Verifica que el archivo no esté corrupto
- Asegúrate de seleccionar "Paquete QTI" como tipo
- Contacta a soporte técnico si persiste

### Preguntas No Aparecen
- Revisa en **"Bancos de Preguntas"** en lugar de exámenes directos
- Actualiza la página del navegador
- Verifica permisos de instructor

### Regenerar Archivo QTI
```bash
python3 generate_qti_canvas.py banco-preguntas-bloque1.json
```

## Contacto Técnico
Para problemas técnicos con la importación o uso del banco de preguntas, consulta la documentación oficial de Canvas o contacta al administrador del LMS.

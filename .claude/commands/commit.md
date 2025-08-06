# Comando /commit

## Descripción
Realiza un commit inteligente con análisis automático de cambios y mensajes en español apropiados para este repositorio educativo.

## Uso
```
/commit                           # Commit automático con mensaje generado
/commit "mensaje personalizado"   # Commit con mensaje específico
```

## Flujo de Trabajo

### 1. Análisis Previo
```bash
git status    # Mostrar estado actual
git diff      # Mostrar cambios específicos  
git log --oneline -3  # Ver estilo de commits recientes
```

### 2. Generación de Mensaje
- **Analizar cambios**: Identificar qué archivos fueron modificados
- **Contexto educativo**: Considerar el propósito pedagógico de los cambios
- **Estilo español**: Usar verbos en infinitivo (Agregar, Actualizar, Corregir)
- **Especificidad**: Mencionar bloques/semanas/ejercicios específicos si aplica

### 3. Formato de Commit
```
[Título descriptivo en español - máximo 50 caracteres]

[Descripción detallada opcional]
- Cambio específico 1
- Cambio específico 2
- Cambio específico 3

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### 4. Ejecución
```bash
git add .        # Agregar todos los cambios
git commit -m "[mensaje]"  # Commit con mensaje generado
git status       # Verificar resultado
```

## Ejemplos de Mensajes

### Cambios en Ejercicios
```
Actualizar ejercicios Semana 3: mejorar instrucciones de funciones

- Clarificar pasos para creación de funciones deportivas
- Agregar ejemplos adicionales con equipos españoles  
- Corregir errores menores en código base
```

### Cambios en Documentación
```
Mejorar documentación de instalación y configuración

- Actualizar requisitos de sistema para Python 3.9+
- Agregar instrucciones específicas para entornos virtuales
- Incluir solución para errores comunes de instalación
```

### Cambios en Datasets
```
Agregar nuevos datasets para análisis Bloque 2

- Incluir datos actualizados Liga Española 2023-24
- Agregar métricas avanzadas de jugadores
- Actualizar documentación de estructura de datos
```

## Reglas Especiales

### Para Este Repositorio
- **Siempre usar español** en títulos y descripciones
- **Mencionar contexto deportivo** cuando sea relevante
- **Especificar bloque/semana** si los cambios son específicos
- **Priorizar claridad educativa** sobre tecnicismos

### Casos Especiales
- **Notebooks (.ipynb)**: Mencionar contenido educativo modificado
- **Datasets (.csv)**: Especificar tipo de datos agregados/actualizados  
- **Rúbricas**: Indicar criterios de evaluación modificados
- **README**: Mencionar secciones actualizadas

## Verificación Post-Commit
```bash
git log -1 --pretty=format:"%h - %s (%an, %ar)"  # Mostrar último commit
git status  # Confirmar estado limpio
```
# Resumen: Nueva Estructura de Evaluación
## Curso de Análisis de Datos de Fútbol con Python

**Fecha de implementación:** Semestre actual  
**Alineación:** Estándares Tecnológico de Monterrey  
**Modalidad:** Competencias y proyectos colaborativos

---

## 1. SISTEMA DE PONDERACIONES

### Distribución General (100%)

```
 EVALUACIÓN COMPLETA DEL CURSO
├── 1er Parcial (35%) - Bloque 1: Python Fundamentals
│   ├── Examen Canvas (20%) - Fundamentos de programación
│   └── Caso Práctico Colaborativo (15%) - Análisis básico de club
│
├── 2do Parcial (35%) - Bloque 2: Exploración de Datos  
│   ├── Examen Canvas (20%) - Análisis y visualización
│   └── Caso Práctico Colaborativo (15%) - Sistema de scouting
│
└── Final (30%) - Bloque 3: Proyecto Integrador
    ├── Notebook Jupyter (20%) - Sistema predictivo completo
    └── Presentación (10%) - Comunicación de resultados
```

### Equivalencias con Syllabus Tec:
- **1er Parcial = Bloque 1** (35%)
- **2do Parcial = Bloque 2** (35%) 
- **Final = Bloque 3** (30%)
- **Sin actividades separadas** - Integradas en casos prácticos

---

## 2. COMPONENTES DE EVALUACIÓN DETALLADOS

### 2.1 Exámenes Canvas (40% total: 20% + 20%)

#### Características:
- **Modalidad:** Individual, automático
- **Formato:** 70% opción múltiple + 30% respuesta numérica
- **Duración:** 45-60 minutos cada uno
- **Banco:** 70-75 preguntas por bloque
- **Selección:** 20-25 preguntas aleatorias por examen

#### Bloque 1 - Canvas (20%):
```python
# Temas evaluados:
- Variables y tipos de datos (20%)
- Estructuras de control (20%) 
- Funciones y parámetros (20%)
- Listas y diccionarios (20%)
- Pandas y numpy básico (20%)
```

#### Bloque 2 - Canvas (20%):
```python
# Temas evaluados:
- Exploración de datos (25%)
- Tipos de datos deportivos (25%)
- Estadística descriptiva (25%)
- Visualización con seaborn (25%)
```

### 2.2 Casos Prácticos Colaborativos (30% total: 15% + 15%)

#### Modalidad de Trabajo:
- **Equipos:** 3-4 estudiantes
- **Duración:** 2 semanas cada caso
- **Entrega:** Notebook + Presentación grupal

#### Caso Bloque 1: "Análisis de Rendimiento de Club" (15%)
```markdown
## Objetivos:
- Aplicar fundamentos de Python
- Trabajar con funciones personalizadas
- Manipular listas y diccionarios
- Crear análisis deportivo básico

## Entregables:
- caso_bloque1_equipo[X].ipynb
- presentacion_equipo[X].pdf  
- reporte_equipo[X].pdf

## Evaluación:
- Análisis Técnico (40%)
- Trabajo Colaborativo (30%)
- Comunicación (30%)
```

#### Caso Bloque 2: "Sistema de Scouting y Análisis Táctico" (15%)
```markdown
## Objetivos:
- Exploración avanzada de datos
- Visualización con seaborn
- Análisis estadístico aplicado
- Dashboard interactivo básico

## Entregables:
- scouting_analysis_equipo[X].ipynb
- dashboard_equipo[X].ipynb
- presentacion_scouting_equipo[X].pdf
- reporte_scouting_equipo[X].pdf

## Evaluación:
- Exploración de Datos (30%)
- Visualizaciones (25%)
- Análisis Estadístico (25%)
- Trabajo Colaborativo (10%)
- Comunicación (10%)
```

### 2.3 Proyecto Integrador Final (30%)

#### Estructura del Proyecto:
```markdown
## "Sistema de Análisis Predictivo para Fútbol"
### Modalidad: Individual
### Duración: 4 semanas

## Componentes:
1. Notebook Jupyter (20% de la calificación total)
   - Análisis Exploratorio (25% del notebook)
   - Modelado ML (35% del notebook)
   - Dashboard Interactivo (25% del notebook)
   - Documentación (15% del notebook)

2. Presentación Final (10% de la calificación total)
   - 15 minutos individuales
   - Demo interactiva
   - Q&A técnico
```

---

## 3. CRONOGRAMA DE IMPLEMENTACIÓN

### Semestre Completo (16 semanas)

```
 CRONOGRAMA DETALLADO

🟦 BLOQUE 1: PYTHON FUNDAMENTALS (Semanas 1-5)
├── Semana 1: Variables y tipos de datos
├── Semana 2: Estructuras de control
├── Semana 3: Funciones
├── Semana 4: Listas y diccionarios  
├── Semana 5: Pandas y numpy básico
└──  Evaluación Bloque 1:
    ├── Examen Canvas B1 (Semana 6)
    └── Caso Práctico B1 (Semanas 6-7)

🟩 BLOQUE 2: EXPLORACIÓN DE DATOS (Semanas 8-12)
├── Semana 8: Introducción exploración
├── Semana 9: Tipos de datos deportivos
├── Semana 10: Estadística descriptiva
├── Semana 11: Visualización datos
├── Semana 12: Análisis e interpretación
└──  Evaluación Bloque 2:
    ├── Examen Canvas B2 (Semana 13)  
    └── Caso Práctico B2 (Semanas 13-14)

🟨 BLOQUE 3: PROYECTO INTEGRADOR (Semanas 15-16)
├── Semana 15: Desarrollo proyecto
├── Semana 16: Presentaciones finales
└──  Evaluación Final (30%)
```

---

## 4. HERRAMIENTAS Y RECURSOS CREADOS

### 4.1 Bancos de Preguntas Canvas

#### Para Profesores:
```
 evaluaciones/canvas/
├── banco-preguntas-bloque1.md (70 preguntas)
│   ├── Variables y tipos (10 preguntas)
│   ├── Estructuras control (10 preguntas)
│   ├── Funciones (10 preguntas) 
│   ├── Listas/diccionarios (15 preguntas)
│   ├── Pandas/numpy (15 preguntas)
│   └── Aplicaciones prácticas (10 preguntas)
│
└── banco-preguntas-bloque2.md (75 preguntas)
    ├── Exploración datos (20 preguntas)
    ├── Tipos datos deportivos (20 preguntas)
    ├── Estadística descriptiva (15 preguntas)
    ├── Visualización (15 preguntas)
    └── Análisis integrado (5 preguntas)
```

#### Configuración Canvas:
- **Importación directa** desde archivos markdown
- **Selección aleatoria** configurada
- **Retroalimentación automática** incluida
- **Análisis por temas** disponible

### 4.2 Casos Prácticos Documentados

```
 evaluaciones/casos-practicos/
├── caso-bloque1.md
│   ├── Contexto del problema
│   ├── Datasets proporcionados
│   ├── Tareas específicas requeridas
│   ├── Rúbricas de evaluación
│   ├── Cronograma detallado
│   └── Recursos de apoyo
│
└── caso-bloque2.md
    ├── Sistema de scouting completo
    ├── Análisis con múltiples datasets
    ├── Dashboard interactivo
    ├── Evaluación por competencias
    └── Templates de código incluidos
```

### 4.3 Proyecto Integrador Estructurado

```
 evaluaciones/proyecto-integrador/
└── README.md
    ├── 4 fases de desarrollo
    ├── Criterios técnicos específicos
    ├── Rúbricas detalladas
    ├── Ejemplos de excelencia
    ├── Recursos y soporte
    └── Cronograma semanal
```

### 4.4 Rúbricas Completas

```
 evaluaciones/rubricas/
└── rubrica-completa.md
    ├── Criterios por componente
    ├── Escalas de calificación
    ├── Conversión a sistema Tec
    ├── Competencias transversales
    ├── Sistema de feedback
    └── Políticas de integridad
```

---

## 5. BENEFICIOS DE LA NUEVA ESTRUCTURA

### 5.1 Para Estudiantes

#### Aprendizaje Progresivo:
- **Scaffolding efectivo:** Cada bloque construye sobre el anterior
- **Contexto consistente:** Todo centrado en análisis deportivo
- **Aplicación práctica:** Conexión directa con casos reales
- **Desarrollo colaborativo:** Habilidades de trabajo en equipo

#### Evaluación Balanceada:
- **Múltiples oportunidades:** 6 componentes de evaluación
- **Diferentes modalidades:** Individual + colaborativa
- **Feedback continuo:** Mejora a lo largo del semestre
- **Competencias integradas:** Técnicas + comunicación + colaboración

### 5.2 Para Profesores

#### Implementación Simplificada:
- **Recursos completos:** Todo documentado y listo para usar
- **Evaluación automatizada:** Canvas configurado automáticamente
- **Rúbricas claras:** Criterios específicos y medibles
- **Flexibilidad:** Adaptable a diferentes contextos

#### Calidad Asegurada:
- **Alineación curricular:** Cumple estándares del Tec
- **Progresión lógica:** Desarrollo incremental de competencias  
- **Evaluación auténtica:** Problemas reales de la industria
- **Mejora continua:** Sistema de feedback integrado

### 5.3 Para la Institución

#### Estándares de Calidad:
- **Competencias verificables:** Resultados medibles y documentados
- **Empleabilidad:** Habilidades demandadas por la industria
- **Innovación pedagógica:** Metodología basada en proyectos
- **Escalabilidad:** Replicable en otros cursos similares

---

## 6. MÉTRICAS DE ÉXITO

### 6.1 Indicadores de Aprendizaje

#### Técnicos:
- **Dominio de Python:** >85% aprueban exámenes Canvas
- **Aplicación práctica:** >80% completan casos prácticos satisfactoriamente
- **Integración de conocimientos:** >75% logran proyecto final competente

#### Competencias:
- **Trabajo colaborativo:** Evidencia documentada en casos prácticos
- **Comunicación técnica:** Calidad de presentaciones y reportes
- **Pensamiento crítico:** Análisis e interpretación de datos

### 6.2 Indicadores de Satisfacción

#### Estudiantes:
- **Relevancia del contenido:** Conexión clara con aplicaciones reales
- **Carga de trabajo:** Balanceada y progresiva
- **Claridad de evaluación:** Criterios transparentes y justos

#### Empleadores:
- **Preparación práctica:** Graduados listos para trabajar
- **Habilidades técnicas:** Competencia en herramientas industriales
- **Capacidad analítica:** Pensamiento basado en datos

---

## 7. PRÓXIMOS PASOS PARA IMPLEMENTACIÓN

### 7.1 Preparación Técnica (Semana 1-2)

#### Canvas Setup:
```bash
# Configuración en Canvas:
1. Crear bancos de preguntas automáticamente
2. Configurar selección aleatoria
3. Establecer criterios de calificación
4. Programar fechas de liberación
```

#### Recursos Digitales:
```bash
# Preparar datasets:
1. Validar y limpiar datos proporcionados
2. Crear datasets de ejemplo adicionales  
3. Verificar compatibilidad con notebooks
4. Documentar estructura de archivos
```

### 7.2 Comunicación (Semana 2-3)

#### A Estudiantes:
- **Sesión informativa:** Nueva estructura y beneficios
- **Guía de transición:** Cambios respecto a formato anterior
- **Recursos de apoyo:** Tutoriales y material adicional
- **Expectativas claras:** Criterios de evaluación y fechas

#### A Colegas:
- **Presentación del sistema:** Compartir metodología y recursos
- **Sesión de calibración:** Unificar criterios de evaluación
- **Documentación completa:** Acceso a todos los materiales
- **Plan de mejora:** Incorporar feedback y ajustes

### 7.3 Monitoreo y Ajuste (Continuo)

#### Métricas de Seguimiento:
- **Tasas de aprobación** por componente
- **Calidad de entregas** según rúbricas
- **Feedback estudiantil** mediante encuestas
- **Tiempo de evaluación** del profesorado

#### Proceso de Mejora:
- **Revisión quincenal** de indicadores
- **Ajustes menores** basados en evidencia
- **Incorporación de feedback** estudiantil
- **Actualización de recursos** según necesidades

---

## 8. CONCLUSIONES

### 8.1 Transformación Lograda

Esta nueva estructura de evaluación representa una **transformación completa** del curso, pasando de un enfoque tradicional a un **sistema basado en competencias y proyectos colaborativos** que:

1. **Alinea con estándares institucionales** del Tecnológico de Monterrey
2. **Integra teoría y práctica** en contextos deportivos reales
3. **Desarrolla competencias profesionales** demandadas por la industria
4. **Proporciona herramientas completas** para implementación inmediata

### 8.2 Valor Agregado

#### Para el Aprendizaje:
- **Relevancia práctica:** Cada concepto aplicado a casos reales
- **Progresión lógica:** Construcción incremental de competencias
- **Evaluación auténtica:** Problemas similares a los profesionales
- **Desarrollo integral:** Técnicas + colaboración + comunicación

#### Para la Enseñanza:
- **Recursos completos:** 70+ preguntas, casos documentados, rúbricas detalladas
- **Implementación inmediata:** Todo listo para usar en el próximo semestre
- **Flexibilidad:** Adaptable a diferentes contextos y necesidades
- **Calidad asegurada:** Basado en mejores prácticas pedagógicas

### 8.3 Impacto Esperado

Con esta estructura, esperamos lograr:

- **95%+ de satisfacción estudiantil** con la relevancia del curso
- **85%+ de tasa de aprobación** con dominio competente
- **Empleabilidad mejorada** de graduados en análisis de datos
- **Modelo replicable** para otros cursos de ciencia de datos

---

*Esta estructura de evaluación representa un avance significativo hacia una educación más práctica, colaborativa y alineada con las necesidades actuales del mercado laboral en análisis de datos deportivos.*
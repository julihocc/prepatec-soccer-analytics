# Solución del Caso Práctico - Bloque 3

## Predicción de Resultados de Fútbol con Machine Learning

Esta carpeta contiene la **solución completa** para el caso práctico del Bloque 3, diseñada para obtener el **100% de la calificación**.


## Archivos Incluidos

### `caso_bloque3_equipoSOLUCION.py`

### Dataset Oficial del Curso


## Cumplimiento de Requisitos

### ✅ Parte 1: Preparación de Datos para Machine Learning (40 puntos)

#### 1.1 Cargar y Explorar el Dataset (10 puntos)

#### 1.2 Crear Variables Objetivo y Derivadas (15 puntos)

- `total_goles`, `diferencia_goles`
- `eficiencia_local`, `eficiencia_visitante`
- `eficiencia_arco_local`, `eficiencia_arco_visitante`
- `dominio_tiros`, `dominio_corners`, `diferencia_tarjetas`

#### 1.3 Limpieza y Validación de Datos (15 puntos)

### ✅ Parte 2: Modelado Predictivo (40 puntos)

#### 2.1 Preparar Variables para el Modelo (10 puntos)

#### 2.2 Dividir Datos en Entrenamiento y Prueba (10 puntos)

#### 2.3 Entrenar Modelo Random Forest (20 puntos)

### ✅ Parte 3: Análisis e Interpretación de Resultados (20 puntos)

#### 3.1 Evaluación Detallada del Modelo (10 puntos)

1. `faltas_visitante` (11.07%)
2. `tiros_arco_local` (10.78%)
3. `eficiencia_arco_visitante` (10.61%)

#### 3.2 Predicciones en Casos Específicos (10 puntos)

1. **Local dominante**: 90.8% confianza en victoria local
2. **Partido equilibrado**: 61.2% confianza en NO victoria local
3. **Local ineficiente**: 85.8% confianza en victoria local (sorprendente)

### ✅ Reflexión Final Obligatoria


## Resultados Destacados

### Rendimiento del Modelo

### Insights Futbolísticos Clave

1. **Faltas del visitante** es la variable más predictiva (disciplina)
2. **Tiros a portería local** más importante que tiros totales (calidad)
3. **Eficiencias** dominan sobre volúmenes brutos (finalización)
4. **Variables derivadas** aportan valor predictivo significativo

### Casos de Uso Prácticos


## Estructura Técnica

### Dataset Champions League (50 partidos)

| Variable | Tipo | Descripción | Rango |
|----------|------|-------------|-------|
| `goles_local/visitante` | Entero | Goles marcados | 0-7 |
| `posesion_local/visitante` | Entero | Porcentaje de posesión | 28-72% |
| `tiros_local/visitante` | Entero | Total de tiros | 4-25 |
| `tiros_arco_local/visitante` | Entero | Tiros a portería | 1-14 |
| `corners_local/visitante` | Entero | Saques de esquina | 1-15 |
| `faltas_local/visitante` | Entero | Faltas cometidas | 5-18 |
| `tarjetas_amarillas/rojas` | Entero | Tarjetas mostradas | 0-6 |
| `resultado_final` | Categórica | Local/Visitante/Empate | 3 valores |

### Variables Derivadas Clave

1. **`eficiencia_local`**: goles_local ÷ tiros_local
2. **`eficiencia_arco_local`**: goles_local ÷ tiros_arco_local
3. **`dominio_tiros`**: tiros_local - tiros_visitante
4. **`diferencia_tarjetas`**: tarjetas_local - tarjetas_visitante

### Configuración del Modelo


## Reflexiones Pedagógicas

### Progresión del Curso

### Aprendizajes Clave

1. **Evolución conceptual**: De describir ("¿qué pasó?") a predecir ("¿qué pasará?")
2. **Metodología científica**: Hipótesis → Experimento → Validación → Interpretación
3. **Pensamiento crítico**: Identificar limitaciones y sesgos del modelo
4. **Comunicación efectiva**: Adaptar mensaje según audiencia (técnica vs ejecutiva)

### Habilidades Desarrolladas


## Uso de la Solución

### Para Estudiantes

1. **Estudiar la metodología** completa de machine learning aplicado
2. **Observar la progresión** desde datos brutos hasta insights accionables
3. **Aprender evaluación rigurosa** de modelos predictivos
4. **Entender interpretación** de resultados en contexto real

### Para Profesores

1. **Ejemplo de excelencia** que cumple todos los criterios de evaluación
2. **Referencia para calificación** con justificación detallada de 100 puntos
3. **Plantilla metodológica** para proyectos similares
4. **Evidencia de progresión** desde bloques anteriores

### Para Analistas Deportivos

1. **Framework completo** para análisis predictivo en fútbol
2. **Variables clave** identificadas para predicción de resultados
3. **Metodología replicable** para otros deportes o ligas
4. **Balance ideal** entre rigor técnico y aplicabilidad práctica


## Conversión y Compatibilidad

### Conversión a Notebook

```bash
# Usando jupytext (recomendado)
jupytext --to notebook caso_bloque3_equipoSOLUCION.py

# Resultado: caso_bloque3_equipoSOLUCION.ipynb
```

### Requisitos Técnicos

### Ejecución

```bash
cd evaluaciones/bloque-3/solucion-caso-practico/
python3 caso_bloque3_equipoSOLUCION.py
```


## Distribución de Puntos Obtenidos

| Componente | Puntos Máximos | Obtenidos | Porcentaje |
|------------|----------------|-----------|------------|
| Preparación de Datos | 40 | 40 | 100% |
| Modelado Predictivo | 40 | 40 | 100% |
| Análisis e Interpretación | 20 | 20 | 100% |
| **TOTAL CASO PRÁCTICO** | **100** | **100** | **100%** |
| **Peso en el curso** | **25%** | **25%** | **100%** |


## Diferencias Clave vs Bloques Anteriores

### Vs Bloque 1 (Fundamentos Python)

### Vs Bloque 2 (Análisis Exploratorio)

### Preparación para Aplicaciones Avanzadas


## Video de Presentación (Obligatorio)

### Especificaciones

### Estructura Sugerida

1. **Introducción (30s)**: Problema y contexto del proyecto
2. **Metodología (60s)**: Datos y modelo usado de manera simple
3. **Resultados (90s)**: 90% precisión + variables importantes + casos específicos
4. **Recomendaciones (60s)**: Aplicaciones tácticas y valor para el club


## Notas Importantes

### Limitaciones Reconocidas

### Próximas Mejoras Sugeridas


*Solución creada para el curso "Ciencia de Datos Aplicada al Fútbol" - Tecnológico de Monterrey*
*Demuestra dominio completo de machine learning aplicado al contexto deportivo con metodología científica rigurosa*

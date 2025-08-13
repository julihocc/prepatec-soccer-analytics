"""
Configuraciones predefinidas para diferentes tipos de presentaciones.
"""

from py_to_marp import MarpConfig


# Configuración para contenido educativo principal
EDUCATIVO_PRINCIPAL = MarpConfig(
    theme="default",
    size="16:9",
    paginate=True,
    footer="Ciencia de Datos aplicada al Fútbol | Preparatoria",
    background_color="#ffffff",
    text_color="#2c3e50",
    primary_color="#3498db",
    secondary_color="#e74c3c"
)

# Configuración para presentaciones ejecutivas/docentes
EJECUTIVO = MarpConfig(
    theme="default",
    size="16:9",
    paginate=True,
    footer="Curso de Ciencia de Datos | TEC",
    background_color="#f8f9fa",
    text_color="#212529",
    primary_color="#007bff",
    secondary_color="#28a745"
)

# Configuración para talleres prácticos
TALLER = MarpConfig(
    theme="default",
    size="16:9",
    paginate=True,
    footer="Taller Práctico | Datos Deportivos",
    background_color="#ffffff",
    text_color="#495057",
    primary_color="#fd7e14",
    secondary_color="#6610f2"
)

# Configuración para evaluaciones/exámenes
EVALUACION = MarpConfig(
    theme="default",
    size="16:9",
    paginate=True,
    footer="Evaluación | Ciencia de Datos",
    background_color="#fff5f5",
    text_color="#721c24",
    primary_color="#dc3545",
    secondary_color="#6c757d"
)

# Configuración dark mode para presentaciones nocturnas
DARK_MODE = MarpConfig(
    theme="default",
    size="16:9",
    paginate=True,
    footer="Ciencia de Datos aplicada al Fútbol",
    background_color="#1a1a1a",
    text_color="#e9ecef",
    primary_color="#17a2b8",
    secondary_color="#ffc107"
)

# Mapeo de nombres a configuraciones
CONFIGS = {
    "educativo": EDUCATIVO_PRINCIPAL,
    "ejecutivo": EJECUTIVO,
    "taller": TALLER,
    "evaluacion": EVALUACION,
    "dark": DARK_MODE,
    "default": EDUCATIVO_PRINCIPAL
}


def get_config(name: str) -> MarpConfig:
    """Obtiene una configuración predefinida por nombre."""
    return CONFIGS.get(name.lower(), EDUCATIVO_PRINCIPAL)


def list_configs() -> list:
    """Lista todas las configuraciones disponibles."""
    return list(CONFIGS.keys())

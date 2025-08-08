# .ai/ - Contexto para Asistentes de IA

Esta carpeta contiene todos los archivos de contexto e instrucciones para asistentes de IA trabajando en este proyecto.

## Archivos en esta carpeta

### 📖 `AI-CONTEXT.md`
**Archivo principal de contexto** - Contiene toda la información necesaria sobre:
- Visión general del proyecto educativo
- Estructura del repositorio
- Estándares de código y desarrollo
- Metodología educativa
- Patrones y convenciones

### 🤖 `copilot-instructions.md`
**Instrucciones específicas para GitHub Copilot** - Contiene:
- Patrones de código preferidos
- Directrices de autocompletado
- Estructura de notebooks
- Referencias al contexto principal

## Uso

### Para Claude Code
- Lee `CLAUDE.md` en la raíz del proyecto
- Será redirigido automáticamente a `AI-CONTEXT.md`

### Para GitHub Copilot
- El archivo `.github-copilot-instructions.md` en la raíz es un enlace simbólico
- Apunta a `copilot-instructions.md` en esta carpeta
- GitHub Copilot lo detecta automáticamente

### Para otros asistentes de IA
- Consulta directamente `AI-CONTEXT.md` para contexto completo
- Usa `copilot-instructions.md` como referencia para patrones de código

## Arquitectura

```
.ai/
├── AI-CONTEXT.md           # 📖 Contexto principal (fuente única)
├── copilot-instructions.md # 🤖 Instrucciones específicas para Copilot
└── README.md              # 📋 Este archivo

/
├── CLAUDE.md              # ↗️ Redirige a .ai/AI-CONTEXT.md
└── .github-copilot-instructions.md # 🔗 Enlace simbólico a .ai/copilot-instructions.md
```

## Beneficios de esta organización

- **📁 Estructura limpia** - Archivos de IA organizados en una carpeta
- **🎯 Sin duplicación** - Una fuente única de contexto
- **🔧 Funcionalidad preservada** - Enlaces simbólicos mantienen compatibilidad
- **📈 Escalabilidad** - Fácil agregar nuevos asistentes
- **🔄 Mantenimiento** - Solo actualizar AI-CONTEXT.md

---

**Archivo principal:** [AI-CONTEXT.md](./AI-CONTEXT.md)

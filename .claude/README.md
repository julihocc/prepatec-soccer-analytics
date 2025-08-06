# Claude Commands

Este directorio contiene comandos personalizados para Claude Code cuando trabaja en este repositorio.

## Estructura

```
.claude/
├── README.md          # Este archivo
└── commands/          # Comandos personalizados
    ├── commit.md      # Comando para commits inteligentes
    └── [otros].md     # Comandos adicionales
```

## Uso

Los comandos se invocan escribiendo `/[comando]` en el chat con Claude:

- `/commit` - Commit inteligente con mensajes en español
- `/commit "mensaje personalizado"` - Commit con mensaje específico

## Características

- **Contexto del repositorio**: Comandos específicos para curso de análisis deportivo
- **Idioma español**: Mensajes de commit en español siguiendo el estilo del repo
- **Flujo completo**: Verificación, análisis y commit automático
- **Atribución Claude**: Incluye automáticamente la atribución requerida
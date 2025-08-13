# Makefile para py-to-marp converter

PYTHON = python3
CONVERTER = ./convert.py
CONTENIDO_DIR = ../../contenido

.PHONY: help test list-configs clean

.DEFAULT_GOAL := help

help:
	@echo "Convertidor py:percent a Marp"
	@echo ""
	@echo "Comandos disponibles:"
	@echo "  help            Muestra esta ayuda"
	@echo "  test            Ejecuta todos los tests"
	@echo "  list-configs    Lista configuraciones disponibles"
	@echo "  convert         Convierte archivo (FILE=path CONFIG=config)"
	@echo "  clean           Limpia archivos generados"

test:
	@echo "🧪 Ejecutando tests..."
	@$(PYTHON) tests/run_tests.py

list-configs:
	@$(PYTHON) $(CONVERTER) --list-configs

convert:
	@if [ -z "$(FILE)" ]; then \
		echo "❌ Error: especifica FILE=path/to/file.py"; \
		exit 1; \
	fi
	@$(PYTHON) $(CONVERTER) $(FILE) --config $(or $(CONFIG),educativo)

clean:
	@echo "🧹 Limpiando archivos de test..."
	@find . -name "test_*.md" -delete 2>/dev/null || true
	@echo "✅ Limpieza completada"

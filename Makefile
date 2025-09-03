# Makefile para PS5005 Programación Básica 1 - Ciencia de Datos aplicada al Fútbol
# Prepa Tec

# Variables
CONTENIDO_DIR = ./contenido
SCRIPTS_DIR = ./scripts
PDFS_DIR = ./pdfs

# Colores para output
GREEN = \033[0;32m
YELLOW = \033[1;33m
NC = \033[0m # No Color

.PHONY: help pdfs pdfs-separate clean-pdfs install-deps test-conversion check-deps notebook-tools

# Regla por defecto
help:
	@echo "$(YELLOW)Makefile para Ciencia de Datos aplicada al Fútbol$(NC)"
	@echo ""
	@echo "$(GREEN)Comandos disponibles:$(NC)"
	@echo "  make pdfs           - Convertir todos los notebooks a PDF"
	@echo "  make pdfs-separate  - Convertir PDFs a directorio separado"
	@echo "  make clean-pdfs     - Eliminar todos los PDFs generados"
	@echo "  make check-deps     - Verificar dependencias instaladas"
	@echo "  make install-deps   - Instalar dependencias (Ubuntu/Debian)"
	@echo "  make test-conversion - Probar conversión con un archivo"
	@echo "  make help           - Mostrar esta ayuda"

# Convertir todos los notebooks a PDF (en mismo directorio)
pdfs: check-deps
	@echo "$(GREEN)Convirtiendo todos los notebooks a PDF...$(NC)"
	$(SCRIPTS_DIR)/convert_notebooks_to_pdf.sh $(CONTENIDO_DIR)

# Convertir PDFs a directorio separado
pdfs-separate: check-deps
	@echo "$(GREEN)Convirtiendo notebooks a PDF en directorio separado...$(NC)"
	@mkdir -p $(PDFS_DIR)
	$(SCRIPTS_DIR)/convert_notebooks_to_pdf.sh -o $(PDFS_DIR) $(CONTENIDO_DIR)

# Limpiar PDFs generados
clean-pdfs:
	@echo "$(GREEN)Eliminando PDFs generados...$(NC)"
	@find $(CONTENIDO_DIR) -name "*.pdf" -delete 2>/dev/null || true
	@rm -rf $(PDFS_DIR) 2>/dev/null || true
	@echo "PDFs eliminados."

# Verificar dependencias
check-deps:
	@echo "$(GREEN)Verificando dependencias...$(NC)"
	@command -v pandoc >/dev/null 2>&1 || { echo "❌ pandoc no está instalado"; exit 1; }
	@command -v xelatex >/dev/null 2>&1 || { echo "⚠️  xelatex no está instalado (recomendado)"; }
	@echo "✓ Dependencias verificadas"

# Instalar dependencias (Ubuntu/Debian)
install-deps:
	@echo "$(GREEN)Instalando dependencias...$(NC)"
	sudo apt update
	sudo apt install -y pandoc texlive-xetex texlive-fonts-recommended
	@echo "✓ Dependencias instaladas"

# Probar conversión con un archivo
test-conversion: check-deps
	@echo "$(GREEN)Probando conversión con modo dry-run...$(NC)"
	$(SCRIPTS_DIR)/convert_notebooks_to_pdf.sh --dry-run --no-recursive $(CONTENIDO_DIR)/bloque-1/semana-1

# Reglas para desarrollo
lint-scripts:
	@echo "$(GREEN)Verificando scripts...$(NC)"
	@shellcheck $(SCRIPTS_DIR)/*.sh 2>/dev/null || echo "shellcheck no disponible"
	@python3 -m py_compile $(SCRIPTS_DIR)/*.py

# Mostrar estadísticas
stats:
	@echo "$(GREEN)Estadísticas del proyecto:$(NC)"
	@echo "Notebooks: $$(find $(CONTENIDO_DIR) -name '*.ipynb' | wc -l)"
	@echo "PDFs: $$(find $(CONTENIDO_DIR) -name '*.pdf' | wc -l)"
	@echo "Scripts: $$(find $(SCRIPTS_DIR) -name '*.sh' -o -name '*.py' | wc -l)"

# === HERRAMIENTAS DE CONVERSIÓN ===

# Convertir notebooks con herramientas profesionales
notebook-tools: ## Usar herramientas profesionales para convertir notebooks
	@echo "$(GREEN)Convirtiendo notebooks con herramientas profesionales...$(NC)"
	python3 herramientas/notebook-to-pdf/smart_convert.py $(CONTENIDO_DIR)/

# Ver estado de conversión
notebook-status: ## Ver estado de conversión de notebooks
	@echo "$(GREEN)Estado de conversión de notebooks:$(NC)"
	python3 herramientas/notebook-to-pdf/smart_convert.py $(CONTENIDO_DIR)/ --status

# Regenerar todos los PDFs
notebook-update: ## Regenerar todos los PDFs con herramientas profesionales
	@echo "$(GREEN)Regenerando todos los PDFs...$(NC)"
	python3 herramientas/notebook-to-pdf/smart_convert.py $(CONTENIDO_DIR)/ --force

# Limpiar PDFs generados por herramientas
notebook-clean: ## Eliminar PDFs generados por herramientas profesionales
	@echo "$(GREEN)Limpiando PDFs generados por herramientas...$(NC)"
	find $(CONTENIDO_DIR)/ -name "*.pdf" -delete
	rm -f .conversion_cache.json
	@echo "✓ PDFs eliminados"

# Vista previa de conversión
notebook-preview: ## Vista previa de qué notebooks se convertirían
	@echo "$(GREEN)Vista previa de conversión:$(NC)"
	python3 herramientas/notebook-to-pdf/smart_convert.py $(CONTENIDO_DIR)/ --dry-run

# Verificar dependencias de herramientas
notebook-deps: ## Verificar dependencias de herramientas de conversión
	@echo "$(GREEN)Verificando dependencias de herramientas...$(NC)"
	python3 herramientas/notebook-to-pdf/convert.py --check-deps

# Tests de herramientas
notebook-test: ## Ejecutar tests de herramientas de conversión
	@echo "$(GREEN)Ejecutando tests de herramientas...$(NC)"
	python3 herramientas/notebook-to-pdf/tests/run_tests.py

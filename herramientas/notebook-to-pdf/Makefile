# Makefile para Notebook to PDF Converter
# 
# Comandos de automatización para conversión de notebooks

.PHONY: help install-tools test-tools pdfs clean-pdfs update-pdfs status-pdfs deps-check

# Configuración
TOOLS_DIR = herramientas/notebook-to-pdf
CONTENT_DIR = contenido

help: ## Mostrar esta ayuda
	@echo "Notebook to PDF Converter - Comandos disponibles:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install-tools: ## Instalar dependencias del sistema
	@echo "Instalando dependencias..."
	sudo apt update
	sudo apt install -y pandoc texlive-xetex texlive-fonts-recommended
	@echo "✓ Dependencias instaladas"

deps-check: ## Verificar dependencias
	@echo "Verificando dependencias..."
	python3 $(TOOLS_DIR)/convert.py --check-deps

test-tools: ## Ejecutar tests de las herramientas
	@echo "Ejecutando tests..."
	python3 $(TOOLS_DIR)/tests/run_tests.py

pdfs: ## Convertir notebooks a PDF (inteligente)
	@echo "Convirtiendo notebooks a PDF..."
	python3 $(TOOLS_DIR)/smart_convert.py $(CONTENT_DIR)/

update-pdfs: ## Regenerar todos los PDFs (forzado)
	@echo "Regenerando todos los PDFs..."
	python3 $(TOOLS_DIR)/smart_convert.py $(CONTENT_DIR)/ --force

status-pdfs: ## Mostrar estado de conversión
	@echo "Estado de conversión de notebooks:"
	python3 $(TOOLS_DIR)/smart_convert.py $(CONTENT_DIR)/ --status

clean-pdfs: ## Eliminar todos los PDFs generados
	@echo "Eliminando PDFs..."
	find $(CONTENT_DIR)/ -name "*.pdf" -delete
	rm -f .conversion_cache.json
	@echo "✓ PDFs eliminados"

dry-run-pdfs: ## Vista previa de conversión (sin ejecutar)
	@echo "Vista previa de conversión:"
	python3 $(TOOLS_DIR)/smart_convert.py $(CONTENT_DIR)/ --dry-run

# Comandos por motor específico
pdfs-xelatex: ## Convertir con XeLaTeX
	python3 $(TOOLS_DIR)/convert.py $(CONTENT_DIR)/ --engine xelatex

pdfs-pdflatex: ## Convertir con PDFLaTeX
	python3 $(TOOLS_DIR)/convert.py $(CONTENT_DIR)/ --engine pdflatex

pdfs-lualatex: ## Convertir con LuaLaTeX
	python3 $(TOOLS_DIR)/convert.py $(CONTENT_DIR)/ --engine lualatex

# Comandos de directorio específico
pdfs-bloque1: ## Convertir solo bloque 1
	python3 $(TOOLS_DIR)/smart_convert.py $(CONTENT_DIR)/bloque-1/

pdfs-bloque2: ## Convertir solo bloque 2
	python3 $(TOOLS_DIR)/smart_convert.py $(CONTENT_DIR)/bloque-2/

pdfs-bloque3: ## Convertir solo bloque 3
	python3 $(TOOLS_DIR)/smart_convert.py $(CONTENT_DIR)/bloque-3/

# Comandos de utilidad
tools-help: ## Mostrar ayuda de herramientas
	@echo "=== Convertidor Inteligente ==="
	python3 $(TOOLS_DIR)/smart_convert.py --help
	@echo ""
	@echo "=== Convertidor Clásico ==="
	python3 $(TOOLS_DIR)/convert.py --help
	@echo ""
	@echo "=== Script Shell ==="
	$(TOOLS_DIR)/convert.sh --help

stats-pdfs: ## Estadísticas de PDFs generados
	@echo "Estadísticas de PDFs:"
	@echo "Total notebooks: $$(find $(CONTENT_DIR)/ -name '*.ipynb' | wc -l)"
	@echo "Total PDFs: $$(find $(CONTENT_DIR)/ -name '*.pdf' | wc -l)"
	@echo "Tamaño total PDFs: $$(find $(CONTENT_DIR)/ -name '*.pdf' -exec stat -c%s {} \; | awk '{sum+=$$1} END {printf "%.1f MB\n", sum/1024/1024}')"

validate-notebooks: ## Validar formato de notebooks
	@echo "Validando notebooks..."
	@for notebook in $$(find $(CONTENT_DIR)/ -name "*.ipynb"); do \
		echo -n "Validando $$notebook... "; \
		if python3 -m json.tool "$$notebook" > /dev/null 2>&1; then \
			echo "✓"; \
		else \
			echo "✗ JSON inválido"; \
		fi; \
	done

# Comandos de desarrollo
dev-setup: ## Configuración para desarrollo
	chmod +x $(TOOLS_DIR)/*.py $(TOOLS_DIR)/*.sh
	@echo "✓ Permisos configurados"

dev-test: ## Test rápido de desarrollo
	python3 $(TOOLS_DIR)/smart_convert.py $(CONTENT_DIR)/bloque-1/semana-1/ --dry-run

# Comandos de CI/CD
ci-install: ## Instalación para CI/CD
	sudo apt-get update
	sudo apt-get install -y pandoc texlive-xetex
	python3 $(TOOLS_DIR)/convert.py --check-deps

ci-test: ## Tests para CI/CD
	python3 $(TOOLS_DIR)/tests/run_tests.py

ci-build: ## Build para CI/CD
	python3 $(TOOLS_DIR)/convert.py $(CONTENT_DIR)/ --dry-run
	python3 $(TOOLS_DIR)/convert.py $(CONTENT_DIR)/

# Información
info: ## Mostrar información del sistema
	@echo "=== Información del Sistema ==="
	@echo "Python: $$(python3 --version)"
	@echo "Pandoc: $$(pandoc --version | head -1)"
	@echo "XeLaTeX: $$(xelatex --version | head -1)"
	@echo ""
	@echo "=== Estructura del Proyecto ==="
	@echo "Notebooks: $$(find $(CONTENT_DIR)/ -name '*.ipynb' | wc -l)"
	@echo "PDFs: $$(find $(CONTENT_DIR)/ -name '*.pdf' | wc -l)"
	@echo ""
	@echo "=== Herramientas Disponibles ==="
	@ls -la $(TOOLS_DIR)/*.py $(TOOLS_DIR)/*.sh

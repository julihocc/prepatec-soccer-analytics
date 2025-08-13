# Makefile para py-to-marp converter
# Convierte archivos py:percent a presentaciones Marp

PYTHON = python3
CONVERTER = ./convert.py

# Directorio de contenido
CONTENIDO_DIR = ../../contenido

# Configuraciones disponibles
CONFIGS = educativo ejecutivo taller evaluacion dark

.PHONY: help install test convert-all convert-bloque list-configs clean

help:  ## Muestra esta ayuda
	@echo "Convertidor py:percent a Marp"
	@echo ""
	@echo "Comandos disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "Ejemplos:"
	@echo "  make convert FILE=path/to/file.py CONFIG=educativo"
	@echo "  make convert-bloque BLOQUE=1 CONFIG=taller"
	@echo "  make convert-all CONFIG=dark"

install:  ## Instala dependencias (si las hay)
	@echo "✅ No hay dependencias adicionales requeridas"
	@echo "   Solo se necesita Python 3.6+ y Marp CLI para exportar"

test:  ## Prueba la conversión con un archivo de ejemplo
	@if [ -f "$(CONTENIDO_DIR)/bloque-1/semana-1/configuracion-fundamentos.py" ]; then \
		echo "🧪 Probando conversión..."; \
		$(PYTHON) $(CONVERTER) $(CONTENIDO_DIR)/bloque-1/semana-1/configuracion-fundamentos.py --config educativo; \
	else \
		echo "❌ No se encontró archivo de prueba"; \
	fi

list-configs:  ## Lista todas las configuraciones disponibles
	@$(PYTHON) $(CONVERTER) --list-configs

convert:  ## Convierte un archivo específico (usar FILE=path CONFIG=config)
	@if [ -z "$(FILE)" ]; then \
		echo "❌ Error: especifica FILE=path/to/file.py"; \
		exit 1; \
	fi
	@$(PYTHON) $(CONVERTER) $(FILE) --config $(or $(CONFIG),educativo)

convert-bloque:  ## Convierte todos los archivos de un bloque (usar BLOQUE=1,2,3 CONFIG=config)
	@if [ -z "$(BLOQUE)" ]; then \
		echo "❌ Error: especifica BLOQUE=1, BLOQUE=2 o BLOQUE=3"; \
		exit 1; \
	fi
	@echo "🔄 Convirtiendo archivos del bloque $(BLOQUE)..."
	@find $(CONTENIDO_DIR)/bloque-$(BLOQUE) -name "*.py" -type f | while read file; do \
		echo "   Procesando $$file"; \
		$(PYTHON) $(CONVERTER) "$$file" --config $(or $(CONFIG),educativo); \
	done

convert-all:  ## Convierte todos los archivos .py del contenido (usar CONFIG=config)
	@echo "🔄 Convirtiendo todos los archivos py:percent a Marp..."
	@find $(CONTENIDO_DIR) -name "*.py" -type f | while read file; do \
		echo "   Procesando $$file"; \
		$(PYTHON) $(CONVERTER) "$$file" --config $(or $(CONFIG),educativo); \
	done
	@echo "✅ Conversión masiva completada"

convert-dir:  ## Convierte todos los archivos .py de un directorio específico (usar DIR=path CONFIG=config)
	@if [ -z "$(DIR)" ]; then \
		echo "❌ Error: especifica DIR=path/to/directory"; \
		exit 1; \
	fi
	@if [ ! -d "$(DIR)" ]; then \
		echo "❌ Error: el directorio $(DIR) no existe"; \
		exit 1; \
	fi
	@echo "🔄 Convirtiendo archivos .py en $(DIR)..."
	@find "$(DIR)" -name "*.py" -type f | while read file; do \
		echo "   Procesando $$file"; \
		$(PYTHON) $(CONVERTER) "$$file" --config $(or $(CONFIG),educativo); \
	done
	@echo "✅ Conversión de directorio completada"

clean:  ## Limpia archivos .md generados
	@echo "🧹 Limpiando archivos .md generados..."
	@find $(CONTENIDO_DIR) -name "*.md" -type f -delete
	@echo "✅ Archivos .md eliminados"

export-pdf:  ## Exporta presentaciones a PDF (requiere marp-cli)
	@echo "📄 Exportando presentaciones a PDF..."
	@find $(CONTENIDO_DIR) -name "*.md" -type f | while read file; do \
		echo "   Exportando $$file"; \
		marp "$$file" -o "$${file%.md}.pdf" 2>/dev/null || echo "   ⚠️  Error exportando $$file (¿marp-cli instalado?)"; \
	done

watch:  ## Modo observación para desarrollo (usar FILE=path)
	@if [ -z "$(FILE)" ]; then \
		echo "❌ Error: especifica FILE=path/to/file.py"; \
		exit 1; \
	fi
	@echo "👀 Observando cambios en $(FILE)..."
	@while true; do \
		$(PYTHON) $(CONVERTER) $(FILE) --config $(or $(CONFIG),educativo); \
		echo "   Esperando cambios... (Ctrl+C para salir)"; \
		sleep 5; \
	done

# Targets específicos por configuración
educativo:  ## Convierte con configuración educativa
	@$(MAKE) convert-all CONFIG=educativo

ejecutivo:  ## Convierte con configuración ejecutiva
	@$(MAKE) convert-all CONFIG=ejecutivo

taller:  ## Convierte con configuración de taller
	@$(MAKE) convert-all CONFIG=taller

evaluacion:  ## Convierte con configuración de evaluación
	@$(MAKE) convert-all CONFIG=evaluacion

dark:  ## Convierte con configuración dark mode
	@$(MAKE) convert-all CONFIG=dark

# Targets por bloque
bloque1:  ## Convierte solo bloque 1
	@$(MAKE) convert-bloque BLOQUE=1 CONFIG=$(or $(CONFIG),educativo)

bloque2:  ## Convierte solo bloque 2
	@$(MAKE) convert-bloque BLOQUE=2 CONFIG=$(or $(CONFIG),educativo)

bloque3:  ## Convierte solo bloque 3
	@$(MAKE) convert-bloque BLOQUE=3 CONFIG=$(or $(CONFIG),educativo)

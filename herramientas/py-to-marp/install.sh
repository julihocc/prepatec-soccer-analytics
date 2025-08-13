#!/bin/bash
# Script de instalación para py-to-marp converter

echo "🚀 Configurando py-to-marp converter..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi

echo "✅ Python 3 encontrado: $(python3 --version)"

# Verificar Node.js para Marp CLI (opcional)
if command -v node &> /dev/null; then
    echo "✅ Node.js encontrado: $(node --version)"
    
    # Verificar si marp-cli está instalado
    if command -v marp &> /dev/null; then
        echo "✅ Marp CLI ya está instalado: $(marp --version)"
    else
        echo "📦 Instalando Marp CLI..."
        npm install -g @marp-team/marp-cli
        
        if command -v marp &> /dev/null; then
            echo "✅ Marp CLI instalado correctamente"
        else
            echo "⚠️  Error instalando Marp CLI. Instálalo manualmente:"
            echo "   npm install -g @marp-team/marp-cli"
        fi
    fi
else
    echo "⚠️  Node.js no encontrado. Para exportar a PDF/PNG, instala:"
    echo "   1. Node.js: https://nodejs.org/"
    echo "   2. Marp CLI: npm install -g @marp-team/marp-cli"
fi

# Hacer ejecutables los scripts
chmod +x convert.py 2>/dev/null || true

echo ""
echo "🎉 Configuración completada!"
echo ""
echo "Comandos disponibles:"
echo "  make help              # Ver ayuda completa"
echo "  make list-configs      # Ver configuraciones"
echo "  make test              # Probar conversión"
echo ""
echo "Ejemplo de uso:"
echo "  python3 convert.py archivo.py --config educativo"

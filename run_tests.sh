#!/bin/bash
# Script para ejecutar todas las pruebas de Behave en el proyecto Migraña App

echo "🚀 Iniciando pruebas BDD con Behave para Migraña App"
echo "=================================================="

# Cambiar al directorio del backend
cd "$(dirname "$0")/backend"

# Verificar que estamos en el directorio correcto
if [ ! -f "manage.py" ]; then
    echo "❌ Error: No se encontró manage.py. Asegúrate de estar en el directorio correcto."
    exit 1
fi

# Configurar variables de entorno
export DJANGO_SETTINGS_MODULE=migraine_app.settings

echo "📦 Instalando dependencias..."
pip install -r requirements.txt

echo "🔄 Ejecutando migraciones de Django..."
python manage.py migrate

echo ""
echo "🧪 Ejecutando pruebas de Agendamiento de Citas..."
behave agendamiento_citas/features/ --format=progress

echo ""
echo "🧪 Ejecutando pruebas de Evaluación y Diagnóstico..."
behave evaluacion_diagnostico/features/ --format=progress

echo ""
echo "🧪 Ejecutando pruebas de Tratamiento..."
behave tratamiento/features/ --format=progress

echo ""
echo "🧪 Ejecutando pruebas de Analíticas..."
behave analiticas/features/ --format=progress

echo ""
echo "📊 Generando reporte consolidado..."
behave --format=json --outfile=behave_results.json
behave --format=pretty

echo ""
echo "✅ Pruebas completadas. Revisa el archivo behave_results.json para más detalles."

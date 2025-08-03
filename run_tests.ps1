# Script PowerShell para ejecutar todas las pruebas de Behave en el proyecto Migraña App

Write-Host "🚀 Iniciando pruebas BDD con Behave para Migraña App" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green

# Cambiar al directorio del backend
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location "$scriptPath\backend"

# Verificar que estamos en el directorio correcto
if (-not (Test-Path "manage.py")) {
    Write-Host "❌ Error: No se encontró manage.py. Asegúrate de estar en el directorio correcto." -ForegroundColor Red
    exit 1
}

# Configurar variables de entorno
$env:DJANGO_SETTINGS_MODULE = "migraine_app.settings"

Write-Host "📦 Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host "🔄 Ejecutando migraciones de Django..." -ForegroundColor Yellow
python manage.py migrate

Write-Host ""
Write-Host "🧪 Ejecutando pruebas de Agendamiento de Citas..." -ForegroundColor Cyan
behave agendamiento_citas/features/ --format=progress

Write-Host ""
Write-Host "🧪 Ejecutando pruebas de Evaluación y Diagnóstico..." -ForegroundColor Cyan
behave evaluacion_diagnostico/features/ --format=progress

Write-Host ""
Write-Host "🧪 Ejecutando pruebas de Tratamiento..." -ForegroundColor Cyan
behave tratamiento/features/ --format=progress

Write-Host ""
Write-Host "🧪 Ejecutando pruebas de Analíticas..." -ForegroundColor Cyan
behave analiticas/features/ --format=progress

Write-Host ""
Write-Host "📊 Generando reporte consolidado..." -ForegroundColor Magenta
behave --format=json --outfile=behave_results.json
behave --format=pretty

Write-Host ""
Write-Host "✅ Pruebas completadas. Revisa el archivo behave_results.json para más detalles." -ForegroundColor Green

# Guía de Pruebas BDD para Migraña App

## Descripción

Este proyecto utiliza **Behave** para pruebas de comportamiento (BDD - Behavior Driven Development) escritas en Gherkin. Las pruebas están organizadas por módulos funcionales de la aplicación.

## Estructura de Pruebas

```
backend/
├── agendamiento_citas/features/
│   ├── agendamiento_citas.feature
│   └── steps/
│       └── step_AgendamientoCitas.py
├── evaluacion_diagnostico/features/
│   ├── autoevaluacion_midas.feature
│   ├── bitacora_digital.feature
│   ├── environment.py
│   └── steps/
│       ├── bitacora_digital_step.py
│       └── bitacora_digital.py
├── tratamiento/features/
│   ├── aseguramiento_tratamiento.feature
│   ├── generacion_seguimiento_tratamiento.feature
│   └── steps/
│       └── generacion_seguimiento_tratamiento.py
└── analiticas/features/
    ├── analisis_factores_desencadenantes.feature
    ├── estadisticas_historial.feature
    └── steps/
```

## Instalación de Dependencias

```bash
cd backend
pip install -r requirements.txt
```

Las dependencias incluyen:
- `behave==1.2.6` - Framework de BDD
- `behave-django==1.4.0` - Integración con Django

## Ejecutar Pruebas

### Opción 1: Scripts Automatizados

**En Windows (PowerShell):**
```powershell
.\run_tests.ps1
```

**En Linux/Mac:**
```bash
chmod +x run_tests.sh
./run_tests.sh
```

### Opción 2: Comandos Manuales

**Todas las pruebas:**
```bash
cd backend
behave
```

**Por módulo específico:**
```bash
# Agendamiento de citas
behave agendamiento_citas/features/

# Evaluación y diagnóstico
behave evaluacion_diagnostico/features/

# Tratamiento
behave tratamiento/features/

# Analíticas
behave analiticas/features/
```

**Con formato específico:**
```bash
# Formato detallado
behave --format=pretty

# Formato de progreso
behave --format=progress

# Formato JSON para integración
behave --format=json --outfile=results.json
```

## CI/CD

El proyecto incluye un workflow de GitHub Actions (`.github/workflows/ci.yml`) que:

1. **Configura el entorno:**
   - Python 3.11
   - PostgreSQL para pruebas
   - Dependencias del proyecto

2. **Ejecuta pruebas por módulo:**
   - Agendamiento de citas
   - Evaluación y diagnóstico
   - Tratamiento
   - Analíticas

3. **Genera reportes:**
   - Reporte consolidado en JSON
   - Artifacts para revisión

4. **Validaciones adicionales:**
   - Linting con flake8
   - Formateo con black
   - Ordenamiento de imports con isort
   - Pruebas de frontend (si existen)

## Configuración

### Variables de Entorno

El archivo `environment.py` configura Django automáticamente:

```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'migraine_app.settings')
```

### Configuración de Behave

El archivo `behave.ini` contiene la configuración global:

```ini
[behave]
paths = agendamiento_citas/features
        evaluacion_diagnostico/features
        tratamiento/features
        analiticas/features
format = pretty
django = true
```

## Escribir Nuevas Pruebas

### 1. Crear archivo .feature

```gherkin
#language: es

Característica: Nueva funcionalidad
  Como usuario
  Quiero realizar una acción
  Para obtener un resultado

  Escenario: Caso de prueba exitoso
    Dado que tengo las condiciones iniciales
    Cuando ejecuto una acción
    Entonces obtengo el resultado esperado
```

### 2. Implementar steps

```python
from behave import given, when, then

@given("que tengo las condiciones iniciales")
def step_given_conditions(context):
    # Configurar estado inicial
    pass

@when("ejecuto una acción")
def step_when_action(context):
    # Ejecutar la acción
    pass

@then("obtengo el resultado esperado")
def step_then_result(context):
    # Verificar resultado
    assert context.result == expected_value
```

## Resolución de Problemas

### Error: Django apps not ready
Asegúrate de que `environment.py` esté configurado correctamente y que Django esté instalado.

### Error: ModuleNotFoundError
Verifica que todas las dependencias estén instaladas y que el PYTHONPATH incluya el directorio del proyecto.

### Error: Database connection
En el CI, PostgreSQL se configura automáticamente. Localmente, asegúrate de tener una base de datos configurada en `settings.py`.

## Mejores Prácticas

1. **Scenarios descriptivos:** Usa nombres claros que describan el comportamiento esperado
2. **Steps reutilizables:** Crea steps que puedan ser reutilizados entre diferentes scenarios
3. **Datos de prueba:** Usa Faker para generar datos de prueba realistas
4. **Aislamiento:** Cada scenario debe ser independiente
5. **Cleanup:** Asegúrate de limpiar datos después de cada prueba

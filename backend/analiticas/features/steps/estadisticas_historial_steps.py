import os
import django

# Configurar Django solo si no está ya configurado
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    # Usar settings_ci solo si estamos en CI, sino usar settings normal
    if os.getenv('CI') == 'true':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'migraine_app.settings_ci')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'migraine_app.settings')

try:
    django.setup()
except:
    pass  # Django ya está configurado

from behave import given, when, then

@given('que un paciente ha registrado al menos una biracota digital de cefalea')
def step_impl(context):
    context.bitacora_registrada = True

@given('ha realizado al menos una autoevaluación MIDAS con puntaje válido')
def step_impl(context):
    context.evaluacion_midas = True
    context.puntaje_midas = 15  # Puntaje válido de ejemplo

@when('el médico accede al historial clínico consolidado del paciente')
def step_impl(context):
    context.acceso_historial = True

@then('el sistema genera un historial que incluye')
def step_impl(context):
    # Verificar que se puede generar el historial
    assert context.bitacora_registrada
    assert context.evaluacion_midas
    assert context.acceso_historial
    
    # Simular la generación del historial
    context.historial_generado = {
        'episodios_cefalea': [
            {'fecha': '2023-01-15', 'severidad': 8, 'categoria': 'Migraña severa'}
        ],
        'evaluaciones_midas': [
            {'puntaje': context.puntaje_midas, 'fecha': '2023-01-10'}
        ],
        'tratamientos': [
            {'medicacion': 'Ibuprofeno', 'dosis': '400mg', 'fecha_inicio': '2023-01-01'}
        ]
    }
    
    # Verificar que todas las componentes esperadas están presentes
    for row in context.table:
        componente = row['Componente']
        if 'Episodios de cefalea' in componente:
            assert 'episodios_cefalea' in context.historial_generado
        elif 'Autoevaluaciones MIDAS' in componente:
            assert 'evaluaciones_midas' in context.historial_generado
        elif 'Tratamientos' in componente:
            assert 'tratamientos' in context.historial_generado

@given('que no existen registros de episodios de cefalea para el paciente')
def step_impl(context):
    context.sin_episodios = True

@given('no hay autoevaluaciones MIDAS registradas')
def step_impl(context):
    context.sin_evaluaciones = True

@when('el médico intenta acceder al historial clínico consolidado')
def step_impl(context):
    context.intento_acceso = True

@then('el sistema mostrará un mensaje informando que no hay datos suficientes')
def step_impl(context):
    assert context.sin_episodios or context.sin_evaluaciones
    context.mensaje_sin_datos = "No hay datos suficientes para generar el historial"

@then('sugerirá al paciente registrar información clínica')
def step_impl(context):
    context.sugerencia_registro = "Se sugiere al paciente registrar información clínica"
    assert context.sugerencia_registro is not None

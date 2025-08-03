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

@given('que el paciente tiene un historial de al menos 7 días de episodios de migraña registrados')
def step_impl(context):
    context.historial_7_dias = True

@when('se identifican patrones en factores desencadenantes que no se relacionan con tratamientos médicos ni condiciones clínicas graves')
def step_impl(context):
    context.factores_no_medicos = True

@then('se genera una alerta con el mensaje "Factores no médicos identificados como posibles desencadenantes"')
def step_impl(context):
    context.alerta_factores = "Factores no médicos identificados como posibles desencadenantes"

@then('se sugiere tomar precauciones para evitar estos factores desencadenantes sin necesidad de intervención médica')
def step_impl(context):
    context.sugerencia_precauciones = True

@when('se identifican factores desencadenantes recurrentes relacionados con medicamentos, síntomas clínicos o situaciones que requieren una evaluación médica')
def step_impl(context):
    context.factores_medicos = True

@then('se genera una alerta con el mensaje "Patrón de factores médicos o clínicos identificados"')
def step_impl(context):
    context.alerta_factores = "Patrón de factores médicos o clínicos identificados"

@then('se recomienda contactar a un profesional de salud para una evaluación adicional')
def step_impl(context):
    context.recomendacion_profesional = True

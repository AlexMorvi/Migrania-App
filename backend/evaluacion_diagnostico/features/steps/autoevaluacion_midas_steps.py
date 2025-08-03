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
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

@given('que el paciente ha realizado una última evaluación en la "{fecha}"')
def step_impl(context, fecha):
    context.ultima_evaluacion = datetime.strptime(fecha, '%Y-%m-%d').date()

@when('pasen 3 meses desde la última evaluación')
def step_impl(context):
    context.fecha_actual = context.ultima_evaluacion + relativedelta(months=3)

@then('el paciente podrá realizar una nueva evaluación')
def step_impl(context):
    # Verificar que han pasado 3 meses
    diferencia = context.fecha_actual - context.ultima_evaluacion
    assert diferencia.days >= 90  # Aproximadamente 3 meses

@given('que el paciente ha realizado una evaluación hace menos de 3 meses')
def step_impl(context):
    context.ultima_evaluacion = date.today() - relativedelta(months=2)  # Hace 2 meses

@when('el paciente intenta realizar una nueva evaluación')
def step_impl(context):
    context.intento_evaluacion = True

@then('el sistema no permitirá realizar una nueva evaluación')
def step_impl(context):
    # Verificar que no han pasado 3 meses
    diferencia = date.today() - context.ultima_evaluacion
    assert diferencia.days < 90  # Menos de 3 meses

@then('se mostrará un mensaje indicando que debe esperar hasta cumplir los 3 meses')
def step_impl(context):
    context.mensaje_espera = "Debe esperar hasta cumplir los 3 meses desde la última evaluación"
    assert context.mensaje_espera is not None

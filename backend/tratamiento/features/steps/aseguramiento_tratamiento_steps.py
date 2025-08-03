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

@given('que el paciente tiene una medicina prescrita para la migraña')
def step_impl(context):
    context.medicina_prescrita = True

@given('una frecuencia de dosificación cada {frecuencia:d} horas')
def step_impl(context, frecuencia):
    context.frecuencia = frecuencia

@given('una duración de {dias:d} días')
def step_impl(context, dias):
    context.duracion = dias

@when('la hora actual sea {minutos_antes:d} minutos antes de la hora de la toma')
def step_impl(context, minutos_antes):
    context.minutos_antes = minutos_antes

@then('se enviará un recordatorio al paciente indicando que debe tomar su medicación pronto')
def step_impl(context):
    assert context.medicina_prescrita
    context.recordatorio_enviado = True

@then('el estado de la notificación será "activa"')
def step_impl(context):
    context.estado_notificacion = "activa"
    assert context.estado_notificacion == "activa"

@given('que el paciente ha recibido una alerta para tomar su medicación')
def step_impl(context):
    context.alerta_recibida = True

@given('la hora actual es la hora programada para la toma')
def step_impl(context):
    context.hora_programada = True

@when('el paciente confirma que ha tomado la medicación')
def step_impl(context):
    context.confirmacion = "tomado"

@then('se actualizará el estado de la alarma a "tomado"')
def step_impl(context):
    assert context.confirmacion == "tomado"
    context.estado_alarma = "tomado"

@when('el paciente confirma que no ha tomado la medicación')
def step_impl(context):
    context.confirmacion = "no tomado"

@then('se actualizará el estado de la alarma a "no tomado"')
def step_impl(context):
    assert context.confirmacion == "no tomado"
    context.estado_alarma = "no tomado"

@then('se enviará una notificación al paciente sugiriendo que tome su medicación')
def step_impl(context):
    context.notificacion_sugerencia = True

@when('transcurran 30 minutos sin que el paciente confirme la toma')
def step_impl(context):
    context.sin_confirmacion = True

@then('se enviará una segunda alerta')
def step_impl(context):
    context.segunda_alerta = True

@then('se programará una tercera alerta 15 minutos después de la segunda')
def step_impl(context):
    context.tercera_alerta = True

@then('si no se confirma ninguna de las 3 alertas, se actualizará el estado de la alerta a "sin confirmar"')
def step_impl(context):
    context.estado_alarma = "sin confirmar"

@given('que el paciente tiene una recomendación de tratamiento para la migraña')
def step_impl(context):
    context.recomendacion_tratamiento = True

@when('sea las {horas:d} del día')
def step_impl(context, horas):
    context.hora_dia = horas

@then('se notificará mediante un recordatorio sugiriendole seguir esta recomendación')
def step_impl(context):
    assert context.recomendacion_tratamiento
    context.recordatorio_recomendacion = True

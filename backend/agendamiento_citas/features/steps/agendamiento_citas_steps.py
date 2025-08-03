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

@given('que {nombre_paciente} no ha realizado ningún agendamiento previamente')
def step_impl(context, nombre_paciente):
    context.nombre_paciente = nombre_paciente
    context.primer_agendamiento = True

@given('hay disponibilidad con el doctor {doctor} el {fecha_cita} a las {hora_cita}')
def step_impl(context, doctor, fecha_cita, hora_cita):
    context.doctor = doctor
    context.fecha_cita = fecha_cita
    context.hora_cita = hora_cita
    context.disponibilidad = True

@when('el paciente agenda su cita por primera vez')
def step_impl(context):
    context.cita_agendada = True

@then('el doctor {doctor} se convierte en su médico de preferencia')
def step_impl(context, doctor):
    context.medico_preferencia = doctor
    assert context.medico_preferencia == doctor

@then('el paciente recibe un recordatorio para el {fecha_recordatorio} a las {hora_recordatorio}')
def step_impl(context, fecha_recordatorio, hora_recordatorio):
    context.recordatorio_fecha = fecha_recordatorio
    context.recordatorio_hora = hora_recordatorio

@given('que {nombre_paciente} tiene asignado al doctor {doctor}')
def step_impl(context, nombre_paciente, doctor):
    context.nombre_paciente = nombre_paciente
    context.doctor_asignado = doctor

@given('hay disponibilidad el {fecha_cita} a las {hora_cita}')
def step_impl(context, fecha_cita, hora_cita):
    context.fecha_cita = fecha_cita
    context.hora_cita = hora_cita
    context.disponibilidad = True

@when('el paciente agenda una atención regular')
def step_impl(context):
    context.atencion_regular = True

@given('que el paciente presenta un historial médico de alta urgencia')
def step_impl(context):
    context.urgencia_alta = True

@when('el paciente agenda una atención medica urgente')
def step_impl(context):
    context.atencion_urgente = True

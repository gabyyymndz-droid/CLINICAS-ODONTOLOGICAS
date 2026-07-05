from datetime import date
import sys
import os

from Modulos.rol import Rol
from Modulos.personal_administrativo import PersonalAdministrativo 
from Modulos.servicio import Servicio
from Modulos.paciente import Paciente
from Modulos.doctor import Doctor
from Modulos.sucursal import Sucursal
from Modulos.especialidad import Especialidad
from Modulos.venta import Venta
from Modulos.cita import Cita
from Modulos.expediente import Expediente

# Listas que simulan nuestra base de datos
roles = []
personal = []
doctores = []
sucursales = []
especialidades = []
pacientes = []
servicios = []

# --- CREACIÓN DE DATOS ---

nuevos_roles = [
    Rol("R01", "Administrador", "Gestiona la sucursal"),
    Rol("R02", "Recepcionista", "Atención al cliente y agenda de citas"),
    Rol("R03", "Contador", "Gestión financiera y contabilidad interna"),
    Rol("R04", "Asistente Médico", "Apoyo directo a los doctores en consulta"),
    Rol("R05", "Gerente de Operaciones", "Supervisión general de múltiples sucursales"),
    Rol("R06", "Soporte Técnico", "Mantenimiento de sistemas y equipos médicos")
]

nuevas_especialidades = [
    Especialidad("ESP01", "Ortodoncia"),
    Especialidad("ESP02", "Pediatría"),
    Especialidad("ESP03", "Endodoncia"),
    Especialidad("ESP04", "Periodoncia"),
    Especialidad("ESP05", "Cirugía Maxilofacial"),
    Especialidad("ESP06", "Implantología")
]

nuevos_servicios = [
    Servicio("S01", "Consulta General", "JVP-4521"),
    Servicio("S02", "Limpieza Dental", "JVP-1122"),
    Servicio("S03", "Tratamiento de Canales", "JVP-9988"),
    Servicio("S04", "Colocación de Brackets", "JVP-7766"),
    Servicio("S05", "Extracción de Cordales", "JVP-5544"),
    Servicio("S06", "Implante Titanio", "JVP-3322")
]

nuevo_personal = [
    PersonalAdministrativo("P01", "Ana Perez", nuevos_roles[0]),
    PersonalAdministrativo("P02", "Marcus Meléndez", nuevos_roles[1]),
    PersonalAdministrativo("P03", "Gabriela Méndez", nuevos_roles[2]),
    PersonalAdministrativo("P04", "Roberto Gomez", nuevos_roles[3]),
    PersonalAdministrativo("P05", "Lucia Flores", nuevos_roles[4]),
    PersonalAdministrativo("P06", "Ricardo Alvarenga", nuevos_roles[5])
]

nuevos_pacientes = [
    Paciente("PA01", "Carlos Ramirez", "12345678-9", "7777-8888", {'alergias': 'Ninguna', 'enfermedades': 'Ninguna', 'notas': 'Primera vez'}),
    Paciente("PA02", "Fernando Calvo", "98765432-1", "6666-5555", {'alergias': 'Polvo', 'enfermedades': 'Asma', 'notas': 'Requiere inhalador'}),
    Paciente("PA03", "Elena Rivas", "45678912-3", "7111-2222", {'alergias': 'Penicilina', 'enfermedades': 'Hipertensión', 'notas': 'Control cada 6 meses'}),
    Paciente("PA04", "Alejandro Sosa", "32165498-7", "7333-4444", {'alergias': 'Ninguna', 'enfermedades': 'Diabetes Tipo 2', 'notas': 'Paciente recurrente'}),
    Paciente("PA05", "Mariana Torres", "74185296-3", "7555-6666", {'alergias': 'Látex', 'enfermedades': 'Ninguna', 'notas': 'Viene por diseño de sonrisa'}),
    Paciente("PA06", "Luis Argueta", "85296374-1", "7999-0000", {'alergias': 'Ibuprofeno', 'enfermedades': 'Ninguna', 'notas': 'Sensibilidad dental extrema'})
]

nuevos_doctores = [
    Doctor("D01", "Dra. Maria Lopez", "JVP-4521", nuevos_pacientes[0]),
    Doctor("D02", "Dr. Roberto Carlos", "JVP-1122", nuevos_pacientes[1]),
    Doctor("D03", "Dr. Alejandro Andrade", "JVP-9988", nuevos_pacientes[2]),
    Doctor("D04", "Dra. Sofia Quintanilla", "JVP-7766", nuevos_pacientes[3]),
    Doctor("D05", "Dr. Enrique Flores", "JVP-5544", nuevos_pacientes[4]),
    Doctor("D06", "Dra. Claudia Benítez", "JVP-3322", nuevos_pacientes[5])
]

nuevas_sucursales = [
    Sucursal("SUC01", "Clinica Central", "Santa Elena", "7676-6767"),
    Sucursal("SUC02", "Clinica Norte", "Escalón", "2222-3333"),
    Sucursal("SUC03", "Clinica Sur", "Antiguo Cuscatlán", "2525-4444"),
    Sucursal("SUC04", "Clinica Poniente", "Santa Tecla", "2626-5555"),
    Sucursal("SUC05", "Clinica Oriente", "San Miguel", "2727-6666")
]

# --- VALIDACIONES Y REGISTROS ---

print("=== VALIDACIÓN DE DATOS ===")

for r in nuevos_roles:
    print(r.validacion_rol(roles) or f"Rol {r.idRol} validado y registrado")
    roles.append(r)

for e in nuevas_especialidades:
    print(e.validacion_especialidad(especialidades) or f"Especialidad {e.idEspecialidad} validada y registrada")
    especialidades.append(e)

for s in nuevos_servicios:
    servicios.append(s)

for p in nuevo_personal:
    print(p.validacion_personal_admin(personal) or f"Personal {p.idPersonalAdministrativo} validado y registrado")
    personal.append(p)

for pac in nuevos_pacientes:
    print(pac.validacion_paciente(pacientes) or f"Paciente {pac.idPaciente} validado y registrado")
    pacientes.append(pac)

for d in nuevos_doctores:
    print(d.validacion_doctor(doctores) or f"Doctor {d.idDoctor} validado y registrado")
    doctores.append(d)

for suc in nuevas_sucursales:
    print(suc.validacion_sucursal(sucursales) or f"Sucursal {suc.idSucursal} validada y registrada")
    sucursales.append(suc)


# --- ASIGNACIONES, CITAS Y VENTAS ---

nuevas_sucursales[0].agregar_personal_admin(nuevo_personal[0])
nuevas_sucursales[0].agregar_doctor(nuevos_doctores[0])

nuevos_doctores[0].crear_cita_interna("CI01", date(2026, 7, 10), nuevos_servicios[0])

nuevas_sucursales[0].crear_venta("V01", date.today(), 25.00)
nuevas_sucursales[0].crear_cita("C01", date(2026, 7, 10), nuevos_servicios[0])


# --- RESUMEN FINAL DEL SISTEMA ---
print("\n--- RESUMEN DEL SISTEMA: CLÍNICA CENTRAL ---")
print("Personal en sucursal: ", [p.idPersonalAdministrativo for p in nuevas_sucursales[0].personal_admin_agregados])
print("Doctores en sucursal: ", [d.idDoctor for d in nuevas_sucursales[0].doctores_agregados])
print("Total de ventas generadas: ", len(nuevas_sucursales[0].ventas_composición))
print("IDs de Ventas: ", [v.idVentas for v in nuevas_sucursales[0].ventas_composición])


# --- PRUEBA DEFINITIVA DE ABSORCIÓN POR CLASE ---
print("\n=== VERIFICACIÓN DE ABSORCIÓN DE DATOS POR CLASE ===")


print(f"1. ROL -> ID: {nuevos_roles[0].idRol} | Nombre: {nuevos_roles[0].nombreRol}")


print(f"2. ESPECIALIDAD -> ID: {nuevas_especialidades[0].idEspecialidad} | Desc: {nuevas_especialidades[0].especialidadDescripcion}")


print(f"3. SERVICIO -> ID: {nuevos_servicios[0].id_servicio} | Desc: {nuevos_servicios[0].descripcion_servicio}")


print(f"4. PERSONAL ADMIN -> ID: {nuevo_personal[0].idPersonalAdministrativo} | Nombre: {nuevo_personal[0].nombrePersonalAdministrativo} | Rol Asignado: {nuevo_personal[0].rol.nombreRol}")


print(f"5. PACIENTE -> ID: {nuevos_pacientes[0].idPaciente} | Nombre: {nuevos_pacientes[0].nombrePaciente}")


expediente_prueba = nuevos_pacientes[0].expediente
print(f"6. EXPEDIENTE -> ID: {expediente_prueba.idExpediente} | Alergias: {expediente_prueba.alergiasMedicamentos}")


print(f"7. DOCTOR -> ID: {nuevos_doctores[0].idDoctor} | Nombre: {nuevos_doctores[0].NombreDoctor} | Paciente Asignado: {nuevos_doctores[0].paciente_registrado.nombrePaciente}")


cita_prueba = nuevos_doctores[0].citas_doctor[0]
print(f"8. CITA -> ID: {cita_prueba.idCita} | Fecha: {cita_prueba.horarioCita} | Servicio: {cita_prueba.servicio.descripcion_servicio}")


venta_prueba = nuevas_sucursales[0].ventas_composición[0]
print(f"9. VENTA -> ID: {venta_prueba.idVentas} | Monto: ${venta_prueba.montoVenta}")


print(f"10. SUCURSAL -> ID: {nuevas_sucursales[0].idSucursal} | Nombre: {nuevas_sucursales[0].nombreSucursal}")

print("Todo el sistema funciona correctamente")
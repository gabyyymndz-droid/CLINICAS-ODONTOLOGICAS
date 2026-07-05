from Modulos.servicio import Servicio
from Modulos.cita import Cita
from datetime import date

class Expediente:
    def __init__(self, idExpediente: str, fechaApertura: date, alergiasMedicamentos: str, enfermedadesPreexistentes: str, notasMedicas: str, historialCitas: list):
        self.idExpediente = idExpediente
        self.fechaApertura = fechaApertura
        self.alergiasMedicamentos = alergiasMedicamentos
        self.enfermedadesPreexistentes = enfermedadesPreexistentes
        self.notasMedicas = notasMedicas
        self.historialCitas = historialCitas
        self.servicios_registrados: list[Servicio] = []

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Expediente): 
            return NotImplemented
        return self.idExpediente == otro.idExpediente

    def validacion_expediente(self, lista_expedientes: list) -> list:
        errores = []
        if not self.idExpediente or not str(self.idExpediente).strip():
            errores.append("El ID del expediente no puede estar vacio")
        if self in lista_expedientes: 
            errores.append("El expediente ya existe.")
        return errores

    
    def crear_servicio_interno(self, idServicio: str, descripcion: str, jvp: str):

        nuevo_servicio = Servicio(idServicio, descripcion, jvp)
        self.servicios_registrados.append(nuevo_servicio)

        
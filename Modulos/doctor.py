from datetime import date
from Modulos.cita import Cita
from Modulos.paciente import Paciente
from Modulos.servicio import Servicio

class Doctor:
    def __init__(self, idDoctor: str, NombreDoctor: str, jvpODoctor: str, paciente: Paciente):
        self.idDoctor = idDoctor
        self.NombreDoctor = NombreDoctor
        self.jvpODoctor = jvpODoctor
        self.paciente_registrado = paciente 
        
        self.citas_doctor: list[Cita] = []

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Doctor): return NotImplemented
        return self.idDoctor == otro.idDoctor

    def validacion_doctor(self, lista_doctores: list) -> list:
        errores = []

        if not self.idDoctor or not str(self.idDoctor).strip():
            errores.append("El ID del doctor no puede estar vacio")

        if self in lista_doctores: 
            errores.append(f"El doctor {self.idDoctor} ya existe")


        return errores

    def Disponibilidad(self):
        pass
    
    def crear_cita(self, idCita: str, horario: date, servicio: Servicio):
        nueva_cita = Cita(idCita, horario, servicio)
        self.citas_doctor.append(nueva_cita)
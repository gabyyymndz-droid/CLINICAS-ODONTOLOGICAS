from datetime import date
from Modulos.cita import Cita
from Modulos.paciente import Paciente
from Modulos.servicio import Servicio

class Doctor:
    def __init__(self, idDoctor: str, NombreDoctor: str, jvpODoctor: str, paciente: Paciente):
        self.idDoctor = idDoctor
        self.NombreDoctor = NombreDoctor
        self.jvpODoctor = jvpODoctor
        self.paciente_registrado = paciente # Asociación simple
        
        # Composición: El doctor crea y controla las citas (rombo lleno en Doctor)
        self.citas_doctor: list[Cita] = []

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Doctor): return NotImplemented
        return self.idDoctor == otro.idDoctor

    def validacion_doctor(self, lista_doctores: list) -> list:
        errores = []
        if self in lista_doctores: 
            errores.append(f"El doctor {self.idDoctor} ya existe.")
        return errores

    def Disponibilidad(self):
        pass
    
    def crear_cita(self, idCita: str, horario: date, servicio: Servicio):
        # Prueba de Composición: Instanciación interna
        nueva_cita = Cita(idCita, horario, servicio)
        self.citas_doctor.append(nueva_cita)
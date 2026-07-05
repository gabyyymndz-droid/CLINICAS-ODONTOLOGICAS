from datetime import date
from Modulos.expediente import Expediente


class Paciente:
    def __init__(self, idPaciente: str, nombrePaciente: str, duiPaciente: str, telefonoPaciente: str, datos_expediente: dict):
        self.idPaciente = idPaciente
        self.nombrePaciente = nombrePaciente
        self.duiPaciente = duiPaciente
        self.telefonoPaciente = telefonoPaciente

        # Un paciente crea un expediente al nacer
        self.expediente = Expediente( 
            idExpediente = f"EXP_{self.idPaciente}",
            fechaApertura = datos_expediente.get('fechaApertura', date.today()),
            alergiasMedicamentos = datos_expediente.get('alergias', ''),
            enfermedadesPreexistentes = datos_expediente.get('enfermedades', ''),
            notasMedicas = datos_expediente.get('notas', ''),
            historialCitas = []
        )

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Paciente): 
            return NotImplemented
        return self.idPaciente == otro.idPaciente

    def validacion_paciente(self, lista_pacientes: list) -> list:
        errores = []

        if not self.idPaciente or not str(self.idPaciente).strip():
            errores.append("El ID del paciente no puede estar vacio")
        if self in lista_pacientes: 
            errores.append(f"El paciente {self.idPaciente} ya existe.")


        return errores
from datetime import date
from Modulos.servicio import Servicio

class Cita:
    def __init__(self, idCita: str, horarioCita: date, servicio: Servicio):
        self.idCita = idCita
        self.horarioCita = horarioCita
        self.servicio = servicio # Asociación a Servicio

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Cita): 
            return NotImplementedError("Operación no permitida: los tipos de datos no son iguales")
        return self.idCita == otro.idCita

    def validacion_cita(self, lista_citas: list) -> list:
        errores = []

        if not self.idCita or not str(self.idCita).strip():
            errores.append("El ID del Rol no puede estar vacio")
        if self in lista_citas: 
            errores.append(f"La cita {self.idCita} ya existe.")
            
        return errores

    def modificar_cita(self):
        pass

    def eliminar_cita(self):
        pass
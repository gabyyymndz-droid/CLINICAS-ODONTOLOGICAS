from Modulos.personal_administrativo import PersonalAdministrativo
from Modulos.venta import Venta
from Modulos.cita import Cita
from Modulos.doctor import Doctor

class Sucursal:
    def __init__(self, idSucursal: str, nombreSucursal: str, direccionSucursal: str, telefonoSucursal: str):
        self.idSucursal = idSucursal
        self.nombreSucursal = nombreSucursal
        self.direccionSucursal = direccionSucursal
        self.telefonoSucursal = telefonoSucursal

        # AGREGACIONES (Rombo Vacío): Reciben el objeto desde afuera
        self.personal_admin_agregados: list[PersonalAdministrativo] = []
        self.doctores_agregados: list[Doctor] = []

        # COMPOSICIONES (Rombo Lleno): Crean el objeto adentro
        self.ventas_composición: list[Venta] = []
        self.citas_composición: list[Cita] = []

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Sucursal): 
            return NotImplemented
        return self.idSucursal == otro.idSucursal


    def validacion_sucursal(self, lista_sucursales: list) -> list:
        errores = []

        if not self.idSucursal or not str(self.idSucursal).strip():
            errores.append("El ID de la sucursal no puede estar vacio")

        if self in lista_sucursales: 
            errores.append(f"La sucursal {self.idSucursal} ya existe.")
        return errores
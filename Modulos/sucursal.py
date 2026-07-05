from Modulos.personal_administrativo import PersonalAdministrativo
from Modulos.venta import Venta
from Modulos.cita import Cita
from Modulos.doctor import Doctor
from Modulos.servicio import Servicio

from datetime import date


class Sucursal:
    def __init__(self, idSucursal: str, nombreSucursal: str, direccionSucursal: str, telefonoSucursal: str):
        self.idSucursal = idSucursal
        self.nombreSucursal = nombreSucursal
        self.direccionSucursal = direccionSucursal
        self.telefonoSucursal = telefonoSucursal

        self.personal_admin_agregados: list[PersonalAdministrativo] = []
        self.doctores_agregados: list[Doctor] = []

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
            errores.append(f"La sucursal {self.idSucursal} ya existe")
        return errores
    
    def agregar_personal_admin(self, personal: PersonalAdministrativo):
        self.personal_admin_agregados.append(personal)

    def agregar_doctor(self, doctor: Doctor):
        self.doctores_agregados.append(doctor)


    def crear_venta(self, idVentas: str, fechVenta: date, montoVenta: float):
        nueva_venta = Venta(idVentas, fechVenta, montoVenta)
        self.ventas_composición.append(nueva_venta)

    def crear_cita(self, idCita: str, horarioCita: date, servicio: Servicio):
        nueva_cita = Cita(idCita, horarioCita, servicio)
        self.citas_composición.append(nueva_cita)
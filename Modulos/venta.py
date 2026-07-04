from datetime import date

class Venta:
    def __init__(self, idVentas: str, fechVenta: date, montoVenta: float):
        self.idVentas = idVentas
        self.fechVenta = fechVenta
        self.montoVenta = montoVenta

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Venta): 
            return NotImplemented
        return self.idVentas == otro.idVentas

    def validacion_venta(self, lista_ventas: list) -> list:
        errores = []

        if not self.idVentas or not str(self.idVentas).strip():
            errores.append("El ID del personal no puede estar vacio")
        if self in lista_ventas: 
            errores.append(f"La venta {self.idVentas} ya existe")
            
        return errores

    def historial_ventas(self):
        pass
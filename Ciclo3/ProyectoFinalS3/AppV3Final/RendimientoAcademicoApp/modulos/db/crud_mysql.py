import modulos.db.modelos_mysql as modelos

class Pais:
    def __init__(self, id_pais:int=None, pais_mdl:modelos.Pais=None):
        self.id_pais:int = id_pais
        self.pais_mdl:modelos.Pais = pais_mdl


class Provincia:
    def __init__(self, id_provincia:int=None, provincia_mdl:modelos.Provincia=None):
        self.id_provincia:int = id_provincia
        self.provincia_mdl:modelos.Provincia = provincia_mdl


class Ciudad:
    def __init__(self, id_ciudad:int=None, ciudad_mdl:modelos.Ciudad=None):
        self.id_ciudad:int = id_ciudad
        self.ciudad_mdl:modelos.Ciudad = ciudad_mdl


class Barrio:
    def __init__(self, id_barrio:int=None, barrio_mdl:modelos.Barrio=None):
        self.id_barrio:int = id_barrio
        self.barrio_mdl:modelos.Barrio = barrio_mdl


class Estudiante:
    def __init__(self, id_estudiante:int=None, estudiante_mdl:modelos.Estudiante=None):
        self.id_estudiante:int = id_estudiante
        self.estudiante_mdl:modelos.Estudiante = estudiante_mdl


class DireccionEmail:
    def __init__(self, id_email:int=None, email_mdl:modelos.DireccionEmail=None):
        self.id_email:int = id_email
        self.email_mdl:modelos.DireccionEmail = email_mdl



class Vivienda:
    def __init__(self, id_vivienda:int=None, vivienda_mdl:modelos.Vivienda=None):
        self.id_vivienda:int = id_vivienda
        self.vivienda_mdl:modelos.Vivienda = vivienda_mdl


class ServicioBasico:
    def __init__(self, id_servicio_basico:int=None, servicio_mdl:modelos.ServicioBasico=None):
        self.id_servicio_basico:int = id_servicio_basico
        self.servicio_mdl:modelos.ServicioBasico = servicio_mdl


class OtraTitulacion:
    def __init__(self, id_otra_titulacion:int=None, titulacion_mdl:modelos.OtraTitulacion=None):
        self.id_otra_titulacion:int = id_otra_titulacion
        self.titulacion_mdl:modelos.OtraTitulacion = titulacion_mdl


class Carrera:
    def __init__(self, id_carrera:int=None, carrera_mdl:modelos.Carrera=None):
        self.id_carrera:int = id_carrera
        self.carrera_mdl:modelos.Carrera = carrera_mdl


class CarreraEstudiante:
    def __init__(self, id_periodo:int=None, periodo_mdl:modelos.CarreraEstudiante=None):
        self.id_periodo:int = id_periodo
        self.periodo_mdl:modelos.CarreraEstudiante = periodo_mdl


class EstructuraFamiliar:
    def __init__(self, id_familiar:int=None, estructura_mdl:modelos.EstructuraFamiliar=None):
        self.id_familiar:int = id_familiar
        self.estructura_mdl:modelos.EstructuraFamiliar = estructura_mdl


class AyudaEconomica:
    def __init__(self, id_ayuda:int=None, ayuda_mdl:modelos.AyudaEconomica=None):
        self.id_ayuda:int = id_ayuda
        self.ayuda_mdl:modelos.AyudaEconomica = ayuda_mdl

class OcupacionEstudiante:
    def __init__(self, id_ocupacion:int=None, ocupacion_mdl:modelos.OcupacionEstudiante=None):
        self.id_ocupacion:int = id_ocupacion
        self.ocupacion_mdl:modelos.OcupacionEstudiante = ocupacion_mdl


class PropiedadExtra:
    def __init__(self, id_propiedad:int=None, propiedad_mdl:modelos.PropiedadExtra=None):
        self.id_propiedad:int = id_propiedad
        self.propiedad_mdl:modelos.PropiedadExtra = propiedad_mdl


class ContactoEmergencia:
    def __init__(self, id_emergencia:int=None, contacto_mdl:modelos.ContactoEmergencia=None):
        self.id_emergencia:int = id_emergencia
        self.contacto_mdl:modelos.ContactoEmergencia = contacto_mdl


class Beca:
    def __init__(self, id_beca:int=None, beca_mdl:modelos.Beca=None):
        self.id_beca:int = id_beca
        self.beca_mdl:modelos.Beca = beca_mdl


class Colegio:
    def __init__(self, id_colegio:int=None, colegio_mdl:modelos.Colegio=None):
        self.id_colegio:int = id_colegio
        self.colegio_mdl :modelos.Colegio= colegio_mdl


class TitulacionColegio:
    def __init__(self, id_titulacion:int=None, titulacion_mdl:modelos.TitulacionColegio=None):
        self.id_titulacion:int = id_titulacion
        self.titulacion_mdl:modelos.TitulacionColegio = titulacion_mdl


class Finanzas:
    def __init__(self, id_finanza:int=None, finanza_mdl:modelos.Finanzas=None):
        self.id_finanza:int = id_finanza
        self.finanza_mdl:modelos.Finanzas = finanza_mdl

class DatosSalud:
    def __init__(self, id_salud:int=None, salud_mdl:modelos.DatosSalud=None):
        self.id_salud:int = id_salud
        self.salud_mdl:modelos.DatosSalud = salud_mdl


class ServicioVivienda:
    def __init__(self, id_servicio_vivienda:int=None, srv_vivienda_mdl:modelos.ServicioVivienda=None):
        self.id_servicio_vivienda:int= id_servicio_vivienda
        self.srv_vivienda_mdl:modelos.ServicioVivienda = srv_vivienda_mdl
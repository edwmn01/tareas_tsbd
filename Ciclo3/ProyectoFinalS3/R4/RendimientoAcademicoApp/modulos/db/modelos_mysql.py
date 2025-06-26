class Pais:
    def __init__(self, nombre_pais=None):
        self.nombre_pais = nombre_pais


class Provincia:
    def __init__(self, nombre_provincia=None, id_pais:int=None):
        self.nombre_provincia = nombre_provincia
        self.id_pais:int = id_pais


class Ciudad:
    def __init__(self, nombre_ciudad=None, id_provincia:int=None):
        self.nombre_ciudad = nombre_ciudad
        self.id_provincia:int = id_provincia


class Barrio:
    def __init__(self, sector=None, tipo_parroquia=None, id_ciudad:int=None):
        self.sector = sector
        self.tipo_parroquia = tipo_parroquia
        self.id_ciudad:int = id_ciudad


class Estudiante:
    def __init__(self, cedula_pasaporte=None, nombres=None, apellidos=None, sexo=None, direccion=None, genero=None,
                 estado_civil=None, lugar_nacimiento=None, fecha_nacimiento=None, nro_hijos:int=None, etnia=None,
                 idioma_nativo=None, celular=None, telefono=None, id_barrio:int=None):
        self.cedula_pasaporte = cedula_pasaporte
        self.nombres = nombres
        self.apellidos = apellidos
        self.sexo = sexo
        self.direccion = direccion
        self.genero = genero
        self.estado_civil = estado_civil
        self.lugar_nacimiento = lugar_nacimiento
        self.fecha_nacimiento = fecha_nacimiento
        self.nro_hijos:int = nro_hijos
        self.etnia = etnia
        self.idioma_nativo = idioma_nativo
        self.celular = celular
        self.telefono = telefono
        self.id_barrio:int = id_barrio


class DireccionEmail:
    def __init__(self, email=None, id_estudiante:int=None):
        self.email = email
        self.id_estudiante:int = id_estudiante


class Vivienda:
    def __init__(self, condicion_vivienda=None, tipo_vivienda=None, estructura_vivienda=None, id_estudiante:int=None):
        self.condicion_vivienda = condicion_vivienda
        self.tipo_vivienda = tipo_vivienda
        self.estructura_vivienda = estructura_vivienda
        self.id_estudiante:int = id_estudiante


class ServicioBasico:
    def __init__(self, nombre_servicio=None):
        self.nombre_servicio = nombre_servicio


class OtraTitulacion:
    def __init__(self, nombre_carrera=None, registro_titulo=None, id_estudiante:int=None):
        self.nombre_carrera = nombre_carrera
        self.registro_titulo = registro_titulo
        self.id_estudiante:int = id_estudiante


class Carrera:
    def __init__(self, nombre_carrera=None):
        self.nombre_carrera = nombre_carrera


class CarreraEstudiante:
    def __init__(self, periodo=None, ciclo=None, razon_estudio=None, razones_eleccion_carrera=None,
                 id_carrera:int=None, id_estudiante:int=None):
        self.periodo = periodo
        self.ciclo = ciclo
        self.razon_estudio = razon_estudio
        self.razones_eleccion_carrera = razones_eleccion_carrera
        self.id_carrera:int = id_carrera
        self.id_estudiante:int = id_estudiante


class EstructuraFamiliar:
    def __init__(self, familiares_conviven=None, familiares_aportan_economicamente=None, cabezas_familia=None,
                 familiares_cubren_estudio=None, id_estudiante:int=None):
        self.familiares_conviven = familiares_conviven
        self.familiares_aportan_economicamente = familiares_aportan_economicamente
        self.cabezas_familia = cabezas_familia
        self.familiares_cubren_estudio = familiares_cubren_estudio
        self.id_estudiante:int = id_estudiante


class AyudaEconomica:
    def __init__(self, tipo_ayuda=None, id_estudiante:int=None):
        self.tipo_ayuda = tipo_ayuda
        self.id_estudiante:int = id_estudiante


class OcupacionEstudiante:
    def __init__(self, tipo_ocupacion=None, id_estudiante:int=None):
        self.tipo_ocupacion = tipo_ocupacion
        self.id_estudiante:int = id_estudiante


class PropiedadExtra:
    def __init__(self, nro_propiedades:int=None, valor_propiedades:float=None, nro_vehiculo:int=None,
                 valor_vehiculos:float=None, id_estudiante:int=None):
        self.nro_propiedades:int = nro_propiedades
        self.valor_propiedades:float = valor_propiedades
        self.nro_vehiculo:int = nro_vehiculo
        self.valor_vehiculos:float = valor_vehiculos
        self.id_estudiante:int = id_estudiante


class ContactoEmergencia:
    def __init__(self, nombre_contacto=None, telefono_contacto=None, id_estudiante:int=None):
        self.nombre_contacto = nombre_contacto
        self.telefono_contacto = telefono_contacto
        self.id_estudiante:int = id_estudiante


class Beca:
    def __init__(self, tipo_beca=None, id_estudiante:int=None):
        self.tipo_beca = tipo_beca
        self.id_estudiante:int = id_estudiante


class Colegio:
    def __init__(self, nombre_colegio=None, tipo_colegio=None):
        self.nombre_colegio = nombre_colegio
        self.tipo_colegio = tipo_colegio


class TitulacionColegio:
    def __init__(self, anio_titulacion:int=None, tipo_titulacion=None, id_estudiante:int=None, id_colegio:int=None):
        self.anio_titulacion:int = anio_titulacion
        self.tipo_titulacion = tipo_titulacion
        self.id_estudiante:int = id_estudiante
        self.id_colegio:int = id_colegio


class Finanzas:
    def __init__(self, ingreso_mensual_estudiante:float=None, ingreso_mensual_conyuge:float=None, ingreso_mensual_padre:float=None,
                 ingreso_mensual_madre:float=None, ingreso_mensual_otros_familiares:float=None, otros_ingreso:float=None,
                 gasto_mensual_vivienda:float=None, gasto_mensual_alimentacion:float=None, gasto_mensual_educacion:float=None,
                 gasto_mensual_transporte:float=None, gasto_mensual_salud:float=None, gasto_mensual_servicios_basicos:float=None,
                 gasto_mensual_vestuarios:float=None, gasto_mensual_otros:float=None, id_estudiante:int=None):
        self.ingreso_mensual_estudiante:float = ingreso_mensual_estudiante
        self.ingreso_mensual_conyuge:float = ingreso_mensual_conyuge
        self.ingreso_mensual_padre:float = ingreso_mensual_padre
        self.ingreso_mensual_madre:float = ingreso_mensual_madre
        self.ingreso_mensual_otros_familiares:float = ingreso_mensual_otros_familiares
        self.otros_ingreso:float = otros_ingreso
        self.gasto_mensual_vivienda:float = gasto_mensual_vivienda
        self.gasto_mensual_alimentacion:float = gasto_mensual_alimentacion
        self.gasto_mensual_educacion:float = gasto_mensual_educacion
        self.gasto_mensual_transporte:float = gasto_mensual_transporte
        self.gasto_mensual_salud:float = gasto_mensual_salud
        self.gasto_mensual_servicios_basicos:float = gasto_mensual_servicios_basicos
        self.gasto_mensual_vestuarios:float = gasto_mensual_vestuarios
        self.gasto_mensual_otros:float = gasto_mensual_otros
        self.id_estudiante:int = id_estudiante


class DatosSalud:
    def __init__(self, tipo_sangre=None, discapacidad=None, tipo_discapacidad=None, porcentaje_discapacidad:float=None,
                 carnet_conadis=None, enfermedad_cronica=None, enfermedad_catastrofica=None, vacuna_covid=None,
                 ultima_vacuna_covid=None, tiempo_embarazo_semanas:int=None, discapacidad_multiple=None,
                 otras_enfermedades=None, antecedentes_patologicos_familiares=None,
                 parentesco_problema_salud=None, id_estudiante:int=None):
        self.tipo_sangre = tipo_sangre
        self.discapacidad = discapacidad
        self.tipo_discapacidad = tipo_discapacidad
        self.porcentaje_discapacidad:float = porcentaje_discapacidad
        self.carnet_conadis = carnet_conadis
        self.enfermedad_cronica = enfermedad_cronica
        self.enfermedad_catastrofica = enfermedad_catastrofica
        self.vacuna_covid = vacuna_covid
        self.ultima_vacuna_covid = ultima_vacuna_covid
        self.tiempo_embarazo_semanas:int = tiempo_embarazo_semanas
        self.discapacidad_multiple = discapacidad_multiple
        self.otras_enfermedades = otras_enfermedades
        self.antecedentes_patologicos_familiares = antecedentes_patologicos_familiares
        self.parentesco_problema_salud = parentesco_problema_salud
        self.id_estudiante:int = id_estudiante


class ServicioVivienda:
    def __init__(self, id_servicio_basico:int=None, id_vivienda:int=None):
        self.id_servicio_basico:int = id_servicio_basico
        self.id_vivienda:int = id_vivienda
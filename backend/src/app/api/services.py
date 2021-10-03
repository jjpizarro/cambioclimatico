from sqlalchemy.orm import Session
from .schemas import MedicionView, Medicion, MedicionQf, Filtro, DatoEstacionesGeoJsonView, DatoDescargaGeoJsonView
from . import models, schemas
from geojson import Feature,Point, FeatureCollection


def conveter_medicion(medicion):
    return MedicionView(id = medicion.id, estacion = medicion.estacion.nombre,
        parametro= medicion.parametro.nombre,
        fecha=medicion.fecha,
        valor=medicion.valor,
        unidad= medicion.parametro.unidad,
        qf = medicion.qf
    )

def conveter_medicionGeoJson(medicion):
    m = MedicionView(estacion = medicion.nombre_estacion,
        parametro= medicion.variable,
        fecha=medicion.fecha,
        valor=medicion.value,
        unidad= medicion.unidad,
        qf = medicion.qf
    )
    
    coords =(medicion.latitud,medicion.longitud)
    p = Point(coords)
    return Feature(geometry=p, properties=m) 

def converter_datosEstacionesGJson(medicion):
    m = DatoEstacionesGeoJsonView( estacion = medicion.estacion, nombre_estacion=medicion.nombre_estacion,
            variable= medicion.variable,
            fecha=medicion.fecha,
            valor=medicion.value,
            unidad= medicion.unidad,
            qf = medicion.qf
        )
    coords =(medicion.latitud,medicion.longitud)
    p = Point(coords)
    return Feature(geometry=p, properties=m) 

def converter_datosdescargaGJson(medicion):
    props = DatoDescargaGeoJsonView(
        estacion=medicion.estacion,
        nombre_estacion=medicion.nombre_estacion,
        fecha=medicion.fecha,
        co2=medicion.co2,
        ch4=medicion.ch4,
        humedad=medicion.humedad,
        temperatura=medicion.temperatura
    )
    coords =(medicion.latitud,medicion.longitud)
    p = Point(coords)
    return Feature(geometry=p, properties=props) 

def get_mediciones(db:Session, skip: int = 0, limit: int=20):
    ms = db.query(models.Medicion).offset(skip).limit(limit).all()
    mediciones = [conveter_medicion(medicion) for medicion in ms]

    return mediciones

def get_medicionesGJson(db:Session,skip: int = 0, limit: int=20):
    ms = db.query(models.Medicion).offset(skip).limit(limit).all()
    mediciones = [conveter_medicionGeoJson(medicion) for medicion in ms]
    return FeatureCollection(mediciones)

def get_datos_estacionesGJson(db:Session):
    data = db.query(models.DatoEstacionesView).offset(0).limit(100).all()
    mediciones  = [converter_datosEstacionesGJson(medicion) for medicion in data]
    return FeatureCollection(mediciones)

def get_datos_descargaGJson(db:Session):
    data = db.query(models.DatoDescargas).offset(0).limit(100).all()
    mediciones  = [converter_datosdescargaGJson(medicion) for medicion in data]
    return FeatureCollection(mediciones)

def get_medicion(db: Session, medicion_id: int):
    return db.query(models.Medicion).filter(models.Medicion.id == medicion_id).first()

def update_qf_medicion(db:Session, medicion: MedicionQf):
    md = db.query(models.Medicion).filter(models.Medicion.id == medicion.id).first()
    md.qf = medicion.qf
    db.commit()
    db.refresh(md)
    return conveter_medicion(md)

def get_estaciones(db:Session):
    return db.query(models.Estacion).all()

def get_parametros(db:Session):
    return db.query(models.Parametro).all()

def filtrar_busqueda(db:Session, filtro:Filtro):
    listaMd = db.query(models.Medicion).filter(models.Medicion.estacion_id == filtro.estacion, models.Medicion.parametro_id == filtro.parametro
    ,
    models.Medicion.fecha > filtro.startdate, models.Medicion.fecha < filtro.enddate
    ).all()
    mediciones = [conveter_medicion(medicion) for medicion in  listaMd]
    return mediciones
import enum
from sqlalchemy.orm import relationship
from sqlalchemy import (Table,
    Column,
    DateTime,
    Integer,
    Float , Enum,
    String,
    Boolean,
    ForeignKey,
)
from sqlalchemy.sql import func
from app.db import Base
from sqlalchemy import Boolean

from sqlalchemy.ext import compiler
from sqlalchemy.schema import DDLElement

from sqlalchemy import event, DDL
from sqlalchemy import MetaData
import uuid

class EstadoEstacion(str, enum.Enum):
    activa = "Activa"
    inactiva = "Inactiva"

class QualityFlag(str, enum.Enum):
    bueno = "bueno"
    no_verificado = "no_verificado"
    sospechoso = "sospechoso"
    malo = "malo"
    dato_faltante = "dato_faltante"



class Estacion(Base):
    __tablename__ = "estaciones"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    latitud = Column(Float)
    longitud = Column(Float)
    fecha_creacion = Column(DateTime, default=func.now(), nullable=False)
    estado = Column(Enum(EstadoEstacion))
    mediciones = relationship("Medicion", back_populates="estacion") 

class Medicion(Base):
    __tablename__ = "mediciones"
    id = Column(Integer, primary_key= True, index=True)
    fecha = Column(DateTime, nullable=False)
    valor = Column(Float)
    qf = Column(Enum(QualityFlag))
    estacion_id = Column(Integer,ForeignKey('estaciones.id'))
    parametro_id = Column(Integer,ForeignKey('parametros.id'))
    estacion = relationship("Estacion", back_populates="mediciones")
    parametro = relationship("Parametro", back_populates="mediciones")

class Parametro (Base):
    __tablename__ = "parametros"
    id = Column(Integer, primary_key= True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    min_valor = Column(Float)
    max_valor = Column(Float)
    unidad = Column(String)
    mediciones = relationship("Medicion", back_populates="parametro",uselist=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)


view_public = """CREATE OR REPLACE VIEW datos_estaciones(
                    id, 
                    estacion,
                    latitud,
                    longitud,
                    fecha,
                    variable,
                    unidad,
                    value,
                    qf,
                    nombre_estacion)
                AS
                SELECT l.id, e.id AS estacion,
                        e.latitud AS lat,
                        e.longitud AS lon,
                        l.fecha,
                        pa.nombre AS variable,
                        pa.unidad,
                        l.valor AS value,
                        l.qf,
                        e.nombre AS nombre_estacion
                FROM estaciones e
                    JOIN mediciones l ON l.estacion_id = e.id
                    JOIN parametros pa ON l.parametro_id = pa.id"""
view_private = """CREATE OR REPLACE VIEW datos_descarga(
                    
                    estacion,
                    nombre_estacion,
                    latitud,
                    longitud,
                    fecha,
                    co2,
                    ch4,
                    humedad,
                    temperatura)
                AS  
                SELECT p.estacion,
                        p.nombre_estacion,
                        p.latitud,
                        p.longitud,
                        p.fecha,
                        max(CASE
                            WHEN p.variable::text = 'co2'::text THEN p.value
                            ELSE NULL::double precision
                            END) AS co2,
                        max(CASE
                            WHEN p.variable::text = 'ch4'::text THEN p.value
                            ELSE NULL::double precision
                            END) AS ch4,
                        max(CASE
                            WHEN p.variable::text = 'Humedad'::text THEN p.value
                            ELSE NULL::double precision
                            END) AS humedad,
                        max(CASE
                            WHEN p.variable::text = 'Temperatura'::text THEN p.value
                            ELSE NULL::double precision
                            END) AS temperatura
                FROM datos_estaciones p
                WHERE p.qf = 'bueno'::qualityflag OR
                        p.qf = 'no_verificado'::qualityflag
                GROUP BY p.estacion,
                        p.nombre_estacion,
                        p.latitud,
                        p.longitud,
                        p.fecha"""


                    
def _createDatoEstacionesView(name,metadata,baseMetadata):
    t = Table(name, metadata,
                Column('id',primary_key=True),
                Column('estacion',Integer),
                Column('latitud',Float),
                Column('longitud',Float),
                Column('fecha',DateTime),
                Column('variable',String),
                Column('unidad',String),
                Column('value',Float),
                Column('qf',String),
                Column('nombre_estacion',String)) 
    event.listen(
                baseMetadata,
                'after_create',
                DDL(view_public).execute_if(dialect=('postgresql','mysql'))
    )

    return t
        
class DatoEstacionesView(Base):
    __table__ = _createDatoEstacionesView("datos_estaciones",MetaData(), Base.metadata)


def _createDatosDescargaView(name,metadata,baseMetadata):
    t = Table(name, metadata,
                Column('estacion',Integer),
                Column('nombre_estacion',String),
                Column('latitud',Float,primary_key=True),
                Column('longitud',Float,primary_key=True),
                Column('fecha',DateTime,primary_key=True),
                Column('co2',Float,primary_key=True),
                Column('ch4',Float,primary_key=True),
                Column('humedad',Float,primary_key=True),
                Column('temperatura',Float,primary_key=True)
                )

      
    event.listen(
                baseMetadata,
                'after_create',
                DDL(view_private).execute_if(dialect=('postgresql','mysql'))
    )

    return t
class DatoDescargas(Base):
    __table__ = _createDatosDescargaView("datos_descarga",MetaData(), Base.metadata)

from typing import List, Optional
from .models import QualityFlag
from pydantic import BaseModel
from datetime import datetime



class MedicionBase(BaseModel):
    id: int
    valor:float

class Medicion(MedicionBase):
    fecha: datetime
    qf: str
    class Config:
        orm_mode = True

class MedicionQf(BaseModel):
    id:int
    qf: QualityFlag


class MedicionView(BaseModel):
    id:int
    estacion:str
    parametro:str
    fecha: datetime
    valor:float
    unidad: str
    qf: str

class Estacion(BaseModel):
    id:int
    nombre: str
    class Config:
        orm_mode = True
        
class Parametro(BaseModel):
    id:int
    nombre:str
    class Config:
        orm_mode = True

class Filtro(BaseModel):
    estacion: int
    parametro:int
    startdate: datetime
    enddate: datetime
    
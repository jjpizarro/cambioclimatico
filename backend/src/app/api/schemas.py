from typing import List, Optional

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
    qf:str


class MedicionView(BaseModel):
    id:int
    estacion:str
    parametro:str
    fecha: datetime
    valor:float
    unidad: str
    qf: str


    
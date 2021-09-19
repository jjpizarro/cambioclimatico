from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from typing import List
from sqlalchemy.orm import Session
from app.api import services, schemas
from app.api.models import Medicion
from app.db import get_db

router = APIRouter()


@router.get("/mediciones/", response_model=List[schemas.MedicionView])
def get_mediciones(skip: int = 0, limit: int = 10000, db: Session = Depends(get_db)):
    monitores = services.get_mediciones(db, skip=skip, limit=limit)
    return monitores

@router.get("/mediciones/{id}", response_model=schemas.Medicion)
def get_mediciones(id: int,  db: Session = Depends(get_db)):
    medicion = services.get_medicion(medicion_id=id,db=db)
    return medicion

@router.put('/mediciones/')
def update_medicion(medicion:schemas.MedicionQf, db:Session = Depends(get_db)):
    return services.update_qf_medicion(db,medicion)

@router.get("/estaciones/", response_model=List[schemas.Estacion])
def get_estaciones(db: Session = Depends(get_db)):
    estaciones = services.get_estaciones(db)
    return estaciones

@router.get('/parametros/',response_model=List[schemas.Parametro])
def get_parametros(db: Session = Depends(get_db)):
    parametros = services.get_parametros(db)
    return parametros
 
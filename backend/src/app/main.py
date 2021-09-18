from fastapi import FastAPI

#from app.database import engine, database, metadata 
#metadata.create_all(engine)
from app.db import engine
from app.api import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
'''
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
'''


#app.include_router(ping.router)
#app.include_router(notes.router, prefix="/notes", tags=["notes"])
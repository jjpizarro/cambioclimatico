from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import engine
from app.api import models
from app.api.mediciones import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.router.prefix = "/api/v1"

app.include_router(router)

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
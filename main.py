from fastapi import FastAPI
from database import engine, Base
from routes import router

# Crée les tables dans la BD automatiquement
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog API",
    description="API REST pour gérer les articles d'un blog",
    version="1.0.0 par Cedrik Darel Yepmo"
)

app.include_router(router, prefix="/api")
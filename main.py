from fastapi import FastAPI
from controllers.universities_controller import router as universities_router

app = FastAPI(
    title="API de Universidades",
    description="Consumo de una API pública de universidades",
    version="1.0.0"
)

app.include_router(universities_router)


@app.get("/")
def root():
    return {
        "message": "API de Universidades funcionando correctamente "
    }

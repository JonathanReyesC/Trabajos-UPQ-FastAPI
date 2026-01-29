from fastapi import FastAPI
from app.routers import estudiantes
from app.routers import calculadora  # <--- NUEVO: Importar calculadora

app = FastAPI(
    title="Sistema Académico API",
    description="API para gestión de estudiantes y utilidades",
    version="1.0.0"
)

# Incluir router de estudiantes
app.include_router(estudiantes.router)

# Incluir router de calculadora
app.include_router(calculadora.router) # <--- NUEVO: Registrar calculadora

@app.get("/")
def read_root():
    return {
        "mensaje": "Bienvenido al Sistema Académico",
        "version": "1.0.0",
        "docs": "/docs"
    }
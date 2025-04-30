from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar carpeta 'static'
app.mount("/static", StaticFiles(directory="static"), name="static")

# Modelos
class Persona(BaseModel):
    nombre: str

# Endpoints API
@app.get("/saludar/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}!"}

@app.post("/saludar")
def saludar_post(persona: Persona):
    return {"mensaje": f"¡Hola, {persona.nombre}!"}

# Servir index.html en la raíz
@app.get("/", response_class=HTMLResponse)
def serve_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    return contenido

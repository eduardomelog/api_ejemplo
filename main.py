from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# Habilitar CORS (por si usas HTML desde otro origen)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar carpeta 'static'
app.mount("/static", StaticFiles(directory="static"), name="static")

# Modelo para el POST
class Persona(BaseModel):
    nombre: str

@app.get("/saludar/{nombre}")
def saludar_get(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}!"}

@app.post("/saludar")
def saludar_post(persona: Persona):
    return {"mensaje": f"¡Hola, {persona.nombre}!"}

# Servir index.html en "/"
@app.get("/", response_class=HTMLResponse)
def serve_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

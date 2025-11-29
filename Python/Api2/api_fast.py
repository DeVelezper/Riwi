from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests
from datetime import datetime, timezone

API_KEY = "dc0787662401ca3a715b01f866ee8e32"

app = FastAPI(title="API Clima FastAPI", description="Consulta el clima de cualquier ciudad", version="1.0")

class Viento(BaseModel):
    velocidad: float
    direccion: int | str
    rafaga: float | str

class Coordenadas(BaseModel):
    lat: float
    lon: float

class ClimaResponse(BaseModel):
    ciudad: str
    pais: str
    temperatura: float
    sensacion_termica: float
    temp_min: float
    temp_max: float
    presion: int
    humedad: int
    viento: Viento
    descripcion: str
    nubosidad: int
    visibilidad: int | str
    lluvia_1h: float
    amanecer: str
    atardecer: str
    coordenadas: Coordenadas

# 🌟 Ruta raíz amigable
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <h2>Bienvenido a la API de Clima</h2>
    <p>Para consultar el clima de cualquier ciudad, ve a la ruta: <a href="/docs">Swagger UI</a></p>
    <p>O usa directamente la ruta /weather con query string: ?ciudad=NombreCiudad</p>
    """

# 🌤 Ruta principal para consultar clima
@app.get("/weather", response_model=ClimaResponse)
def get_weather(ciudad: str = Query(..., description="Nombre de la ciudad a consultar")):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    data = res.json()
    
    if "main" not in data:
        raise HTTPException(status_code=404, detail=f"No se encontraron datos para la ciudad '{ciudad}'")
    
    result = {
        "ciudad": data["name"],
        "pais": data["sys"]["country"],
        "temperatura": data["main"]["temp"],
        "sensacion_termica": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "presion": data["main"]["pressure"],
        "humedad": data["main"]["humidity"],
        "viento": {
            "velocidad": data["wind"]["speed"],
            "direccion": data["wind"].get("deg", "No disponible"),
            "rafaga": data["wind"].get("gust", "No disponible")
        },
        "descripcion": data["weather"][0]["description"],
        "nubosidad": data["clouds"]["all"],
        "visibilidad": data.get("visibility", "No disponible"),
        "lluvia_1h": data.get("rain", {}).get("1h", 0),
        "amanecer": datetime.fromtimestamp(data["sys"]["sunrise"], tz=timezone.utc).strftime('%H:%M:%S'),
        "atardecer": datetime.fromtimestamp(data["sys"]["sunset"], tz=timezone.utc).strftime('%H:%M:%S'),
        "coordenadas": {
            "lat": data["coord"]["lat"],
            "lon": data["coord"]["lon"]
        }
    }
    return result

from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files from frontend/static
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")

# Templates directory (frontend root contains index.html)
templates = Jinja2Templates(directory="../frontend")

# Conversion functions

def convert_length(value: float, unit_from: str, unit_to: str) -> float:
    # Base unit: meter
    to_meters = {
        "meter": 1,
        "kilometer": 1000,
        "cm": 0.01,
        "inches": 0.0254,
        "feet": 0.3048
    }
    if unit_from not in to_meters or unit_to not in to_meters:
        return value
    meters = value * to_meters[unit_from]
    return meters / to_meters[unit_to]

def convert_weight(value: float, unit_from: str, unit_to: str) -> float:
    # Base unit: kg
    to_kg = {
        "kg": 1,
        "pounds": 0.453592,
        "g": 0.001,
        "ounces": 0.0283495
    }
    if unit_from not in to_kg or unit_to not in to_kg:
        return value
    kg = value * to_kg[unit_from]
    return kg / to_kg[unit_to]

def convert_temperature(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == unit_to:
        return value

    # Convert input to Celsius first
    if unit_from == "Celsius":
        celsius = value
    elif unit_from == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif unit_from == "Kelvin":
        celsius = value - 273.15
    else:
        return value

    # Convert from Celsius to target
    if unit_to == "Celsius":
        return celsius
    elif unit_to == "Fahrenheit":
        return (celsius * 9 / 5) + 32
    elif unit_to == "Kelvin":
        return celsius + 273.15
    else:
        return value

def convert_storage(value: float, unit_from: str, unit_to: str) -> float:
    # Base unit: bytes
    to_bytes = {
        "bytes": 1,
        "KB": 1024,
        "MB": 1024 ** 2,
        "GB": 1024 ** 3,
        "TB": 1024 ** 4
    }
    if unit_from not in to_bytes or unit_to not in to_bytes:
        return value
    bytes_value = value * to_bytes[unit_from]
    return bytes_value / to_bytes[unit_to]

def convert_speed(value: float, unit_from: str, unit_to: str) -> float:
    # Base unit: m/s
    to_mps = {
        "m/s": 1,
        "km/h": 1 / 3.6,
        "mph": 0.44704,
        "ft/s": 0.3048
    }
    if unit_from not in to_mps or unit_to not in to_mps:
        return value
    mps_value = value * to_mps[unit_from]
    return mps_value / to_mps[unit_to]

def convert_volume(value: float, unit_from: str, unit_to: str) -> float:
    # Base unit: liters
    to_liters = {
        "L": 1,
        "mL": 0.001,
        "gal": 3.78541,
        "in³": 0.0163871
    }
    if unit_from not in to_liters or unit_to not in to_liters:
        return value
    liters_value = value * to_liters[unit_from]
    return liters_value / to_liters[unit_to]

def convert_area(value: float, unit_from: str, unit_to: str) -> float:
    # Base unit: square meters (m²)
    to_m2 = {
        "m²": 1,
        "km²": 1_000_000,
        "ft²": 0.092903,
        "in²": 0.00064516,  # inch squared to m²
        "cm²": 0.0001
    }
    if unit_from not in to_m2 or unit_to not in to_m2:
        return value
    m2_value = value * to_m2[unit_from]
    return m2_value / to_m2[unit_to]

def convert_time(value: float, unit_from: str, unit_to: str) -> float:
    to_seconds = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2629800,   # average month (30.44 days)
        "year": 31557600    # average year (365.25 days)
    }
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()
    if unit_from not in to_seconds or unit_to not in to_seconds:
        return value
    seconds = value * to_seconds[unit_from]
    return seconds / to_seconds[unit_to]

# Root endpoint serves index.html template
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API endpoint for conversion
@app.get("/convert")
async def convert(
    value: float = Query(...),
    unit_from: str = Query(...),
    unit_to: str = Query(...),
    category: str = Query(...)
):
    result = value  # default fallback

    if category == "length":
        result = convert_length(value, unit_from, unit_to)
    elif category == "weight":
        result = convert_weight(value, unit_from, unit_to)
    elif category == "temperature":
        result = convert_temperature(value, unit_from, unit_to)
    elif category == "storage":
        result = convert_storage(value, unit_from, unit_to)
    elif category == "speed":
        result = convert_speed(value, unit_from, unit_to)
    elif category == "volume":
        result = convert_volume(value, unit_from, unit_to)
    elif category == "area":
        result = convert_area(value, unit_from, unit_to)
    elif category == "time":
        result = convert_time(value, unit_from, unit_to)

    return JSONResponse({"converted_value": result})
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "frontend"))

# Length conversions
def convert_length(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "inches" and unit_to == "cm":
        return value * 2.54
    elif unit_from == "cm" and unit_to == "inches":
        return value / 2.54
    elif unit_from == "feet" and unit_to == "cm":
        return value * 30.48
    elif unit_from == "cm" and unit_to == "feet":
        return value / 30.48
    elif unit_from == "meter" and unit_to == "cm":
        return value * 100
    elif unit_from == "cm" and unit_to == "meter":
        return value / 100
    elif unit_from == "kilometer" and unit_to == "cm":
        return value * 100000
    elif unit_from == "cm" and unit_to == "kilometer":
        return value / 100000
    elif unit_from == "meter" and unit_to == "kilometer":
        return value / 1000
    elif unit_from == "kilometer" and unit_to == "meter":
        return value * 1000
    return value

# Weight conversions
def convert_weight(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "kg" and unit_to == "pounds":
        return value * 2.20462
    elif unit_from == "pounds" and unit_to == "kg":
        return value / 2.20462
    elif unit_from == "g" and unit_to == "ounces":
        return value * 0.035274
    elif unit_from == "ounces" and unit_to == "g":
        return value / 0.035274
    return value

# Temperature conversions
def convert_temperature(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "Celsius" and unit_to == "Fahrenheit":
        return (value * 9/5) + 32
    elif unit_from == "Fahrenheit" and unit_to == "Celsius":
        return (value - 32) * 5/9
    elif unit_from == "Celsius" and unit_to == "Kelvin":
        return value + 273.15
    elif unit_from == "Kelvin" and unit_to == "Celsius":
        return value - 273.15
    elif unit_from == "Fahrenheit" and unit_to == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif unit_from == "Kelvin" and unit_to == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

# Data storage conversions
def convert_storage(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "KB" and unit_to == "bytes":
        return value * 1024
    elif unit_from == "bytes" and unit_to == "KB":
        return value / 1024
    elif unit_from == "MB" and unit_to == "KB":
        return value * 1024
    elif unit_from == "KB" and unit_to == "MB":
        return value / 1024
    elif unit_from == "GB" and unit_to == "MB":
        return value * 1024
    elif unit_from == "MB" and unit_to == "GB":
        return value / 1024
    elif unit_from == "TB" and unit_to == "GB":
        return value * 1024
    elif unit_from == "GB" and unit_to == "TB":
        return value / 1024
    return value

# Speed conversions
def convert_speed(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "m/s" and unit_to == "km/h":
        return value * 3.6
    elif unit_from == "km/h" and unit_to == "m/s":
        return value / 3.6
    elif unit_from == "km/h" and unit_to == "mph":
        return value / 1.60934
    elif unit_from == "mph" and unit_to == "km/h":
        return value * 1.60934
    elif unit_from == "mph" and unit_to == "ft/s":
        return value * 1.46667
    elif unit_from == "ft/s" and unit_to == "mph":
        return value / 1.46667
    return value

# Volume conversions
def convert_volume(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "L" and unit_to == "mL":
        return value * 1000
    elif unit_from == "mL" and unit_to == "L":
        return value / 1000
    elif unit_from == "gal" and unit_to == "L":
        return value * 3.78541
    elif unit_from == "L" and unit_to == "gal":
        return value / 3.78541
    elif unit_from == "in³" and unit_to == "L":
        return value * 0.0163871
    elif unit_from == "L" and unit_to == "in³":
        return value / 0.0163871
    return value

# Area conversions
def convert_area(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "m²" and unit_to == "km²":
        return value / 1_000_000
    elif unit_from == "km²" and unit_to == "m²":
        return value * 1_000_000
    elif unit_from == "ft²" and unit_to == "m²":
        return value * 0.092903
    elif unit_from == "m²" and unit_to == "ft²":
        return value / 0.092903
    elif unit_from == "in²" and unit_to == "cm²":
        return value * 6.4516
    elif unit_from == "cm²" and unit_to == "in²":
        return value / 6.4516
    return value

# Time conversions (NEW)
def convert_time(value: float, unit_from: str, unit_to: str) -> float:
    to_seconds = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2629800,   # average month (30.44 days)
        "year": 31557600,   # average year (365.25 days)
    }
    # Lowercase for safety
    unit_from, unit_to = unit_from.lower(), unit_to.lower()
    if unit_from not in to_seconds or unit_to not in to_seconds:
        return value
    seconds = value * to_seconds[unit_from]
    result = seconds / to_seconds[unit_to]
    return result

@app.get("/convert")
def convert(request: Request, value: float, unit_from: str, unit_to: str, category: str):
    print(f"Received: value = {value}, unit_from = {unit_from}, unit_to = {unit_to}, category = {category}")

    converted_value = value
    if category == "length":
        converted_value = convert_length(value, unit_from, unit_to)
    elif category == "weight":
        converted_value = convert_weight(value, unit_from, unit_to)
    elif category == "temperature":
        converted_value = convert_temperature(value, unit_from, unit_to)
    elif category == "storage":
        converted_value = convert_storage(value, unit_from, unit_to)
    elif category == "speed":
        converted_value = convert_speed(value, unit_from, unit_to)
    elif category == "volume":
        converted_value = convert_volume(value, unit_from, unit_to)
    elif category == "area":
        converted_value = convert_area(value, unit_from, unit_to)
    elif category == "time":  # Added time category support
        converted_value = convert_time(value, unit_from, unit_to)

    print(f"Converted value: {converted_value}")
    return templates.TemplateResponse("index.html", {"request": request, "converted_value": converted_value})
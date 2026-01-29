from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/calculadora",
    tags=["Calculadora"]
)

@router.get("/sumar/{num1}/{num2}")
def sumar(num1: float, num2: float):
    """Suma dos números."""
    return {
        "operacion": "suma",
        "num1": num1,
        "num2": num2,
        "resultado": num1 + num2
    }

@router.get("/restar/{num1}/{num2}")
def restar(num1: float, num2: float):
    """Resta el segundo número al primero."""
    return {
        "operacion": "resta",
        "num1": num1,
        "num2": num2,
        "resultado": num1 - num2
    }

@router.get("/multiplicar/{num1}/{num2}")
def multiplicar(num1: float, num2: float):
    """Multiplica dos números."""
    return {
        "operacion": "multiplicacion",
        "num1": num1,
        "num2": num2,
        "resultado": num1 * num2
    }

@router.get("/dividir/{num1}/{num2}")
def dividir(num1: float, num2: float):
    """Divide el primer número entre el segundo."""
    if num2 == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir por cero.")
    
    return {
        "operacion": "division",
        "num1": num1,
        "num2": num2,
        "resultado": num1 / num2
    }
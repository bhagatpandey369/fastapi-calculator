from fastapi import APIRouter, HTTPException
from .schemas import CalculationRequest, CalculationResult

router = APIRouter()

@router.post("/calculate", response_model=CalculationResult)
def calculate(req: CalculationRequest):
    if req.operator == "+":
        result = req.a + req.b
    elif req.operator == "-":
        result = req.a - req.b
    elif req.operator == "*":
        result = req.a * req.b
    elif req.operator == "/":
        if req.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        result = req.a / req.b
    else:
        raise HTTPException(status_code=400, detail="Invalid operator")
    return {"result": result}

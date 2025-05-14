from pydantic import BaseModel

class CalculationRequest(BaseModel):
    a: float
    b: float
    operator: str  # "+", "-", "*", "/"

class CalculationResult(BaseModel):
    result: float
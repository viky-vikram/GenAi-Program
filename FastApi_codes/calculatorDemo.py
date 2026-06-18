from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Define request body for calculator operations
class CalculatorRequest(BaseModel):
    a: float
    b: float

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Calculator API", "endpoints": {
        "/add": "Add two numbers",
        "/subtract": "Subtract two numbers",
        "/multiply": "Multiply two numbers",
        "/divide": "Divide two numbers"
    }}

# Addition endpoint
@app.post("/add")
def add(request: CalculatorRequest):
    result = request.a + request.b
    return {"a": request.a, "b": request.b, "operation": "addition", "result": result}

# Subtraction endpoint
@app.post("/subtract")
def subtract(request: CalculatorRequest):
    result = request.a - request.b
    return {"a": request.a, "b": request.b, "operation": "subtraction", "result": result}

# Multiplication endpoint
@app.post("/multiply")
def multiply(request: CalculatorRequest):
    result = request.a * request.b
    return {"a": request.a, "b": request.b, "operation": "multiplication", "result": result}

# Division endpoint
@app.post("/divide")
def divide(request: CalculatorRequest):
    if request.b == 0:
        return {"error": "Cannot divide by zero"}
    result = request.a / request.b
    return {"a": request.a, "b": request.b, "operation": "division", "result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

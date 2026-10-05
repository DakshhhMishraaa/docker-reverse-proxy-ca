
from fastapi import FastAPI

app = FastAPI(title="Orders Service")


@app.get("/")
def get_orders():
    return {
        "service": "Order Service",
        "orders": [
            {"id": 101, "product": "Laptop"},
            {"id": 102, "product": "Phone"}
        ]
    }


@app.get("/health")
def health_check():
    return {
        "service": "Order Service",
        "status": "healthy"
    }

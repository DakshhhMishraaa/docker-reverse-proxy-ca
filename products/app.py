
from fastapi import FastAPI

app = FastAPI(title="Products Service")


@app.get("/")
def get_products():
    return {
        "service": "Product Service",
        "products": ["Laptop", "Phone", "Keyboard"]
    }


@app.get("/health")
def health_check():
    return {
        "service": "Product Service",
        "status": "healthy"
    }

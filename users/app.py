
from fastapi import FastAPI

app = FastAPI(title="Users Service")


@app.get("/")
def get_users():
    return {
        "service": "User Service",
        "users": ["Daksh", "Rahul", "Aman"]
    }


@app.get("/health")
def health_check():
    return {
        "service": "User Service",
        "status": "healthy"
    }

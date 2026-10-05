import os

import psycopg2
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Users Service")


def get_db_connection():
    return psycopg2.connect(
        host="database",
        database=os.getenv("POSTGRES_DB", "ecommerce"),
        user=os.getenv("POSTGRES_USER", "admin"),
        password=os.environ["POSTGRES_PASSWORD"],
    )


@app.get("/")
def get_users():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name FROM users ORDER BY id")
                users = [
                    {"id": row[0], "name": row[1]}
                    for row in cursor.fetchall()
                ]

        return {
            "service": "User Service",
            "users": users,
        }

    except psycopg2.Error:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve users from the database",
        )


@app.get("/health")
def health_check():
    return {
        "service": "User Service",
        "status": "healthy",
    }
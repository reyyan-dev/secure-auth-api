from fastapi import FastAPI

app = FastAPI(
    title="Secure Auth API",
    description="Production-style authentication and user management API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Secure Auth API is running",
        "status": "ok",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
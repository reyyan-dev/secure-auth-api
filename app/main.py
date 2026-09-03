from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.db.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Auth API")

app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Secure Auth API is running"}
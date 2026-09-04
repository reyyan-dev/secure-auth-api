from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.core.config import settings
from app.db.database import Base, engine
from app.models.user import User


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Secure Auth API is running"}

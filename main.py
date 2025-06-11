from fastapi import FastAPI
from routers.user_router import user_router
from config import settings

app = FastAPI(title="User Service", version="1.0.0")

# Include user routes
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}

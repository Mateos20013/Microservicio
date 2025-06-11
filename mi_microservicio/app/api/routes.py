from fastapi import APIRouter, Depends
from app.domain.service import SimpleGreetingService
from app.domain.interface import GreetingService

router = APIRouter()

def get_greeting_service() -> GreetingService:
    return SimpleGreetingService()

@router.get("/saludo")
def saludar(nombre: str, service: GreetingService = Depends(get_greeting_service)):
    return {"mensaje": service.greet(nombre)}

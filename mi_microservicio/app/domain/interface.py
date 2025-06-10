from abc import ABC, abstractmethod

class GreetingService(ABC):
    @abstractmethod
    def greet(self, name: str) -> str:
        pass

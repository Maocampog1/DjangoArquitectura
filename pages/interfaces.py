from abc import ABC, abstractmethod
from django.http import HttpRequest

class ImageStorage(ABC):
    @abstractmethod  # cualquier clase que herede debe implementar este método
    def store(self, request: HttpRequest):
        pass

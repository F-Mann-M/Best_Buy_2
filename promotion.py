from abc import ABC, abstractmethod

class Promotion(ABC):

    def __init__(self, name):
        self._member = name
    @abstractmethod
    def apply_promotion(product, quantity) -> float:
        """apply promotion to product"""
        pass
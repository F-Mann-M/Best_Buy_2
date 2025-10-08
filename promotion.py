from abc import ABC, abstractmethod

class Promotion(ABC):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """apply promotion to product"""
        pass


class PercentDiscount(Promotion):

    def __init__(self, name, discount):
        super().__init__(name)
        self._discount = discount

    def apply_promotion(self, product, quantity) -> float:
        """reduce price by discount"""
        price = product.get_price() - (product.get_price() * (self._discount/100))
        return price * quantity


class SecondHalfPrice(Promotion):

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """Second product half price"""
        full_price = (quantity - (quantity // 2)) * product.get_price()
        half_price = (quantity // 2) * (product.get_price()/2)
        return full_price + half_price


class ThirdOneFree(Promotion):

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """price of every third product is 0"""
        return (quantity - (quantity // 3)) * product.get_price()


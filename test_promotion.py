from promotion import PercentDiscount, SecondHalfPrice, ThirdOneFree
from products import Product

def test_promotion_discount():
    product = Product("Laptop", 100, 10)
    promotion_discount = PercentDiscount("discount_30", 30)
    assert promotion_discount.apply_promotion(product, 1) == 70
    promotion_discount = PercentDiscount("discount_10", 10)
    assert promotion_discount.apply_promotion(product, 1) == 90


def test_second_half_price():
    product = Product("Laptop", 20, 10)
    half_price = SecondHalfPrice("half_price")
    assert half_price.apply_promotion(product, 2) == 30
    assert half_price.apply_promotion(product, 3) == 50
    assert half_price.apply_promotion(product, 4) == 60


def test_third_free():
    product = Product("Laptop", 10, 10)
    half_price = ThirdOneFree("third_free")
    assert half_price.apply_promotion(product, 2) == 20
    assert half_price.apply_promotion(product, 3) == 20
    assert half_price.apply_promotion(product, 4) == 30
    assert half_price.apply_promotion(product, 6) == 40
import pytest
from src.category import Category
from src.product import Product

@pytest.fixture
def product_unit() -> Product:
    """ осуществляет возврат Класс Product """
    return Product(
        "Iphone 16PRO",
        "Smartphone",
        107990,
        2
    )

@pytest.fixture
def product_category() -> Category:
    """ осуществляет возврат Класс Сategory"""
    products = [Product(
        "Iphone 16PRO",
        "Smartphone",
        107990,
        2
    )]
    return Category(
        "Мобильная электроника",
        "Smartphone",
        products
    )



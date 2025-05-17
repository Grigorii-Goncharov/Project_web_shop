import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_unit() -> Product:
    """осуществляет возврат Класс Product"""
    return Product("Iphone 16PRO", "Smartphone", 107990, 2)


@pytest.fixture
def product_category() -> Category:
    """осуществляет возврат Класс Сategory"""
    products = [Product("Iphone 16PRO", "Smartphone", 107990, 2)]
    return Category("Мобильная электроника", "Smartphone", products)


@pytest.fixture
def product_unit_2() -> Product:
    """Второй продукт для теста сложения"""
    return Product("Samsung S23", "Smartphone", 90000, 3)


@pytest.fixture
def products_list():
    return [
        Product("Iphone 15", "Smartphone", 115450, 2),
        Product("Samsung S23", "Smartphone", 90000, 3),
        Product("Xiaomi Mi", "Smartphone", 50000, 5),
    ]


@pytest.fixture
def category(products_list):
    return Category("Мобильная электроника", "Смартфоны", products_list)


@pytest.fixture
def product_category_for_iter(product_unit, product_unit_2) -> Category:
    """Фикстура возвращает категорию с двумя продуктами"""
    products = [product_unit, product_unit_2]
    return Category("Мобильная электроника", "Smartphone", products)

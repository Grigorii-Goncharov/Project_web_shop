import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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


# Тесты 16.1
@pytest.fixture
def smartphone_item() -> Product:
    """осуществляет возврат Класс Smartphone"""
    return Smartphone("Iphone",
                      "Американский Сматфон",
                      12000,
                      20,
                      20.0,
                      "16 PRO",
                      512,
                      "Gold")


@pytest.fixture
def lawngrass_item() -> Product:
    """осуществляет возврат Класс LawnGrass"""
    return LawnGrass("Зелёный ковер",
                     "Газонная трава",
                     1000,
                     500,
                     "Россия",
                     "3 месяца",
                     "Зеленая")

@pytest.fixture
def category_item() -> Category:
    # Создаем список товаров (с одним товаром)
    product1 = Product("Samsung QLED", "4K TV", 50000, 5)
    product2 = Product("Samsung LED", "HD TV", 20000, 20)
    products = [product1, product2]
    return Category("Телевизоры", "Устройство отображения фильмов и тв-передач", products)
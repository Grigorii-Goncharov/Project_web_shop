import pytest

from src.category import Category, Order
from src.product import Product


def test_product_category(product_category: Category) -> None:
    """Проверка имеющегося вывода продукта"""

    assert product_category.name == "Мобильная электроника"
    assert product_category.description == "Smartphone"
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_wrong_product_category(product_category: Category) -> None:
    """Проверка вывода отсутствующего продукта"""

    assert product_category.name != "Спорт инвентарь"
    assert product_category.description != "Scooter"
    assert Category.category_count != 3
    assert Category.product_count != 0


def test_add_product_increases_count(product_category: Category) -> None:
    """Проверка добавления нового продукта и увеличения счётчика"""
    initial_count = Category.product_count
    new_product = Product("Samsung Galaxy S23", "Flagship smartphone", 180000, 5)
    product_category.add_product(new_product)
    assert Category.product_count == initial_count + 1
    assert new_product in product_category.products_list


def test_add_product_type_check(product_category: Category) -> None:
    """Проверка, что добавлять можно только объекты Product"""
    with pytest.raises(TypeError):
        product_category.add_product("не продукт")  # строка вместо объекта Product


def test_products_property_returns_string(product_category: Category) -> None:
    """Проверка строкового свойства products"""
    products_str = product_category.products
    for product in product_category.products_list:
        assert product.name in products_str
        assert str(product.price) in products_str
        assert str(product.quantity) in products_str


def test_products_list_property_returns_list(product_category: Category) -> None:
    """Проверка, что products_list возвращает список объектов Product"""
    products_list = product_category.products_list
    assert isinstance(products_list, list)
    assert all(isinstance(prod, Product) for prod in products_list)


def test_category_str(category, products_list):
    """Тест подсчета количества продуктов"""
    total_quantity = sum(p.quantity for p in products_list)
    expected_str = f"{category.name}, количество продуктов: {total_quantity}"
    assert str(category) == expected_str


def test_category_str_empty():
    """Тест на проверку пустого значения Описания товаров и продуктов"""
    empty_category = Category("Пустая категория", "Нет товаров", [])
    expected_str = f"{empty_category.name}, количество продуктов: 0"
    assert str(empty_category) == expected_str


def test_order_invalid_quantity_zero(product_unit: Product, capsys) -> None:
    """Тест класса заказа при невалидных данных (нулевое количество) и вывод строки в консоль"""
    order = Order(product_unit, 0)  # Проверяем значение total_price
    assert order.total_price == 0  # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "Ошибка: Количество товара должно быть больше нуля" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_order_invalid_quantity(product_unit: Product, capsys) -> None:
    """Тест класса заказа при невалидных данных (превышающее количество) и вывод строки в консоль"""
    order = Order(product_unit, 25)
    assert order.total_price == 2699750
    captured = capsys.readouterr()
    assert "Вызвана ошибка: Количество заказа превышает количество на складе" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_add_non_product_to_category(category_item: Category) -> None:
    """Тест, что нельзя добавить не-Product в категорию"""
    with pytest.raises(TypeError):
        category_item.add_product("Не является продуктом!")


def test_init_raise() -> None:
    """Тест, проверки на несоответствие типа продуктов"""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    with pytest.raises(TypeError):
        Category("Смартфоны", "Высокопроизводительные смартфоны", [product, 200])

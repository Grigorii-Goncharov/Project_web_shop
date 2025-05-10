from unittest.mock import patch

from src.category import Category
from src.product import Product


def test_product_unit(product_unit: Product) -> None:
    """Проверка имеющегося вывода продукта"""

    assert product_unit.name == "Iphone 16PRO"
    assert product_unit.description == "Smartphone"
    assert product_unit.price == 107990
    assert product_unit.quantity == 2


def test_wrong_product_unit(product_unit: Product) -> None:
    """Проверка вывода отсутствующего продукта"""

    assert not product_unit.name == "Xiaomi"
    assert not product_unit.description == "Scooter"
    assert not product_unit.price == 43000
    assert not product_unit.quantity == 1


def test_new_product_add_and_update():
    products_list = []
    data1 = {"name": "Samsung Galaxy S23", "description": "Flagship", "price": 180000.0, "quantity": 5}
    data2 = {"name": "Samsung Galaxy S23", "description": "Flagship", "price": 190000.0, "quantity": 3}
    data3 = {"name": "Iphone 15", "description": "Smartphone", "price": 115450.0, "quantity": 2}

    p1 = Product.new_product(products_list, data1)
    assert p1.name == "Samsung Galaxy S23"
    assert p1.quantity == 5
    assert p1.price == 180000.0
    assert len(products_list) == 1

    p2 = Product.new_product(products_list, data2)
    assert p2 is p1
    assert p2.quantity == 8
    assert p2.price == 190000.0
    assert len(products_list) == 1

    p3 = Product.new_product(products_list, data3)
    assert p3.name == "Iphone 15"
    assert p3.quantity == 2
    assert len(products_list) == 2


def test_price_setter_zero_or_negative(product_unit: Product, capsys):
    product_unit.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_unit.price == 107990  # цена не изменилась

    product_unit.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_unit.price == 107990  # цена не изменилась


def test_price_setter_lower_price_confirm_yes(product_unit: Product):
    with patch("builtins.input", return_value="y"):
        product_unit.price = 100000
    assert product_unit.price == 100000


def test_price_setter_lower_price_confirm_no(product_unit: Product, capsys):
    with patch("builtins.input", return_value="n"):
        product_unit.price = 100000
    captured = capsys.readouterr()
    assert "Цена осталась прежней" in captured.out
    assert product_unit.price == 107990  # цена не изменилась


def test_category_initialization(product_category: Category) -> None:
    assert product_category.name == "Мобильная электроника"
    assert product_category.description == "Smartphone"
    assert Category.category_count >= 1
    assert Category.product_count >= 1

from unittest.mock import patch
import pytest
from src.category import Category
from src.product import Product, Smartphone, LawnGrass


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


def test_add_method():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert (product1 + product2) == 2580000.0
    assert (product1 + product3) == 1334000.0
    assert (product2 + product3) == 2114000.0

    # тесты модуля 16.1
def test_smartfone_check(smartphone_item: Smartphone) -> None:
    """Тест инициализации объекта класса Smartphone"""
    assert smartphone_item.name == "Iphone"
    assert smartphone_item.description == "Американский Сматфон"
    assert smartphone_item.price == 12000
    assert smartphone_item.efficiency == 20.0
    assert smartphone_item.model == "16 PRO"
    assert smartphone_item.memory == 512
    assert smartphone_item.color == "Gold"

def test_lawngrass_item_check(lawngrass_item: LawnGrass) -> None:
    """Тест инициализации объекта класса LawnGrass"""
    assert lawngrass_item.name == "Зелёный ковер"
    assert lawngrass_item.description == "Газонная трава"
    assert lawngrass_item.price == 1000
    assert lawngrass_item.quantity== 500
    assert lawngrass_item.country == "Россия"
    assert lawngrass_item.germination_period == "3 месяца"
    assert lawngrass_item.color == "Зеленая"

def test_add_method_smartphone(smartphone_item: Smartphone) -> None:
    """Тест сложения объектов класса Smartphone"""
    smartphone_new = Smartphone("Iphone",
                       "512GB, Красный цвет, 150MP камера",
                       300000.0,
                       4,
                        19.0,
                             "16Pro",
                             32,
                             "Red")
    smartphone_sum = smartphone_new  + smartphone_item
    assert smartphone_sum


def test_add_method_smartphone_rise_call() -> None:
    """Тест вызова исключения при сложении вместо продукта или его наследников любой другой объект."""
    with pytest.raises(TypeError):
        smartphone1 = Smartphone("Samsung Galaxy S23 Ultra",
                           "256GB, Серый цвет, 200MP камера",
                           180000.0,
                           5,
                            11.0,
                                 "s20",
                                 8,
                                 "green")
        smartphone2 = "Неправильная строка"
        smartphone_sum = smartphone1  + smartphone2
        assert smartphone_sum

def test_add_method_lawngrass(lawngrass_item: LawnGrass) -> None:
    """Тест сложения объектов класса LawnGrass"""
    lawngrass_new = LawnGrass("Лесной ковёр",
                              "Газонная трава",
                              1000,
                              30,
                              "Россия",
                              "2 месяца",
                            "Зеленая")

    lawngrass_sum = lawngrass_new + lawngrass_item
    assert lawngrass_sum

def test_add_method_lawngrass_rise_call() -> None:
    """Тест вызова исключения при сложении вместо продукта или его наследников любой другой объект."""
    with pytest.raises(TypeError):
        lawngrass_1 = LawnGrass("Зеленые ковер",
                           "Трава для гольфа",
                           1500,
                           2,
                            "Новая Зеландия",
                            "1 неделя",
                                "Синяя")
        lawngrass_2 = 1
        lawngrass_sum = lawngrass_1  + lawngrass_2
        assert lawngrass_sum

def test_add_method_rise_call(smartphone_item, lawngrass_item) -> None:
    """Тест вызова исключения при сложении продуктов с разных категорий."""
    with pytest.raises(TypeError):
        product1 = smartphone_item
        product2 =  lawngrass_item
        product3 = "smartphone"

        assert product1 + product2
        assert product1 + product3


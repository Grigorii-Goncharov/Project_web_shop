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

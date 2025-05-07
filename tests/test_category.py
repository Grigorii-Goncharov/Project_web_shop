from src.category import Category

def test_product_category(product_category: Category) -> None:
    """ Проверка имеющегося вывода продукта"""

    assert product_category.name == "Мобильная электроника"
    assert product_category.description == "Smartphone"
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_wrong_product_category(product_category: Category) -> None:
    """ Проверка вывода отсутствующего продукта"""

    assert product_category.name != "Спорт инвентарь"
    assert product_category.description != "Scooter"
    assert Category.category_count == 1
    assert Category.product_count == 1
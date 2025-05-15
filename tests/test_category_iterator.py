from src.category_iterator import CategoryIterator
from src.product import Product


def test_iterator_returns_all_products(product_category_for_iter, product_unit, product_unit_2):
    iterator = CategoryIterator(product_category_for_iter)
    products = list(iterator)
    assert len(products) == 2
    assert products[0] == product_unit
    assert products[1] == product_unit_2


def test_iterator_in_for_loop(product_category_for_iter, product_unit, product_unit_2):
    expected = [product_unit.name, product_unit_2.name]
    result = []
    for product in CategoryIterator(product_category_for_iter):
        result.append(product.name)
    assert result == expected


def test_iterator_multiple_passes(product_category_for_iter):
    iterator = CategoryIterator(product_category_for_iter)
    first_pass = [p.name for p in iterator]
    second_pass = [p.name for p in iterator]
    assert first_pass == second_pass


def test_iterator_returns_product_instances(product_category):
    iterator = CategoryIterator(product_category)
    for product in iterator:
        assert isinstance(product, Product)

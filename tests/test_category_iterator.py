from src.category_iterator import CategoryIterator
from src.product import Product


def test_iterator_returns_product_instances(product_category):
    iterator = CategoryIterator(product_category)
    for product in iterator:
        assert isinstance(product, Product)
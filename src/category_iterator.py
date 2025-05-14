from src.category import Category
from src.product import Product


class CategoryIterator:
    """Итеротор перебирает товары одной категории и возвращает очередной товар категории."""

    def __init__(self, category_obj):
        self.category_obj = category_obj


    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        """Итератор"""
        products = self.category_obj.get_products() # Сноска 1  метод def get_products в классе Category
        if self.index < len(products):
            product = products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    iterator = CategoryIterator(category)

    for product in iterator:
        print(product)

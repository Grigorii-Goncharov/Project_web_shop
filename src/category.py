from src.product import Product


class Category:
    """Класс категория"""

    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Метод добавления нового продукта"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Геттер с выводом списка товаров. Геттер должен возвращать строку, чтобы пользователь класса мог
        их распечатать или записать в какой-то другой интерфейс.
        """
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

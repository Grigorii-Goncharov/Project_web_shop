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

    def get_products(self):
        """Безопасное получение Атрибута (копия) - нужна для инкапсуляции в классе CategoryIterator. см. сноска 1"""
        return self.__products.copy()

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в категорию"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты от класса Product или его подклассов")

        # Проверка на наличие позиции товара
        for existing_product in self.__products:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                if product.price > existing_product.price:
                    existing_product.price = product.price
                return

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

    def __str__(self):
        """Метод преобразования атрибутов в строку и выводом в консоль"""
        return f"{self.name}, количество продуктов: {len(self.__products)}"


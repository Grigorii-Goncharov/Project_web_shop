from src.abstract_class import FormationProduct
from src.class_of_exception import ClassOfException
from src.product import Product


class Category(FormationProduct):
    """Класс категория"""

    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        for product in products:
            if not isinstance(product, Product):
                raise TypeError("В категорию можно добавлять только объекты класса Product или его наследников")
        self.name = name
        self.description = description
        self.__products = products
        try:
            if self.__products == []:
                raise ClassOfException("Передан пустой список")
        except ClassOfException as e:
            print(f"Вызвана ошибка: {e}")
        else:
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Метод  суммировать количество каждого продукта (quantity). общее количество единиц товара в категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity}"

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

    @property
    def products_list(self):
        return self.__products

    def middle_price(self):
        """
        Метод, который подсчитывает средний ценник всех товаров.
        """
        try:
            if not self.products_list:
                raise TypeError("Список товаров пуст")

            prices = [product.price for product in self.products_list if product.price]
            average_sum_product = sum(prices) / len(prices)

        except ZeroDivisionError:
            print("На ноль делить нельзя")
        except TypeError as e:
            print(f"Ошибка: {e}")
            return 0
        else:
            return average_sum_product
        finally:
            print("Операция завершена")


class Order(FormationProduct):
    """Класс для оформления заказа"""

    def __init__(self, product, quantity):
        self.product = product  # Ссылка на объект товара (например, Smartphone или LawnGrass)
        self.quantity = quantity  # Количество купленного товара
        try:
            if product.quantity < self.quantity:
                raise ValueError("Количество заказа превышает количество на складе")
            elif self.quantity <= 0:
                raise ClassOfException("Количество товара должно быть больше нуля")
        except ValueError as e:
            print(f"Вызвана ошибка: {e}")
        except ClassOfException as e:
            print(f"Ошибка: {e}")
            self.total_price = 0  # Дефолтное значение
        else:
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")

        self.total_price = product.price * quantity  # Итоговая стоимость

    def __str__(self):
        return f"{self.product}, {self.quantity}, {self.total_price}"


# if __name__ == "__main__":
#     category = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [],
#     )
#     print(category)

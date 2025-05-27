from src.abstract_class import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if self.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    @classmethod
    def new_product(cls, products_list, products_dict):
        """
        Добавляет новый продукт в список или обновляет существующий:
        - Если продукт с таким именем найден, увеличивает quantity, а цену делает максимальной.
        - Если не найден - добавляет новый продукт (new_product).
        """

        name = products_dict["name"]
        description = products_dict["description"]
        price = float(products_dict["price"])
        quantity = int(products_dict["quantity"])

        for product in products_list:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        new_product = cls(name=name, description=description, price=price, quantity=quantity)
        products_list.append(new_product)
        return new_product

    @property
    def price(self):
        """Получение цены из приватного статуса"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Корректор цены из приватного статуса"""

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer = input(
                f"Новая цена {new_price} ниже текущей {self.__price}. Подтвердите изменение (y/n): "
            ).lower()
            if answer != "y":
                print("Цена осталась прежней")
                return

        self.__price = new_price
        print(f"Цена успешно изменена на {self.__price}")

    def __str__(self):
        """Метод преобразования атрибутов в строку и выводом в консоль"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод получения суммы всех товаров на складе"""
        if not isinstance(other, Product):
            raise TypeError("Можно добавлять только объекты от класса Product или его подклассов")
        cost_all_products = self.__price * self.quantity + other.__price * other.quantity
        return cost_all_products


class Smartphone(Product):
    """Дочерний класс Smartphone"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Складывать можно только объекты Smartphone и дочерние от них.")
        return self.price + other.price


class LawnGrass(Product):
    """Дочерний класс газонная трава"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Складывать можно только объекты LawnGrass и дочерние от них.")
        return self.price + other.price

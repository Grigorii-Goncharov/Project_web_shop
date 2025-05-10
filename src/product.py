class Product:
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


    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int):
        """Класс метод для добавления нового продукта"""


        return cls(name, description, price, quantity)


    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str


    @classmethod
    def new_product(cls, products_dict, products_list):
        """
        Добавляет новый продукт в список или обновляет существующий:
        - Если продукт с таким именем найден, увеличивает quantity, а цену делает максимальной.
        - Если не найден - добавляет новый продукт (new_product).
        """

        name = products_dict['name']
        description = products_dict['description']
        price = float(products_dict['price'])
        quantity = int(products_dict['quantity'])

        for product in products_list:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        new_product = cls(
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )
        products_list.append(new_product)
        return new_product


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
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



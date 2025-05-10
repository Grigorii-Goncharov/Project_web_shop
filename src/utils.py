import json

from config import path_to_json
from src.category import Category
from src.product import Product


def read_json(path_to_json: str):
    """Функция чтения JSON файла"""

    with open(path_to_json, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def create_object_from_json(data):
    """Преобразования Данных из JSON в объекты"""

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)

        category = Category(name=category_data["name"], description=category_data["description"], products=products)
        categories.append(category)

    return categories


# if __name__ == "__main__":
#     # 1. Загружаем данные
#     data = read_json(path_to_json)
#     categories = create_object_from_json(data)  # Получаем список категорий
#
#     # 2. Выводим общую информацию
#     print(f"\nВсего категорий: {Category.category_count}")
#     print(f"Всего товаров: {Category.product_count}")
#
#     # 3. Выводим подробную информацию по каждой категории
#     for category in categories:  # Теперь categories определена
#         print(f"\nКатегория: {category.name}")
#         print(f"Описание: {category.description}")
#         print(f"Количество товаров: {len(category.products)}")
#
#         # Выводим все товары в категории
#         for product in category.products:
#             print(f"  {product}")

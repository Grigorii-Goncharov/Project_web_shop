class ClassOfException(Exception):
    """
    Класс исключения, который отвечает за обработку событий, когда в «Категорию» или «Заказ»
    добавляется товар с нулевым количеством.
    """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Отсутствует значение"

    def __str__(self):
        return self.message

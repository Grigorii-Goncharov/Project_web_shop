from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """базовый абстрактный класс, который станет родительским для класса продуктов."""

    @abstractmethod
    def __add__(self, other) -> float | int:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class FormationProduct(ABC):
    """Абстрактный класс, для оформления продукта заказа."""

    @abstractmethod
    def __str__(self) -> str:
        pass

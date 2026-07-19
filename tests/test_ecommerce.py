import json

import pytest

from src.base_group import BaseGroup
from src.category import Category
from src.iterator import CategoryIterator
from src.order import Order
from src.product import BaseProduct, LawnGrass, Product, Smartphone
from src.utils import read_json


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта."""
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def sample_category(sample_product):
    """Фикстура для создания тестовой категории."""
    Category.category_count = 0
    Category.product_count = 0

    return Category(
        name="Смартфоны",
        description="Электронные устройства для связи",
        products=[sample_product],
    )


def test_product_init(sample_product):
    """Тест корректности инициализации объекта класса Product."""
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_product_str(sample_product):
    """Тест строкового отображения продукта (__str__)."""
    assert str(sample_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_str(sample_category):
    """Тест строкового отображения категории (__str__)."""
    assert str(sample_category) == "Смартфоны, количество продуктов: 5 шт."


def test_product_add(sample_product):
    """Тест сложения двух продуктов одного типа (__add__)."""
    product2 = Product("Iphone 15", "512GB", 210000.0, 8)
    assert sample_product + product2 == 2580000.0


def test_category_init(sample_category):
    """Тест корректности инициализации объекта класса Category."""
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Электронные устройства для связи"


def test_category_iterator():
    """Тест работы класса-итератора CategoryIterator в цикле."""
    p1 = Product("Товар 1", "Описание 1", 100.0, 1)
    p2 = Product("Товар 2", "Описание 2", 200.0, 2)
    cat = Category("Категория", "Описание", [p1, p2])

    iterator = CategoryIterator(cat)
    iterated_products = []

    for product in iterator:
        iterated_products.append(product)

    assert len(iterated_products) == 2
    assert iterated_products[0].name == "Товар 1"
    assert iterated_products[1].name == "Товар 2"


def test_smartphone_init():
    """Тест инициализации класса Smartphone."""
    phone = Smartphone(
        name="iPhone 15",
        description="Флагман",
        price=100000.0,
        quantity=5,
        efficiency=4.5,
        model="15 Pro",
        memory=256,
        color="Space Gray",
    )
    assert phone.name == "iPhone 15"
    assert phone.color == "Space Gray"


def test_lawngrass_init():
    """Тест инициализации класса LawnGrass."""
    grass = LawnGrass(
        name="Изумруд",
        description="Трава",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period=14,
        color="Зеленый",
    )
    assert grass.name == "Изумруд"
    assert grass.germination_period == 14


def test_add_different_types_raises_error():
    """Тест, что сложение продуктов разного типа вызывает TypeError."""
    phone = Smartphone("iPhone 15", "Desc", 100000.0, 2, 4.5, "15", 256, "Gray")
    grass = LawnGrass("Изумруд", "Desc", 500.0, 20, "Россия", 14, "Зеленый")

    with pytest.raises(TypeError):
        _ = phone + grass


def test_category_add_subclass_products(sample_category):
    """Тест успешного добавления подклассов в категорию."""
    phone = Smartphone("iPhone 15", "Desc", 100000.0, 2, 4.5, "15", 256, "Gray")
    sample_category.add_product(phone)
    assert phone in sample_category.get_products_list()


def test_category_add_invalid_type_raises_error(sample_category):
    """Тест добавления некорректного типа данных."""
    with pytest.raises(TypeError):
        sample_category.add_product("Строка")


def test_read_json_success(tmp_path):
    """Тест успешного чтения JSON."""
    test_data = [{"name": "Электроника", "description": "Гаджеты", "products": []}]
    file = tmp_path / "test_products.json"
    file.write_text(json.dumps(test_data), encoding="utf-8")
    categories = read_json(str(file))
    assert len(categories) == 1


def test_read_json_file_not_found():
    """Тест возврата пустого списка, если файла нет."""
    assert read_json("non_existent.json") == []


# === НОВЫЕ ТЕСТЫ ДЛЯ ТЕКУЩЕГО ЗАДАНИЯ ===


def test_base_product_cannot_be_instantiated():
    """Проверка абстрактности BaseProduct."""
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Описание", 100.0, 5)


def test_print_mixin_logs_to_stdout(capsys):
    """Проверка работы миксина логирования PrintMixin."""
    _ = Product("Тест-продукт", "Описание", 100.0, 5)
    captured = capsys.readouterr()
    assert "Product('Тест-продукт', 'Описание', 100.0, 5)" in captured.out


def test_order_init(sample_product):
    """Проверка инициализации заказа и расчета итоговой стоимости."""
    order = Order(product=sample_product, quantity=3)
    assert order.product == sample_product
    assert order.quantity == 3
    assert order.total_price == 180000.0 * 3
    assert "Заказ: Samsung Galaxy S23 Ultra, 3 шт." in str(order)


def test_base_group_cannot_be_instantiated():
    """Проверка абстрактности BaseGroup."""
    with pytest.raises(TypeError):
        BaseGroup("Группа", "Описание")

from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


@pytest.fixture
def burger():  # фикстура создания бургера
    return Burger()


@pytest.fixture
def mock_bun():  # мок для булочки
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Булочка"
    mock_bun.get_price.return_value = 20.0
    return mock_bun


@pytest.fixture
def mock_ingredient():  # мок для ингредиента
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = "SAUCE"
    mock_ingredient.get_name.return_value = "Соус"
    mock_ingredient.get_price.return_value = 20.0
    return mock_ingredient


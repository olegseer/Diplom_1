from unittest.mock import Mock

import pytest

from data import Menu
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun


@pytest.fixture
def mock_black_bun():  # мок для булочки
    mock_black_bun = Mock(spec=Bun)
    mock_black_bun.get_name.return_value = Menu.BLACK_BUN_NAME
    mock_black_bun.get_price.return_value = Menu.BLACK_BUN_PRICE
    return mock_black_bun


@pytest.fixture
def mock_white_bun():  # мок для булочки
    mock_white_bun = Mock(spec=Bun)
    mock_white_bun.get_name.return_value = Menu.WHITE_BUN_NAME
    mock_white_bun.get_price.return_value = Menu.WHITE_BUN_PRICE
    return mock_white_bun


@pytest.fixture
def mock_sauce():  # мок для соуса
    mock_sauce = Mock(spec=Ingredient)
    mock_sauce.get_type.return_value = Menu.SAUCE_TYPE
    mock_sauce.get_name.return_value = Menu.SAUCE_NAME
    mock_sauce.get_price.return_value = Menu.SAUCE_PRICE
    return mock_sauce


@pytest.fixture
def mock_filling():  # мок для начинки
    mock_filling = Mock(spec=Ingredient)
    mock_filling.get_type.return_value = Menu.FILLING_TYPE
    mock_filling.get_name.return_value = Menu.FILLING_NAME
    mock_filling.get_price.return_value = Menu.FILLING_PRICE
    return mock_filling

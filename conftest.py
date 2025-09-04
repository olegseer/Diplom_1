from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from data import Menu
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun


@pytest.fixture
def burger():  # фикстура создания бургера
    return Burger()

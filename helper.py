from data import Menu
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class Helpers:

    @staticmethod
    def mock_black_bun():  # мок для булочки
        mock_black_bun = Mock(spec=Bun)
        mock_black_bun.get_name.return_value = Menu.BLACK_BUN_NAME
        mock_black_bun.get_price.return_value = Menu.BLACK_BUN_PRICE
        return mock_black_bun

    @staticmethod
    def mock_white_bun():  # мок для булочки
        mock_white_bun = Mock(spec=Bun)
        mock_white_bun.get_name.return_value = Menu.WHITE_BUN_NAME
        mock_white_bun.get_price.return_value = Menu.WHITE_BUN_PRICE
        return mock_white_bun

    @staticmethod
    def mock_sauce():  # мок для соуса
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = Menu.SAUCE_TYPE
        mock_sauce.get_name.return_value = Menu.SAUCE_NAME
        mock_sauce.get_price.return_value = Menu.SAUCE_PRICE
        return mock_sauce

    @staticmethod
    def mock_mayonnaise():  # мок для соуса
        mock_mayonnaise = Mock(spec=Ingredient)
        mock_mayonnaise.get_type.return_value = Menu.MAYONNAISE_TYPE
        mock_mayonnaise.get_name.return_value = Menu.MAYONNAISE_NAME
        mock_mayonnaise.get_price.return_value = Menu.MAYONNAISE_PRICE
        return mock_mayonnaise

    @staticmethod
    def mock_filling():  # мок для начинки
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = Menu.FILLING_TYPE
        mock_filling.get_name.return_value = Menu.FILLING_NAME
        mock_filling.get_price.return_value = Menu.FILLING_PRICE
        return mock_filling

    @staticmethod
    def mock_fish():  # мок для начинки
        mock_fish = Mock(spec=Ingredient)
        mock_fish.get_type.return_value = Menu.FISH_TYPE
        mock_fish.get_name.return_value = Menu.FISH_NAME
        mock_fish.get_price.return_value = Menu.FISH_PRICE
        return mock_fish

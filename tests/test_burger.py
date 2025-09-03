from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import Menu


class TestBurger:

    # проверка, что булочку можно назначить
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # проверка добавления ингредиента
    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    # проверка удаления ингредиента
    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # проверка метода перемещения ингредиентов
    def test_move_ingredient(self, burger, mock_ingredient):
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = Menu.SAUCE_TYPE
        mock_ingredient_2.get_name.return_value = "Соус"
        mock_ingredient_2.get_price.return_value = 20.0
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient_2

    # проверка метода получения цены
    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()
        assert burger.get_price() == expected_price

    # проверка получения чека
    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_receipt = (
                               "(==== Булочка ====)\n"
                               "= sauce Соус =\n"
                               "(==== Булочка ====)\n"
                               "\n"
                               f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_receipt

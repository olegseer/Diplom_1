from data import Answer
from praktikum.burger import Burger
from unittest.mock import patch


class TestBurger:

    # проверка, что булочку можно выбрать
    def test_set_buns_success(self, mock_black_bun):
        burger = Burger()
        burger.set_buns(mock_black_bun)
        assert burger.bun == mock_black_bun

    # выбранная булочка заменяется, если выбрать другую
    def test_set_buns_multiple_times_success(self, mock_black_bun, mock_white_bun):
        burger = Burger()
        burger.set_buns(mock_black_bun)
        burger.set_buns(mock_white_bun)
        assert burger.bun == mock_white_bun

    def test_add_ingredient_success(self, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        assert mock_filling in burger.ingredients

    # проверка добавления нескольких ингредиентов
    def test_add_ingredient_multiple_times_success(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert len(burger.ingredients) == 2
        assert mock_sauce in burger.ingredients and mock_filling in burger.ingredients

    # удаления ингредиента
    def test_remove_ingredient_success(self, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # перемещения ингредиентов
    def test_move_ingredient_success(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_filling

    # проверка метода получения цены
    def test_get_price_success(self, mock_black_bun, mock_filling):
        burger = Burger()
        burger.set_buns(mock_black_bun)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == Answer.EXPECTED_PRICE

    # проверка получения чека
    @patch('praktikum.burger.Burger.get_price', return_value=30)
    def test_get_receipt_success(self, mock_get_price, mock_black_bun, mock_filling):
        burger = Burger()
        burger.set_buns(mock_black_bun)
        burger.add_ingredient(mock_filling)
        assert burger.get_receipt() == Answer.EXPECTED_RECEIPT

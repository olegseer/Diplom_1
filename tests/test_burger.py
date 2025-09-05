from unittest.mock import patch

import pytest

from helper import Helpers
from data import Answer


class TestBurger:

    # проверка, что булочку можно выбрать
    def test_set_buns_success(self, burger):
        bun = Helpers.mock_black_bun()
        burger.set_buns(bun)
        assert burger.bun == bun

    # выбранная булочка заменяется, если выбрать другую
    def test_set_buns_multiple_times_success(self, burger):
        bun_1 = Helpers.mock_black_bun()
        bun_2 = Helpers.mock_white_bun()
        burger.set_buns(bun_1)
        burger.set_buns(bun_2)
        assert burger.bun == bun_2

    # проверка добавления ингредиента: соуса или начинки
    @pytest.mark.parametrize('ingredient', [Helpers.mock_sauce(), Helpers.mock_filling()])
    def test_add_ingredient_success(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    # проверка добавления нескольких ингредиентов
    @pytest.mark.parametrize('ingredient', [[Helpers.mock_sauce(), Helpers.mock_mayonnaise()],
                                            [Helpers.mock_filling(), Helpers.mock_fish()]])
    def test_add_ingredient_multiple_times_success(self, burger, ingredient):
        first_ingredient = ingredient[0]
        second_ingredient = ingredient[1]
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        assert len(burger.ingredients) == 2
        assert first_ingredient in burger.ingredients and second_ingredient in burger.ingredients

    # удаления ингредиента
    def test_remove_ingredient_success(self, burger):
        ingredient = Helpers.mock_filling()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # перемещения ингредиентов
    def test_move_ingredient_success(self, burger):
        ingredient_1 = Helpers.mock_sauce()
        ingredient_2 = Helpers.mock_filling()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient_2

    # проверка метода получения цены
    def test_get_price_success(self, burger):
        bun = Helpers.mock_black_bun()
        ingredient = Helpers.mock_filling()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == Answer.EXPECTED_PRICE

    # проверка получения чека
    @patch('praktikum.burger.Burger.get_price', return_value=30)
    def test_get_receipt_success(self, mock_get_price, burger):
        bun = Helpers.mock_black_bun()
        ingredient = Helpers.mock_filling()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_receipt() == Answer.EXPECTED_RECEIPT

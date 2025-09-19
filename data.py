class Menu:
    BLACK_BUN_NAME = 'black bun'
    BLACK_BUN_PRICE = 10

    WHITE_BUN_NAME = 'white bun'
    WHITE_BUN_PRICE = 20

    SAUCE_TYPE = 'SAUCE'
    SAUCE_NAME = 'ketchup'
    SAUCE_PRICE = 5

    MAYONNAISE_TYPE = 'SAUCE'
    MAYONNAISE_NAME = 'mayonnaise'
    MAYONNAISE_PRICE = 5

    FILLING_TYPE = 'FILLING'
    FILLING_NAME = 'meat'
    FILLING_PRICE = 10

    FISH_TYPE = 'FILLING'
    FISH_NAME = 'fish'
    FISH_PRICE = 10


class Answer:

    EXPECTED_PRICE = 30
    EXPECTED_RECEIPT = (
        "(==== black bun ====)\n"
        "= filling meat =\n"
        "(==== black bun ====)\n"
        "\n"
        f"Price: {30}"
    )

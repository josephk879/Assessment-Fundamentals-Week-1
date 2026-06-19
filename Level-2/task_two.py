"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####


def add_to_basket(item: dict) -> list[dict]:
    """Adds an item and its price to a list."""
    basket.append(item)
    return basket


def duplicate_count(item_price: str, item_name: str, basket: list) -> dict:
    """Counts duplicate names"""
    count = 0
    for item in basket:
        if item["price"] == item_price:
            if item["name"] == item_name:
                count += 1
    return count


def generate_receipt(basket: list) -> str:
    """Generates a receipt for a basket of items."""
    receipt = ""
    item_list = []
    total_price = 0

    if len(basket) >= 1:
        for item in basket:
            no_of_duplicates = duplicate_count(
                item["price"], item["name"], basket)
            item_list.append(item["name"])
            if item["price"] != 0:
                receipt += f"{item["name"]} x {no_of_duplicates} - £{item["price"] * no_of_duplicates:.2f}" + "\n"

            else:
                receipt += f"{item["name"]} - Free" + "\n"

            if no_of_duplicates > 1:
                basket.remove(item)

            total_price += item["price"] * no_of_duplicates

        receipt += f"Total: £{total_price:.2f}"

    else:
        receipt = "Basket is empty"

    return receipt  # return the receipt string

#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))

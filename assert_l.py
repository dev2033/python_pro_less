def apply_discount(product, discount):
    """
    Делает скидку, при чем скидка не может быть больше
    100 процентов - ошибка AssertionError
    """
    price = int(product['цена'] * (1.0 - discount))
    assert 0 <= price <= product['цена']
    return price


from pricefox import apply_discount, format_price


def test_apply_discount():
    assert apply_discount(100, 20) == 80


def test_apply_discount_no_discount():
    assert apply_discount(50, 0) == 50


def test_format_price():
    assert format_price(80) == "$80.00"

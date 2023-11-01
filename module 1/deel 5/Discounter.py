from test_lib import test, report

month_discount_brands = 'Vespa,Kymco,Yamaha'
MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if brand in month_discount_brands:
        return round(price * MONTH_DISCOUNT_PERC / 100.0, 2)
    else:
        return 0.0


# Testen
price = 1000.0
brand = 'Vespa'
discount = calc_discount(price, brand, month_discount_brands)
test("Test 1", 100.0, discount)


price = 800.0
brand = 'Kymco'
discount = calc_discount(price, brand, month_discount_brands)
test("Test 2", 80.0, discount)

price = 1500.0
brand = 'Yamaha'
discount = calc_discount(price, brand, month_discount_brands)
test("Test 3", 150.0, discount)

price = 1200.0
brand = 'Suzuki'  
discount = calc_discount(price, brand, month_discount_brands)
test("Test 4", 0.0, discount)

price = 2000.0
brand = 'Piaggio' 
discount = calc_discount(price, brand, month_discount_brands)
test("Test 5", 0.0, discount)


report()

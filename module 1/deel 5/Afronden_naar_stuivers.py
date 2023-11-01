from test_lib import test, report

def afronden_naar_5_cent(getal):
    return round(getal * 20) / 20

# testen
original_getal = 2.13
expected_getal = 2.10
rounded_getal = afronden_naar_5_cent(original_getal)
test("test1", expected_getal, rounded_getal)

original_getal = 13.01
expected_getal = 13.0
rounded_getal = afronden_naar_5_cent(original_getal)
test("test2", expected_getal, rounded_getal)

original_getal = 7.44
expected_getal = 7.45
rounded_getal = afronden_naar_5_cent(original_getal)
test("test3", expected_getal, rounded_getal)

original_getal = 0.99
expected_getal = 1.0
rounded_getal = afronden_naar_5_cent(original_getal)
test("test4", expected_getal, rounded_getal)

original_getal = 3.52
expected_getal = 3.5
rounded_getal = afronden_naar_5_cent(original_getal)
test("test5", expected_getal, rounded_getal)


report()


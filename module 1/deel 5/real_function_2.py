from test_lib import test, report

def afronden_naar_5_cent(getal):
    return round(getal * 20) / 20

# Testgevallen en testen
original_getal = 2.24
expected_getal = 2.25
rounded_getal = afronden_naar_5_cent(original_getal)
name = f"Original amount: {original_getal}, Rounded amount: {rounded_getal}"
test(name, expected_getal, rounded_getal)

original_getal = 13.01
expected_getal = 13.0
rounded_getal = afronden_naar_5_cent(original_getal)
name = f"Original amount: {original_getal}, Rounded amount: {rounded_getal}" 
test(name, expected_getal, rounded_getal)

original_getal = 7.44
expected_getal = 7.45
rounded_getal = afronden_naar_5_cent(original_getal)
name = f"Original amount: {original_getal}, Rounded amount: {rounded_getal}"
test(name, expected_getal, rounded_getal)

original_getal = 0.99
expected_getal = 1.0
rounded_getal = afronden_naar_5_cent(original_getal)
name = f"Original amount: {original_getal}, Rounded amount: {rounded_getal}"
test(name, expected_getal, rounded_getal)

original_getal = 3.52
expected_getal = 3.5
rounded_getal = afronden_naar_5_cent(original_getal)
name = f"Original amount: {original_getal}, Rounded amount: {rounded_getal}"
test(name, expected_getal, rounded_getal)

# Rapport genereren
report()


def is_adult(age: int) -> bool:
    if not isinstance(age, int) or age < 0:
        return False
    elif age >= 18:
        return True
    else:
        return False
    
print(is_adult(20)) #True
print(is_adult(16)) #False


age = 20
if is_adult(age):
    print("Võib valid")
else:
    print("Ei või valid")


eu_northen_country_codes = ("DK", "EE", "FI", "IS", "LT", "LV", "NO", "SE")
def is_northen_country(country_code: str) -> bool:
    if not isinstance(country_code, str) or len(country_code) != 2:
        return False
    return country_code in eu_northen_country_codes

print(is_northen_country("EE")) #True
print(is_northen_country("US")) #False
print(is_northen_country("EST")) #False


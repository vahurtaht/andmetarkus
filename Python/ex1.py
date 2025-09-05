first_name = "Vahur"
print(first_name)
surname = "Täht"
print(surname)
full_name = first_name + " " + surname
print(full_name)

all_caps = first_name.lower() + str(1)
print(all_caps)

age = 50
print(age)
height = 1.80
print(height)
print("Minu vanus on " + str(age) + " ja minu pikkus on " + str(height) + ".")

surname[0]
print(surname[0])

surname[1:]
print(surname[1:])

muutuja = surname[0]+(len(surname)-1)*surname[0].lower()
print(muutuja)

initials = first_name[:2] + surname[:2]
print(initials)

print(age * first_name)
age = 18
if age >= 18:
    print("Võid hääletada Riigikogu valimistel.")
elif age >= 16:
    print("Võid hääletada kohalikel valimistel.")
else:
    print("Oota veel veidi, saad varsti hääletada.")

age = 17
if age >= 16:
    print("Võid hääletada kohalikel valimistel.")
    if age >= 18:
        print("Võid hääletada Riigikogu valimistel.")
else:
    print("Oota veel veidi, saad varsti hääletada.")

#väärtuse kontroll
number_to_check = 150
if number_to_check < 100:
    print(f"Muutuja väärtus {number_to_check} on alla 100")
elif number_to_check == 100:
    print(f"Muutuja väärtus {number_to_check} on täpselt 100")
else: 
    print(f"Muutuja väärtus {number_to_check} on üle 100")

#Kas täiskasvanud
is_adult = age >= 18
print(f"Kas isik on täiskasvanud? {is_adult}")

if age >= 18:
    print("Isik on täiskasvanud")
else:
    print("Isik ei ole täiskasvanud")


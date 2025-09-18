# FOR tsükkel

girl_names = ["Jaanika", "Malle", "Kersti", "Ann", "Mari", "Kati"]

 #Väljastada kõik tüdrukute nimed ükshaaval, kasutades FOR tsüklit
for name in girl_names:
    print(name)

# Väljastada esimesed 2 - lahendus 1
# Lisatud reavahetusega
print("Lahendus 1 \n")
for i in range(2):
    print(girl_names[i])

print("\n Lahendus 2 \n")

# piira,e järjendi pikkust 2 esimese lemendiga
for name in girl_names[:2]:
    print(name)

print("\n Lahendus 3 \n")

# teine kuni neljas
for name in girl_names[1:4]:
    print(name)

# teine kuni neljas üksteise järel
for name in girl_names[1:4]:
    print(name, end=" ")

print("\n Lahendus elemendid tagurpidi \n")

for name in reversed(girl_names):
    print(name, end=" ")

print("\n Lahendus paaris indeksiga elemendid \n")

for i in range(0, len(girl_names), 2):
    print(girl_names[i])
    

#Väljastame nimed mis algavad "K" tähega
print("\n Lahendus nimed mis algavad K tähega \n")

for name in girl_names:
    if name.startswith("K"):
        print(name)


# Moodusta sõnastik, mis sisaldab M tähega algavaid nimesid
print("\n Lahendus mis saldab M tähega algavaid nimesid \n")
sorted_names = {"M": []}
for name in girl_names:
    if name.startswith("M"):
        sorted_names["M"].append(name)





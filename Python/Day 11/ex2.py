# andmed csv failis

import csv

data_from_csv = []

with open('/Users/vaga_vesi/Projects/andmetarkus2025/andmetarkus/day-2/ANALYSIS/input/CustomerTable.csv', 'r', encoding='utf-8') as file:
    # tekitab reader objekti
    reader = csv.reader(file, delimiter=',')
    # teisendab reader objekti listiks
    data_from_csv = list(reader)

print(data_from_csv)

# esimene rida
insert_statement = "INSERT INTO customers"

# insert_statement + veergude nimed
# insert_statement += pikalt kirjutades insert_statement2 = insert_statement + ....

insert_statement += f"\n({','.join(data_from_csv[0])}) \nVALUES "

# mis väärtused lisada (read kuni eelviimane)
for row in data_from_csv[1:-1]:
    insert_statement += f"\n({','.join(row)}),"

# viimase rea jaoks ei ole koma vajalik
# seega eraldi käsitlus
insert_statement += f"\n({','.join(data_from_csv[-1])});"
print(insert_statement)


# oodatav tulemmus
# INSERT INTO customers
# (CustomerID,CustomerName,Industry,Country,RegionID)
# VALUES
# (C001,Alice Ltd,Retail,USA,R01),
# (C002,Bob Inc,Wholesale,Canada,R02),
# (C003,Charlie LLC,E-commerce,USA,R01),
# (C004,Delta Group,Retail,UK,R03);

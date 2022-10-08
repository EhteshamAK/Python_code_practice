raw_data = ["Ehtesham Ali Khan", "Muhammad Ismail", "Syed Ali Abbas", "Saqib Mehmood", 39000, 85000, 37500, 34500]
name = []
age = []

for x in raw_data:
    if type(x) == int:
        age.append(x)
    else:
        name.append(x)

print(name)
print(age)


country = input("Please enter your country name ")
# capitalize every word of the input
countre = country.title()
if len(country) == 0:
 print("Write some thing if ")
else:
    if countre == "Pakistan":
        print("Oh my God! you are from my homeland")
    elif countre == "United States":
        print("Oh technological advance country")
    elif countre == "Saudia Arabia":
        print("Land of holy Prophets and the birth place of Islam ")
    else:
        print("You write the name of country is" + country)

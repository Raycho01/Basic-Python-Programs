

dict_1 = {"Name" : "Raycho", "Age" : 19, "Gender" : "Male"}
print(dict_1)
dict_1["Love"] = {"Nya" : "Female", "Mom" : "Female", "Me" : "Male"}
print(dict_1)

print("Only the values: " +str(dict_1.values()))

print("Name is: " +dict_1["Name"])

dict_1["Love"].pop("Me")
print(dict_1)

dict_1["Love"]["Himself"] = "Male"
print(dict_1)

print(dict_1["Love"]["Nya"])


def firstAttempt(brand1, brand2, brand3):
    print(brand3)

firstAttempt(brand1 = "Apple", brand2 = "Huawei", brand3 = "Samsung")

def secondAttempt(**dictionary):
    print(("The model is: " +dictionary["model"]))

secondAttempt(brand = "Toyota", year = 2000, model = "Celica")

def sortingMethod(*lang):
    for cell in lang:
        if cell == "Java":
            for character in cell:
                print(character)

sortingMethod("C++", "JavaScript", "Java", "Python")

def taxCalculation(salary, tax = 0.22):
    helping_var = salary * tax
    return salary - helping_var

print(taxCalculation(5000, 0.2))
print(taxCalculation(5000, 0.22))
print(taxCalculation(1000))
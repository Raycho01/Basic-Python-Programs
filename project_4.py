

months = {"January" : 1, "February" : 2, "March" : 3}

key_list = list(months.keys())

print("Hello, do you want to get month or number: ")
answer = input()

if answer == "month":
    print("Enter number")
    second_answer = input()
    second_answer = int(second_answer)
    print(key_list[second_answer - 1])

elif answer == "number":
    print("Enter month")
    second_answer = input()
    print(months.get(second_answer))

else:
    print("Error")
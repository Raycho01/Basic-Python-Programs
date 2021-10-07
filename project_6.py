

businesses_list = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10 , 15001]
taxes_sum = 0

for cell in businesses_list:
    if cell >= 1 and cell <= 2000:
        tax = cell * 5/100
    elif cell >= 2001 and cell <= 5000:
        tax = cell * 10/100
    elif cell >= 5001 and cell <= 15000:
        tax = cell * 15/100
    else:
        tax = cell * 17/100

    net_income = cell - tax
    after_healthcare = net_income * 98/100
    print("The income after the taxes and healthcare for starting income " +str(cell) +" is " +str(after_healthcare))
    taxes_sum = taxes_sum + tax

print("The taxes for all business are " +str(taxes_sum))
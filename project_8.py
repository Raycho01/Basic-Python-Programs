

class Car():


    def __init__(self, arr):
        self.arr = arr


    def insurance_price(self):
        if self.arr[0] >= 2010 and self.arr[0] <= 2020 and self.arr[1] >= 6000 and self.arr[1] <= 17000:
            insurance = self.arr[1] * 5/100
        else:
            insurance = self.arr[1] * 7/100

        print("The insurance is %s" %insurance)
        return insurance


    def car_data(self):
        print("The car model is %s, the year is %s, the price is %s" %(self.arr[2], self.arr[0], self.arr[1]))


    def door_status(self):
        if self.arr[3] == True:
            print("The doors are closed")
        else:
            print("The doors are not closed")



ford_focus = Car([2005, 2000, "ford_focus", True])
audi_a3 = Car([2011, 15000, "audi_a3", False ])

ford_focus.car_data()
ford_focus.insurance_price()
ford_focus.door_status()
print("\n")
audi_a3.car_data()
audi_a3.insurance_price()
audi_a3.door_status()
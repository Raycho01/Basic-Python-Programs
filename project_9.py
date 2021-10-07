

class Employee():


    def __init__(self, years_exp, position_name, employee_name):
        self.years_exp = years_exp
        self.position_name = position_name
        self. employee_name = employee_name


    def calculate_salary(self):
        salary = 2500
        if self.years_exp >= 0 and self.years_exp <= 2:
            salary += 1500
        elif self.years_exp > 2 and self.years_exp <= 5:
            salary += 2500
        elif self.years_exp > 5:
            salary += 3500
        else:
            print("Invalid information.")
        print("The salary for %s is %s" %(self.employee_name, salary))
        return salary


    def candidate_for_bonus(self, salary):
        if "front-end" in self.position_name and self.years_exp <= 2:
            salary = salary + 1/10*salary
        elif self.years_exp > 2:
            salary = salary + 2/10*salary
        else:
            print("%s can't get bonus." %self.employee_name)
        print("The salary with the bonus for %s is %s" %(self.employee_name, salary))
        return salary


class Programmer (Employee):

    def __init__(self, years_exp, position_name, employee_name, years_old):
        self.years_exp = years_exp
        self. position_name = position_name
        self.employee_name = employee_name
        self.years_old = years_old
        super().__init__(years_exp, position_name, employee_name)


    def programmer_info(self):
        print("The name of the programmer is %s, he is %s years old and his position is %s." %(self.employee_name, self.years_old, self.position_name))


employee1 = Employee(1, "front-end", "Joseph")
employee2 = Employee(6, "senior_devops", "Dan")
employee3 = Programmer(3, "back-end", "Rick", 28)
print("\n")
emp1_salary = employee1.calculate_salary()
employee1.candidate_for_bonus(emp1_salary)
print("\n")
emp2_salary = employee2.calculate_salary()
employee2.candidate_for_bonus(emp2_salary)
print("\n")
employee3.programmer_info()
emp3_salary = employee3.calculate_salary()
employee3.candidate_for_bonus(emp3_salary)
print("\n")

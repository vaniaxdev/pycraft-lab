# inheritance

# employee -- name, id, department, gender
# salaried -- + salary, tenure
# casual -- rates
class Employee:
    def __init__(self, name:str, id_no:str, department:str, gender:str):
        self.full_names = name
        self.identity_no = id_no
        self.department = department
        self.gender = gender

    def print_details(self):
        print(self.full_names)
        print(self.identity_no)
        print(self.department)
        print(self.gender)
        print("-----------")
    def print_namr(self):
        print(f"Name is {self.full_names}")

class SalariedEmployee(Employee):
    def __init__(self, name:str, id_no:str, department:str, gender:str, salary:int, tenure:int):
        super().__init__(name, id_no, department, gender)
        self.salary = salary
        self.tenure = tenure

class CasualWorkers(Employee):
    def __init__(self, name:str, id_no:str, department:str, gender:str, rate: float):
      super().__init__(name, id_no, department, gender)
      self.rate = rate

    def calc_wage(self, hours: float):
        return hours * self.rate


s1 = SalariedEmployee("Vania Nam", "22233344", "HR", "F", 98_000, 57)
c1 = CasualWorkers("James za", "44455566", "Sales", "M", 56)

s1.print_details()
c1.print_details()
print(c1.calc_wage(19))

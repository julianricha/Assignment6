#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def calculate_salary(self):
        raise NotImplementedError("Not Implemented Error")


class HourlyEmployee(Employee):
    def __init__(self, name, position, hourly_rate, hours_worked):
        super().__init__(name, position)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class SalariedEmployee(Employee):
    def __init__(self, name, position, annual_salary):
        super().__init__(name, position)
        self.annual_salary = annual_salary
        
    def calculate_salary(self):
        return self.annual_salary / 12  

class CommissionEmployee(Employee):
    def __init__(self, name, position, sales_amount, commission_rate):
        super().__init__(name, position)
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate
        
    def calculate_salary(self):
        return self.sales_amount * self.commission_rate


def process_salaries(employees):
    for employee in employees:
        print(f"{employee.name} ({employee.position}): ${employee.calculate_salary()}")


employees = [
    HourlyEmployee("Julian", "Advertising", 25, 160),
    SalariedEmployee("Bader", "IT", 60000),
    CommissionEmployee("Bob", "Sales", 500000, 0.04)
]


process_salaries(employees)


# In[ ]:





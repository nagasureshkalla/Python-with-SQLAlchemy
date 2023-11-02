
from Employee import Employee

class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, ssn, weekly_salary):
        super().__init__(first_name, last_name, ssn)  # Initialize inherited attributes
        self._weekly_salary = weekly_salary  # Initialize the weekly salary attribute

    @property
    def weekly_salary(self):
        return self._weekly_salary  # Getter method for weekly salary

    @weekly_salary.setter
    def weekly_salary(self, value):
        if value >= 0:
            self._weekly_salary = value  # Setter method for weekly salary with non-negative validation
        else:
            raise ValueError("Weekly salary must be non-negative")  # Raise an exception for negative salary

    def earnings(self):
        return self._weekly_salary  # Calculate earnings (weekly salary)

    def __str__(self):
        return f"SalariedEmployee: {super().__str__()}\nsalary: {self._weekly_salary:.2f}"

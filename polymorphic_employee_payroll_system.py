
"""
HW 3
Problem 2
Author : Kalla Naga Suresh

"""

from Employee import Employee
from SalariedEmployee import SalariedEmployee
from CommissionEmployee import CommissionEmployee
from HourlyEmployee import HourlyEmployee



if __name__ == '__main__':
    try:
        e3 = SalariedEmployee("Taylor", "Swift", "123-00-0005", 30000000)
        e1 = HourlyEmployee("Donald", "Trump", "123-00-0001", 100, 20)
        e2 = CommissionEmployee("Elon", "Musk", "123-00-0003", 6, 10000000)

        employee_list = [e1, e2, e3]

        for employee in employee_list:
            print(employee)
            print(f'earnings: ${employee.earnings():,.2f}')
            print()

    except ValueError as e:
        print(e)


    print("__________________Exception____________________")

    try:
        # Creating a SalariedEmployee with a negative weekly salary
        salaried_employee = SalariedEmployee("Alice", "Smith", "987-65-4321", -1000.00)
        salaried_employee.weekly_salary = -1000.00  # updating value
        print(salaried_employee)
    except ValueError as e:
        print(e)

    try:
        # Creating an HourlyEmployee with invalid hours (outside the range 0-168)
        hourly_employee = HourlyEmployee("Bob", "Johnson", "234-56-7890", 180, 15.00)
        hourly_employee.hours = 180
        print(hourly_employee)
    except ValueError as e:
        print(e)

    try:
        # Creating a CommissionEmployee with an invalid commission rate (16%)
        commission_employee = CommissionEmployee("Charlie", "Brown", "345-67-8901", 16, 2000.00)
        commission_employee.commission_rate=16
        print(commission_employee)
    except ValueError as e:
        print(e)


    try:
        # Attempt to create an Employee object (abstract class)
        employee = Employee("John", "Doe", "123-45-6789")
    except TypeError as e:
        print(e)

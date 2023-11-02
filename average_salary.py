"""

HW : 4
Problem : 4
Author : Kalla Naga Suresh

"""

import os
from large_dataset import generate_file

if __name__=='__main__':
    # Create the data file if does not exists
    if not os.path.exists("Salary.txt"):
        generate_file()

# Read and process the data file to calculate average salaries
    faculty_data = {
        "assistant": [],
        "associate": [],
        "full": [],
    }

    with open("Salary.txt", "r") as file:
        for line in file:
            data = line.split()
            rank, salary = data[2], float(data[3])
            faculty_data[rank].append(salary)

    # Calculate and display the average salaries
    for rank, salaries in faculty_data.items():
        count = len(salaries)
        total_salary = sum(salaries)
        if count > 0:
            average_salary = total_salary / count
            print(f"{rank.capitalize()} ({count}): ${average_salary:.2f}")

    # Calculate and display the average salary for all faculty
    all_salaries = [salary for salaries in faculty_data.values() for salary in salaries]
    count = len(all_salaries)
    total_salary = sum(all_salaries)
    average_salary = total_salary / count
    print(f"All Faculty ({count}): ${average_salary:.2f}")
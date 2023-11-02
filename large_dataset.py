"""

HW : 4
Problem : 3
Author : Kalla Naga Suresh

"""

import random

# Function to generate a random salary based on rank
def generate_salary(rank):
    if rank == "assistant":
        return round(random.uniform(50000, 80000), 2)
    elif rank == "associate":
        return round(random.uniform(60000, 110000), 2)
    elif rank == "full":
        return round(random.uniform(75000, 130000), 2)

def generate_file():
    with open("Salary.txt", "w") as file:
        for i in range(1, 1001):
            first_name = f"FirstName{i}"
            last_name = f"LastName{i}"
            rank = random.choice(["assistant", "associate", "full"])
            salary = generate_salary(rank)
            line = f"{first_name} {last_name} {rank} {salary:.2f}\n"
            file.write(line)



if __name__=='__main__':
    generate_file()


'''
HW 5
Problem 2
Author : Kalla Naga Suresh

'''
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from Creating_City_Population_Database_using_ORM import City

# Create the SQLite database engine
engine = create_engine('sqlite:///city.db')
Session = sessionmaker(bind=engine)
session = Session()

def formatted_seperator(st):
    return "{:,}".format(st)
def printCities(cities):
    print(f"{'City':<15} {'Population':<20}")
    for city in cities:
        formatted_value = formatted_seperator(city.population)
        print(f"{city.name:<15} {formatted_value:<20}")
def display_cities_sorted_by_population(ascending=True):
    cities = session.query(City).order_by(City.population.asc() if ascending else City.population.desc()).all()
    printCities(cities)

def display_cities_sorted_by_name():
    cities = session.query(City).order_by(City.name).all()
    print("Cities sorted by name:")
    printCities(cities)

def display_total_population():
    total_population = session.query(func.sum(City.population)).scalar()
    print(f"Total population: "+formatted_seperator(total_population))

def display_average_population():
    average_population = session.query(func.avg(City.population)).scalar()
    print(f"Total population: "+formatted_seperator(int(average_population)))

def display_highest_population_city():
    city = session.query(City).order_by(City.population.desc()).first()
    print(f"{city.name} has the highest population   "+formatted_seperator(city.population))

def display_lowest_population_city():
    city = session.query(City).order_by(City.population).first()
    print(f"{city.name} has the lowest population:   "+formatted_seperator(city.population))

def add_new_city_population(name, population):
    new_city = City(name=name, population=population)
    session.add(new_city)
    session.commit()
    print(f"Added new city: {name} - "+formatted_seperator(population))

def delete_city_population(name):
    city = session.query(City).filter(City.name == name).first()
    if city:
        session.delete(city)
        session.commit()
        print(f"Deleted city: {name}")
    else:
        print(f"City '{name}' not found in the database.")

# Menu loop
while True:

    # Open and read a text file
    file_path = 'menu.txt'

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print("The Menu file was not found.")

    choice = input("Please select (1 - 10): ")

    if choice == '1':
        print("Cities Sorted by population in Ascending Order")
        print('-'*40)
        display_cities_sorted_by_population()
    elif choice == '2':
        print("Cities Sorted by population in Descending Order")
        print('-' * 40)
        display_cities_sorted_by_population(ascending=False)
    elif choice == '3':
        display_cities_sorted_by_name()
    elif choice == '4':
        display_total_population()
    elif choice == '5':
        display_average_population()
    elif choice == '6':
        display_highest_population_city()
    elif choice == '7':
        display_lowest_population_city()
    elif choice == '8':
        display_cities_sorted_by_population()
        name = input("please enter the city: ")
        try:
            population = int(input("please enter the population: "))
            add_new_city_population(name, population)
            display_cities_sorted_by_population()
        except:
            print("Please Retry by entering valid population to add")


    elif choice == '9':
        display_cities_sorted_by_population()
        name = input("please enter the city to delete: ")
        delete_city_population(name)
        display_cities_sorted_by_population()
    elif choice == '10':
        y=input("Do you want to Exit the System?Enter Y to confirm:")
        if y== 'y' or y== 'Y':
            print("Exit the System...")
            break
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")

# Close the session
session.close()




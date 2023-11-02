
'''

HW 5
Problem 1
Author : Kalla Naga Suresh

'''


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the SQLite database
engine = create_engine('sqlite:///city.db', echo=True)
Base = declarative_base()



# Define the City table
class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    population = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Establish a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

city_data = [
    {"name": "New York", "population": 18593220},
    {"name": "Cairo", "population": 18771769},
    {"name": "Osaka", "population": 20237645},
    {"name": "Beijing", "population": 20383994},
    {"name": "Mexico City", "population": 20998543},
    {"name": "Mumbai", "population": 21042538},
    {"name": "Sao Paulo", "population": 21066245},
    {"name": "Shanghai", "population": 23740778},
    {"name": "Delhi", "population": 25703168},
    {"name": "Tokyo", "population": 38001000}
]

# Delete all records from the City table, making empty
session.query(City).delete()
session.commit()



# Insert data into the City table
for city_info in city_data:
    city = City(name=city_info["name"], population=city_info["population"])
    session.add(city)
# Commit the changes to the database
session.commit()



# Query all records from the City table
cities = session.query(City).all()
print("-" * 40)
print(f"{'City':<15} {'Population':<20}")
print("-" * 40)
for city in cities:
    print(f"{city.name:<15} {city.population:<20}")
print("-" * 40)


# Close the session
session.close()
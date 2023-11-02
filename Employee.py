
from abc import ABC, abstractmethod  # Import abstract base class module

class Employee(ABC):  # Abstract base class Employee
    def __init__(self, first_name, last_name, ssn):
        self._first_name = first_name  # Initialize the first name attribute
        self._last_name = last_name    # Initialize the last name attribute
        self._ssn = ssn                # Initialize the Social Security Number attribute


    @property
    def first_name(self):
        return self._first_name  # Getter method for the first name

    @property
    def last_name(self):
        return self._last_name  # Getter method for the last name

    @property
    def ssn(self):
        return self._ssn  # Getter method for the Social Security Number

    @abstractmethod
    def earnings(self):
        pass  # Abstract method, to be implemented by subclasses

    def __str__(self):
        return f"{self._first_name} {self._last_name} \nsocial security number: {self._ssn}"


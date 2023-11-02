from Employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, ssn, hours, hourly_rate):
        super().__init__(first_name, last_name, ssn)  # Initialize inherited attributes
        self._hours = hours         # Initialize the hours worked attribute
        self._hourly_rate = hourly_rate  # Initialize the hourly rate attribute

    @property
    def hours(self):
        return self._hours  # Getter method for hours worked

    @hours.setter
    def hours(self, value):
        if 0 <= value <= 168:
            self._hours = value  # Setter method for hours worked with validation
        else:
            raise ValueError("Hours must be in the range 0-168")  # Raise an exception for invalid hours

    @property
    def hourly_rate(self):
        return self._hourly_rate  # Getter method for hourly rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value >= 0:
            self._hourly_rate = value  # Setter method for hourly rate with non-negative validation
        else:
            raise ValueError("Hourly rate must be non-negative")  # Raise an exception for negative hourly rate

    def earnings(self):
        if self._hours <= 40:
            return self._hours * self._hourly_rate  # Calculate earnings for regular hours
        else:
            regular_pay = 40 * self._hourly_rate
            overtime_pay = (self._hours - 40) * (self._hourly_rate * 1.5)
            return regular_pay + overtime_pay  # Calculate earnings for overtime hours

    def __str__(self):
        return f"HourlyEmployee: {super().__str__()}\nhours worked: {self._hours}\nhourly rate: {self._hourly_rate:.2f}"


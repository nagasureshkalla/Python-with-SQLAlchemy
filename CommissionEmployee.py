from Employee import Employee


class CommissionEmployee(Employee):
    def __init__(self, first_name, last_name, ssn, commission_rate, weekly_sales):
        super().__init__(first_name, last_name, ssn)  # Initialize inherited attributes
        self._commission_rate = commission_rate  # Initialize the commission rate attribute
        self._weekly_sales = weekly_sales        # Initialize the weekly sales attribute

    @property
    def commission_rate(self):
        return self._commission_rate  # Getter method for commission rate

    @commission_rate.setter
    def commission_rate(self, value):
        if 3.0 <= value <= 6.0:
            self._commission_rate = value  # Setter method for commission rate with validation
        else:
            raise ValueError("Commission rate must be greater than 3.0 and less than 6.0")  # Raise an exception for invalid commission rate

    @property
    def weekly_sales(self):
        return self._weekly_sales  # Getter method for weekly sales

    @weekly_sales.setter
    def weekly_sales(self, value):
        if value >= 0:
            self._weekly_sales = value  # Setter method for weekly sales with non-negative validation
        else:
            raise ValueError("Weekly sales must be non-negative")  # Raise an exception for negative weekly sales

    def earnings(self):
        return self._commission_rate * self._weekly_sales / 100  # Calculate earnings based on commission rate and sales

    def __str__(self):
        return f"CommissionEmployee: {super().__str__()}\ncommission Rate: {self._commission_rate :.2f}%\n" \
               f"gross sales: ${self._weekly_sales:.2f}"

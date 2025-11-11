class Bill:
    """Class to represent a bill among flatmates.
    Attributes:
        amount (float): The total amount of the bill.
        period (str): The period the bill covers (e.g., "March 2021").
    """

    def __init__(self):
        while True:
            try:
                self.amount = float(input("Enter the total bill amount: $"))
                if self.amount < 0:
                    raise ValueError("Bill amount cannot be negative.")
                break
            except ValueError as e:
                print(f'Invalid input: {e}. Please enter a valid number.')
        self.period = input("Enter the bill period (e.g., March 2021): ")
        print(f"Bill of ${self.amount} for the period {self.period} created.")

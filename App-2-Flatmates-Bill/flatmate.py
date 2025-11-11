class Flatmate:
    """Class to represent a flatmate.
    Attributes:
        name (str): The name of the flatmate.
        days_in_house (int): The number of days the flatmate stayed in the house during the bill period.
    """

    def __init__(self):
        self.name = str(input("Enter the name of the flatmate: "))
        while True:
            try:
                self.days_in_house = int(input(
                    f"Enter the number of days {self.name} stayed in the house during the bill period: "))
                if self.days_in_house < 0:
                    raise ValueError("Days cannot be negative.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid integer.")

    def pays(self, bill, flatmates):
        """Calculate the amount this flatmate has to pay.
        Args:
            bill (Bill): The bill to be paid.
            flatmates (list[Flatmate]): All flatmates sharing the bill.
        Returns:
            float: The amount this flatmate has to pay.
        """
        total_days = sum(f.days_in_house for f in flatmates)
        if total_days == 0:
            return 0.0
        ratio = self.days_in_house / total_days
        return round(bill.amount * ratio, 2)

from fpdf import FPDF
import os

from bill import Bill
from flatmate import Flatmate
from pdf_report import PdfReport


def no_of_flatmates():
    flatmates = []

    while True:
        n = input("Enter number of flatmates: ")
        if not n.isdigit():
            print("Please enter a valid number.")
            continue
        n = int(n)

        if n < 2:
            print("At least two flatmates are required.")
            continue

        for _ in range(n):
            flatmate = Flatmate()
            print(flatmate)
            flatmates.append(flatmate)

        return flatmates


bill = Bill()
total_flatmates = no_of_flatmates()
print(f"\nBill details 💥💥: \n{bill}")
print(f"\nFlatmates details 💥💥: \n{total_flatmates}")
# print("\nAll flatmates:")
# for f in total_flatmates:
#     print(
#         f"  {f.name}: {f.days_in_house} days, pays ${f.pays(bill, total_flatmates)}")

report = PdfReport(bill)
report.generate(total_flatmates, bill)
print(f"\nPDF report generated: pdf/{report.filename}")

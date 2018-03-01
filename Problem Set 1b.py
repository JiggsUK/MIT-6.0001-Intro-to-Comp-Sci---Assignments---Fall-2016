#!/usr/bin/env python
"""
@author: JiggsUK

Program that calculates how many months it will take to save for a deposit
given the users annual salary, proportion of their salary they wish to save and
the cost of the house they wish to buy.
It is assumed a deposit will be 25% of the cost of the house and an annual
interest rate on savings of 4%. A raise will be received every 6 months of 7%.
"""

annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("What portion of your monthly salary would you "
                            "like to save? "))
total_cost = float(input("How much is your dream house? "))
semi_annual_raise = float(input("What is your 6 month raise?"))

portion_down_payment = int(total_cost * 0.25)
r = 0.04

current_savings = 0
month = 0

while current_savings < portion_down_payment:
    month = month + 1
    monthly_saving = (annual_salary / 12) * portion_saved
    current_savings = current_savings + (monthly_saving +
                                         ((current_savings * r) / 12))
    if month % 6 == 0:
        annual_salary = annual_salary * (semi_annual_raise + 1)

print("It will take " + str(month) +
      " months to save for a house. With a deposit of: £"
      + str(portion_down_payment))

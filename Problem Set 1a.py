#!/usr/bin/env python
"""
@author: JiggsUK

Program that calculates how many months it will take to save for a deposit
given the users annual salary, proportion of their salary they wish to save and
the cost of the house they wish to buy.
It is assumed a deposit will be 25% of the cost of the house and an annual
interest rate on savings of 4%
"""

annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("What portion of your monthly salary would you "
                            "like to save? "))
total_cost = float(input("How much is your dream house? "))

portion_down_payment = int(total_cost * 0.25)
r = 0.04

current_savings = 0

month = 0

monthly_saving = (annual_salary / 12) * portion_saved

while current_savings < portion_down_payment:
    month = month + 1
    current_savings = current_savings + (
                monthly_saving + ((current_savings * r) / 12))

print("It will take " + str(month) +
      " months to save for a house. With a deposit of: £" +
      str(portion_down_payment))

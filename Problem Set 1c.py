#!/usr/bin/env python
"""
@author: JiggsUK

Program to calculate the best % rate of savings to achieve the target savings
amount (to within £100) within a given time frame. An annual rate of return on
savings of 4% is assumed.
"""

starting_salary = float(input("What is your annual salary? "))
total_cost = float(input("How much is your dream house? "))
semi_annual_raise = float(input("What is your 6 month raise?"))
portion_down_payment = int(total_cost * 0.25)
r = 0.04

epsilon = 100  # how close to the target we need to be
number_of_bisection_guesses = 0
high = 100  # percent
low = 0
guess = high # start the guess at the top and bi-sectionally search down
bisection_loop = True

while bisection_loop is True:  # loop allows calculation to run each guess
    number_of_bisection_guesses += 1
    annual_salary = starting_salary
    percentage_saved = guess
    monthly_saving = (annual_salary / 12) * percentage_saved

    current_savings = 0
    months = 0

    while months <= 36:  # only interested in if it can be achieved in 3 years
        current_savings += monthly_saving + ((current_savings * r) / 12)
        months += 1
        if months % 6 == 0:  # add on the raise every 6 months
            annual_salary += annual_salary * semi_annual_raise
            monthly_saving = (annual_salary / 12) * percentage_saved

    if abs(current_savings - portion_down_payment) <= epsilon:
        print("After 36 months, your total savings will be "
              "£{:0,.0f}".format(current_savings))
        print("The optimum savings rate for that amount is: "
              "{:,.2f}%".format(percentage_saved))
        print("The search took " + str(
            number_of_bisection_guesses) + " steps to complete.")
        break
        # break out of the loop as we are within £100 of our target and can
        # stop

    if current_savings > portion_down_payment:
        # if guess is wrong, edit the high or low limit and run the code again
        high = guess
    else:
        low = guess
    guess = (high + low) / 2.0

    if high <= low:
        """
        if the high guess is less than or equal to the low guess, it is not 
        going to get to our target in 3 years. This tells the user that. 
        """
        print("It is not possible to save enough within 36 months.")
        print("At a best savings rate of " + str(
            percentage_saved) + "%, " + "you will have saved £{:0,.0f}".format(
            current_savings))
        loop = False

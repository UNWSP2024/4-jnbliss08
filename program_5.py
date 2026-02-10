# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the
# month and keep a running total. (Enter 0 to exit the loop)
# When the loop finishes, the program should display the amount that the
# user is over or under budget.

budget = float(input('what is your budget?'))

while budget <= 0:
    print('ERROR please enter a number greater than 0')
    budget = float(input('what is your budget?'))

total_expenses = 0

while True:
    expenses = float(input('enter an expense (enter 0 to finish): '))
    while expenses < 0:
        float(input('ERROR please enter a number greater than 0'))
    if expenses == 0:
        break
    total_expenses += expenses

difference = budget - total_expenses

if difference > 0:
    print(f'you are ${difference:.2f} under budget')
elif difference < 0:
    print(f'you are ${-difference:.2f} over budget')
else:
    print('you are on budget')
# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average
# rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall per month for the entire period.

total_rainfall = 0

number_of_years = int(input('How many years do you want to measure? '))
while number_of_years < 1:
    print('ERROR please enter a number greater than 1')
    number_of_years = int(input('How many years do you want to measure? '))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

total_months = 0

year = 1

while year <= number_of_years:
    for month in months:
        rainfall = float(input(f'how much rainfall in {month}?' ))
        while rainfall < 0:
            print('ERROR please enter positive number')
            rainfall = float(input(f'how much rainfall in {month}?'))
        total_rainfall += rainfall
        total_months += 1
    year += 1

average_rainfall = total_rainfall / total_months

print(f'in {total_months} months, there was {total_rainfall:.2f} inches of rainfall')
print(f'the average rainfall over {total_months} months was {average_rainfall:.2f} inches')

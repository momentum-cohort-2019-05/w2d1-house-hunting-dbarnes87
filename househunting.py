annual_salary = int(input("What is your annual salary?"))
portion_saved = float(input("What percentage of your salary will you save each month in a decical?"))
total_cost = float(input("What is the cost of your dream home?"))

done = False
monthly_salary = annual_salary / 12
current_savings = 0
r = 0.04
down_payment = .25 * total_cost
monthly_savings = ((annual_salary/12)*portion_saved) + current_savings*r/12

months = 0

while (current_savings <= down_payment):
    monthly_savings = ((annual_salary/12)*portion_saved) + current_savings*r/12
    current_savings = current_savings + monthly_savings
    months = months + 1
print("It will take {} months to reach your goal." .format(months))





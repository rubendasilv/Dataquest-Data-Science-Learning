import csv
import random

opened_file = open("expenses.csv")
read_file = csv.reader(opened_file)
expenses_data = list(read_file)[1:]
opened_file.close()
categories = {
    "groceries": [],
    "transportation": [],
    "utilities": []
}

for row in expenses_data:
    for i, category in enumerate(categories, start=1):
        categories[category].append(int(row[i]))

ranges = {}
for category, values in categories.items():
    ranges[category + '_low'] = min(values)
    ranges[category + '_high'] = max(values)

groceries_budget = 85
transportation_budget = 58
utilities_budget = 45

weekly_budget = groceries_budget + transportation_budget + utilities_budget

total_spent = 0
print("--- Simulated 12-Week Run ---")
for week in range(1, 13):
    groceries_cost = random.randint(ranges['groceries_low'], ranges['groceries_high'])
    transportation_cost = random.randint(ranges['transportation_low'], ranges['transportation_high'])
    utilities_cost = random.randint(ranges['utilities_low'], ranges['utilities_high'])
    week_total = groceries_cost + transportation_cost + utilities_cost
    total_spent += week_total

    week_label = "Week " + str(week)
    spent_label = "spent $" + str(week_total)

    if week_total > weekly_budget:
        status = "OVER budget by $" + str(week_total - weekly_budget)
    elif week_total < weekly_budget:
        status = "under budget by $" + str(weekly_budget - week_total)
    else:
        status = "exactly on budget"

    print(week_label + ": " + spent_label + " - " + status)

total_budgeted = weekly_budget * 12
difference = total_budgeted - total_spent
print("--- Final Summary ---",
      total_spent,
      total_budgeted)

if difference > 0:
    print("you've come out ahead by ", str(difference))
elif difference < 0:
    print("you've come out behind by ", str(0 - difference))
else:
    print("youve come out exactly even")

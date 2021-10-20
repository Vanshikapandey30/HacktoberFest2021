## This is a simple program to calculate your daily/weekly/monthly savings

## Hope it is useful 


print("Your Savings Calculator")
hours_in_a_day= int(input("How many hours you work in a day?"))
user_input=int(input("How much do you earn per hour?"))
daily_savings= user_input * hours_in_a_day
print("This is your daily savings: ", daily_savings)

days_in_a_week= int(input("How many days you work in a week?"))
weekly_savings= daily_savings * days_in_a_week
print("This is your weekly savings: ", weekly_savings)

monthly_savings= weekly_savings * 4
print("This is your monthly savings: ", monthly_savings)
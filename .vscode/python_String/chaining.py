from datetime import date

str='''|Name|
You are selected.
|Date|'''

name = input("Enter your name: ")

# automatically use today's date instead of asking the user
# user can still override by uncommenting the next line
# date_str = input("Enter the date (dd-mm-yyyy): ")

today = date.today()
date_str = today.strftime("%d-%m-%Y")

print(str.replace("|Name|", name).replace("|Date|", date_str))
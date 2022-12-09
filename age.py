#get current date in year-month-day format
from datetime import date

current_date = date.today()
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day	

month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 
			  10: 31, 11: 30, 12: 31}

keys = month_days.keys()

def get_birthday():
	birthday_entry = input("Enter birthday YYYY-MM-DD: ")
	b_year, b_month, b_day = map(int, birthday_entry.split('-'))

	if b_year in range(1900,date.today().year):

		if b_month in keys:

			if b_day in range(1,month_days[b_month]+1):

				print('B-date is valid')
			else:
				print('B-day is not valid for this month, please give another birthday')
				birthday_entry = get_birthday()
		else:
			print('B-month is not valid, please give another birthday')
			birthday_entry = get_birthday()
	else:
		print('B-year is not valid, please give another birthday')
		birthday_entry = get_birthday()

	return b_year, b_month, b_day

year, month, day = get_birthday()

#calculate age 

def age():
	if current_month > month:
		my_age = current_year - year
	elif current_month < month:
		my_age = current_year - year - 1
	else:
		if current_day >= day: 
			my_age = current_year - year
		elif current_day < day:
			my_age = current_year - year - 1

	return my_age

print("You are ", age(), "years old")	

# difference when in the same year:
# days left in the current month + full months + days until the wanted date
def calc_difference(start, end):
	middle = 0 

	for i in range(start[0] +1, end[0]):
		middle += month_days[i]

	if start[0] != end[0]:
		diff = (month_days[start[0]] - start[1]) + middle + end[1] 
	else:
		diff = end[1] - start[1]

	return diff 
		

def next_bday():
	real_age = age()
	math_age = current_year - year 

	if real_age < math_age :
		# means my bday for the current year hasn't come yet 
		days_left = calc_difference((current_month, current_day), (month, day))

	elif real_age == math_age :
		# means my bday has passed, so the next is in 365 - the days after my bday
		days_left = 365 - calc_difference((month,day), (current_month,current_day))
		
	return days_left

print('Your next bday is in: ', next_bday(), 'days')











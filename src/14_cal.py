"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


curr_month = datetime.today().month
curr_year = datetime.today().year


def cal_func(month=curr_month, year=curr_year):
    text_cal = calendar.TextCalendar()
    text_cal.prmonth(year, month)


args = list(sys.argv)

if len(args) == 3:
    cal_func(int(args[1]), int(args[2]))

elif len(args) == 2:
    cal_func(int(args[1]))

else:
    cal_func()
    print('\n Input "14_cal.py month [year]"  to see calendar \n')

#!/usr/bin/python3

import sys
import calendar

class CustomHTMLCal(calendar.HTMLCalendar):
    '''
    cssclasses = [style + " text-nowrap" for style in
                  calendar.HTMLCalendar.cssclasses]
    '''
    cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat blue", "sun red"]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"

tc = CustomHTMLCal(firstweekday=6)

with open('output.html', 'w') as out_f:
    out_f.write(tc.formatmonth(2019, 3))

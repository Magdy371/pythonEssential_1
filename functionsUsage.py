#function_1 leap year list
def leap_year_list(lst):
    ly_result = []
    last_stand_years = []
    for ele in lst:
        if ele % 4 !=0:
            ele = False
        elif ele % 100 !=0:
            last_stand_years.append(ele)
            ele = True
        elif ele % 400 !=0:
            ele = False
        else:
            last_stand_years.append(ele)
            ele =  True
        ly_result.append(ele)
    return ly_result , last_stand_years
lst_1 = [2000, 2004, 2008, 2012, 2016, 2021]
ly_result = leap_year_list(lst_1)
print(leap_year_list(lst_1))

def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and leap_year_list(lst_1):
        res = 29
    return res
print(days_in_month(2021,2))

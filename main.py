from Day01.solution import day01
from Day02.solution import day02

option = input('Which day would you like to run?\n')

days = {
        '01': day01,
        '02': day02,
    }

def notFound():
    print('Day not found, please try again.\n')

def switcher(x):
    return days.get(x, notFound)

switcher(option)()


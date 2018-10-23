day = 2

switcher = {
    0: 'sunday',
    1: 'monday',
    2: 'tuesday'
}

def get_sunday():
    return 'sunday'
def get_monday():
    return 'monday'
def get_tuesday():
    return 'tuesday'
day_name = switcher.get(day, 'Unkown')
print(day_name)
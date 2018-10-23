day = 8

def get_sunday():
    return 'sunday'
def get_monday():
    return 'monday'
def get_tuesday():
    return 'tuesday'
def get_default():
    return 'Unkown'

switcher = {
    0: get_sunday,
    1: get_monday,
    2: get_tuesday
}

day_name = switcher.get(day, get_default)()
print(day_name)
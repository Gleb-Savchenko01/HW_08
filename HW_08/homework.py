from datetime import datetime, timedelta
from collections import defaultdict
from pprint import pprint

def get_next_week_start(d: datetime):
    diff_days = 7 - d.weekday()
    return d + timedelta(days=diff_days)

def prepare_birthday(text: str):
    bd = datetime.strptime(text, '%d, %m, %Y')
    return bd.replace(year=datetime.now().year).date()

def get_birthdays_per_week(users):
    birthday = defaultdict(list)

    today = datetime.now().date()

    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)

    happy_users = [user for user in users
                   if start_period <= prepare_birthday(user['birthday']) <= end_period]

    for user in happy_users:
        current_bd = date = prepare_birthday((user['birthday']))
        if current_bd.weekday() in (5,6):
            birthday['Monday'].append(user['name'])
        else:
            birthday[current_bd.strftime('%A')].append(user['name']) 

    for day, names in birthday.items():
        print(f"{day}: {', '.join(names)}")

if __name__ == "__main__":
    users = [{"name": "Anna", "birthday": "02, 12, 1998"},
             {"name": "Gleb", "birthday": "15, 04, 2000"},
             {"name": "Maks", "birthday": "01, 02, 2002"},
             {"name": "Igor", "birthday": "08, 08, 1975"},
             {"name": "Ira", "birthday": "27, 11, 1975"},
             {"name": "Alla", "birthday": "05, 06, 1973"},
             {"name": "Kolya", "birthday": "19, 11, 1973"},
             {"name": "Vanya", "birthday": "6, 04, 1973"}]
    
    get_birthdays_per_week(users)
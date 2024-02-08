from collections import namedtuple
import pickle
from datetime import datetime
import csv
def qwe():
    Country = namedtuple('Country', 'name,capital,president,language,currency')
    iceland = Country('Iceland', 'Reykjavik', 'Gwydni Jouhannesson', 'Icelandic', 'Iceland krona')
    _, _, *data = iceland
    return data

def add_fields():
    Game = namedtuple('Game', 'name developer publisher')
    ExtendedGame = namedtuple("ExtendedGame", [*Game._fields, "release_date", "price"])
    return True

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
def asd():
    with open("namedtuple_unit/data.pkl", "rb") as input_file:
        file = pickle.load(input_file)
        for line in file:
            for field, value in zip(Animal._fields, line):
                print(f"{field}: {value}")
            print()
    return True

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
def users_plans():
    users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
             User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
             User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
             User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
             User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
             User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
             User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
             User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
             User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
             User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
             User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
             User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
             User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
             User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
             User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
    my_dict = {"Gold": 0, "Silver": 1, "Bronze": 3, "Basic": 4}
    for line in sorted(users, key=lambda line: (my_dict[line.plan], line.email)):
        print(f"{line.name} {line.surname}")
        print(f"  Email: {line.email}")
        print(f"  Plan: {line.plan}")
        print()
    return True

Meet = namedtuple("Meet", ['surname', 'name', 'meeting_date', 'meeting_time'])
def with_csv():
    with open("namedtuple_unit/meetings.csv", encoding="utf-8") as input_file:
        data = [Meet._make(line) for line in list(csv.reader(input_file, delimiter=","))[1:]]
        a = sorted(data, key= lambda item: (datetime.strptime(item.meeting_date, "%d.%m.%Y"),
                                            datetime.strptime(item.meeting_time, "%H:%S")))
        for line in a:
            print(f"{line.surname} {line.name}")
    return data

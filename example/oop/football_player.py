# %%
# http://www.liverpoolfc.in.th/squad.php
from collections import namedtuple
from datetime import date

# %%
class Dummy:
    pass

class Player:
    # def __init__(self):
    #     self.fname = ""
    #     self.lname = ""
    #     self.number = 0

    total_players = 0

    def __init__(self, fname, lname, number):
        self.fname = fname.title()
        self.lname = lname.title()
        self.number = number
        # self.total_players += 1
        Player.total_players += 1

    def __str__(self):
        return "({:>2}) {} {}".format(self.number, self.fname, self.lname)

    def name(self):
        return "{:>2}. {}".format(self.number, self.lname.upper())


# %%
class Team:
    def __init__(self, team_name, players):
        self.team_name = team_name
        self.players = players

    def __str__(self):
        a = [p.name() for p in self.players]
        return "{}\n{}".format(self.team_name, "\n".join(a))


# %%
class Person:
    fname = ""
    lname = ""


# %%
def demo_tuple_list():
    p1 = ("Loris", "Karius", 1)
    p2 = ["Simon", "Mignolet", 22]
    print(p1)
    print(p1[0], p1[1], p1[2])


# %%
def demo_namedtuple():
    P = namedtuple("Player", ["fname", "lname", "number"])
    p1 = P("Loris", "Karius", 1)
    p2 = P(number=1, fname="Simon", lname="Mignolet")
    print(p1)
    print(p2)


# %%
def demo_dict():
    p1 = {"First": "Loris", "Last": "Karius", "Number": 1}
    p2 = {"First": "Simon", "Last": "Mignolet", "Number": 23}
    print(p1)
    print(p1["First"], p1["Last"], p1["Number"])

# %%


# %%
def demo_dummy():
    p1 = Dummy()
    p1.fname = "Loris"
    p1.lname = "Karius"
    p1.number = 1
    print(p1.fname, p1.lname, p1.number)

# %%
def demo_class():
    p1 = Player("Loris", "Karius", 1)
    p2 = Player("Simon", "Mignolet", 22)
    print(p1)
    print(p2)
    print(p1.fname, p1.lname, p1.number)
    print(dir(p1))
    print(dir(Player))
    print(p1.__dict__)
    print(Player.__dict__)


# %%
def demo_person():
    p1 = Person()
    p1.fname = "Peter"
    p1.lname = "Parker"
    p2 = Person()
    p2.fname = "Bruce"
    print(p1.fname, p2.fname)
    # print(dir(p1))
    print(p1.__dict__)
    print(p1.__class__)
    print(p1.__dict__.keys())
    print(p2.__dict__)
    Person.fname = "Taylor"
    print(Person.__dict__)


# %%
def demo_team():
    p1 = Player("Loris", "Karius", 1)
    p2 = Player("Simon", "Mignolet", 22)
    t1 = Team("Liverpool", [p1, p2])
    print(t1.players[1])
    print(t1)
    # for p in liverpool.players:
    #     print(p)


# %%
if __name__ == '__main__':
    demo_dummy()
    # demo_tuple_list()
    # demo_namedtuple()
    # demo_dict()
    # demo_class()
    # demo_person()
    # demo_team()
    # print(date(1994, 7, 20))

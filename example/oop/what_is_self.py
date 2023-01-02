# %%
class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total(self):  # instance method
        return self.gold + self.silver + self.bronze

    def dummy(self, a, b):
        return a + b


# %%
if __name__ == '__main__':
    th = Medal("Thailand", 5, 3, 2)
    print(th.country)
    print(th.total())
    print(Medal.total(th))
    print(th.dummy(1, 2))
    print(Medal.dummy(th, 1, 2))
    th.rank = 10
    print(th.rank)

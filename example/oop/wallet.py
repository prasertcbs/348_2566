# %%
class Wallet:
    def __init__(self):
        self.amount = 0

    def earn(self, a):
        self.amount += a

    def spend(self, a):
        self.amount -= a

    def __str__(self):
        return "amount = {:,}".format(self.amount)
        # return "{} -> amount = {:,}".format(self.__name__, self.amount)

# %%
def value_type():
    a = 5
    b = a
    print(id(a), id(b))
    b = 2
    print(id(a), id(b))
    print("id(a)={}, id(b)={}".format(id(a), id(b)))
    print("a={}, b={}".format(a, b))

# %%
def ref_type():
    f = ["lily", "rose", "lily"]
    g = f
    print("{} {}".format(id(f), id(g)))
    print("BEFORE:\nf = {}\ng = {}".format(f, g))
    g[0] = "magnolia"
    # g.append("tulip")
    print("{} {}".format(id(f), id(g)))
    print("AFTER :\nf = {}\ng = {}".format(f, g))


# %%
def ref_class_type():
    dad = Wallet()
    dad.earn(100)
    print("dad's wallet", dad)
    mom = dad
    print(id(dad), id(mom))
    print("mom's wallet ", mom)
    mom.spend(20)
    print("dad's wallet", dad)
    kid = Wallet()
    kid.earn(400)
    mom = kid
    print(id(dad), id(mom), id(kid))
    mom.earn(300)
    print("kid's wallet", dad)
    print(id(dad), id(mom), id(kid))


# %%
def print_bullet(lst, bullet="-"):
    print("id(lst) = {}".format(id(lst)))
    for e in lst:
        print("{} {}".format(bullet, e))


# %%
def foo(a, b):
    print("id(a) = {}, id(b) = {}".format(id(a), id(b)))
    a = .11
    b = .999
    print("id(a) = {}, id(b) = {}".format(id(a), id(b)))


# %%
def bar(a, b):
    print("id(a) = {}, id(b) = {}".format(id(a), id(b)))
    a = .11
    b[1] = "coconut"
    print("id(a) = {}, id(b) = {}".format(id(a), id(b)))


# %%
if __name__ == '__main__':
    # value_type()
    # ref_type()
    # ref_class_type()
    a = ["coffee", "tea", "soft drink"]
    print("id(a) = {}".format(id(a)))
    print_bullet(a)

    x = 5
    y = 10
    print("id(x) = {}, id(y) = {}".format(id(x), id(y)))
    foo(x, y)
    print(x, y)

    # p = 5
    # q = ["apple", "banana", "cherry"]
    # print(q)
    # print("id(x) = {}, id(y) = {}".format(id(p), id(q)))
    # bar(p, q)
    # print(q)

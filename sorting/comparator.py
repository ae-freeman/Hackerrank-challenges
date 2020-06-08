from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # __repr__ should return a printable 'representation' of an object
    def __repr__(self):
        return self.name, self.score
        # other option: return "{} {}".format(self.name, self.score)

    def comparator(a, b):

        # a and b are exactly equal, so return 0
        if a.name == b.name and a.score == b.score:
            return 0

        # if the score is the same, then need to sort based on letter
        if a.score == b.score:
            return 1 if a.name > b.name else -1

        # if score is different, letter isn't relevant
        return 1 if a.score < b.score else -1

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)

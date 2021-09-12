class Game:

    def __init__(self, n):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagnol = 0
        self.anti_diagnol = 0
        self.size = n

    def move(self, x, y, player):
        player = player if player == 1 else -1
        self.rows[x] += player
        self.cols[x] += player
        if x == y: self.diagnol += player
        if x == self.size - 1 - y: self.anti_diagnol += player

        if self.anti_diagnol == self.size or self.diagnol == self.size or self.rows[x] == self.size or self.cols[
            y] == self.size:
            return 1
        elif self.anti_diagnol == -self.size or self.diagnol == -self.size or self.rows[x] == -self.size or self.cols[
            y] == -self.size:
            return -1
        else:
            return 0


g = Game(3)
print(g.move(0, 0, 1))
print(g.move(0, 1, 1))
# print(g.move(0, 2, 2))
print(g.move(0, 2, 1))

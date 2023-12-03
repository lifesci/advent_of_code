from dataclasses import dataclass

@dataclass
class Draw:
    clr: str
    amt: int

class Game:
    def __init__(self, index, draws):
        self.index = index
        self.draws = draws

    def p1_valid(self):
        limits = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        for rnd in self.draws:
            for draw in rnd:
                if limits[draw.clr] < draw.amt:
                    return False
        return True

    def power(self):
        mins = {}
        for rnd in self.draws:
            for draw in rnd:
                if draw.clr not in mins:
                    mins[draw.clr] = draw.amt
                else:
                    mins[draw.clr] = max(mins[draw.clr], draw.amt)
        pwr = 1
        for key in mins:
            pwr *= mins[key]
        return pwr

    @staticmethod
    def from_string(s):
        raw_game, rounds_str = s.split(": ")
        _, game_index = raw_game.split(" ")
        game_index = int(game_index)
        rounds = rounds_str.split("; ")
        raw_rnd_draws = [rnd.split(", ") for rnd in rounds]
        draws = []
        for rnd in raw_rnd_draws:
            round_draws = []
            for raw_draw in rnd:
                draw = raw_draw.split(" ")
                round_draws.append(Draw(draw[1], int(draw[0])))
            draws.append(round_draws)
        return Game(game_index, draws)

with open("input") as f:
    games = []
    for line in f:
        game = Game.from_string(line.strip())
        games.append(game)

    p1_sum = 0
    for game in games:
        if game.p1_valid():
            p1_sum += game.index
    print(p1_sum)

    power = sum(game.power() for game in games)
    print(power)

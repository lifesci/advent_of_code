class Card:
    def __init__(self, index, winning, mine):
        self.index = index
        matches = sum([x in winning for x in mine])
        self.rule = [index + x for x in range(1, matches + 1)]

class CardSet:
    def __init__(self, cards):
        self.num_cards = len(cards)
        self.rules = [[x for x in card.rule if x < self.num_cards] for card in cards]
        self.cards = [1 for card in cards]

    def run(self):
        total = 0
        cards = self.cards
        card_count = sum(cards)
        while card_count > 0:
            total += card_count
            new_cards = [0 for _ in range(self.num_cards)]
            for i, count in enumerate(cards):
                rule = self.rules[i]
                for index in rule:
                    new_cards[index] += count
            cards = new_cards
            card_count = sum(cards)
        return total

def p2():
    line_num = 0
    cards = []
    with open("input") as f:
        for raw_line in f:
            matches = 0
            line = raw_line.strip()
            _, nums = line.split(":")
            winning_str, mine_str = nums.split("|")
            winning = set([int(x) for x in winning_str.split()])
            mine = [int(x) for x in mine_str.split()]
            card = Card(line_num, winning, mine)
            cards.append(card)
            line_num += 1
    card_set = CardSet(cards)
    return card_set.run()

def p1():
    total = 0
    with open("input") as f:
        for raw_line in f:
            matches = 0
            line = raw_line.strip()
            _, nums = line.split(":")
            winning_str, mine_str = nums.split("|")
            winning = set([int(x) for x in winning_str.split()])
            mine = [int(x) for x in mine_str.split()]
            for num in mine:
                if num in winning:
                    matches += 1
            if matches > 0:
                total += pow(2, matches - 1)
    return total

print(p1())
print(p2())

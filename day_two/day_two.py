# Advent of Code - 2022, Day 2: Rock Paper Scissors

# Strat guide decrpyted, including point values per result
strats = {
    'B Z': 9,      
    'A Y': 8, 
    'C X': 7, 
    'C Z': 6, 
    'B Y': 5, 
    'A X': 4, 
    'A Z': 3, 
    'C Y': 2, 
    'B X': 1
}

# Opening strats
with open('strategy_guide.txt') as f:
    strategy_guide = f.read()
 
# Getting round-by-round strats
rounds = strategy_guide.split("\n")

# Calculating the score
score = 0
for round in rounds:
    score += strats[round]

# part I
print("If everything goes exactly according to the strategy guide, your score will be", score)
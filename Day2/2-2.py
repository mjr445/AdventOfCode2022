# X = A is Rock (1 Pt)
# Y = B is Paper (2 pt)
# Z = C is Scissors (3 pt)

# Win  = 6 pt
# Draw = 3 pt
# Lose = 0 pt

def main():
    game_tree = {
        "A": {
            "X": 3 + 0,
            "Y": 1 + 3,
            "Z": 2 + 6
        },
        "B": {
            "X": 1 + 0,
            "Y": 2 + 3,
            "Z": 3 + 6
        },
        "C": {
            "X": 2 + 0,
            "Y": 3 + 3,
            "Z": 1 + 6
        }
    }
    total_score = 0
    with open('2.txt', 'r') as input_file:
        for line in input_file.readlines():
            opponent_move, player_move = line.strip().split()
            total_score += game_tree[opponent_move][player_move]
    print(total_score)
if __name__ == "__main__":
    main()
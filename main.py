import random
import time
from collections import Counter
#author: John Ryan
#date: 08-17-2025

#Possible moves
MOVES = ["rock", "paper", "scissors"]

#Game logic
def get_winner(move1, move2):
    if move1 == move2:
        return 0 # tie game outcome
    if (
        (move1 == "rock" and move2 == "scissors") 
        or (move1 == "paper" and move2 == "rock") 
        or (move1 == "scissors" and move2 == "paper")
    ):
        return 1 #player1 wins
    return 2 #player2 wins

#player strategies
class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.history = [] #store past moves
        self.wins = self.losses = self.draws = 0
        self.moveCounter = Counter()
        self.moveWins = Counter()
        self.moveLosses = Counter()
        self.moveDraws = Counter()

    def choose_move(self, opponent=None):
        if self.strategy == "random":
            return random.choice(MOVES)
        elif self.strategy == "cycle":
            if not self.history: #if no history, just play rock
                return "rock"
            next_in_cycle = (MOVES.index(self.history[-1]) + 1) % 3 #get next move in MOVES
            return MOVES[next_in_cycle]
        elif self.strategy == "rock-enjoyer":
            weight = random.randint(0,9) #60% rock, 20% scissors, 20% paper
            if weight < 6:
                return "rock"
            elif weight < 8:
                return "scissors"
            else:
                return "paper"
        elif self.strategy == "counter-last" and opponent:
            if opponent.history: # if opponent has history, counter their last move
                last = opponent.history[-1]
                if last == "rock": return "paper"
                if last == "paper": return "scissors"
                if last == "scissors": return "rock"
            return random.choice(MOVES) #if no history, go random style
        elif self.strategy == "copycat" and opponent:
            if opponent.history: #if opponent has history, copy last move
                return opponent.history[-1]
            return random.choice(MOVES) #if opponent has no history, go random style
        
class RPSGame:
    def __init__(self, players):
        self.players = players
        self.records = [] #game logs
    
    def simulate(self, n):
        start = time.time()
        for i in range(n):
            p1, p2 = random.sample(self.players, 2) #randomly select 2 players
            m1, m2 = p1.choose_move(p2), p2.choose_move(p1) #get their moves
            winner = get_winner(m1, m2) #determine winner
            
            #update player history
            p1.history.append(m1)
            p2.history.append(m2)
            p1.moveCounter[m1] +=1
            p2.moveCounter[m2] +=1

            if winner == 0: #tie
                p1.draws += 1
                p2.draws += 1
                p1.moveDraws[m1] += 1
                p2.moveDraws[m2] += 1
            elif winner == 1: #p1 wins
                p1.wins += 1
                p2.losses += 1
                p1.moveWins[m1] += 1
                p2.moveLosses[m2] +=1
            else: #p2 wins
                p2.wins += 1
                p1.losses += 1
                p2.moveWins[m2] += 1
                p1.moveLosses[m1] +=1
            
            #Log the game
            self.records.append({
                "p1": p1.name,
                "p2": p2.name,
                "m1": m1,
                "m2": m2,
                "winner": "tie" if winner == 0 else (p1.name if winner == 1 else p2.name)
            })
        end = time.time()
        return end - start

    def print_stats(self):
        for p in self.players:
            total = p.wins + p.losses +p.draws
            ratio = p.wins / p.losses if p.losses > 0 else float(p.wins)
            print(f"Stats for {p.name} (Strategy: {p.strategy}):")
            print(f"  Games: {total}, Wins: {p.wins}, Losses: {p.losses}, Draws: {p.draws}")
            print(f"  Win/Loss Ratio: {ratio:.2f}")
            print(f"  Move Counts: {dict(p.moveCounter)}")
            print(f"  Move Wins: {dict(p.moveWins)}")
            print(f"  Move Losses: {dict(p.moveLosses)}")
            print(f"  Move Draws: {dict(p.moveDraws)}")
            print("-"*70)
            
def test():
    players = [
        Player("Rachelle", "random"),
        Player("Rambo", "rock-enjoyer"),
        Player("Celine", "cycle"),
        Player("Charles", "counter-last"),
        Player("Carlyle", "copycat"),
    ]
    game = RPSGame(players)
    runtime = game.simulate(1000000)  # run fewer for demo
    game.print_stats()

    #Print all games played
    def all_game():
        for i, record in enumerate(game.records, 1):
            print(f"Game {i}: {record['p1']}({record['m1']}) vs {record['p2']}({record['m2']}) → Winner: {record['winner']}")
    #all_game()

    # Print runtime at the end
    print(f"\nFinished printing all games. Total simulation time: {runtime*1000:.3f} ms")
    
# Run the test
test()
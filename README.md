## Rock-Paper-Scissors Simulation

A Python-based Rock-Paper-Scissors (RPS) simulation framework that allows different strategies to play against each other over thousands of rounds. The program tracks move history, player statistics, and overall match results.

## Multiple built-in player strategies:

  Random – picks a random move each round.

  Cycle – cycles through Rock → Paper → Scissors.

  Rock Enjoyer – biased toward Rock (60% Rock, 20% Scissors, 20% Paper).

  Counter-Last – plays the winning counter to the opponent’s last move.

  Copycat – copies the opponent’s last move.

## Tracks:

  Wins, losses, draws per player.

  Per-move win/loss/draw counts.

  Full game logs (optional).

  Simulation speed measurement (runtime in milliseconds).

  The test() function creates 5 players with different strategies and simulates 1,000,000 (adjustable) rounds of play.

# Author

  John Ryan – August 17, 2025

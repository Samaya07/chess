# chess
This repository contains a move_generators and evaluation_function code for the game of chess.
The move_generator function considers all the moves, kills and checks possible.
The evaluation function which takes into account 3 factors:
1. Piece values : Pawn-1, Bishop-3, Knight-3, Rook-5, Queen-9. More the piece value, more the advantage.
2. Mobility : The total number of legal moves possible for each chess piece. If all the white pieces together have more legal moves, then the white has the advantage.
3. King safety : The number of checks that the white pieces can achieve with the current configuration increases its advantage, as this means the black king is less safe.
Hence, this is a very basic evaluation function, there are many more factors that it needs to take into account. The piece values also change depending on the stage of the game.

A positive value of the evaluation function means, advantage for the white pieces. Higher the value, higher is the advantage for the white pieces in the current configuration.
A negative value means, advantage to the black pieces. Lower the negative value, more is the advantage to the black pieces.

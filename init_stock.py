from stockfish import Stockfish

RELATIVE_PATH_STOCKFISH = "bin/stockfish"
stockfish = Stockfish(path=RELATIVE_PATH_STOCKFISH)

print(stockfish.get_parameters())


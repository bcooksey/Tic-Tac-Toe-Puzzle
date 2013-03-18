import random

def did_win(moves, player):
    if moves[:3].count(player) == 3:
        return True
    elif moves[:4].count(player) == 3:
        return True
    elif moves[:5].count(player) == 4:
        return True
    elif moves.count(player) == 4:
        return True
    else:
        return False

def debug(msg):
    pass
#    print msg

def play_game(cash_x, cash_o):
    moves = []
    x_plays = 0
    while len(moves) < 6:
        if did_win(moves, 'x'):
            debug(moves)
            return True
        elif did_win(moves, 'o'):
            debug(moves)
            return False

        # x's betting
        if cash_o == 0:
            bet_x = 1
        elif x_plays == 3:
            bet_x = cash_o + 1
        else:
            bet_x = (cash_x / (3 - x_plays))
            if bet_x > cash_o:
                bet_x = cash_o + 1

        if bet_x > cash_x: # Catch case where x is out of money, or almost out
            bet_x = cash_x

        # Does o bet against x?
        if random.randint(0, 1) == 0:
            bet_o = bet_x + 1
            if bet_o > cash_o:
                bet_o = 0
        else:
            bet_o = 0

        debug('X bet %d of %d. O bet %d of %d' % (bet_x, cash_x, bet_o, cash_o))

        # Add the move
        if bet_x > bet_o:
            moves.append('x')
            cash_x -= bet_x
            x_plays += 1
        else:
            moves.append('o')
            cash_o -= bet_o
    debug(moves)
    return did_win(moves, 'x')

#### Game Params ########
cash_o = 100
cash_x = 300
outcomes = {}

outcomes[cash_x] = 0
for game_count in range(1, 1000):
    did_x_win = play_game(cash_x, cash_o)
    if did_x_win:
        outcomes[cash_x] += 1
        debug("X won")
    debug("~~~~~~~~~~~")
print 'X won %i/%i games' % (outcomes[cash_x], game_count)

import hardware
import time

MOVES = [
    (0,1,3),    (0,2,5),
    (1,4,8),    (1,3,6),
    (2,4,7),    (2,5,9),
    (3,1,0),    (3,4,5),
    (3,7,12),   (3,6,10),   (4,8,13), (4,7,11),
    (5,2,0),    (5,4,3),    (5,8,12), (5,9,14),
    (6,3,1),    (6,7,8),
    (7,4,2),    (7,8,9),
    (8,7,6),    (8,4,1),
    (9,5,2),    (9,8,7),
    (10,6,3),   (10,11,12),
    (11,7,4),   (11,12,13),
    (12,11,10), (12,7,3),   (12,8,5), (12,13,14),
    (13,12,11), (13,8,4),
    (14,13,12), (14,9,5),
]

off = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
board = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

def is_move_valid(move):
    if board[move[0]] and board[move[1]] and not board[move[2]]:
        return True
    return False

def play_one_game():
    for i in range(15):
        board[i] = True    
    hardware.set_leds(board)
    hardware.wait_buttons_released()

    empty = hardware.wait_button_press()
    board[empty] = False
    hardware.set_leds(board)

    play_to_finish()

def play_to_finish():
    while True:
        a = hardware.wait_button_press()
        hardware.set_leds(board)
        b = hardware.wait_button_press(blink=[a])
        hardware.set_leds(board)

        found = None
        for move in MOVES:        
            if move[0] == a and b in move[1:] and is_move_valid(move):
                found = move
                break

        if not found:
            continue

        board[move[0]] = False
        hardware.set_leds(board)
        time.sleep(0.25)
        board[move[1]] = False
        hardware.set_leds(board)
        time.sleep(0.25)
        board[move[2]] = True
        hardware.set_leds(board)
        time.sleep(0.25)

        done = True
        for m in MOVES:
            if is_move_valid(m):
                done = False
                break

        if done:
            while True:
                data = hardware.get_buttons()
                if data[0] and data[10] or data[0] and data[14] or data[10] and data[14]:
                    break
                hardware.set_leds(off)
                time.sleep(0.1)
                hardware.set_leds(board)
                time.sleep(0.1)

while True:
    try:
        play_one_game()
    except hardware.ResetException:
        pass

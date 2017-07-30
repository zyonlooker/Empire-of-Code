import itertools
COLS = "abcdefgh"
ROWS = "12345678"
length = 8  # length of the chess board sides
total = 8   # total number of chess pieces need to be placed

def place_queens(placed):
    if not check_precondition(placed):
        return set()
    
    # -------- initialization --------
    placed_list = list(placed)
    remain = total - len(placed_list)    # remained number pieces need to be placed
    positions_init = availabel_positions(placed_list)
    if len(positions_init) < remain:
        return set()

    avail_rows = set([positions_init[n][1] for n in range(len(positions_init))])
    position_groups = []
    for n in avail_rows:
        row = []
        for m in range(len(positions_init)):
            if positions_init[m][1] == n:
                row.append(positions_init[m])
        position_groups.append(row)
    # --------------------------------
    		
    # -------- main process --------
    # generate all available combinations of positions
    all_groups = list(itertools.product(*position_groups))
    
    for n in all_groups:
        replaced = placed.union(n)
        if check_precondition(replaced):
            return placed
            
    return set()
    # ------------------------------

def check_precondition(placed):
    """
    check precondition
    """
    placed_pre = list(placed)
    for p in placed:
        del placed_pre[placed_pre.index(p)]
        if check_validity(p, placed_pre):
            placed_pre = list(placed)
        else:
            return False
    return True

def check_validity(p, placed_list):
    """
    check if the position it will occupy next is available
    """
    if p in placed_list:
        return False
    else:
        board_placed = board_init(placed_list)
        row = ROWS.index(p[1])
        col = COLS.index(p[0])
        # check cols
        x = row
        while x > 0:
            if board_placed[x-1][col] == 1:
                return False
            x -= 1
        x = row
        while x < length - 1:
            if board_placed[x+1][col] == 1:
                return False
            x += 1
        
        # check rows
        y = col
        while y > 0:
            if board_placed[row][y-1] == 1:
                return False
            y -= 1
        y = col
        while y < length - 1:
            if board_placed[row][y-1] == 1:
                return False
            y += 1
        
        # check diags
        x = row
        y = col
        while x > 0 and y > 0:
            if board_placed[x-1][y-1] == 1:
                return False
            x -= 1
            y -= 1
        x = row
        y = col
        while x < length - 1 and y < length - 1:
            if board_placed[x+1][y+1] == 1:
                return False
            x += 1
            y += 1
        x = row
        y = col
        while x < length - 1 and y > 0:
            if board_placed[x+1][y-1] == 1:
                return False
            x += 1
            y -= 1
        x = row
        y = col
        while x > 0 and y < length - 1:
            if board_placed[x-1][y+1] == 1:
                return False
            x -= 1
            y += 1
        
        return True
        
def board_init(placed_list):
    # initialize the board
    board_placed = [[0 for y in range(length)] for x in range(length)]
    for p in placed_list:
        row = ROWS.index(p[1])
        col = COLS.index(p[0])
        board_placed[row][col] = 1
    return board_placed

def availabel_positions(placed_list):
    """
    choose available positions except placed
    """
    board = board_init(placed_list)

    # exclude unavailable rows and cols
    threats_rows = []
    threats_cols = []
    for p in placed_list:
        row = ROWS.index(p[1])
        col = COLS.index(p[0])
        threats_rows.append(row)
        threats_cols.append(col)
    for x in range(length):
        if x in threats_rows:
            for n in range(length):
                board[x][n] = 1
    for y in range(length):
        if y in threats_cols:
            for n in range(length):
                board[n][y] = 1
    
    # exclude unavailable diagonals           
    for p in placed_list:
        x = ROWS.index(p[1])
        y = COLS.index(p[0])
        while x > 0 and y > 0:
            board[x-1][y-1] = 1
            x -= 1
            y -= 1
            
        x = ROWS.index(p[1])
        y = COLS.index(p[0])
        while x < length - 1 and y < length - 1:
            board[x+1][y+1] = 1
            x += 1
            y += 1
            
        x = ROWS.index(p[1])
        y = COLS.index(p[0])
        while x < length - 1 and y > 0:
            board[x+1][y-1] = 1
            x += 1
            y -= 1
            
        x = ROWS.index(p[1])
        y = COLS.index(p[0])
        while x > 0 and y < length - 1:
            board[x-1][y+1] = 1
            x -= 1
            y += 1

    # possibly available positions
    avail_p = []
    for x in range(length):
        for y in range(length):
            if board[x][y] == 0:
                avail_p.append(COLS[y] + ROWS[x])
    return avail_p


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import combinations

    COLS = "abcdefgh"
    ROWS = "12345678"

    THREATS = {c + r: set(
        [c + ROWS[k] for k in range(8)] +
        [COLS[k] + r for k in range(8)] +
        [COLS[k] + ROWS[i - j + k] for k in range(8) if 0 <= i - j + k < 8] +
        [COLS[k] + ROWS[- k + i + j] for k in range(8) if 0 <= - k + i + j < 8])
        for i, r in enumerate(ROWS) for j, c in enumerate(COLS)}

    def check_coordinate(coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True

    #assert checker(place_queens, {"b2", "c4", "d6", "e8"}, True), "1st Example"
    #assert checker(place_queens, {"b2", "c4", "d6", "e8", "a7", "g5"}, False), "2nd Example"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")


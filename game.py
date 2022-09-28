def next_generation(board):
    width = len(board[0])
    height = len(board)
    new_generation = [x for x in range(height)]
    for i in range(height):
        new_generation[i] = board[i].copy()
    for i in range(height):
        for j in range(width):
            if board[i][j] != '#':
                sample = [[board[i - 1][j - 1], board[i - 1][j], board[i - 1][j + 1]],
                          [board[i][j - 1], board[i][j + 1]],
                          [board[i + 1][j - 1], board[i + 1][j], board[i + 1][j + 1]]]
                alive = sample[0].count('+') + sample[1].count('+') + sample[2].count('+')
                if board[i][j] == '+' and alive != 2 and alive != 3:
                    new_generation[i][j] = '-'
                if board[i][j] == '-' and alive == 3:
                    new_generation[i][j] = '+'
    return new_generation

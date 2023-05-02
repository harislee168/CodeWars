def display_board(board, width):
    dash_str = '-'
    return_str = ''
    counter = 1
    board_length = len(board)

    for index in range(board_length):
        if counter == board_length:
            return_str += ' ' + board[index] + ' '
            continue
        if counter % width == 0:
            return_str += ' ' + board[index] + ' '
            return_str += '\n'
            return_str += (dash_str*width*4)[:-1]
            return_str += '\n'
        else:
            return_str += ' ' + board[index] + ' |'
        counter += 1
        
    return return_str
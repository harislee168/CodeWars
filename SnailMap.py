def snail(snail_map):
    #the total n which is the row and column. this is to know the range of loop in row and columns
    #need to keep track of the status of highest and lowest row and column so the loop will not overlap
    highest_row, highest_col = len(snail_map), len(snail_map)
    lowest_row, lowest_col = -1, -1
    
    if len(snail_map[0]) == 0:
        return []
    
    #I need to know how many loops in total to exhaust the list
    how_many_loop = 2 * highest_row - 1
    
    #need to store the current state of row and column. It starts from 0 and 0
    current_row, current_col= 0 ,0
    result_list = []
    
    for i in range(how_many_loop):        
        #modulus by 4 because the loop will be either:
        #i = 0 means row stay constant and column is incremental
        #i = 1 means column stay constant and row is incremental
        #i = 2 means row stay constant and column is decremental
        #i = 3 means column stay constant and row is decremental
        
        which_plot = i % 4
        
        #plot 0 row stay constant and loop the column incrementally and start with the latest/current column
        if which_plot == 0:
            for col in range(current_col, highest_col, 1):
                # add to the result list and update the current col
                result_list.append(snail_map[current_row][col])
                current_col = col
            #after loop add the current row by 1 because at this plot we are always at the top of the row
            current_row = current_row + 1
            #add the lowest row by 1 because this row has been traversed to prevent the next loop that will enter this row
            lowest_row = lowest_row + 1
        
        #plot 1 column stay constant and loop the row incrementally and start with the latest/current row
        if which_plot == 1:
            for row in range(current_row, highest_row, 1):
                #add to the result list and update the current row
                result_list.append(snail_map[row][current_col])
                current_row = row
            #after loop, need to update the current col by minus 1, because in this plot, we are always at the end of the column
            current_col = current_col - 1
            #reduce the highest col by 1 because the highest col has been traversed
            highest_col = highest_col - 1
        
        #plot 2 row stay constant and loop the column decrementally and start with the latest/current column
        if which_plot == 2:
            for col in range(current_col, lowest_col, -1):
                #add to the result list and update the current col
                result_list.append(snail_map[current_row][col])
                current_col = col
            #after loop, need to update the current row by minus 1, because in this plot, we are always at the end of the row
            current_row = current_row - 1
            highest_row = highest_row - 1
            
        #plot 3 column stay constant and loop the row decrementally
        if which_plot == 3:
            for row in range(current_row, lowest_row, -1):
                #add to the result list and update the current row
                result_list.append(snail_map[row][current_col])
                current_row = row
            #add the current col by 1 because at this plot we are always at the most left of the row
            current_col = current_col + 1
            lowest_col = lowest_col + 1

    return result_list
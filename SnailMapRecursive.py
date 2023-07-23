def snail(snail_map):
    if len(snail_map[0]) == 0:
        return []
    
    #get the row and col length
    result = []
    
    def recursive_snail(snail_map, result):
        row_len = len(snail_map)
        col_len = len(snail_map)
        if row_len == 0:
            return     
        elif row_len == 1:
            result.append(snail_map[0][0])
        else:            
            #travel top row and to the right
            for col in range(col_len):
                result.append(snail_map[0][col])

            #delete the row and reduce the row by 1
            del snail_map[0]
            row_len = row_len - 1

            #travel down and end of the column
            for row in range(row_len):
                result.append(snail_map[row][col_len-1])
                del snail_map[row][col_len-1]

            #reduce the column length by 2 because the start of the column is inclusive
            col_len = col_len - 2

            #travel the lowest row and to the left
            for col in range(col_len, -1, -1):
                result.append(snail_map[-1][col])

            del snail_map[-1]
            #reduce the row length by 2 because the start of the column is inclusive
            row_len = row_len - 2

            #travel up and most left column
            for row in range(row_len, -1, -1):
                result.append(snail_map[row][0])
                del snail_map[row][0]
                
            return recursive_snail(snail_map, result)
    recursive_snail(snail_map, result)
    return result
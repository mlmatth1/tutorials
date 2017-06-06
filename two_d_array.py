def two_d_array():
    d = [[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2],[4,4,4,4,4]]
    for i in d:
        for j in d:
            temp = d[i][j]
            top = d[i+1][j]

two_d_array()

def find(mat):
    h = len(mat)
    for g in range(int(h / 2)):
        nh = h - g - 1
        for i in range(g, nh + 1):
            print(str(nh - i) + ":" + str(g) + " <- " + str(g) + ":" + str(i))
            print(str(g) + ":" + str(i) + " <- " + str(i) + ":" + str(nh))
            print(str(nh) + ":" + str(nh - i) + " <- " + str(nh - i) + ":" + str(g))
            print(str(nh - i) + ":" + str(nh) + " <- " + str(nh) + ":" + str(nh - i))
            mat[nh - i][g], \
            mat[g][i], \
            mat[nh][nh - i], \
            mat[nh - i][nh] = \
                mat[g][i], \
                mat[nh - i][nh], \
                mat[nh - i][g], \
                mat[nh][nh - i]
    return mat


mat = [[8, 1, 2, 3],
       [4, 5, 6, 8],
       [7, 8, 9, 0],
       [1, 4, 9, 0]]
# mat = [[8, 1],
#        [4, 5],
#        ]
d = [
    [5, 1],
    [8, 5]
]
print(find(mat))

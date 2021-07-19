def find(input):
    if len(input) < 2: return 0
    bA = -input[0]
    sA = 0
    cA = 0
    for i in input[1:]:
        nbA = max(bA, cA - i)
        nsA = max(sA, bA + i)
        ncA = max(cA, sA)
        bA = nbA
        sA = nsA
        cA = ncA  # if you want more cooling days then make arrey and update cooling agent for last n cooling days
    return sA


input = [1, 2, 3, 0, 2]
input = [2, 1, 4, 4, 2, 3, 2, 5, 1, 2]
print(find(input))

#https://leetcode.com/problems/longest-substring-without-repeating-characters
import sys

def findUsingDict(arr)-> int:
    char_index={}
    max_len=-sys.maxsize
    left=0
    for right, element in enumerate(arr):
        left = max(left, char_index.get(element,0) + 1)
        max_len = max(max_len, right - left + 1)
        char_index[element] = right
    return max_len

#Test cases
assert findUsingDict("ABDEFGABEF")==6
assert findUsingDict("GEEKSFORGEEKS")==7
assert findUsingDict("BBBB")==1
print(findUsingDict("ABDEFGABEF"))


def findUsingSet(data: str) -> int:
    uniqueCharacters=set()
    length=len(data)
    left=0
    max_len=0
    for right in range(length):
        currentEl=data[right]
        if currentEl in uniqueCharacters:
            while uniqueCharacters and data[left] in uniqueCharacters and data[left]!=currentEl:
                uniqueCharacters.remove(data[left])
                left+=1
            uniqueCharacters.remove(data[left])
            left+=1
        uniqueCharacters.add(currentEl)
        max_len=max(max_len, right-left+1)
    return max_len


assert findUsingSet("ABDEFGABEF")==6
assert findUsingSet("GEEKSFORGEEKS")==7
assert findUsingSet("BBBB")==1
assert findUsingSet("")==0
print(findUsingSet("GEEKSFORGEEKS"))

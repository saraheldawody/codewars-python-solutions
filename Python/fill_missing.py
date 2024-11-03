"""
Task Explaination:
    Write a function that accepts a list that can contain missing data, and an integer representing the method on how to fill the missing data if there is any. Missing data is represented as None. The list will only contain integers and None values.

The fill method rules are outlined below:

Fill method: 
  -1: backwards 
   0: nearest      
   1: forwards

Example
    arr = [None, 1, None, None, None, 2, None]
    fill(arr, -1) == [1, 1, 2, 2, 2, 2, None]  # None replaced by closest int on the right
    fill(arr,  0) == [1, 1, 1, 1, 2, 2, 2]     # None replaced by closest int. If equidistant, choose the smallest int
    fill(arr,  1) == [None, 1, 1, 1, 1, 2, 2]  # None replaced by closest int on the left

Notes
    [] should return []
    [None] should return [None]
    Arrays will only contain integers and None values
"""

def get_nearest_number(arr, index):
    index_diff = 1
    while index_diff < len(arr):
        if index < len(arr)-1 and index >0 and index+index_diff < len(arr):
            if arr[index+index_diff] is not None and arr[index-index_diff] is not None:
                return min(arr[index+index_diff], arr[index-index_diff])
        if index >0 and index >= index_diff:
            if arr[index-index_diff] is not None:
                return arr[index-index_diff]
        if index < len(arr)-1 and index+index_diff < len(arr):
            if arr[index+index_diff] is not None:
                return arr[index+index_diff]
        
        index_diff += 1
    return None
        
def fill(arr, method=0):
    if method == -1:
        new_arr = arr[::-1]
        for i in range(len(arr)):
            if new_arr[i] is None and i != 0:
                new_arr[i]=new_arr[i-1]
        return new_arr[::-1]
    elif method == 1:
        for i in range(len(arr)):
            if arr[i] is None and i != 0:
                arr[i]=arr[i-1]
        return arr
    elif method == 0:
        res = []
        for i in range(len(arr)):
            if arr[i] is None:
                res.append(get_nearest_number(arr, i))
            else:
                res.append(arr[i])
        return res
    else:
        return None


assert fill([],-1) == [], "Example 1: fill([],-1) should return []"
assert fill([],0) == [], "Example 2: fill([],0) should return []"
assert fill([],1) == [], "Example 3: fill([],1) should return []"
assert fill([None],-1) == [None], "Example 4: fill([None],-1) should return [None]"
assert fill([None],0) == [None], "Example 5: fill([None],0) should return [None]"
assert fill([None],1) == [None], "Example 6: fill([None],1) should return [None]"
assert fill([1],-1) == [1], "Example 7: fill([1],-1) should return [1]"
assert fill([1],0) == [1], "Example 8: fill([1],0) should return [1]"
assert fill([1],1) == [1], "Example 9: fill([1],1) should return [1]"
assert fill([1,None],-1) == [1,None], "Example 10: fill([1,None],-1) should return [1,None]"
assert fill([1,None],0) == [1,1], "Example 11: fill([1,None],0) should return [1,1]"
assert fill([1,None],1) == [1,1], "Example 12: fill([1,None],1) should return [1,1]"
assert fill([None,1,None,None,None,2,None],-1) == [1, 1, 2, 2, 2, 2, None], "Example 13: fill([None,1,None,None,None,2,None],-1) should return [1, 1, 2, 2, 2, 2, None]"
assert fill([None,1,None,None,None,2,None],0) == [1, 1, 1, 1, 2, 2, 2], "Example 14: fill([None,1,None,None,None,2,None],0) should return [1, 1, 1, 1, 2, 2, 2]"
assert fill([None,1,None,None,None,2,None],1) == [None, 1, 1, 1, 1, 2, 2], "Example 15: fill([None,1,None,None,None,2,None],1) should return [None, 1, 1, 1, 1, 2, 2]"
assert fill([4, 5, None, None, None, 2, None, 2],-1) == [4, 5, 2, 2, 2, 2, 2, 2], "Example 16: fill([4, 5, None, None, None, 2, None, 2],-1) should return [4, 5, 2, 2, 2, 2, 2, 2]"
assert fill([4, 5, None, None, None, 2, None, 2],0) == [4, 5, 5, 2, 2, 2, 2, 2], "Example 17: fill([4, 5, None, None, None, 2, None, 2],0) should return [4, 5, 5, 2, 2, 2, 2, 2]"
assert fill([4, 5, None, None, None, 2, None, 2],1) == [4, 5, 5, 5, 5, 2, 2, 2] , "Example 18: fill([4, 5, None, None, None, 2, None, 2],1) should return [4, 5, 5, 5, 5, 2, 2, 2]"
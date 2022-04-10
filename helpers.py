def maxLenSeqAboveNumber(arr, number):
    """ return the length of longest subarray of 'arr' with consecutive elements above 'number' """
    longest,curr=0,0
    for x in arr:
        if x > number:
            curr+=1
        else:
            curr=0
        if curr>longest:longest=curr
    return longest

assert maxLenSeqAboveNumber([1, 2, 1, 3, 2], 4) == 0
assert maxLenSeqAboveNumber([1, 2, 1, 4, 2], 4) == 0
assert maxLenSeqAboveNumber([1], 1) == 0
assert maxLenSeqAboveNumber([2], 1) == 1
assert maxLenSeqAboveNumber([1, 2, 3], 1) == 2
assert maxLenSeqAboveNumber([1, 2, 1, 3], 1) == 1
assert maxLenSeqAboveNumber([1, 2, 1, 3], 1) == 1
assert maxLenSeqAboveNumber([1, 2, 1, 3, 2], 1) == 2
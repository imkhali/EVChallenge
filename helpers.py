def maxLenSeqAboveNumber(arr, number):
    """return the length of longest subarray whith consecutive elements above number"""
    max,curr=0,0
    for x in arr:
        if x > number:
            curr+=1
        else:
            curr=0
        if curr>max:max=curr
    return max

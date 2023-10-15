#kadane's algo

def max_sum_of_subarray(l):
    currentsum=0
    maxsum=-32968
    // maxsum is set to minimum bound of int. 
    for i in l:
        currentsum+=i
        if(maxsum<currentsum):
            maxsum=currentsum
        if(currentsum<0):
            currentsum=0
    return maxsum

l=map(int,input("Enter elements of an array:").split())
out=max_sum_of_subarray(l)
print(out)

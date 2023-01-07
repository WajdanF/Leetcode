def minSubArrayLen(target, nums):
    start,end = 0,0 # start and end of the window
    currentSum = 0 # currentSum of the window
    minLength = float('inf') # minimum length of the subarray

    for i in range(len(nums)):
        currentSum += nums[i] # add the current element to the currentSum
        end = i
        
        while currentSum >= target: # if the currentSum is greater than or equal to the target
            minLength = min(minLength, end-start+1) # update the minLength with the current window size (end-start+1) 
            currentSum -= nums[start] # subtract the first element of the window from the currentSum
            start += 1 # move the window 
         
    
    return minLength if minLength != float('inf') else 0 # return the minLength if it is not infinity, else return 0

#make test cases for the above function
def main():
    print("Minimum Size Subarray Sum: ", minSubArrayLen(7, [2,3,1,2,4,3]))
    print("Minimum Size Subarray Sum: ", minSubArrayLen(4, [1,4,4]))
    print("Minimum Size Subarray Sum: ", minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
    print("Minimum Size Subarray Sum: ", minSubArrayLen(11, [1,2,3,4,5]))

main()

#runtime: O(N + N) - Only iterate over the list once and then iterate over the window once
#Space Complexity O(1) - No extra space is needed 
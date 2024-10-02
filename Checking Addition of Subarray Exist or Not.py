# Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements) that has sum equal to s. You mainly need to return the left and right indexes(1-based indexing) of that subarray.
# In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.
# Input: arr[] = [1,2,3,7,5], s = 12
# Output: 3 4

def Fun(arr, s):
  left, right = 0, len(arr)-1
  
  while left < right:
    current = arr[left] + arr[right]
    if current == s:
      return left, right
    
    elif current < s:
      left += 1
    
    else:
      right -= 1
  return -1

a = int(input(":"))
arr = []
for i in range(a):
  c=int(input(":"))
  arr.append(c)
s = int(input(":"))
print(Fun(arr, s))

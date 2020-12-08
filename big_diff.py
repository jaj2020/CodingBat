#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
#Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.	
def count_evens(nums):
  count = 0 
  for num in nums: 
    if num%2 == 0:
      count += 1
  return count
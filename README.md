# CodingBat
#These are my solutions to advanced Coding Bat challenges. 

#Logic 2, List 2, String 2 

#We want to make a row of bricks that is goal inches long. 
#We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
#Return True if it is possible to make the goal by choosing from the given bricks.

def make_bricks(small, big, goal):
    return (goal%5)<=small and (goal-(big*5))<=small
	
	
#Given 3 int values, a b c, return their sum. However, if one of the values 
#is the same as another of the values, it does not count towards the sum. 

def lone_sum(a, b, c):
  sum = 0
  sum += a if a not in [b,c] else 0
  sum += b if b not in [a,c] else 0
  sum += c if c not in [a,b] else 0
  return sum
  
#Given 3 int values, a b c, return their sum. 
#However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
#So for example, if b is 13, then both b and c do not count.

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  return a + b + c
  
#Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
#Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
#In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
#Define the helper below and at the same indent level as the main no_teen_sum().

def fix_teen(n):
  if n in [13, 14, 17, 18, 19]:
    return 0
  return n
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. 
#Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
#Given 3 ints, a b c, return the sum of their rounded values. 
#To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. 
#Write the helper entirely below and at the same indent level as round_sum().

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
def round10(num):
    if num % 10 < 5:
        return num - (num % 10)
    return num + (10 - num % 10)
	
#Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. 
#Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
  situation1 = abs(a-b) <= 1 and abs(b-c) >=2 and abs(a-c) >= 2
  situation2 = abs(a-c) <= 1 and abs(a-b) >=2 and abs(c-b) >= 2
  return situation1 or situation2
  
#We want make a package of goal kilos of chocolate. 
#We have small bars (1 kilo each) and big bars (5 kilos each). 
#Return the number of small bars to use, assuming we always use big bars before small bars. 
#Return -1 if it can't be done.

def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
    if remainder <= small:
        return remainder    
    return -1

#Return the number of even ints in the given array. 
#Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
	
def count_evens(nums):
  count = 0 
  for num in nums: 
    if num%2 == 0:
      count += 1
	return count
	
#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
#Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.	
def count_evens(nums):
  count = 0 
  for num in nums: 
    if num%2 == 0:
      count += 1
  return count
  
#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. 
#If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. 
#Use int division to produce the final average. You may assume that the array is length 3 or more.

def centered_average(nums):
    small = min(nums)
    big = max(nums)
    return (sum(nums) - small - big) / (len(nums) - 2)
	
#Return the sum of the numbers in the array, returning 0 for an empty array. 
#Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
	num = 0
    i = 0
	while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        total += nums[i]
        i += 1
	return num
	
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
#Return 0 for no numbers.

def sum67(nums):
  for i in range(0, len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      for x in range(i+1, len(nums)):
        temp = nums[j]
        nums[x] = 0
        if temp == 7:
          i = x + 1
          break
  return sum(nums)
	
#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.	

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
	return False

#Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  new_str = ''
  for letter in str: 
    new_str += letter*2
  return new_str
  
#Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == "hi":
            count += 1
    return count
	
#Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
    return str.count('cat') == str.count('dog')
	
#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
  count = 0
  for i in range(0, len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count

#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
#Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)
	
#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
return str.count('.xyz') != str.count('xyz')

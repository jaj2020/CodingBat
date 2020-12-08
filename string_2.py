#Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  new_str = ''
  for letter in str: 
    new_str += letter*2
  return new_str
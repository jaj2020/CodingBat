#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
return str.count('.xyz') != str.count('xyz')
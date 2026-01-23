str1 = "ABCDEFGH"
str2 = 'ABC'
str3 = ''' aBC dEF'''

str4 =  """ABC
DEF
GHI
""" 
# Multi line String

# 4 Ways to create strings
# string slicing

print("String Slicing")
print(str1[0:3])

print("\nString Negative Slicing")
print(str1[-4:-1])

print("\nString Skip Slicing---str[start:stop:skip]")
print(str1[0:7:2])

print("\nString Advanced Slicing Techniques")
print(str1[0:])
print(str1[:7])

print("\nString Functions")
print(len(str2)) # Returns Length
print(str2.endswith("BC")) # Returns bool
print(str3.startswith("a")) # Returns bool
print(str3.capitalize()) # Only first lettter capitalize
print(str3.upper())
print(str3.lower())
print(str3.title()) # Returns a string where each word is titlecased.
print(str3.replace("aBC","ABC"))
print(str3.strip())
print(str3.find("aBC")) # Returns index of the occurence of the word in the string.

print("\nString Concatenation")
str5 = str1 + str3
print(str5)

print("\nF-Strings")
num = 123
str6 = f"{num}ABC"
print(str6)

print("\nString Escape Characters")
print("\"DOUBLE QUOTE\"")
print("\nNewLine")
print("\\BACKSLASH\\")
print("\tTab")
print("\'SINGLE QUOTE\'")
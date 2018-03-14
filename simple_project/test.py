import string

old_str = 'my name is lance mone'
new_str1 = string.capwords(old_str)
new_str2 = string.capwords(old_str, 's ')
print(new_str1, new_str2)

# a-z
# 0-9
# @ (1 time)
# _ and . (1 time)
# . after @  (at position 3, or 4 from reverse side)

import re

emailCondition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"   
#^[a-z] element start with alphabet and + sign show joining
# \ use for searching in regex
# ? mark show character on left comes 1 times 
# ? mark work on 0 or 1
# \w use for searching
# $ search for reverse

userEmail = input('Enter Your Email')

if re.search(emailCondition,userEmail):
	print("Email is Valid")
else:
	print("Email is invalid")




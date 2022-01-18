"""
Given a and b as input, print the follow pattern
Input-> a=5, b=4
Output-> 10#15#20#25#
"""

a = 5
b = 4
pt = "#"
st = ""
for i in range(2,b+2):
  st = st + str(a*i) + pt
print(st)

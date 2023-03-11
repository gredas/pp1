import re

txt = "The rain in Spain"
x = re.search("\s", txt)
print(x.start())
print(x)
print(x.span())
print(x.string)
print(x.group())
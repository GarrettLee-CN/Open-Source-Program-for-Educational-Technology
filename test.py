from oset import file
from oset import chineseword

s = "天津师范大学教育学部教育技术研究所"
s = chineseword.cutword(s)
print(s)
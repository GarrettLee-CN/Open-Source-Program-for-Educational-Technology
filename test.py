from oset import File
from oset import Chineseword

s = "天津师范大学教育学部教育技术研究所"
c = Chineseword.cutword(s)
print(c)
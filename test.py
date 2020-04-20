from oset import File
from oset import Chineseword

#print(Chineseword.cutword(File.readfile('C:\\Users\\Administrator\\Desktop\\test\\教育学部.txt')))
#print(Chineseword.wordcount(Chineseword.cutword(File.readfile('C:\\Users\\Administrator\\Desktop\\test\\教育学部.txt'))))
#Chineseword.wordcloud(Chineseword.wordcount(Chineseword.cutword(File.readfile('C:\\Users\\Administrator\\Desktop\\test\\教育学部.txt'))))
Chineseword.wordcloud('C:\\Users\\Administrator\\Desktop\\test')
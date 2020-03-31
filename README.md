# Open-Source-Program-for-Educational-Technology(V1.0)
This project builds an open source program that will provide educators with simple, actionable Python functions.

**Author：**Tan Li(Master Student of Educational Technology, Tianjin Normal University)
**Email：**litanyouxiang@foxmail.com

## Class:File
> This class is used to handle everything related to files.

### function : readfile()
> This function is used to read the characters in the file and return the result.
**The full syntax is:**
```python
readfile(filename)
```
+ filename: is the file path, and the file is **encoded in UTF-8**.

#### Example
```python
from oset import File
data = File.readfile('C:\\Users\\Administrator\\Desktop\\dict.txt')
for word in data:
	print(word)
>>> 这是一个测试文本
```
## Class:Chineseword
> This Class is used to deal with simple chinese.There 1 function:cutword()...

### function : cutword()
>This function can cut the chinese words.
**The full syntax is:**
```python
cutword(sentence,*stopwordfile)
```
+ sentence: is the sentence that need to cut
+ stopwordfile : Optional parameter,is the stopwords file path

#### Example
```python
from oset import Chineseword
s = "天津师范大学教育学部教育技术研究所"
c = Chineseword.cutword(s)
print(c)
>>> ['天津', '师范大学', '教育学', '部', '教育', '技术', '研究所']
```

## About Me 
Follow me:[CSDN](https://me.csdn.net/qq_32863549);[Personal Website](http://www.litan.tech)
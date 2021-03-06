# Open-Source-Program-for-Educational-Technology(V1.0)
This project builds an open source program that will provide educators with simple, actionable Python functions.

**Author**:Tan Li(Master Student of Educational Technology, Tianjin Normal University)

**Email**:litanyouxiang@foxmail.com

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
### function : readfilesname()
> This function is used to read all file names in the folder and return a list of all file names.

**The full syntax is:**
```python
readfilesname(filename)
```
+ filename: is the file path.

#### Example
```python
from oset import File
filelist = File.readfilesname('C:\\Users\\Administrator\\Desktop\\images')
for fl in filelist:
	print(fl)
```
![Markdown](http://i2.tiimg.com/712071/4276dd8f46835fd5.png)

### function : combfile()
> This function is used to merge all the sub file contents under a folder and output them to the specified location

**The full syntax is:**
```python
combfile(filepath,**outpath)
```
+ filepath：is the file path
+ outpath：is the file path that have combined(Optinal)
#### Example
```python
from oset import File
File.combfile('C:\\Users\\Administrator\\Desktop\\test')
```
There are three sub files under the test file: one.txt, tjnu.txt, two.txt. The automatic merge generates a file named "combfile_Fin. TXT", in which the contents of the above sub files have been merged.

![Markdown](http://i2.tiimg.com/712071/78416e216b0035cb.png)


## Class:Chineseword
> This Class is used to deal with simple chinese.There 1 function:cutword()...

### function : cutword()
>This function can cut the chinese words.In this function, I have built a stop word list and a professional vocabulary word list in the field of education.The main purpose is to reduce the difficulty of the researcher when segmenting words.(stop word list like:'我','是','这'...;vocabulary word list like:'课程论','导师制','双轨制'...)
**The full syntax is:**
```python
cutword(sentence)
```
+ sentence: is the sentence that need to cut
#### Example
```python
from oset import Chineseword
s = "天津师范大学教育学部教育技术研究所"
c = Chineseword.cutword(s)
print(c)
>>>[' 天津师范大学', ' 教育学部', ' 教育技术研究所']
```

## About Me 
Follow me:[CSDN](https://me.csdn.net/qq_32863549);[Personal Website](http://www.litan.tech)
# 教育技术开源库(V1.0)
说明文档英文版请点击[英文版](README-EN.md)
>该项目是以Python为基础，旨在为教育工作者提供一系列常用的处理功能——如词频统计，字符云等，减少教育研究者使用Python的难度。计划V1.0版本维护时间为1年。

**作者**:李坦(天津师范大学教育技术学硕士研究生)
**Email**:litanyouxiang@foxmail.com

## File 类
> 该类用于处理所有涉及到文件的操作

### 函数： readfile()
> 该函数用于读取文件并返回出文件内的结果

**完整结构**
```python
readfile(filename)
```
+ filename: 您的文件路径, 并且文件路径以**utf-8**编码.

#### 示例
```python
from oset import File
data = File.readfile('C:\\Users\\Administrator\\Desktop\\dict.txt')
for word in data:
	print(word)
>>> 这是一个测试文本
```
### 函数: readfilesname()
> 该函数主要是为了将一个文件夹内所有的文件名读取出来

**完整结构**
```python
readfilesname(filename)
```
+ filename: 文件路径

#### 示例
```python
from oset import File
filelist = File.readfilesname('C:\\Users\\Administrator\\Desktop\\images')
for fl in filelist:
	print(fl)
```
![Markdown](http://i2.tiimg.com/712071/4276dd8f46835fd5.png)

### 函数：combfile()
> 该函数用于合并某一个文件夹下所有的子文件内容，并输出到指定位置

**完整结构**
```python
combfile(filepath,**outpath)
```
+ filepath：文件夹路径
+ outpath：合并文件输出位置（可选，若不选则输出到读取文件的位置）

#### 示例
```python
from oset import File
File.combfile('C:\\Users\\Administrator\\Desktop\\test')
```
test文件下存在三个子文件：one.txt,TJNU.txt,two.txt。自动合并产生一个文件名为“combfile_Fin.txt”的文件，该文件中已经上上述子文件内容合并进来。

![Markdown](http://i1.fuimg.com/712071/defc699c1e8d878a.png)

## Chineseword 类
> 该类主要用于处理所有涉及到简体中文的任务，如分词，词频统计，字符云等。

### 函数: cutword()
>这个函数可以切分出文本中的中文词汇。在这个函数中，该函数已经内嵌了停用词表和教育领域专业分词词表。主要目的是减少研究人员在分词时的难度。（停用词表，如：'我'，'是'，'这'...;专业词汇表，如：'课程论'，'导师制'，'双轨制'...）

**完整结构**
```python
cutword(sentence)
```
+ sentence: is the sentence that need to cut
#### 示例
```python
from oset import Chineseword
s = "天津师范大学教育学部教育技术研究所"
c = Chineseword.cutword(s)
print(c)
>>>[' 天津师范大学', ' 教育学部', ' 教育技术研究所']
```

## 关于我 
Follow me:[CSDN](https://me.csdn.net/qq_32863549);[Personal Website](http://www.litan.tech)
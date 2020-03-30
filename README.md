# Open-Source-Program-for-Educational-Technology
This project builds an open source program that will provide educators with simple, actionable Python functions.

### 作者：李坦(天津师范大学教育技术学硕士研究生)；联系方式：litanyouxiang@foxmail.com

## Class name:file
> This class is used to handle everything related to files.

### readfile(filename)
> This function is used to read the characters in the file and return the result.The ** filename ** parameter is the file path, and the file is ** encoded in UTF-8 **.
#### Example
(```)
	from oset import file
	data = file.readfile('C:\\Users\\Administrator\\Desktop\\dict.txt')
	for word in data:
		print(word)
	>>> 这是一个测试文本
(```)


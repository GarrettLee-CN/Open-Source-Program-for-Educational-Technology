'''
开源库作者：李坦，天津师范大学教育学部教育技术学硕士研究生
创建时间：2020年3月30日
'''
import jieba
import codecs
import os
from config import root_path
import re

class File:

	def readfile(filename):#读取文件内容
		data = open(filename,'r',encoding = 'utf-8')
		return data.read()

	def readfilesname(filename):#读取文件夹下的子文件
		fileList = os.listdir(filename)
		return fileList
	
	def  combfile(filepath,**outpath):#将文件夹下子文件全部合并起来
		filelist = File.readfilesname(filepath)
		if outpath != {}:
			data = open(outpaht+'/combfile_Fin.txt','w+',encoding = 'utf-8')
		else:
			data = open(filepath+'/combfile_Fin.txt','w+',encoding = 'utf-8')
		for file in filelist:
			data.write(File.readfile(filepath+'/'+file)+'\n')

	def encodfile(filepath,**outencod):
		filedata = open(filepath,"rb")
		data = open(filepath,"w+",encoding ='utf-8')
		data.write(str(filedata.read()))

	def repfilecont(filepath,content,replacecontent):
		f=open(filepath,'r')
		alllines=f.readlines()
		f.close()
		f=open(filepath,'w+')
		for eachline in alllines:
			a=re.sub(content,replacecontent,eachline)
			f.writelines(a)
		f.close()

	def repbatfilecont(filepath,content,replacecontent):
		filelist = File.readfilesname(filepath)
		content = content
		replacecontent = replacecontent
		for file in filelist:
			File.repfilecont(filepath+'/'+file,content,replacecontent)
			print(file+' 处理完毕！')


class Chineseword:
	def cutword(sentence):
		sentments = jieba.cut(sentence, cut_all=False)
		userdicfile = os.path.join(root_path, 'data/userdic.txt')
		jieba.load_userdict(userdicfile)
		stopwordsfile = os.path.join(root_path, 'data/stop_words.txt')
		f_stopwords=codecs.open(stopwordsfile,'r',encoding='utf-8')
		stopwords=f_stopwords.readlines()
		new_sentence=[]
		for w in sentments:
			if (w+'\r\n') not in stopwords:
				new_sentence.append(' '+w)   
			else:
				continue
		return new_sentence

	#def wordcloud():




		
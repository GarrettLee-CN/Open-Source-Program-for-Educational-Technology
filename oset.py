'''
开源库作者：李坦，天津师范大学教育学部教育技术学硕士研究生
创建时间：2020年3月30日
'''
import pynlpir
import codecs
import os

class File:

	def readfile(filename):
		data = open(filename,'r',encoding = 'utf-8')
		return data

	def readfilesname(filename):
		fileList = os.listdir(filename)
		return fileList

class Chineseword:
	#
	def cutword(sentence,**stopwordfile):
		if stopwordfile == ():
			pynlpir.open()
			sentments=pynlpir.segment(sentence)
			all_sentence=[]
			for segment in sentments:
				all_sentence.append(segment[0])
			return all_sentence
		else:
			pynlpir.open()
			sentments=pynlpir.segment(sentence)
			all_sentence=[]
			for segment in sentments:
				all_sentence.append(segment[0])
			f_stopwords=codecs.open(stopwordfile,'r',encoding='utf-8')
			stopwords=f_stopwords.readlines()
			new_sentence=[]
			for w in all_sentence:
				if (w+'\r\n') not in stopwords:
					new_sentence.append(' '+w)   
				else:
					continue
			pynlpir.close()
			return new_sentence


		
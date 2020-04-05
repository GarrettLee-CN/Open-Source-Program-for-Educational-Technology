'''
开源库作者：李坦，天津师范大学教育学部教育技术学硕士研究生
创建时间：2020年3月30日
'''
import jieba
import codecs
import os
from config import root_path

class File:

	def readfile(filename):
		data = open(filename,'r',encoding = 'utf-8')
		return data

	def readfilesname(filename):
		fileList = os.listdir(filename)
		return fileList

class Chineseword:
	def cutword(sentence):
		sentments = jieba.cut(sentence, cut_all=False)
		# for segment in sentments:
		# 	all_sentence.append(segment[0])
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


		
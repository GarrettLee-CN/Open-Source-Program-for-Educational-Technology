
class file:
	def readfile(filename):
		data = open(filename,'r',encoding = 'utf-8')
		return data

class chineseword:
	def cutword(sentence,stopwordfile,):
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
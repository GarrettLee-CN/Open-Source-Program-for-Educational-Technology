from oset import File
from oset import Chineseword

filelist = File.readfilesname('C:\\Users\\Administrator\\Desktop\\images')
for fl in filelist:
	print(fl)
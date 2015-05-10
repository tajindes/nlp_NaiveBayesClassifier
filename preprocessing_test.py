import sys;
import glob;
import os;
import re;

outputfile = sys.argv[2];
file2 = open(outputfile, "w");
fileNames =  glob.glob(sys.argv[1]+'/*');
fileNames.sort();

''' 
for item in fileNames:
	print (item, "\n");
print ("type is :",type(fileNames));
'''
#for name in glob.glob(sys.argv[1]+'/*'):
for name in fileNames:
	path = re.search('/(.+?).[0-9]+.txt', name).group(1);
	index = path.rfind('/');
	index = index+1;

	file1 = open(name, 'r', errors='ignore')
	lines  = file1.readlines()
	str_temp = ' '.join([line.strip() for line in lines]);

#	str_temp = re.sub('[^A-Za-z0-9_\s-]+','',str_temp);		
	str_temp = str_temp.lower();

	file1.close();

#	print ("name is :",path, "index is:", found,"done");
#	print ("substring is :", path[index:]);
	file2.write(str_temp +"\n");
file2.close();

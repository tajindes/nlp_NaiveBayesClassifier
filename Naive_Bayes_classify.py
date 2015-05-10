import sys;
import ast;
import math;
from sys import stdin;


inputfile = sys.argv[1];
file1 = open(inputfile, "r");
total_count = 0.0 ;

count_dict = { };
word_count_dict = { };
content_dict = { };

vocabulary = file1.readline();
total_count  = float(file1.readline());
count_dict = file1.readline();
vocabulary_size = float(file1.readline());
word_count_dict = file1.readline();
content_dict = file1.readline();

file1.close();

outputfile = sys.argv[2];
file2 = open(outputfile, "r");
line = file2.readline();

count_dict = ast.literal_eval(count_dict);
content_dict = ast.literal_eval(content_dict);
word_count_dict = ast.literal_eval(word_count_dict);

vocabulary = ast.literal_eval(vocabulary);

prob_class = { };

prob_msg_class = { };

for item in count_dict:
	if(item not in prob_msg_class):
		prob_msg_class[item] = 0.0;

	if(item not in prob_class):
		prob_class[item] = float(count_dict[item]/total_count);
		prob_class[item] = math.log(prob_class[item]);		

prob_class_msg = { };

for item in count_dict:
	if(item not in prob_class_msg):
		prob_class_msg[item] = 0.0

while(line):
	temp_list = line.split();
	for item in temp_list:
		for generic_class in content_dict:
			if(item in vocabulary):
				if(item in content_dict[generic_class]):
					prob_msg_class[generic_class] = prob_msg_class[generic_class] +	math.log(((content_dict[generic_class])[item]+ 1.0)/(word_count_dict[generic_class]+ vocabulary_size + 1.0))
				else:
 					prob_msg_class[generic_class] = prob_msg_class[generic_class] +	math.log(1.0/(word_count_dict[generic_class]+ vocabulary_size +1.0));

	for item in prob_class_msg:
		prob_class_msg[item] = prob_class[item] + prob_msg_class[item];

	
	maxx = max(prob_class_msg.values());
	keys = [x for x,y in prob_class_msg.items() if y==maxx]

	#print((str(keys))[2:-2]);
	sys.stdout.write(str((str(keys))[2:-2]) + "\n");

	for item in prob_class_msg:
		prob_class_msg[item] = 0.0

	for item in prob_msg_class:
		prob_msg_class[item] = 0.0
	
	line = file2.readline();
file2.close();

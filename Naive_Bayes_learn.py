import sys;

inputfile = sys.argv[1];
file1 = open(inputfile, "r");
outputfile = sys.argv[2];
count_dict = { };
word_count_dict = { };
content_dict = { };

total_count = 0 ;
vocabulary = set();

line = file1.readline();

while(line):
	total_count = total_count +1;
	line = line.strip();
	temp_list = line.split();
	generic_class = temp_list[0];
	if(generic_class in count_dict):
		count_dict[generic_class] = count_dict[generic_class] + 1;
		word_count_dict[generic_class] = word_count_dict[generic_class] + len(temp_list) -1;	
	else:
		word_count_dict[generic_class] = len(temp_list) -1;	
		count_dict[generic_class] = 1;

	if(generic_class not in content_dict):
		content_dict[generic_class] = { };

	for i in range(1, len(temp_list)):
		vocabulary.add(temp_list[i]);
		if(temp_list[i] in content_dict[generic_class]):
			(content_dict[generic_class])[temp_list[i]] =  (content_dict[generic_class])[temp_list[i]] + 1; 
		else:
			(content_dict[generic_class])[temp_list[i]] = 1;
	line = file1.readline();

file1.close();

file2  =open(outputfile, "w");
file2.write(str(vocabulary) + "\n");
file2.write(str(total_count) + "\n");
file2.write(str(count_dict) + "\n");
file2.write(str(len(vocabulary)) + "\n");
file2.write(str(word_count_dict) + "\n");
file2.write(str(content_dict) + "\n");

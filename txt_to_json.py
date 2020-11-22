import json
import os

rootdir = '/home/hardy/Downloads/BTP/output/out_translation'

# questions = data['questions']

with open('./input.json') as f:
	data = json.load(f)

questions = data['questions']


trans_file = open('output.txt','r')

for i in questions:
	try:
		line = trans_file.readline()
		print(line)
	except OSError:
		break
	if (line == ""):
		break
	i['question'] = str(line) + '?'

data['questions'] = questions

with open('output.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)

f.close()
trans_file.close()
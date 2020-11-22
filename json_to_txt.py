import json

with open('./input.json') as f:
	data = json.load(f)

questions = data['questions']

ques_file = open('input.txt','w')

for i in questions:
	print(i['question'][0:-1], file = ques_file)

ques_file.close()
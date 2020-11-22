inp = open('input.txt','r')

count = 0
file_num = 0
for line in inp:
    if (count == 0):
        f = open('input/input_'+format(file_num, '02d')+'.txt','w')
    f.write(line)
    count += 1
    if (count == 10000):
        f.close()
        count = 0
        file_num += 1

import os

rootdir = '/home/hardy/Downloads/BTP/output/out_translation/'

out_file = open ('output.txt', 'w')

count = 0

for subdir, dirs, files in os.walk(rootdir):
	dirs.sort(key=str)
	# print(dirs)
	for dir_ in dirs:
		# print(dir_)
		try:
			path_ = rootdir+dir_+'/input_translation_input_input_'+format(count, '02d')+'_hi_translations.txt'
			print(path_)
			f = open (path_, 'r')
		except OSError:
			print ('number of files = ' + str(count))
			break
		count += 1
		out_file.write (f.read())
		f.close()

out_file.close()
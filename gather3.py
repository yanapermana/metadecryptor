import sys

def gather_digit(filename):
	array, files = [], open(filename)
	for lines in files:
		lists = lines.rstrip().split()
		for i in range(0, len(lists), 1):
			word = lists[i]
			for j in range(0, len(word), 1):
				if word[j].isdigit() == True:
					array.append(word[j])
		return ''.join(array)
		i += 1
	files.close()

def gather_lower(filename):
	array, files = [], open(filename)
	for lines in files:
		lists = lines.rstrip().split()
		for i in range(0, len(lists), 1):
			word = lists[i]
			for j in range(0, len(word), 1):
				if word[j].islower() == True:
					array.append(word[j])
		return ''.join(array)
		i += 1
	files.close()

def gather_upper(filename):
	array, files = [], open(filename)
	for lines in files:
		lists = lines.rstrip().split()
		for i in range(0, len(lists), 1):
			word = lists[i]
			for j in range(0, len(word), 1):
				if word[j].isupper() == True:
					array.append(word[j])
		return ''.join(array)
		i += 1
	files.close()

def gather_upper_digit(filename):
	array, files = [], open(filename)
	for lines in files:
		lists = lines.rstrip().split()
		for i in range(0, len(lists), 1):
			word = lists[i]
			for j in range(0, len(word), 1):
				if word[j].isupper() == True or word[j].isdigit() == True:
					array.append(word[j])
		return ''.join(array)
		i += 1
	files.close()

def gather_lower_digit(filename):
	array, files = [], open(filename)
	for lines in files:
		lists = lines.rstrip().split()
		for i in range(0, len(lists), 1):
			word = lists[i]
			for j in range(0, len(word), 1):
				if word[j].islower() == True or word[j].isdigit() == True:
					array.append(word[j])
		return ''.join(array)
		i += 1
	files.close()

if __name__ == '__main__':
	filename = sys.argv[1]
	print(gather_digit(filename))
	print(gather_lower(filename))
	print(gather_upper(filename))
	print(gather_upper_digit(filename))
	print(gather_lower_digit(filename))
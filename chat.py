def read(filename):
	chatlist = []
	with open(filename, 'r', encoding='utf-8-sig') as f:  #-sig去除首行的編碼符號
		for line in f:	
			chatlist.append(line.strip())
	return chatlist	

def convert(chatlist):	
	new = []
	person = None
	for line in chatlist:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:		#if person 有值的話才執行避免首行無人名情況
			new.append(person + ': ' + line)	
	return new

def write(filename, chatlist):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chatlist:
			f.write(line + '\n')

def main():
	chatlist = read('input.txt')
	chatlist = convert(chatlist)
	write('output.txt', chatlist)


main()	
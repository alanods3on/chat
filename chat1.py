def read(filename):
	chatlist = []
	with open(filename, 'r', encoding='utf-8-sig') as f:  #-sig去除首行的編碼符號
		for line in f:	
			chatlist.append(line.strip())
	return chatlist	


def convert(chatlist):	
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	person = None
	for line in chatlist:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1	
			else:	
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1	
			else:	
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen一共說了', allen_word_count, '個字')
	print('Allen一共傳了', allen_sticker_count, '張貼圖')				
	print('Allen一共傳了', allen_image_count, '張圖片')
	print('Vike一共說了', viki_word_count, '個字')
	print('Viki一共傳了', viki_sticker_count, '張貼圖')				
	print('Viki一共傳了', viki_image_count, '張圖片')			


def write(filename, chatlist):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chatlist:
			f.write(line + '\n')


def main():
	chatlist = read('LINE-Viki.txt')
	chatlist = convert(chatlist)
	# write('output.txt', chatlist)


main()	
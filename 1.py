def freq(str):
	str_list=str.split()

	unique_words = set(str_list)

	for words in unique_words:
		print('Frequency of',words,'is:',str_list.count(words))

if __name__=="__main__":
	str='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

	freq(str)

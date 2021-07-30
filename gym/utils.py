def StripAndCapital(text):
	name = ''
	text = text.split(' ')
	# Strip and capitalize every word
	for word in text:
		word = word.capitalize()
		word = word.strip()
		if len(word) >= 1:
			name += word + ' '
	# Strip final text
	name = name.strip()
	return name
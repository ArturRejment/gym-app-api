def StripAndCapital(text):
	name = ''
	text = text.split(" ")
	for word in text:
		word = word.capitalize()
		name += word + ' '
	name = name.strip()
	return name
def generate_key(string, keyword):
	keyword = list(keyword)
	
	if len(string) == len(keyword):
		return keyword
	else:
		for i in range(len(string) -
					len(keyword)):
			keyword.append(keyword[i % len(keyword)])
	
	return ("" . join(keyword))
	
def cipher(text, key):
	cipher_text = []

	for i in range(len(text)):
		x = (ord(text[i]) + ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))	

	return ("".join(cipher_text))
	
def decipher(cipher_text, key):
	orig_text = []

	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))

	return ("" . join(orig_text))

import re

a = ord("a")
A = ord("A")
z = ord("z")
Z = ord("Z")

def encrypt(plain, key):
	key = key.lower()
	key_len = len(plain)
	key = "".join([key[i % len(key)] for i in range(key_len)])

	cypher = ""
	i = 0
	for ch in plain:
		p = ord(ch)
		k = ord(key[i])
		i = i + 1
		cypher += chr((p + k) % 256)
	return cypher

def decrypt(cypher, key):
	key = key.lower()
	key_len = len(cypher)
	key = "".join([key[i % len(key)] for i in range(key_len)])

	plain = ""
	i = 0
	for ch in cypher:
		p = ord(ch)
		k = ord(key[i])
		i = i + 1
		plain += chr((p - k) % 256)
	return plain

def encryptLetters(plain, key):
	key = key.lower()
	key_len = len(re.sub(r"[^A-Za-z]", "", plain))
	key = "".join([key[i % len(key)] for i in range(key_len)])

	cypher = ""
	i = 0
	for ch in plain:
		p = ord(ch)
		if p >= a and p <= z:
			k = ord(key[i]) - a
			p = p - a
			i = i + 1
			cypher += chr((p + k) % 26 + a)
		elif p >= A and p <= Z:
			k = ord(key[i]) - a
			p = p - A
			i = i + 1
			cypher += chr((p + k) % 26 + A)
		else:
			cypher += ch

	return cypher

def decryptLetter(cypher, key):
	key = key.lower()
	key_len = len(re.sub(r"[^A-Za-z]", "", cypher))
	key = "".join([key[i % len(key)] for i in range(key_len)])

	plain = ""
	i = 0
	for ch in cypher:
		p = ord(ch)
		if p >= a and p <= z:
			k = ord(key[i]) - a
			p = p - a
			i = i + 1
			plain += chr((p - k) % 26 + a)
		elif p >= A and p <= Z:
			k = ord(key[i]) - a
			p = p - A
			i = i + 1
			plain += chr((p - k) % 26 + A) 
		else:
			plain += ch

	return plain

if __name__ == "__main__":
    text = "Hello World"
    key = "ABCD"

    cypher = encrypt(text, key)
    print(cypher)

    plain = decrypt(cypher, key)
    print(plain)
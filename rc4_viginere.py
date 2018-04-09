import viginere
import rc4
import random

def encode(text, key):
	keystream = rc4.prga(rc4.ksa(key))
	J = random.randint(0, 255)
	k = [keystream.__next__() for i in range(255)]
	k = "".join([chr(ki) for ki in k])

	crc4 = rc4.rc4(text, keystream)
	C1 = viginere.encrypt(crc4[:J], k[:J])
	C2 = viginere.encrypt(crc4[J:], k[J:])
	return C1 + C2 + str(J).zfill(3)

def decode(text, key):
	J = int(text[-3:])
	text = text[:-3]
	keystream = rc4.prga(rc4.ksa(key))
	k = [keystream.__next__() for i in range(255)]
	k = "".join([chr(ki) for ki in k])

	C1 = viginere.decrypt(text[:J], k[:J])
	C2 = viginere.decrypt(text[J:], k[J:])
	crc4 = rc4.rc4(C1 + C2, keystream)
	return crc4	

if __name__ == "__main__":
	text = "Hello World"
	key = "ABCD"
	cypher = encode(text, key)
	print(rc4.toHexString(cypher))
	print(cypher)
	plain = decode(cypher, key)
	print(rc4.toHexString(plain))
	print(plain)
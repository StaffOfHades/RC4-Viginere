import binascii

M = "Hello world"
key = "ABCD"
byte_size = len(key) * 4
K = (bin(int(key, 16))[2:]).zfill(byte_size)

T = []
S = []
for i in range(256):
	S.append(i)
	T.append(int(K[i % len(K)], 2))

print(T)
print("\n")
print(S)

j = 0
for i in range(256):
	j = j + S[i] + T[i]
	j = j % 256
	temp = S[i]
	S[i] = S[j]
	S[j] = temp

print("\n")
print(S)
print("\n")

M1 = M.encode()
M1 = [b for b in bytearray(M1)]
print(M1)
print("\n")

i = j = 0
for index, m in enumerate(M1):
	i = (i + 1) % 256
	j = (j + S[i]) % 256
	temp = S[i]
	S[i] = S[j]
	S[j] = temp
	t = (S[i] + S[j]) % 256
	k = S[t]
	M1[index] = m ^ k

M2 = bytes(M1)
M2 = M2.decode()

print(M2)
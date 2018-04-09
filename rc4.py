key_size = 256

def ksa(key):
    S = list(range(key_size))
    T = [ord(key[i % len(key)]) for i in range(key_size)]

    j = 0
    for i in range(key_size):
        j = (j + S[i] + T[i]) % key_size
        S[i], S[j] = S[j], S[i]
    #print(S)
    return S

def prga(S):
    i = j = 0
    while True:
        i = (i + 1) % key_size
        j = (j + S[i]) % key_size
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % key_size
        k = S[t]
        yield k

def rc4(text, keystream):
    out = []
    k = [keystream.__next__() for i in range(len(text))] 
    #print([hex(l) for l in k])

    out = [ord(ch) ^ k[i] for i, ch in enumerate(text)]
    #print([hex(l) for l in out])

    return "".join([chr(o) for o in out])

def encrypt(text, key):
    keystream = prga(ksa(key))
    return rc4(text, keystream)

def decrypt(text, key):
    keystream = prga(ksa(key))
    return rc4(text, keystream)

def toHexString(hexx):
    return "".join([hex(ord(h)) for h in hexx]).replace("0x", "")

if __name__ == "__main__":
    text = "Hello World"
    key = "ABCD"

    cypher = encrypt(text, key)
    #print(cypher)
    print(toHexString(cypher))

    plain = decrypt(cypher, key)
    print(plain)
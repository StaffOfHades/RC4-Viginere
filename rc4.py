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

def rc4(text, key):
    out = []
    keystream = prga(ksa(key))
    for ch in text:
        out.append(chr(ord(ch) ^ keystream.__next__()))

    return "".join(out)

if __name__ == "__main__":
    text = "Hello World"
    key = "ABCD"

    cypher = rc4(text, key)
    print(cypher)
    
    hexs = cypher.encode()
    byt = [hex(b) for b in bytearray(hexs)]
    k = ' '.join(map(bin, bytearray(cypher, 'utf8')))

    #print(hexs)
    #print(byt)
    #print(k)

    plain = rc4(cypher, key)
    print(plain)    
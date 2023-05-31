import math
msg = int(input("enter msg to encrypt: "))

p = 7
q = 17
n = p*q
m = (p-1)*(q-1)

for i in range(2,m):
    if math.gcd(i,m) == 1:
        e = i
        break
for i in range(m):
    if(e*i) % m == 1:
        d = i
        break
        
def encrypt(me):
    c = pow(msg, e, n)
    return c

def decrypt(ct):
    p = pow(ct, d, n)
    return p

print("Original message is: ", msg)
ct = encrypt(msg)
print("Encrypted message is: ", ct)
pt = decrypt(ct)
print("Decrypted message is: ", pt)

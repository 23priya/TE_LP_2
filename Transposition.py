def encrypt(pt, key):
    ct = [""]*key
    for column in range(key):
        pointer = column
        while pointer < len(pt):
            ct[column] += pt[pointer]
            pointer += key
    return ct

def decrypt(e_text):
        key = len(e_text)
        pt_length = 0
        for i in e_text:
            pt_length += len(i)
            d_text = [""]*pt_length 
        
        for column in range(key):
            pointer = column
            word = e_text[column]
            c = 0
            while pointer < pt_length:
                d_text[pointer] = word[c]
                pointer += key
                c += 1
        return d_text

pt = input (" Enter the message: ")

e_text = encrypt(pt, 3)
print(" ".join(e_text))

d_text = decrypt(e_text)
print(" ".join(d_text))

def decrypt(encrypted_text, n):
    if encrypted_text and len(encrypted_text)>1 and n>=0:
        lst = [l for l in encrypted_text]
        if len(encrypted_text)%2==0:
            k = 0
        else:
            k = 1
        for _ in range(n):
            a = [l for l in lst[:(len(lst)//2)]]
            for n in range(len(encrypted_text)//2+k):
                a.insert(n*2, lst[(len(lst)//2)+n])
            lst = a
        return ''.join(lst)
    else:
        return encrypted_text


def encrypt(text, n):
    if text and len(text)>1 and n>=0:
        lst = [l for l in text]
        for _ in range(n):
            a = [l for l in lst[1::2]]
            b = [l for l in lst[::2]]
            a.extend(b)
            lst=a
        return ''.join(lst)
    else:
        return text
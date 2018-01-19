def increment_string(strng):
    k=0
    for item in strng[::-1]:
        if item in '0123456789':
            k+=1
        else:
            break
    if k == 0:
        result =  ''.join([strng, '1'])
    else:
        w = (len(strng)-k)
        num = str(int(strng[w:])+1)
        result = ''.join([strng[:w], '0'*(k-len(num)), num])
    return result
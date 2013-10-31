

def createstring(n):
    import random
    a=']'*n
    b='['*n
    string=a+b
    temp=list(string)
    random.shuffle(temp)
    string=''
    for x in temp:
        string +=x
    return string

def teststring(s):
    op='['
    cl=']'
    state=op
    for i in range(len(s)):
        if s[i]==state:
            if state==op:
                state=cl
            else:
                state=op
        else: return 'NOT OK'
    return 'OK'

import itertools


def getwordlist():
    f=open('words.txt')
    ls=[]
    a='word'
    while a!='':
        a=f.readline()
        ls.append(a[:-2])
    return ls

def getdict(ls):
    d=dict()
    for x in ls:
        temp=list(x)
        temp.sort()
        temp=tuple(temp)
        d[temp]=d.get(temp,[])+[x]
    return d


def findthesplits(word,d):
    temp=list(word)
    temp.sort()
    clist=[]
    answer=dict()
    for i in range(2,len(temp)/2+1):
        clist.extend(list(itertools.combinations(temp,i)))
    for x in clist:
        if x in d:
            temp2=temp[:]
            for l in x:
                temp2.remove(l)
            temp2=tuple(temp2)
            if temp2 in d:
                answer[word]=[d.get(x),d.get(temp2)]
    return answer
            

def wholewordlist(ls,d):
    answer=dict()
    for x in ls:
        answer.update(findthesplits(x,d))
    return answer
        

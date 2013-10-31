pokemon='audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'

pokemon=pokemon.split()

temp=pokemon[:]

def makenextlist(word,ls):
    lst=ls[:]
    nlist=[]
    for x in lst:
        if x[0]==word[-1]:
            nlist.append(x)
    return nlist


def makedic(ls):
    d=dict()
    for x in ls:
        d[x]=makenextlist(x,ls)
    return d
        
def make2dic(d):
    d2=dict()
    for x in d:
        if len(d[x])!=0:
            for y in d[x]:
                a=d[y][:]
                if x in a:
                    a.remove(x)
                if y in a:
                    a.remove(y)
                d2[(x,y)]=a
    return d2

def makeidic(d2,d):
    d3=dict()
    for x in d2:
        if len(d2[x])!=0:
            for y in d2[x]:
                a=d[y][:]
                t=list(x)+[y]
                for j in t:
                    if j in a:
                        a.remove(j)
                d3[tuple(t)]=a
    return d3


def getithdic(d2,d,c):
    for i in range(c-2):
        d2=makeidic(d2,d)
    return d2

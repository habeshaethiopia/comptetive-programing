from collections import defaultdict
n,m=map(int,input().split())
graph=defaultdict(list)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
fr=False
fb=False
fs=False
for i in graph:
    if len(graph[i])==2:
        pass
    else:
        break
else:
    fr=True
    print('ring topology')
if not fr:
    for i in graph:
        if len(graph[i])==2 or len(graph[i])==1 :
            pass
        else:
            break
    else:
        fb=True
        print('bus topology')
if not(fr or fb):
    center=0
    ed=0
    for i in graph:
        if len(graph[i])==1 :
            ed+=1
        else:
            if len(graph[i])==len(graph)-1:
                center+=1
    if ed==len(graph)-1 and center==1:
        fs=True
        print('star topology')

if not(fr or fb or fs):
    print("unknown topology")
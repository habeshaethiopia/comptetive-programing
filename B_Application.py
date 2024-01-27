DB=set()
count={}
for i in range(int(input())):
    name=input()
    if name in DB:
        count[name]+=1
        print(name+str(count[name]-1))
    else:
        DB.add(name)
        count[name]=1
        print("OK")
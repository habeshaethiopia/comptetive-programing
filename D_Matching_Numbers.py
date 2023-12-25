n = int(input())

for i in range(n):
    num=int(input())
    if num%2:
        pair=list(range(1, 2*num+1))
        print('Yes')
        to_left=num
        to_right=num+1
        while to_left >0:
            print(to_left,to_right)
            to_left-=2
            to_right+=1
        to_right = 2
        to_left = 2*num
        while to_right < num+1:
            print(to_right,to_left)
            to_right+=2
            to_left-=1
        # sm = (sum(pair))//num

        # add = [i for i in range(-(num//2),num)]

        # pairsum=[sm + add[i] for i in range(num)]
        # pair.sort(key=lambda x: x%2==1)
        # print('Yes')
        # for i in pairsum:
        #     for j in pair:
        #         if (i-j) in pair:
        #             print(i-j, j)
        #             pair.remove(j)
        #             pair.remove(i-j)
        #             break
    else:
        print('No')
    
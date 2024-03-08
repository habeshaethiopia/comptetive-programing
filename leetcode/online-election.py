class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times=times
        self.person=persons
        self.winner={}
        count={}
        nump=len(set(persons))
        candidate=deque()
        for i in range(len(persons)):
            candidate.append(persons[i])
            count[persons[i]]=count.get(persons[i],0)+1
            x=0
            tempwin=0
            for j in candidate:
                if x<=count[j]:
                    x=count[j]
                    tempwin=j
                # print(x,tempwin,i)


            self.winner[times[i]]=tempwin
        print('count',count)
        print(self.winner)
    def q(self, t: int) -> int:
        find=bisect_right(self.times,t)-1
        if find<0:
            find=0
        return self.winner[self.times[find]]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
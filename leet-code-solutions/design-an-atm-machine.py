class ATM:

    def __init__(self):
        self.notes=[0,0,0,0,0]
    def deposit(self, banknotesCount: List[int]) -> None:
        for j, i in enumerate(banknotesCount):
                self.notes[j]+=i
    def withdraw(self, amount: int) -> List[int]:
        # $20, $50, $100, $200, and $500
        note=[500,200,100,50,20]
        rev = self.notes[::-1]
        result=[0,0,0,0,0]
        for i in range(5):
            div = amount//note[i]
            mn=min(div, rev[i])
            rev[i]-=mn
            result[i]=mn
            amount -= mn*note[i]
        if amount == 0:
            self.notes=rev[::-1]
            return result[::-1]
        else:
            return [-1]
        


        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
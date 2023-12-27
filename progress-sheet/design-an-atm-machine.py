class ATM:

    def __init__(self):
        self.d={20:0,50:0,100:0,200:0,500:0}

    def deposit(self, banknotesCount: List[int]) -> None:
        ind=0
        for i in [20,50,100,200,500]:
            self.d[i]+=banknotesCount[ind]
            ind+=1

    def withdraw(self, amount: int) -> List[int]:
        d1=self.d.copy()
        ret={20:0,50:0,100:0,200:0,500:0}
        for i in [500,200,100,50,20]:
            temp=min(d1[i],amount//i)
            if amount>=i:
                amount-=temp*i
                d1[i]-=temp
                ret[i]=temp
            if amount<=0:
                break
        if amount==0:
            self.d=d1.copy()
            return ret.values()
        else:
            return [-1]   


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
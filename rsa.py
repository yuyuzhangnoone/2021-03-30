import sys
class rsa:
    def __init__(self):
        print(self.genPrime())
        self.p,self.q=mop(int,input().split())
        self.N=self.p*self.q
        self.N1=(self.p-1)*(self.q-1)
        self.e=int(input())

    def encrypt(self,msg):
        print("Encrypt")
    def dencrypt(self,msg):
        print("Dencrypt")
    def genRandomList(self):
        data=[]
        while  len(data)<6:
            y=rand.randint(1024,65536)
            if isPrimaly(y):
                data.append(y)
        return data
    def isPrimaly(self,x):
        # for i in range(2,x/2):
        #     if x/i==0:
        #         print("Not prime")
        #         break
        #     else: 
        #         return x
        flag=True
        i=2
        while i<x//2:
            if x%i==0:
                flag=False
                break
            i=i+1
        return flag

    def fun(self,N1,e):
        maxVat=max(N1,e)
        minVat=min(N1,e)
        if maxVat%minVat==0:
            return True
        else:
            return self.fun(minVat,maxVat%minVat)

if __name__ == '__main__':
    rsa = RSA()
    rsa.encrypt()
    
    
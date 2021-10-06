
'''
NIM 
|
||
|||
||||
the goal of the game is to pickup the last stick. Each player picks up as many sticks as they want as long as it's in contained within 
that row. There are always n sticks in the nth row. The computer will always go first and play against it's self. 
'''

import random


class Nim:
    def randomizer(self,n):
        import random
        r=random.randint(1,n)
        r1=random.randint(1,r)
        self.r=r
        self.r1=r1
        print("r=", r,r1)
        return r,r1
    def create_board(self,n):
        lst =[]
        for i in range(1,n+1):
            row =[]
            for j in range (i):
                row.append('|')
            lst.append(row)
        print(lst)
        return lst
    def firstmove(self,lst,r,r1):
        print(r,r1)
        row = lst[r-1]
        while r1>r:
            r1=random.randint(1,r)
        for i in range(r1):
            row.pop()
        return lst
    def play(self,lst,n,r,r1):
       flag3=False
       i=0
       count=0
       while flag3==False:
            while count==0:
                import random
                r=random.randint(1,n)
                count=lst[r-1].count('|')
                print(lst)
            while r1>count:
                import random
                r1=random.randint(1,count)
                count=lst[r-1].count('|')
                print(r,r1)
                print(lst)
            Nim.firstmove(self,lst,r,r1)
            if lst[r-1]==None and i==n:
                    flag3=True
                    return lst
            else:
                flag3=False



rows=4            
nim=Nim()
r,r1=nim.randomizer(rows)
print("r=", r,r1)
lst=nim.create_board(rows)
print(nim.firstmove(lst,r,r1))
print(nim.play(lst,rows,r,r1))

'''
NIM 
|
||
|||
||||
the goal of the game is to pickup the last stick. Each player picks up as many sticks as they want as long as it's in contained within 
that row. There are always n sticks in the nth row. The computer will always play against it's self. 
'''

import random


class Nim:

    def randomizer(self,n):
        import random
        r=random.randint(0,n-1)
        if r>1:
            r1=random.randint(1,r)
        else:
            r1=1
        return r,r1
    def create_board(self,n):
        lst =[]
        for i in range(0,n):
            row =[]
            for j in range (i+1):
                row.append('|')
            lst.append(row)
        print(lst)
        return lst
    def firstmove(self,lst,row,sticks,n):
        print('r,r1=',row,sticks)
        count=lst[row].count('|')
        rows = lst[row]
        for i in range(sticks):
                rows.pop()
        while sticks>count:
                row,sticks=Nim.randomizer(self,n)
                count=lst[row].count('|')
        return lst
    def play(self,lst,n,row,sticks):
       move=0
       icanplay=True
       while icanplay==True:
           count=lst[row].count('|')
           checklst=[]
           while sticks>count:
                row,sticks=Nim.randomizer(self,n)
                count=lst[row].count('|')
                for i in range(n):
                     if lst[i]==[]:
                        checklst.append(False)
                     else:
                        checklst.append(True)
                if checklst.count(True)==1:
                    element=checklst.index(True)
                    x=lst[element].count('|')
                    print('rand pair=', element,x)
                    lst.pop(element)
                    break
           v=len(lst)
           if v==3 :
               break
           for i in range(len(lst)):
                if lst[i]==[]:
                    if i==n:
                        icanplay=False
                        break
           Nim.firstmove(self,lst,row,sticks,n)
           print(lst)
       move+=1
       if move%2==0:
        print('player 2 wins')
       else:
        print('player 1 wins')
      
       return lst
           
rows=4            
nim=Nim()
r,r1=nim.randomizer(rows)
print("random=", r,r1)
lst=nim.create_board(rows)
lst=nim.firstmove(lst,r,r1,rows)
print(lst)
flag=True
lst=Nim.play(nim,lst,rows,r,r1)
print(lst)
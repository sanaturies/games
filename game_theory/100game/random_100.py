
#random 100 game
import random
sum=0
def game(maxchoosablemum,desiredtotal):
    sum=0
    count=0
    while sum<desiredtotal:
        r=random.randint(0,maxchoosablemum)
        sum+=r
        count+=1
        print(sum,count)
    if count%2==0:
        winner='player one'
    else:
        winner='player two'

    return sum,winner
print(game(10,100))

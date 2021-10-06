
# make the 100 game but smarter (no reuseing)

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
    if count%2==1:
        winner='player one'
    else:
        winner='player two'

    return sum,winner
print(game(10,100))




def add_dots(string):
    dot='.'
    string1=list(string)
    for i in range(2*len(string1)-1):
        if i%2==1:
          string1.insert(i,dot)
    s = ""
    for j in range (len(string1)):
        s += string1[j]
        
    return s
print(add_dots)
def remove_dots(string):
    string=string.replace('.','')
    print(string)     
    return string
        

def count(string):
    count=0
    for i in range(len(string)):
        if string[i]=='-':
            count+=1
    return count+1

def isanagram(ana,gram):
    flag=False
    if len(ana)==len(gram):
        for i in range(len(ana)):
            if ana[i] in gram:
                flag=True
            else:
                flag=False
                return flag
        return flag
    else:
        return flag

print(isanagram('hi','ih'))


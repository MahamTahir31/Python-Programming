### program for stack
##def push(a,val):
##    a.append(val)
##    print('element pushed successfully at\n', a)
##
##def popitem(a):
##    val=a.pop()
##    print('popped item=', val)
##
##def peek(a):
##    index= len(a)-1
##    print('peek element=',a[index])
##
##
##a=[]
##while True:
##    choice=int(input(' 1-->push\n 2-->pop\n 3-->peek\n 4-->exit\n Enter your choice:'))
##    if (choice==1):
##        val=int(input('enter number which you want to insert in stack:'))
##        push(a,val)
##    elif (choice==2):
##        if(len(a)==0):
##            print('Stack is empty')
##        else:
##            popitem(a)
##    elif (choice==3):
##        if(len(a)==0):
##            print('Stack is empty')
##        else:
##            peek(a)
##    else:
##        break
##  break

# program for ascending linked list
'''
a=[34,56,12,3,58,98,15,25,64]
a.sort()
print(a)
a.reverse()
print(a)
'''
##a=[[0,48,4],[1,29,0],[2,66,6],[3,23,1],[4,64,2],[5,91,-1],[6,72,5]]
##si=3
##i=si
##l=[]
##while (i>=0):
##    n=a[i][1]
##    l.append(n)
##    i=a[i][2]
##print('top two marks=',l[-2:0],'least two marks=',l[0:2])
    

# program for descending linked list    

##
##a=[[0,48,1],[1,29,3],[2,66,4],[3,23,-1],[4,64,0],[5,91,6],[6,72,2]]
##si=5
##i=si
##l=[]
##while (i>=0):
##    n=a[i][1]
##    l.append(n)
##    i=a[i][2]
##print('top two marks=',l[0:2],'least two marks=',l[5:])

# program of sequential research
##a=[34,56,12,3,58,98,15,25,64]
##search=int(input(' enter number which you want to search:'))
##flag=0
##for i in range(len(a)):
##    if (a[i]==search):
##        flag=1
##        position=i+1
##        break
##if (flag==1):
##    print('element found at position:',position)
##else:
##    print('element not found')
# program of selection sort
##a=[34,56,12,3,58,98,15,25,64]
##for i in range(len(a)):
##    m=a[i]
##    for j in range(i,len(a)):
##        if(a[j]<m):
##            m=a[j]
##            p=j
##    t=a[i]
##    a[i]=m
##    a[p]=t
##print(a)
# program of power by recursion
##def power(a,b):
##    if(b==0):
##        return(1)
##    else:
##        return (a*power(a,b-1))
##n=int(input('enter number which is base:'))
##m=int(input('enter number which is power:'))
##p=power(n,m)
##print(p)

# Q7 of evening exam
# program of binary searchng
# a=[34,56,12,3,58,98,15,25,64]
# n=int(input('enter searched value:'))
# si=0
# ei=0
# for i in range(len(a)):
#     mid=int((si+ei)/2)
#     if(mid[a]<a):
#         si=si+1
#     elif(mid[a]>a):
#         ei=ei-1
#     else:
#         pos=mid[a[i]]
#         print('we got searched value at', pos)
# if(i>len(a)):
#     print('not found ')

'''
RECURSIVE FUNCTION:
def factorial(n):
    if (n==0):
        return (1)
    else:
        return (n*factorial(n-1))

n=int(input('enter number:'))
f= factorial(n)
print (f)
'''
'''
RECURSIVE FUNCTION:
def power(a,b):
    if (b==0):
        return(1)
    else:
        return(a*power(a,b-1))

n=float(input('enter number:'))
p=int(input('enter power:'))
x=power(n,p)
print(x)
'''

##L=['A','B','C','D']
##for i in range (L):
##    nc=ord(i)
##    L[nc]+=1
##for i in range (L):
##    print (chr(i), L[i])

##for i ,i<10,i=i+1:
##    print ("hi maham")

##a={'a':1,'b':2,'c':3}
##print(a.get('a',4))
##print(a.get('b'))
##print(a.get('d'))
##print(a.get('d','default value set by programmer'))
##
##

class student:
    def __init__(self, aname, aclasss,asection):
        self.name=aname
        self.classs=aclasss
        self.section=asection



    
    def printdetails(self):
        return f"name is {self.name}.class is{self.classs} and section is{self.section}"
    
maham = student("maham", 12, "a")
print(maham.name)
summary= printdetails(maham)
print(summary)

















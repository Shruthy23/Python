import re
n=int(input("Enter the number of mails"))
lst=[]
lst2=[]
for i in range(n):
    lst.append(input())
for i in lst:
    if re.search(r'[-|\w+]@\w+[.]\w{1,3}',i):
        lst2.append(i) 
lst2.sort()
print(lst2)
    

print("Enter the num")
n = int(input())
str1=[]
d={}
for i in range(n):
    str1.append(input())
for x in str1:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]+=1
print(len(d))
list1=[]
for i in d.values():
        list1.append(i)
print(list1)

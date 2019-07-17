n=int(input("Enter the number of elements"))
lst1=[]
for i in range(n):
    lst1.append(input())
for i in range(n):
    t=lst1[i]
    for j in range(n-1):
        if lst1[i] < lst1[j]:
            t=lst1[i]
            lst1[i]=lst1[j]
            lst1[j]=t
print(lst1)

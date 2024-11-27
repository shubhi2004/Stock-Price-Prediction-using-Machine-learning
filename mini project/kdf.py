lst=[2,6,5,3,4,3]
lst.sort()
j=[]
key=7
for i in range(0,len(lst)):
    if key==lst[i]:
        j.append(i)
if j==[]:
    print("false")
else:
    print(j)
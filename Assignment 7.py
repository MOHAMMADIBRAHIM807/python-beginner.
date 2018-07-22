
#1
l=[1,3,5,10,12,15,18,20,21,30]
n=int(input("enter a number"))
c=lambda x:x**3
print(c(n))

#2
l_filter=[x for x in filter(lambda x:True if x%15==0 else False,l)]
print(l_filter)


#3
l1=[1,2,4,5]
l2=[3,4,5,6]
l3=[5,6,7,7]
l4=[5,6,7,8]
def sum4(a,b,c,d):
    return a+b+c+d
s=[x for x in map(sum4,l1,l2,l3,l4)]
print(s)

s=[x for x in map(lambda a,b,c,d:a+b+c+d,l1,l2,l3,l4)]
print(s)

#4
l1=[7,6,4]
l2=[2,3,5]
d={a:b for a,b in map(lambda x,y:((x,y**2) if x>y else (y,x**2)),l1,l2)}
print(d)
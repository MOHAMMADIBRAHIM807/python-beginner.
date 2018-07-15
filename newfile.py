1.
s=input("enter a sentence:")
w=input("enter the word to search:")
print("WORD:",w)
s=s.upper()
w=w.upper()
l=s.split()
if not(w in l):
    print("sorry word does not exist")
else:
    print("COUNT:",l.count(w))

2.
x=["is","am","are","of","as","on","a"]
print(x)
y=[]
s=input("ENTER A SENTENCE:")
s=s.lower()
l=s.split()
for i in l:
    if not(i in x):
        y.append(i)

print (" ".join(y))
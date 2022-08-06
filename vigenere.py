pt = input()
key = input()
pt = pt.lower()
key = key.lower()
pt = [ord(a)-97 for a in pt]
key = [ord(a)-97 for a in key]

i=0
while(len(key)!=len(pt)):
    key.append(key[i])
    i+=1
    if(i==len(key)):
        i=0

for i,j in zip(pt,key):
    res = (i+j)%26
    print(chr(res+97),end="")
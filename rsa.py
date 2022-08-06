m = int(input("Enter the plan text"))
p = int(input("Enter the first prime number"))
q = int(input("Enter the second prime number"))
n = p*q
pi = (p-1)*(q-1)

e = int(input("Enter your public key e"))
d=1
while((e*d)%pi!=1):
    d+=1

print("corresponding d(private key) is ",d)
cip = (m**e)%n
print("The cipher text is",cip)
dec = (cip**d)%n
print("The decrypted text is ",dec)
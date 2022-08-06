key = int(input("Enter Key: "))
encrypt = int(input("Enter: \n'1' to Encrypt \n'0' to Decrypt\n"))
input = input("Enter Text: ").upper()
output = ""

if encrypt!=1:
    key *= -1
for i in input:
    output += chr(((ord(i) + key - 65) % 26) + 65)

print(output)
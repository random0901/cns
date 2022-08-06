a=int(input("enter alpha\n"))
q=int(input("enter prime number\n"))
xa=int(input("enter the private key of alice\n"))
xb=int(input("enter private key of bob\n"))
ya=(a**xa)%q
yb=(a**xb)%q

print(ya,yb)

ka=(yb**xa)%q
kb=(ya**xb)%q

print(ka,kb)
a,b = 0, 1
while b <= 1597:
    if a == 0:
        print(a, b, sep=".",end=".")
        a+=b
        b+=a 
    if b == 1597:
        print(a, b,sep=".", end="")
        a+=b
        b+=a 
    else:
        print(a, b, sep=".", end=".")
        a+=b
        b+=a      # 0.1.1.2.3.5.8.13.21.34.55.89.144.233.377.610.987.1597
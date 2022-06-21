a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
n =  b**2-4*a*c 
ans = 0
ans1 = 0
if n < 0 :
    print("0")
else:
    ans = (-b + n ** 0.5) / 2
    ans1 = (-b - n ** 0.5) / 2
    if ans == ans1:
        print(ans)
    else:
        print(ans)
        print(ans1)
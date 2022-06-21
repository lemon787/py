x = int(input("輸入:"))
ans = 0
for i in range(0,x):
    n = int(input())
    if n > ans:
        ans = n
print(ans)
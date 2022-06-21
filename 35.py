from msilib.schema import BBControl


aa = str(input("sA:"))
bb = str(input("sB:"))
l = len(aa)
tf = True
for a in range(0,len(bb)-l):
    if bb[a:a+l] == aa:
        print("子字串判斷為:Yes")
        tf = False
        break
if tf:
    print("子字串判斷為:No")
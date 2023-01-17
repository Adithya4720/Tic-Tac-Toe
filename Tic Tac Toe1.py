a= [1,2,3,4,5,6,7,8,9]
b=[1,4,7]
for i in range(5):
    for j in a[0:3]:
        
        print(j,end=" | ")
    print("\n-----------")
    for z in a[3:6]:
        
        print(z,end=" | ")
    print("\n-----------")
    for p in a[6:9]:
        print(p,end=" | ")
    print("\n")
    if a[0]==a[1]==a[2]:
        print("Game won by", a[0])
        break
    elif a[3]==a[4]==a[5]:
        print("Game won by", a[3])
        break
    elif a[6]==a[7]==a[8]:
        print("Game won by", a[6])
        break
    elif a[1]==a[4]==a[7]:
        print("Game won by", a[1])
        break
    elif a[2]==a[5]==a[8]:
        print("Game won by", a[2])
        break
    elif a[3]==a[6]==a[8]:
        print("Game won by", a[3])
        break
    elif a[1]==a[5]==a[8]:
        print("Game won by", a[0])
        break
    elif a[3]==a[5]==a[7]:
        print("Game won by", a[0])
        break
    
    a1 =int(input("Player 1 :"))
    if a[a1-1] ==   "X":
        print("Already Occupied!!")
        i-=1
    if a[a1-1] ==   "O":
        print("Already Occupied!!")
        i-=1
    a2 = int(input("Player 2: "))
    if a[a2-1] ==   "X":
        print("Already Occupied!!")
        i-=1
    if a[a2-1] ==   "O":
        print("Already Occupied!!")
        i-=1

    a[a1-1]="X"
    a[a2-1]="O"


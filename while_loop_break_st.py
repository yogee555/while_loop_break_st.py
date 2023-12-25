list = [10,20,30,40,50]
n = len(list)-1
while n >= 0 :
    if list[n] == 30:
        print("the number which we are looking for is present")
        n=n-1
        break
    print(list[n])
    n=n-1
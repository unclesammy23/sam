def some(n):
    for a in n:
        if a%5==0 and a%3==0:
            n[n.index(a)]="strive school"
            print(n)
        elif a%3==0:
            n[n.index(a)]="strive"
        elif a%5==0:
            n[n.index(a)]="school"
        

some([1,2,3,4,20,10,15])


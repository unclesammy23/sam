totalrows=int(input("what is your number of rows: "))
for row in range(1, totalrows+1):
    for space in range(1, (totalrows-row)+1):
        print(" ", end="")
    for symobol in range(1, row+1):
        print("#", end="")
    print()
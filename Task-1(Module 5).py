with open("s.txt","r") as f:
    data=f.readline()
    while data:
        print(data)
        data=f.readline()
with open("Sample.txt","r") as f:
    data=f.readline()
    while data:
        print(data)
        data=f.readline()
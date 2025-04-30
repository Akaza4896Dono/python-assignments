with open("output.txt","w") as f:
    data=input("Enter text to write to the file: " )
    f.write(data)
    print("Data successfully written to output.txt ")

with open("output.txt","a") as f:
    data=input("Enter additional text to append: " )
    f.write("\n"+data)
    print("Data successfully appended ")

with open("output.txt","r") as f:
    data=f.read()
    print("Final content of output.txt:\n")
    print(data)
        
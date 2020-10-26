# Update very often or will break!
print("1: Save 2: View")
inputx = input("@User: ")
if inputx == "1":
    print("Enter what you want to save (such as  a code)")
    inputx = input("@User: ")
    i = inputx
    print("Slot 1, 2 or 3")
    inputx = input("@User: ")
    if inputx == "1":
        with open("slot1.txt", "r+") as f:
         f.seek(0) 
         f.write(i) 
    if inputx == "2":
        with open("slot2.txt", "r+") as f:
          f.seek(0) 
          f.write(i)
         
         